from Utilities import constants, misc, data
import queue

# Used to cache beatmaps retrieved from update_sources() and record beatmap ids
# Note: the beatmaps is a list of (beatmapset_id, beatmapid)
class Beatmaps():
    def __init__(self):
        self.all_beatmaps=[]
        self.unavailable_beatmaps=[]
    # def get_all_beatmapset(self):
    #     return self.all_beatmaps
    # def get_available_beatmaps(self):
    #     return list(set(self.all_beatmaps)-set(self.unavailable_beatmaps))
    # def get_unavailable_beatmaps(self):
    #     return self.unavailable_beatmaps
    # def add_uanavilable_beatmaps(self, unavailable_beatmap):
    #     self.unavailable_beatmaps.append(unavailable_beatmap)
    # def add_beatmap(self, beatmap):
    #     self.beatmaps.append(beatmap)
    # def delete_beatmap(self, beatmap):
    #     self.beatmaps.remove(beatmap)

# TODO: check if beatmaps that are unavailable can be come availabel again; unavailable_beatmaps should hence have an add function  
class UserSource(Beatmaps):
    def __init__(self, ids, scope):
        super().__init__(self)
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

class TournamentSource(Beatmaps):
    def __init__(self, id):
        super().__init__(self)
        self.id=id
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id=id

class MappackSource(Beatmaps):
    def __init__(self, status, gamemode, download_count):
        super().__init__(self)
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
    def set_download_count(self, download_count):
        self.download_count=download_count

class OsucollectorSource(Beatmaps):
    def __init__(self, id):
        super().__init__(self)
        self.id=id
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id=id

# Data for the sources tab
class Sources():
    def __init__(self):
        self.user_source={}
        self.osucollector_source={}
        self.mappack_source={}
        self.tournament_source={}

    # get source object by using source_key to query the source dicts
    def get_source(self, source_key):
        if source_key in self.user_source:
            return self.user_source[source_key]
        if source_key in self.tournament_source:
            return self.tournament_source[source_key]
        if source_key in self.mappack_source:
            return self.mappack_source[source_key]
        if source_key in self.osucollector_source:
            return self.osucollector_source[source_key]
        return None

    # returns [(source_key1, source1), (source_key2, source2), ...]
    def read(self):
        return list(self.user_source.items()) + list(self.tournament_source.items()) + list(self.mappack_source.items()) + list(self.osucollector_source.items())

    def update(self):
        # apy.py stuff here
        # output: store beatmaps in source.all_beatmaps as a pair (beatmapsetid, beatmapid)
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
    # source_key is the key used to get source by data.Sources.get_source()
    def __init__(self, source_key, beatmapset_ids):
        self.job_source_key=source_key
        self.beatmapset_ids=beatmapset_ids
    def get_job_source_key(self):
        return self.job_source_key
    def set_job_source(self, source):
        self.job_source=source
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

    def get_jobs(self):
        return self.job_queue

    # Note: this is called after Sources.update() has been called
    def refresh_jobs(self):
        #job_queue_copy.pop() -> maps=diff(job.beatmapsetids , db.get_data())
        job_queue=queue.Queue()
        pending_beatmapset_ids=[]
        for source_key, source in data.get_sources_list():
            pending_beatmapset_ids=misc.diff_local_and_source(source)
            job_queue.append(Job(source_key, pending_beatmapset_ids))

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
