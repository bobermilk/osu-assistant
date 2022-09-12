# for flask and osu api requests
from pubsub import pub
import time
import requests
import json
import data, constants, oauth
import webbrowser
import asyncio

# OSU API 
async def query_osu_user_beatmapsets(session, user_id, type):
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {get_token()}",
    }
    page=1
    jsons=[]
    while True:
        response=await session.get(f"{constants.OSU_API_URL}/users/{user_id}/beatmapsets/{type}?limit={page*100}&offset={(page-1)*100}", headers=headers)
        await asyncio.sleep(constants.api_get_interval)
        j=await response.json() # https://osu.ppy.sh/docs/index.html#get-user-beatmaps
        if str(j)=="[]":
            break
        jsons.append(j)
        page+=1
    return jsons


# returns (hash, beatmapset_id) for validity check and use the output to write collections
async def query_osu_beatmap(session, beatmap_id):
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {get_token()}",
    }

    response=await session.get(f"{constants.OSU_API_URL}/beatmaps/{beatmap_id}", headers=headers)
    await asyncio.sleep(constants.api_get_interval)
    j=await response.json()
    try:
        return j["checksum"], j["beatmapset_id"]
    except:
        # The beatmap is not hosted
        return None,None

# check if beatmapset exist
def query_osu_beatmapset(beatmapset_id):
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {get_token()}",
    }

    response=requests.get(f"{constants.OSU_API_URL}/beatmapsets/{beatmapset_id}", headers=headers)
    time.sleep(constants.api_get_interval)
    j=json.loads(response.text)
    return "error" in j

def test_oauth(oauth):
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {oauth}"
    }
    response=requests.get(f"https://osu.ppy.sh/api/v2/beatmapsets/1", headers=headers)
    try:
        response.json()["artist"]
    except:
        return False
    return True

def get_oauth(self):
    webbrowser.open(constants.oauth_url)
    oauth.ask_token()

# Generate a oauth token
def get_token():
    if data.OAUTH_TOKEN is not None and test_oauth(data.OAUTH_TOKEN):
        return data.OAUTH_TOKEN
    else:
        get_oauth(None)
        pub.sendMessage("show.dialog", msg="Api access is required and is not granted. Please go to your web browser and click allow")
        return None

async def check_cookies(session):
    url=constants.osu_beatmap_url_download.format(1)
    settings=data.Settings
    cookie={"XSRF-TOKEN":settings.xsrf_token,"osu_session":settings.osu_session}
    osu_header={ "referer":constants.osu_beatmap_url.format(1) }
    try:
        async with session.head(url, allow_redirects=True, cookies=cookie, headers=osu_header) as s:
            if s.status==200:
                settings.valid_osu_cookies=True
    except:
        settings.valid_osu_cookies=False
        pub.sendMessage("show.dialog", msg="Invalid XSRF-TOKEN or osu_session provided")