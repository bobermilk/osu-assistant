# for flask and osu api requests

import time
import requests
import json
import data, constants

# FLASK API
def query_flask_tournaments(tournament_id):
    json=b''
    return json 

# OSU API 
def query_osu_user_beatmapsets(user_id, type):
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {get_token()}",
    }
    page=1
    jsons=[]
    while True:
        response=requests.get(f"{constants.OSU_API_URL}/users/{user_id}/beatmapsets/{type}?limit={page*100}&offset={(page-1)*100}", headers=headers)
        time.sleep(constants.api_get_interval)
        j=response.json() # https://osu.ppy.sh/docs/index.html#get-user-beatmaps
        if str(j)=="[]":
            break
        jsons.append(j)
        page+=1
    return jsons


# returns (hash, beatmapset_id) for validity check and use the output to write collections
def query_osu_beatmap(beatmap_id):
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {get_token()}",
    }

    response=requests.get(f"{constants.OSU_API_URL}/beatmaps/{beatmap_id}", headers=headers)
    time.sleep(constants.api_get_interval)
    j=response.json()
    try:
        return j["checksum"], j["beatmapset_id"]
    except:
        # The beatmap is not hosted
        return 0,0

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

# Generate a oauth token
def get_token():
    if data.OAUTH_TOKEN is not None:
        return data.OAUTH_TOKEN

    credentials={
        'client_id': data.get_settings().oauth[0],
        'client_secret': data.get_settings().oauth[1],
        'grant_type': 'client_credentials',
        'scope': 'public'
    }
    response=requests.post(constants.OSU_TOKEN_URL, data=credentials)
    try:
        data.OAUTH_TOKEN=response.json().get('access_token')
    except:
        raise Exception("Invaild oauth token, osu assistant can't work without it")
    return data.OAUTH_TOKEN
