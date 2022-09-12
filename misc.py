import os
import webbrowser
import entity
import requests
import download
import asyncio
import data, database, constants, strings
from pubsub import pub
import aiohttp

# Update sources/jobs on startup
# 
async def init():
    # Load app data
    has_savefile=data.load_data()
    # Check for update
    if requests.get("https://milkies.ml/json/osu-assistant.json").json()["latest"]>constants.APP_VERSION:
        pub.sendMessage("show.dialog", msg="New update available! Download from github?", ok=lambda: webbrowser.open(constants.link_github_releases))

    # Get the jsons
    data.TournamentJson=requests.get("https://milkies.ml/json/tournament.json").json()
    data.MappackJson=requests.get("https://milkies.ml/json/mappack.json").json()
    return has_savefile
    
# WARNING: this function WILL hang the main thread, so remember to make it async in production
async def do_job(job):
    downloads=job.get_job_downloads()

    source=data.Sources.get_source(job.get_job_source_key())
    async with aiohttp.ClientSession() as session:
        for i, beatmap in enumerate(downloads, 1):
            # Check if cancel button has been pressed (user cancelled opration)
            if data.cancel_jobs_toggle:
                return False
            # Check source beatmap cache for availability of beatmap
            is_hosted=source.query_cache(beatmap)
            # Start downloading
            if is_hosted:
                success=await download.download_beatmap(session, beatmap[0])
                
                # Intervals between jobs
                download_interval=data.Settings.download_interval/1000
                if success==2:
                    download_interval+=constants.osu_get_interval # add 3 seconds if its downloading from osu website
                await asyncio.sleep(download_interval)
            
            # Update progressbar
            pub.sendMessage("update.progress", value=i, range=len(downloads), progress_message=None)
    
    return True  

# called by job refresh to find out what to download
def diff_local_and_source(source):
    missing_beatmaps=[]
    for beatmap in source.get_available_beatmaps():
        if beatmap[0] != None and not database.query_osudb(beatmap):
            missing_beatmaps.append(beatmap)
    return missing_beatmaps

# The following creates source objects to be inserted into the Sources entities
def create_userpage_source(links, scope):
    users=strings.parse_userpages_urlstrings(links) # returns set of (userid, gamemode)

    #Example
    # User: played=top&fav status=r&gp&p&g mode=m Polyester
    source_key=strings.generate_userpage_source_key(users, scope)

    return (source_key, entity.UserpageSource(users, scope))

def create_tournament_source(tournament_id, source_key):
    # Example
    # SOFT-4: Springtime Osu!mania Free-for-all Tournament 4
    return (source_key, entity.TournamentSource(tournament_id))

def create_mappack_source(ids):
    #Example
    # Mappack mode=m #109 #108
    
    source_key=strings.generate_mappack_source_key(ids)

    return (source_key, entity.MappackSource(ids))

def create_osucollector_source(links):
    #Example
    # Osucollector: DT SPEED

    # Get id
    ids=strings.parse_osucollector_urlstrings(links)

    # Generate source key
    source_key=strings.generate_osucollector_source_key(ids)

    # Generate new source
    new_source=entity.OsucollectorSource(ids)

    return (source_key, new_source)
