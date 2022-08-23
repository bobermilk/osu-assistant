from Utilities import constants, misc

# Note: the beatmaps below is a list of beatmapid
# TODO: check if beatmaps that are unavailable can be come availabel again; unavailable_beatmaps should hence have an add function  
class UserSource:
    def __init__(self, ids, scope):
        self.ids=ids
        self.scope=scope
        self.all_beatmaps=[]
        self.unavailable_beatmaps=[]
    def get_ids(self):
        return self.ids
    def set_ids(self, ids):
        self.ids=ids
    def get_scope(self):
        return self.scope
    def set_scope(self, scope):
        self.scope=scope
    def get_all_beatmaps(self):
        return self.all_beatmaps
    def get_unavailable_beatmaps(self):
        return self.unavailable_beatmaps
    def add_uanavilable_beatmaps(self, unavailable_beatmap):
        self.unavailable_beatmaps.append(unavailable_beatmap)
    def add_beatmap(self, beatmap):
        self.beatmaps.append(beatmap)
    def delete_beatmap(self, beatmap):
        self.beatmaps.remove(beatmap)

class TournamentSource:
    def __init__(self, id):
        self.id=id
        self.all_beatmaps=[]
        self.unavailable_beatmaps=[]
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id=id
    def get_all_beatmaps(self):
        return self.all_beatmaps
    def get_unavailable_beatmaps(self):
        return self.unavailable_beatmaps
    def add_uanavilable_beatmaps(self, unavailable_beatmap):
        self.unavailable_beatmaps.append(unavailable_beatmap)
    def add_beatmap(self, beatmap):
        self.beatmaps.append(beatmap)
    def delete_beatmap(self, beatmap):
        self.beatmaps.remove(beatmap)

class MappackSource:
    def __init__(self, status, gamemode, download_count):
        self.number=download_count
        self.status=status
        self.gamemode=gamemode
        self.all_beatmaps=[]
        self.unavailable_beatmaps=[]
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
    def set_download_count(self, download_count):
        self.download_count=download_count
    def get_all_beatmaps(self):
        return self.all_beatmaps
    def get_unavailable_beatmaps(self):
        return self.unavailable_beatmaps
    def add_uanavilable_beatmaps(self, unavailable_beatmap):
        self.unavailable_beatmaps.append(unavailable_beatmap)
    def add_beatmap(self, beatmap):
        self.beatmaps.append(beatmap)
    def delete_beatmap(self, beatmap):
        self.beatmaps.remove(beatmap)

class OsucollectorSource:
    def __init__(self, id):
        self.id=id
        self.all_beatmaps=[]
        self.unavailable_beatmaps=[]
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id=id
    def get_all_beatmaps(self):
        return self.all_beatmaps
    def get_unavailable_beatmaps(self):
        return self.unavailable_beatmaps
    def add_uanavilable_beatmaps(self, unavailable_beatmap):
        self.unavailable_beatmaps.append(unavailable_beatmap)
    def add_beatmap(self, beatmap):
        self.beatmaps.append(beatmap)
    def delete_beatmap(self, beatmap):
        self.beatmaps.remove(beatmap)
    

# Data for the sources tab
class Sources():
    def __init__(self):
        self.user_source={}
        self.osucollector_source={}
        self.mappack_source={}
        self.tournament_source={}

    def read(self):
        return list(self.user_source.items()) + list(self.tournament_source.items()) + list(self.mappack_source.items()) + list(self.osucollector_source.items())

    def update(self):
        # apy.py stuff here
        # output: store beatmaps in source.all_beatmaps
        pass

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

class Jobs:
    def __init__(self):
        # job_queue: a fifo queue of lists
        # status: invalid, pending, downloading, downloaded
        self.job_queue=None
        self.status=constants.job_status[1]

    # Note: this is called after source.update() has been called
    def refresh_jobs(self):
        #job_queue_copy.pop() -> maps=diff(job.beatmapsetids , db.get_data())
        pass

    def get_jobs(self):
        return self.job_queue
        
    def start_jobs(self):
        # refresh_jobs --> job_queue.pop() -> download(maps) -> write_collections -> progressbar+=1 
        pass

# Settings
class Settings:
    def __init__(self):
        self.osu_install_folder=None
        self.oauth=(constants.oauth_client_id,constants.oauth_client_secret) #client id, client secret
        self.source_show_missing=True
        self.download_on_start=True
        self.xsrf_token=None
        self.download_interval=1000
