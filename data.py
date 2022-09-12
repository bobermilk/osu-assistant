# data provider (store variables, hardcode things and functions to get and set data)
from os.path import isfile
import pickle
import entity
from pubsub import pub

# Credentials
OAUTH_TOKEN=None

# Lists
MappackJson=None
TournamentJson=None

# data (singletons)
Sources=entity.Sources()
Jobs=entity.Jobs()
Settings=entity.Settings()

# Database of integers of ids
osudb_beatmap_ids=set()
osudb_beatmapset_ids=set()

# User toggles
cancel_jobs_toggle=False

def save_data():
    with open("osu-assistant.data", 'wb') as f:
        pickle.dump((OAUTH_TOKEN, Sources, Settings), f)

def load_data():
    global OAUTH_TOKEN, Sources, Settings
    if isfile("osu-assistant.data"):
        try:
            with open("osu-assistant.data", 'rb') as f:
                OAUTH_TOKEN, Sources, Settings = pickle.load(f)
                pub.sendMessage("update.sources")
        except:
            pub.sendMessage("show.dialog", msg="osu assistant data file is corrupted, please delete the osu-assistant.data file")
        return True
    else:
        return False # first time