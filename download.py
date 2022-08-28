# downloading from mirror
# returns (success, )
import constants, data
import os
import requests
import time
import aiofiles
import aiohttp

async def download_beatmap(beatmapset_id):
    success=False
    settings=data.get_settings()
    filename = os.path.join(settings.osu_install_folder, "Songs", str(beatmapset_id) + ".osz")

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
                async with aiohttp.ClientSession() as session:
                    async with session.get(r.url, allow_redirects=True, headers=beatconnect_header) as r:
                        async with aiofiles.open(filename, mode="wb") as f:
                            await f.write(r.content)
                time.sleep(settings.download_interval/1000)
                success=os.path.isfile(filename)
            except:
                pass

    if not success and settings.download_from_osu and settings.valid_osu_cookies():
        url=constants.osu_beatmap_url_download.format(beatmapset_id)
        cookie={"XSRF-TOKEN":settings.xsrf_token,"osu_session":settings.osu_session}
        osu_header={ "referer":constants.osu_beatmap_url.format(beatmapset_id) }
        try:
            r = requests.get(url, allow_redirects=True, cookies=cookie, headers=osu_header)
            async with aiohttp.ClientSession() as session:
                async with session.get(r.url, allow_redirects=True, headers=beatconnect_header) as r:
                    async with aiofiles.open(filename, mode="wb") as f:
                        await f.write(r.content)
            time.sleep(settings.download_interval/1000)
            success=os.path.isfile(filename)
        except:
            pass

    return success