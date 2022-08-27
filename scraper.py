# for userpage and osucollector 
import requests
import time
import api
import data
import constants
# returns https://osu.ppy.sh/beatmapsets/<beatmapset_id>

def pausechamp(r):
    if r.status_code != 200:
        raise Exception()
    time.sleep(constants.api_get_interval)

# TODO: write test
def get_userpage_beatmaps(source):
    all_beatmaps=set()
    
    scope=source.get_scope()
    # Not from api
    if scope[0]:
        beatmaps=set()
        for user_id, gamemode in source.get_ids():
            on_page=1
            if gamemode=="":
                url=constants.scrape_top_plays_defaultmode.format(user_id, on_page*100, (on_page-1)*100)
            else:
                url=constants.scrape_top_plays.format(user_id, gamemode, on_page*100, (on_page-1)*100)
            r=requests.get(url)
            time.sleep(3)
            for item in r.json():
                beatmap_id=item['beatmap_id']
                beatmap_checksum, beatmapset_id = api.query_osu_beatmap(beatmap_id)
                beatmap=(beatmapset_id, beatmap_id, beatmap_checksum)
                beatmaps.add(beatmap)
        all_beatmaps.update(beatmaps)


    # From osu api

    # beatmaps=set()
    # for user_id, gamemode in source.get_ids():
    #     j=api.query_osu_user_beatmapsets(user_id, gamemode, "loved") # list of jsons on each page
    # Sample json test:
    #     with open("test.json", "w") as f:
    #         f.write(str(j))
    #     for item in j:
    #         for beatmap in item:
    #             beatmapset_id=beatmap["beatmaps"][0]["beatmapset_id"]
    #             beatmaps.add((beatmapset_id, None, None))

    # with open("test.json", "w") as f:
    #     f.write(str(beatmaps))

    if scope[1]:
        # Favourites
        beatmaps=set()
        for user_id, gamemode in source.get_ids():
            j=api.query_osu_user_beatmapsets(user_id, "favourite") # list of jsons on each page
            for item in j:
                for beatmap in item:
                    beatmaps.add((beatmap["beatmaps"][0]["beatmapset_id"], None, None))
        all_beatmaps.update(beatmaps)
        
    if scope[2]:
        # Everything played
        beatmaps=set()
        for user_id, gamemode in source.get_ids():
            j=api.query_osu_user_beatmapsets(user_id, "most_played")
            for item in j:
                for beatmap in item:
                    beatmapset_id=beatmap["beatmap"]["beatmapset_id"]
                    beatmap_id=beatmap["beatmap_id"]
                    beatmaps.add((beatmapset_id, beatmap_id, None))
        all_beatmaps.update(beatmap)
        

    if scope[3]:
        beatmaps=set()
        for user_id, gamemode in source.get_ids():
            j=api.query_osu_user_beatmapsets(user_id, "ranked")

            for item in j:
                for beatmap in item:
                    beatmapset_id=beatmap["beatmaps"][0]["beatmapset_id"]
                    beatmaps.add((beatmapset_id, None, None))
        all_beatmaps.update(beatmap)

        
    if scope[4]:
        beatmaps=set()
        for user_id, gamemode in source.get_ids():
            j=api.query_osu_user_beatmapsets(user_id, "loved")

            for item in j:
                for beatmap in item:
                    beatmapset_id=beatmap["beatmaps"][0]["beatmapset_id"]
                    beatmaps.add((beatmapset_id, None, None))
        all_beatmaps.update(beatmap)

    if scope[5]:
        beatmaps=set()
        for user_id, gamemode in source.get_ids():
            j=api.query_osu_user_beatmapsets(user_id, "pending")

            for item in j:
                for beatmap in item:
                    beatmapset_id=beatmap["beatmaps"][0]["beatmapset_id"]
                    beatmaps.add((beatmapset_id, None, None))
        all_beatmaps.update(beatmap)

    if scope[6]:
        beatmaps=set()
        for user_id, gamemode in source.get_ids():
            j=api.query_osu_user_beatmapsets(user_id, "graveyard")

            for item in j:
                for beatmap in item:
                    beatmapset_id=beatmap["beatmaps"][0]["beatmapset_id"]
                    beatmaps.add((beatmapset_id, None, None))
        all_beatmaps.update(beatmap)
    return all_beatmaps

def get_tournament_beatmaps(source):
    all_beatmaps=set()
    all_beatmaps.add(data.TournamentJson[source.get_id()])
    return all_beatmaps
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