import entity
import re
import requests
import time
from Network import download, api
from Utilities import data, database, constants

# Update sources/jobs on startup
# 
async def init():
    # Initialize the cache db
    await database.create_osudb()
    # Refresh sources and jobs (the views will update)
    await data.Sources.refresh()

# WARNING: this function WILL hang the main thread, so remember to make it async in production
def do_job(job):
    downloads=job.get_beatmapset_ids()

    source=data.get_sources().get_source(job.get_job_source_key())
    for beatmapset_id in downloads:
        # Check if cancel button has been pressed (user cancelled opration)
        if data.cancel_jobs_toggle:
            return False
        # Check source beatmap cache for availability of beatmap
        is_hosted=source.query_cache(beatmapset_id)
        # Start downloading
        download.download_beatmap(beatmapset_id, is_hosted)
    
    return True  

# called by job refresh to find out what to download
def diff_local_and_source(source):
    missing_beatmapset_ids=[]
    for beatmap in source.get_available_beatmaps():
        if not database.query_osudb(beatmap):
            missing_beatmapset_ids.append(beatmap)
    return missing_beatmapset_ids

# The following creates source objects to be inserted into the Sources entities
def create_userpage_source(links, scope):
    #Example
    # User: played=top&fav status=r&gp&p&g Polyester

    # TODO: create the name of the source
    key=""

    # TODO: get source data
    ids=parse_urlstring(links)
    return (key, entity.UserpageSource(ids, scope))

def create_tournament_source(id):
    #Example
    # Tournament: osu!mania 4K World Cup 2022

    # TODO: create the name of the source
    key=""

    return (key, entity.TournamentSource(id))

def create_mappack_source(status, gamemode, url):
    #Example
    # Mappack size=51 mode=m status=r

    # TODO: create the name of the source
    key=""

    # TODO: get source data
    status=1
    gamemode=1
    download_count=1
    return (key, entity.MappackSource(status, gamemode, download_count))

def create_osucollector_source(links):
    #Example
    # Osucollector: DT SPEED
    # TODO: create the name of the source
    key=""

    # TODO: get source data
    ids=[]
    return (key, entity.OsucollectorSource(ids))

# Extract beatmapset_ids from osu beatmap urls
def parse_urlstring(urlstring):
    beatmapset_ids=[]

    ra = "(?<=beatmapsets\/)([0-9]*)(?=#|\n)" # matches format /beatmapsets/xxxxx#xxxxx or /beatmapsets/xxxxx
    rb = "(.*\/b\/.*)" # matches format /b/xxxxx

    for i in re.findall(ra, urlstring):
        beatmapset_ids.append(i)

    for url in re.findall(rb, urlstring):
        try:
            r = requests.head(url, allow_redirects=True, timeout=10)
            beatmapset_ids.append(re.findall(ra, r.url)[0])
            time.sleep(data.get_settings().download_interval)
        except:
            pass
    return beatmapset_ids

# Gets the directory this application is installed in
def get_install_directory():
    if constants.DEBUG:
        return constants.test_folder
    else:
        # TODO: get the install directory here
        pass
