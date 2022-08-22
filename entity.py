from Utilities import constants, misc

class UserSource:
    def __init__(self, ids, scope):
        self.ids=ids
        self.scope=scope
    def get_ids(self):
        return self.ids
    def set_ids(self, ids):
        self.ids=ids
    def get_scope(self):
        return self.scope
    def set_scope(self, scope):
        self.scope=scope

class TournamentSource:
    def __init__(self, id):
        self.id=id
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id=id

class OsucollectorSource:
    def __init__(self, id):
        self.id=id
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id=id

class MappackSource:
    def __init__(self, status, gamemode, download_count):
        self.number=download_count
        self.status=status
        self.gamemode=gamemode
    def get_status(self):
        return self.status
    def set_status(self, status):
        self.status=status
    def get_gamemode(self):
        return self.gamemode
    def set_gamemode(self, gamemode):
        self.gamemode=gamemode
    def get_download_count(self):
        return self.download_count
    def set_number(self, download_count):
        self.download_count=download_count

# Data for the sources tab
class Sources():
    def __init__(self):
        self.user_source={}
        self.osucollector_source={}
        self.mappack_source={}
        self.tournament_source={}

    def read(self):
        return self.user_source + self.osucollector_source + self.mappack_source + self.tournament_source
        
    def add_user_source(self, links, scope):
        key, data=misc.create_userpage_source(links, scope)
        self.user_source[key]=data

    def add_osucollector_source(self, links):
        key, data=misc.create_osucollector_source(links)
        self.osucollector_source[key]=data

    def add_mappack_source(self, status, gamemode, download_count):
        key, data=misc.create_mappack_source(status, gamemode, download_count)
        self.mappack_source[key]=data

    def add_tournament_source(self, selection):
        id=selection.split(":")[0] # SOFT-4: Springtime Osu!mania Free-for-all Tournament 4
        key, data=misc.create_tournament_source(id)
        self.tournament_source[key]=data

# Job
class Job:
    def __init__(self, source_id, beatmapset_ids):
        self.source_id=source_id
        self.beatmapset_ids=beatmapset_ids
    def get_source_id(self):
        return self.source_id
    def set_source_id(self, source_id):
        self.source_id=source_id
    def get_beatmapset_ids(self):
        return self.beatmapset_ids
    def set_beatmapset_ids(self, beatmapset_ids):
        self.beatmapset_ids=beatmapset_ids

# Settings
class Settings:
    def __init__(self):
        self.osu_install_folder=None
        self.oauth=(constants.oauth_client_id,constants.oauth_client_secret) #client id, client secret
        self.source_show_missing=True
        self.download_on_start=True
        self.xsrf_token=None
        self.download_interval=1000
