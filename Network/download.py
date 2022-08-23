# downloading from mirror
# returns (success, )
from Utilities import constants, data
from Network import api
import os
import requests
import time

def download_beatmap(beatmapset_id):
    if not api.query_osu(beatmapset_id):
        return False

    success=False
    url=constants.beatconnect_beatmap_url.format(beatmapset_id)
    settings=data.get_settings()
    filename = os.path.join(settings.osu_install_folder, str(beatmapset_id) + ".osz")

    if os.path.isfile(filename):
        success = True

    if not success:
        try:
            r = requests.get(url, allow_redirects=True)
            with open(filename, "wb") as f:
                f.write(r.content)
            time.sleep(settings.download_interval/1000)
            success=True
        except:
            pass

    if not success and settings.download_from_osu and settings.valid_osu_cookies():
        cookie={"XSRF-TOKEN":settings.xsrf_token, "osu_session":settings.osu_session}
        header={ "referer":constants.osu_beatmap_url.format(beatmapset_id) }
        try:
            r = requests.get(url, allow_redirects=True, cookies=cookie, headers=header)
            with open(filename, "wb") as f:
                f.write(r.content)
            time.sleep(settings.download_interval/1000)
        except:
            pass

    if os.path.isfile(filename):
        print("\nDownloaded {}".format(beatmapset_id))
        success = True

    return success