# for userpage and osucollector 
import requests
import time
import api
import constants
# returns https://osu.ppy.sh/beatmapsets/<beatmapset_id>

def pausechamp(r):
    if r.status_code != 200:
        raise Exception()
    time.sleep(constants.api_get_interval)

# TODO: write test
def get_userpage_beatmaps(source):
    all_beatmaps=set()
    unavailable_beatmaps=set()
    
    if source.scope[0]:
        # Top plays
        for user_id, gamemode in source.get_ids():
            on_page=1
            r=requests.get(constants.scrape_top_plays.format(user_id, gamemode, on_page*100, (on_page-1)*100))
            for item in r.json():
                beatmap_id=item['beatmap_id']
                beatmap_checksum, beatmapset_id = api.query_osu_beatmap(beatmap_id)
                beatmap=(beatmapset_id, beatmap_id, beatmap_checksum)
                all_beatmaps.add(beatmap)
                if beatmap_checksum == False:
                    # Not hosted
                    unavailable_beatmaps.add(beatmap)
        
    if source.scope[1]:
        # Favourites
        pass
        
    if source.scope[2]:
        # Everything played
        pass

    if source.scope[3]:
        pass
    if source.scope[4]:
        pass
    if source.scope[5]:
        pass
    if source.scope[6]:
        pass

    if source.scope[7]:
        pass

    return all_beatmaps, unavailable_beatmaps
def get_tournament_beatmaps(source):
    pass
def get_mappack_beatmaps(source):
    pass
def get_osucollector_beatmaps(source):
    all_beatmaps=set()
    unavailable_beatmaps=set()
    page=1
    cursor=None
    while True:
        url=constants.osucollector_url.format(source.get_id(), page*100)
        if cursor!=None:
            url+="&cursor={}".format(cursor)
        r=requests.get(url)
        for item in r.json()['beatmaps']:
            beatmapset_id=item['beatmapset']['id']
            time.sleep(2)
            if api.query_osu_beatmapset(beatmapset_id):
                unavailable_beatmaps.add(beatmap)
            beatmap=(beatmapset_id, None, None)
            all_beatmaps.add(beatmap)
        cursor=r.json()['nextPageCursor']
        if cursor == None:
            break

    return all_beatmaps, unavailable_beatmaps