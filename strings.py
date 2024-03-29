import re
import constants
import random, string

# Create userpage ids
def generate_userpage_source_key(users, scope):
    played="played="
    if scope[0]:
        played+="top&"
    if scope[1]:
        played+="fav&"
    if scope[2]:
        played+="all"
    if played[-1]=='&':
        played=played[:-1]
    status="status="
    if scope[3]:
        status+="r&"
    if scope[4]:
        status+="l&"
    if scope[5]:
        status+="p&"
    if scope[6]:
        status+="g"
    if status[-1]=='&':
        status=status[:-1]
    ids="ids="
    for userid, gamemode in users:
        ids+=str(userid)
        ids+=","
    if ids[-1]==",":
        ids=ids[:-1]
    return f"User: {played} {status} {ids}"
def generate_mappack_source_key(mappack_ids):
    ids="ids="
    for id in mappack_ids:
        ids+=str(id)
        ids+=","
    if ids[-1]==",":
        ids=ids[:-1]
    return f"Mappack: {ids}"
def generate_osucollector_source_key(collection_ids):
    ids="ids="
    for id in collection_ids:
        ids+=str(id)
        ids+=","
    if ids[-1]==",":
        ids=ids[:-1]
    return f"Osucollector: {ids}"

def generate_osuweblinks_source_key(title):
    return f"Osuweblinks: {title}"

# Extract (user_id, gamemode) from osu beatmap urls
# https://osu.ppy.sh/users/15656848/fruits
def parse_userpages_urlstrings(urlstring):
    users=set()
    ra = "(?<=users\/)(.*)" # matches format /user_id/gamemode

    for user in re.findall(ra, urlstring):
        user=user.split("/")
        user_id=int(user[0])

        # check if gamemode is specified
        if len(user) > 1 and user[1] in constants.gamemode_dict:
            gamemode=user[1]
        else:
            gamemode=""
        users.add((user_id, gamemode))

    return users

    # for url in re.findall(rb, urlstring):
    #     try:
    #         r = requests.head(url, allow_redirects=True, timeout=10)
    #         beatmapset_ids.append(re.findall(ra, r.url)[0])
    #         time.sleep(data.Settings.download_interval)
    #     except:
    #         pass
    # return beatmapset_ids

# Extract beatmapset_ids from osu collector urls
def parse_osucollector_urlstrings(urlstring):
    collections=set()
    ra = "(?<=collections\/)([0-9]*)" # matches format /collections/collection_id

    for collection_id in re.findall(ra, urlstring):
        collections.add(int(collection_id))

    return collections

# Extract beatmap_id, beatmapset_id from osu website urls
def parse_osuweblinks_urlstrings(urlstring):
    beatmapset_ids=set() # beatmapset_id
    beatmap_ids=set() # (beatmapset_id, beatmap_id) cant use dict cuz multiple same key

    ra = "(?<=beatmapsets\/)(.*)" # matches format beatmapset_id#gamemode/beatmap_id

    for beatmap_data in re.findall(ra, urlstring):
        # beatmap_id
        data=re.findall(r'\d+', beatmap_data)
        if len(data)==1:
            beatmapset_ids.add(data[0])
        elif len(data)==2:
            beatmapset_ids.add(data[0])
            beatmap_ids.add(data[1])

    return beatmapset_ids, beatmap_ids

def generate_random_name(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def generate_collection_name(n):
    letters=''
    while n:
        letters+=(chr(64+n%25))
        n//=25 # int division
    return letters