import constants, data
import os
import aiofiles

# The exit codes are as follows
# 0: Failed to download
# 1: Success from chimu
# 2. Success from osu
async def download_beatmap(session, beatmapset_id):
    success=0
    settings=data.Settings
    filename = os.path.join(settings.osu_install_folder, "Songs", str(beatmapset_id) + ".osz")
    try:
        # If osu install folder is none, it will just download at current directory
        os.mkdir(os.path.join(settings.osu_install_folder, "Songs"))
    except:
        pass
    if os.path.isfile(filename):
        success = True

    if not success:
        try: 
            url=constants.chimu_beatmap_url.format(beatmapset_id)
            async with session.get(url, allow_redirects=True) as s:
                if s.status==200:
                    async with aiofiles.open(filename, mode="wb") as f:
                        await f.write(await s.read())
            if os.path.isfile(filename) and os.stat(filename).st_size == 0:
                os.remove(filename)
                success=0 # Empty file (no bytes received)
            else:
                success=1
        except:
            return success # download failed

    if not success and settings.download_from_osu and settings.valid_osu_cookies:
        url=constants.osu_beatmap_url_download.format(beatmapset_id)
        cookie={"XSRF-TOKEN":settings.xsrf_token,"osu_session":settings.osu_session}
        osu_header={ "referer":constants.osu_beatmap_url.format(beatmapset_id) }
        try:
            async with session.get(url, allow_redirects=True, cookies=cookie, headers=osu_header) as s:
                async with aiofiles.open(filename, mode="wb") as f:
                    await f.write(await s.read())
            if os.path.isfile(filename) and os.stat(filename).st_size == 0:
                os.remove(filename)
                success=0 # Empty file (no bytes received)
            else:
                success=2
        except:
            return success

    return success