from Network import scraper
from Utilities import constants, misc, data
from pubsub import pub
from copy import copy

# Used to cache beatmaps retrieved from update_sources() and record beatmap ids
# Note: the beatmaps is a set    of (beatmapset_id, beatmap_id, beatmap_checksum)
class Beatmaps():
    def __init__(self):
        self.all_beatmaps=set()
        self.unavailable_beatmaps=set()
        
    # def get_all_beatmapset(self):
    #     return self.all_beatmaps
    def get_available_beatmaps(self):
        return list(self.all_beatmaps-self.unavailable_beatmaps)
    def get_unavailable_beatmaps(self):
        return self.unavailable_beatmaps

    def query_cache(self, beatmapset_id):
        return beatmapset_id not in self.unavailable_beatmaps

    # caches api queries for beatmaps
    def cache_beatmaps(self, all_beatmaps, unavailable_beatmaps):
        self.all_beatmaps=all_beatmaps
        self.unavailable_beatmaps=unavailable_beatmaps
        
# Note: ids is a set of pairs (user_id, gamemode)
class UserpageSource(Beatmaps):
    def __init__(self, ids, scope):
        super().__init__()
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
        super().__init__()
        self.id=id
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id=id

class MappackSource(Beatmaps):
    def __init__(self, ids, gamemode):
        super().__init__()
        self.ids=ids
        self.gamemode=gamemode
    def get_ids(self):
        return self.ids
    def set_id(self, ids):
        self.ids=ids
    def get_gamemode(self):
        return self.gamemode
    def set_gamemode(self, gamemode):
        self.gamemode=gamemode   

class OsucollectorSource(Beatmaps):
    def __init__(self, id):
        super().__init__()
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

    async def refresh(self):
        # TODO: api shit, call query_osu and store beatmaps in source.all_beatmaps as a triple (beatmapsetid, beatmapid, checksum)
        for source in self.user_source:
            all_beatmaps, unavailable_beatmaps=scraper.get_userpage_beatmaps(source)
            source.cache_beatmaps(all_beatmaps, unavailable_beatmaps)
        for source in self.tournament_source:
            pass
        for source in self.mappack_source:
            pass
        for source in self.osucollector_source:
            beatmaps=scraper.get_osucollector_beatmaps(source)

        # refresh the jobs
        await data.get_jobs().refresh()
        # Update the views
        pub.sendMessage("update.sources")
        pub.sendMessage("update.activity")
        # Initiate automatic downloads
        if data.get_settings().download_on_start:
            await data.get_jobs().start_jobs()

    def add_user_source(self, links, scope):
        key, source=misc.create_userpage_source(links, scope)
        all_beatmaps, unavailable_beatmaps=scraper.get_userpage_beatmaps(source)
        source.cache_beatmaps(all_beatmaps, unavailable_beatmaps)
        self.user_source[key]=source

    def add_tournament_source(self, selection):
        tournament_id=selection.split(":")[0]
        key, source=misc.create_tournament_source(tournament_id, selection)
        all_beatmaps, unavailable_beatmaps=scraper.get_tournament_beatmaps(source)
        source.cache_beatmaps(all_beatmaps, unavailable_beatmaps)
        self.tournament_source[key]=source

    def add_mappack_source(self, ids, gamemode):
        key, source=misc.create_mappack_source(ids, gamemode)
        all_beatmaps, unavailable_beatmaps=scraper.get_mappack_beatmaps(source)
        source.cache_beatmaps(all_beatmaps, unavailable_beatmaps)
        self.mappack_source[key]=source

    def add_osucollector_source(self, link):
        key, source=misc.create_osucollector_source(link)
        all_beatmaps, unavailable_beatmaps=scraper.get_osucollector_beatmaps(source)
        source.cache_beatmaps(all_beatmaps, unavailable_beatmaps)
        self.osucollector_source[key]=source

# Job
class Job:
    # source_key is the key used to get source by data.get_sources().get_source()
    def __init__(self, source_key, beatmapset_ids):
        self.job_source_key=source_key
        self.beatmapset_ids=beatmapset_ids
        self.status=constants.job_status[1] # status: invalid, pending, downloading, downloaded
    def get_job_source_key(self):
        return self.job_source_key
    def set_job_source(self, source):
        self.job_source=source
    def get_beatmapset_ids(self):
        return self.beatmapset_ids
    def set_beatmapset_ids(self, beatmapset_ids):
        self.beatmapset_ids=beatmapset_ids
    def get_status(self):
        return self.status
    def set_status(self, status_id):
        self.status=constants.job_status[status_id]

class Jobs:
    def __init__(self):
        # job_queue: a ordered list to determine job priority in decending order
        self.job_queue=[]

    def read(self):
        return copy(self.job_queue)

    # Note: this is responsible for caching source available beatmaps and updating the job list
    # Note: this is called after Sources.update() has been called
    async def refresh(self):
        #job_queue_copy.pop() -> maps=diff(job.beatmapsetids , db.get_data())
        job_queue=[]
        for source_key, source in data.get_sources().read():
            pending_downloads=misc.diff_local_and_source(source)
            job_queue.append(Job(source_key, pending_downloads))

        self.job_queue=job_queue
        pub.sendMessage("update.activity")

    async def start_jobs(self):
        # refresh --> job_queue.pop() -> download(maps) -> write_collections -> progressbar+=1 
        print("Jobs: " + str([x.get_beatmapset_ids() for x in self.read()]))
        while len(self.job_queue) > 0:
            job=self.job_queue.pop(0)
            misc.do_job(job) # TODO: use the success/failure of the job to show notification or something
            pub.sendMessage("update.activity")
        pub.sendMessage("update.activity")


# Settings
class Settings:
    def __init__(self):
        self.osu_install_folder=None
        self.oauth=None
        self.source_show_missing=True
        self.download_on_start=True
        self.download_from_osu=False
        self.xsrf_token=""
        self.osu_session=""
        self.download_interval=1000
    def valid_osu_cookies(self):
        if self.xsrf_token=="" or self.xsrf_token.isspace():
            return False
        if self.osu_session=="" or self.osu_session.isspace():
            return False
        return True
