# for userpage and osucollector 

import requests
import time
from Utilities import constants
from Network import api
# returns https://osu.ppy.sh/beatmapsets/<beatmapset_id>

# TODO: write test
def get_userpage_beatmaps(source):
    all_beatmaps=set()
    unavailable_beatmaps=set()
    
    if source.scope[0]:
        # Top plays
        for user_id, gamemode in source.get_ids():
            page=1
            while True:
                r=requests.get(constants.scrape_top_plays.format(user_id, gamemode, page*100, (page-1)*100))
                if r.content == b'[]':
                    break
                for item in r.json():
                    beatmap_id=item['beatmap_id']
                    time.sleep(constants.api_scrape_interval)
                    beatmap_checksum, beatmapset_id = api.query_osu_beatmap(beatmap_id)
                    beatmap=(beatmapset_id, beatmap_id, beatmap_checksum)
                    all_beatmaps.add(beatmap)
                    if beatmap_checksum == False:
                        # Not hosted
                        unavailable_beatmaps.add(beatmap)
                page+=1
        
    if source.scope[1]:
        # Favourites
        for user_id in source.get_ids():
            page=1
            while True:
                r=requests.get(constants.scrape_favourites.format(user_id, page*100, (page-1)*100))
                if r.content == b'[]':
                    break
                for item in r.json():
                    beatmap_id=item['beatmap_id']
                    time.sleep(constants.api_scrape_interval)
                    beatmap_checksum, beatmapset_id = api.query_osu_beatmap(beatmap_id)
                    beatmap=(beatmapset_id, beatmap_id, beatmap_checksum)
                    all_beatmaps.add(beatmap)
                    if beatmap_checksum == False:
                        # Not hosted
                        unavailable_beatmaps.add(beatmap)
                page+=1
        
    if source.scope[2]:
        # Everything played
        for user_id in source.get_ids():
            page=1
            while True:
                r=requests.get(constants.scrape_everything.format(user_id, page*100, (page-1)*100))
                if r.content == b'[]':
                    break
                for item in r.json():
                    beatmap_id=item['beatmap_id']
                    time.sleep(constants.api_scrape_interval)
                    beatmap_checksum, beatmapset_id = api.query_osu_beatmap(beatmap_id)
                    beatmap=(beatmapset_id, beatmap_id, beatmap_checksum)
                    all_beatmaps.add(beatmap)
                    if beatmap_checksum == False:
                        # Not hosted
                        unavailable_beatmaps.add(beatmap)
                page+=1

    if source.scope[3]:
        # Ranked
        for user_id in source.get_ids():
            page=1
            while True:
                r=requests.get(constants.scrape_ranked.format(user_id, page*100, (page-1)*100))
                if r.content == b'[]':
                    break
                for item in r.json():
                    beatmap_id=item['beatmap_id']
                    time.sleep(constants.api_scrape_interval)
                    beatmap_checksum, beatmapset_id = api.query_osu_beatmap(beatmap_id)
                    beatmap=(beatmapset_id, beatmap_id, beatmap_checksum)
                    all_beatmaps.add(beatmap)
                    if beatmap_checksum == False:
                        # Not hosted
                        unavailable_beatmaps.add(beatmap)
                page+=1
    if source.scope[4]:
        # Loved
        for user_id in source.get_ids():
            page=1
            while True:
                r=requests.get(constants.scrape_loved.format(user_id, page*100, (page-1)*100))
                if r.content == b'[]':
                    break
                for item in r.json():
                    beatmap_id=item['beatmap_id']
                    time.sleep(constants.api_scrape_interval)
                    beatmap_checksum, beatmapset_id = api.query_osu_beatmap(beatmap_id)
                    beatmap=(beatmapset_id, beatmap_id, beatmap_checksum)
                    all_beatmaps.add(beatmap)
                    if beatmap_checksum == False:
                        # Not hosted
                        unavailable_beatmaps.add(beatmap)
                page+=1
    if source.scope[5]:
        # Guest participation
        for user_id in source.get_ids():
            page=1
            while True:
                r=requests.get(constants.scrape_guest_participation.format(user_id, page*100, (page-1)*100))
                if r.content == b'[]':
                    break
                for item in r.json():
                    beatmap_id=item['beatmap_id']
                    time.sleep(constants.api_scrape_interval)
                    beatmap_checksum, beatmapset_id = api.query_osu_beatmap(beatmap_id)
                    beatmap=(beatmapset_id, beatmap_id, beatmap_checksum)
                    all_beatmaps.add(beatmap)
                    if beatmap_checksum == False:
                        # Not hosted
                        unavailable_beatmaps.add(beatmap)
                page+=1
    if source.scope[6]:
        # Pending
        for user_id in source.get_ids():
            page=1
            while True:
                r=requests.get(constants.scrape_pending.format(user_id, page*100, (page-1)*100))
                if r.content == b'[]':
                    break
                for item in r.json():
                    beatmap_id=item['beatmap_id']
                    time.sleep(constants.api_scrape_interval)
                    beatmap_checksum, beatmapset_id = api.query_osu_beatmap(beatmap_id)
                    beatmap=(beatmapset_id, beatmap_id, beatmap_checksum)
                    all_beatmaps.add(beatmap)
                    if beatmap_checksum == False:
                        # Not hosted
                        unavailable_beatmaps.add(beatmap)
                page+=1

    if source.scope[7]:
        # Graveyarded
        for user_id in source.get_ids():
            page=1
            while True:
                r=requests.get(constants.scrape_graveyarded.format(user_id, page*100, (page-1)*100))
                if r.content == b'[]':
                    break
                for item in r.json():
                    beatmap_id=item['beatmap_id']
                    time.sleep(constants.api_scrape_interval)
                    beatmap_checksum, beatmapset_id = api.query_osu_beatmap(beatmap_id)
                    beatmap=(beatmapset_id, beatmap_id, beatmap_checksum)
                    all_beatmaps.add(beatmap)
                    if beatmap_checksum == False:
                        # Not hosted
                        unavailable_beatmaps.add(beatmap)
                page+=1

    return all_beatmaps, unavailable_beatmaps

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
            time.sleep(constants.api_scrape_interval)
            if api.query_osu_beatmapset(beatmapset_id):
                unavailable_beatmaps.add(beatmap)
            beatmap=(beatmapset_id, None, None)
            all_beatmaps.add(beatmap)
        cursor=r.json()['nextPageCursor']
        if cursor == None:
            break

    return all_beatmaps, unavailable_beatmaps