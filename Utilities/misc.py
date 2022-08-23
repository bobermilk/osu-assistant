import database
import entity

# called by job refresh to find out what to download
def diff_local_and_source(source):
    for beatmap in source.get_available_beatmaps():
        if database.query_osudb(beatmap)
    return 

# The following creates source objects to be inserted into the Sources entities
def create_userpage_source(links, scope):
    #Example
    # User: played=top&fav status=r&gp&p&g Polyester

    # TODO: create the name of the source
    key=""

    # TODO: get source data
    ids=parse_urlstring(links)
    return (key, entity.UserSource(ids, scope))

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

def parse_urlstring(urlstring):
    pass