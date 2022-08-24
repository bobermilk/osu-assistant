# downloading from mirror
# returns (success, )
from Utilities import constants, data, io
from Network import api
import os
import requests
import time

def download_beatmap(beatmapset_id):
    if not api.query_osu(beatmapset_id):
        return False

    success=False
    settings=data.get_settings()
    filename = os.path.join(settings.osu_install_folder, str(beatmapset_id) + ".osz")

    if os.path.isfile(filename):
        success = True

    if not success:
        url=constants.beatconnect_beatmap_url.format(beatmapset_id)
        beatconnect_header={ "referer":"https://beatconnect.io/" , "host":"beatconnect.io"}
        try:
            r = requests.head(url, allow_redirects=True, timeout=constants.request_timeout, headers=beatconnect_header)
            print(url+" "+str(r))
        except:
            return False

        if r.status_code==200:
            try:
                r = requests.get(r.url, allow_redirects=True, headers=beatconnect_header)
                with open(filename, "wb") as f:
                    f.write(r.content)
                time.sleep(settings.download_interval/1000)
                success=io.file_exist(filename)
            except:
                pass

    if not success and settings.download_from_osu and settings.valid_osu_cookies():
        url=constants.osu_beatmap_url_download.format(beatmapset_id)
        cookie={"XSRF-TOKEN":settings.xsrf_token,"osu_session":settings.osu_session}
        print(settings.xsrf_token,)
        osu_header={ "referer":constants.osu_beatmap_url.format(beatmapset_id) }
        try:
            r = requests.get(url, allow_redirects=True, cookies=cookie, headers=osu_header)
            with open(filename, "wb") as f:
                f.write(r.content)
            time.sleep(settings.download_interval/1000)
            success=io.file_exist(filename)
        except:
            pass

    return success