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

    settings=data.get_settings()
    filename = os.path.join(settings.osu_install_folder, str(beatmapset_id) + ".osz")

    if os.path.isfile(filename):
        return True

    url=constants.beatconnect_beatmap_url.format(beatmapset_id)
    try:
        r = requests.head(url, allow_redirects=True, timeout=constants.request_timeout)
    except:
        return False

    if r.status_code==200:
        try:
            r = requests.get(r.url, allow_redirects=True)
            with open(filename, "wb") as f:
                f.write(r.content)
            time.sleep(settings.download_interval/1000)
        except:
            if settings.download_from_osu and settings.valid_osu_cookies():
                url=constants.osu_beatmap_url_download.format(beatmapset_id)
                try:
                    r = requests.head(url, allow_redirects=True, timeout=constants.request_timeout)
                except:
                    return False

                if r.status_code==200:
                    cookie={"XSRF-TOKEN":settings.xsrf_token, "osu_session":settings.osu_session}
                    header={ "referer":constants.osu_beatmap_url.format(beatmapset_id) }
                    try:
                        r = requests.get(r.url, allow_redirects=True, cookies=cookie, headers=header)
                        with open(filename, "wb") as f:
                            f.write(r.content)
                        time.sleep(settings.download_interval/1000)
                    except:
                        pass

    if os.path.isfile(filename):
        print("\nDownloaded {}".format(beatmapset_id))
        success = True

    return success