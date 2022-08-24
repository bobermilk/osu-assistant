import os
DEBUG=True

test_folder=os.getcwd()
request_timeout=10

# urlsh
OSU_API_URL = "https://osu.ppy.sh/api/v2"
OSU_TOKEN_URL = 'https://osu.ppy.sh/oauth/token'

beatconnect_beatmap_url="https://beatconnect.io/b/{}"
osu_beatmap_url="https://osu.ppy.sh/beatmapsets/{}"
osu_beatmap_url_download="https://osu.ppy.sh/beatmapsets/{}/download"

# dicts
gamemode_dict={ 1: "osu", 2:"taiko", 3:"catch", 4:"mania" }
job_status={ 0: "invalid", 1: "pending", 2: "downloading", 3: "downloaded" } # Used to text progress of jobs

# strings
activity_stop="Stop Downloading"
activity_start="Start Downloading (top to bottom)"
