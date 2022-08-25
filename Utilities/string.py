import re
from Utilities import data, constants
from Network import api

# Create userpage ids
def generate_userpage_source_key(users, scope, gamemode):
    pass
def generate_mappack_source_key(ids, gamemode):
    pass
def generate_osucollector_source_key(id):
    pass

# Extract (user_id, gamemode) from osu beatmap urls
# https://osu.ppy.sh/users/15656848/fruits
def parse_userpages_urlstring(urlstring):
    
    user_ids=set()
    ra = "(?<=users\/)(.*)" # matches format /user_id/gamemode
    # rb = "(.*\/b\/.*)" # matches format /b/xxxxx

    for user in re.findall(ra, urlstring):
        user_id=user[0]

        # check if gamemode is specified
        if len(user) > 1 and user[1] in constants.gamemode_dict:
            gamemode=constants.gamemode_dict[user[1]]
        else:
            gamemode=api.query_user_default_gamemode(user_id)
        user_ids.add(user_id, gamemode)
    return user_ids

    # for url in re.findall(rb, urlstring):
    #     try:
    #         r = requests.head(url, allow_redirects=True, timeout=10)
    #         beatmapset_ids.append(re.findall(ra, r.url)[0])
    #         time.sleep(data.get_settings().download_interval)
    #     except:
    #         pass
    # return beatmapset_ids

# Extract beatmapset_ids from osu collector urls
def parse_osucollector_urlstring(urlstring):
    pass
