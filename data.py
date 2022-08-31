# data provider (store variables, hardcode things and functions to get and set data)
from genericpath import isfile
import pickle
import entity
import constants
import fake_provider as fake
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

# Use these test functions below for testing purposes
# The sources tab will only display the mock data when DEBUG=True
# Adding things will add to the actual data, but it is not shown

def get_sources():
    if constants.DEBUG:
        return Sources
    else:
        return Sources

def get_jobs():
    if constants.DEBUG:
        return Jobs
    else:
        return Jobs
        
def get_settings():
    if constants.DEBUG:
        return fake.Settings
    else:
        return Settings

def save_data():
    with open("osu-assistant.data", 'wb') as f:
        pickle.dump((Sources, Settings), f)

def load_data():
    global Sources, Settings
    if isfile("osu-assistant.data"):
        try:
            with open("osu-assistant.data", 'rb') as f:
                Sources, Settings = pickle.load(f)
                pub.sendMessage("update.sources")
        except:
            pub.sendMessage("show.dialog", msg="osu assistant data file is corrupted, please delete the osu-assistant.data file")