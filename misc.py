import entity
import requests
import download, api
import data, database, constants, strings
import scraper

# Update sources/jobs on startup
# 
async def init():
    # Get the jsons
    data.TournamentJson=requests.get("https://raw.githubusercontent.com/bobermilk/osu-assistant-data/main/tournament.json").json()
    data.MappackJson=requests.get("https://raw.githubusercontent.com/bobermilk/osu-assistant-data/main/mappack.json").json()
    # Initialize the cache db
    await database.create_osudb()
    # Refresh sources and jobs (the views will update)
    await data.Sources.refresh()
    
# WARNING: this function WILL hang the main thread, so remember to make it async in production
def do_job(job):
    downloads=job.get_job_downloads()

    source=data.get_sources().get_source(job.get_job_source_key())
    for beatmap in downloads:
        # Check if cancel button has been pressed (user cancelled opration)
        if data.cancel_jobs_toggle:
            return False
        # Check source beatmap cache for availability of beatmap
        is_hosted=source.query_cache(beatmap)
        # Start downloading
        if is_hosted:
            success=download.download_beatmap(beatmap[0])
            if not success:
                source.cache_missing_beatmap(beatmap)
            else:
                source.uncache_missing_beatmap(beatmap)
        else:
            source.cache_unavailable_beatmap(beatmap)
    
    return True  

# called by job refresh to find out what to download
def diff_local_and_source(source):
    missing_beatmap=[]
    for beatmap in source.get_available_beatmaps():
        if not database.query_osudb(beatmap):
            missing_beatmap.append(beatmap)
    return missing_beatmap

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

# Gets the directory this application is installed in
def get_install_directory():
    if constants.DEBUG:
        return constants.test_folder
    else:
        # TODO: get the install directory here
        pass
