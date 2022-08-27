import os
DEBUG=True

test_folder=os.getcwd()
request_timeout=10
api_get_interval=0.5 # actual api

# scraper.py endpoints
user_url="https://osu.ppy.sh/users/"
#scrape_pinned=user_url+"{}/scores/pinned?mode={}&limit={}&offset={}"
scrape_top_plays=user_url+"{}/scores/best?mode={}&limit={}&offset={}"
#scrape_first_place=user_url+"{}/scores/firsts?mode={}&limit={}&offset={}"
scrape_favourites=user_url+"{}/beatmapsets/favourite?limit={}&offset={}"
scrape_everything=user_url+"{}/beatmapsets/most_played?limit={}&offset={}"
scrape_ranked=user_url+"{}/beatmapsets/ranked?limit={}&offset={}"
scrape_loved=user_url+"{}/beatmapsets/loved?limit={}&offset={}"
scrape_guest_participation=user_url+"{}/beatmapsets/guest?limit={}&offset={}"
scrape_pending=user_url+"{}/beatmapsets/pending?limit={}&offset={}"
scrape_graveyarded=user_url+"{}/beatmapsets/graveyard?limit={}&offset={}"

osucollector_url="https://osucollector.com/api/collections/{}/beatmapsv2?perPage={}&sortBy=beatmapset.artist&orderBy=asc"
# urls
OSU_API_URL = "https://osu.ppy.sh/api/v2"
OSU_TOKEN_URL = 'https://osu.ppy.sh/oauth/token'

beatconnect_beatmap_url="https://beatconnect.io/b/{}"
osu_beatmap_url="https://osu.ppy.sh/beatmapsets/{}"
osu_beatmap_url_download="https://osu.ppy.sh/beatmapsets/{}/download"
osu_beatmap_url_full="https://osu.ppy.sh/beatmapsets/{}#{}/{}"

# dicts
gamemode_dict={ "osu":1, "taiko":2, "fruits":3, "mania":4 }
job_status={ 0: "invalid", 1: "pending", 2: "downloading", 3: "downloaded" } # Used to text progress of jobs

# strings
activity_stop="Stop Downloading"
activity_start="Start Downloading (top to bottom)"
