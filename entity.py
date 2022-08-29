import scraper
import constants, misc, data
from pubsub import pub
from copy import copy

# Used to cache beatmaps retrieved from update_sources() and record beatmap ids
# Note: the beatmaps is a set    of (beatmapset_id, beatmap_id, beatmap_checksum)
class Beatmaps():
    def __init__(self):
        self.all_beatmaps=set()
        self.unavailable_beatmaps=set() # if api checksum is none, the beatmap will not be there forever
        self.missing_beatmaps=set() # used solely for showing beatmap status on the sources tab
        
    # def get_all_beatmapset(self):
    #     return self.all_beatmaps
    def get_available_beatmaps(self):
        return list(self.all_beatmaps-self.unavailable_beatmaps)
        
    def get_unavailable_beatmaps(self):
        return self.unavailable_beatmaps

    def query_cache(self, beatmapset_id):
        return beatmapset_id not in self.unavailable_beatmaps

    # caches api queries for beatmaps
    def cache_beatmaps(self, all_beatmaps):
        self.all_beatmaps=all_beatmaps
    
    def cache_unavailable_beatmap(self, unavailable_beatmap):
        self.unavailable_beatmaps.add(unavailable_beatmap)
    def cache_missing_beatmap(self, beatmap):
        self.missing_beatmaps.add(beatmap)
    def uncache_missing_beatmap(self, beatmap):
        if beatmap in self.missing_beatmaps:
            self.missing_beatmaps.remove(beatmap)
        
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
    def __init__(self, ids):
        super().__init__()
        self.ids=ids
    def get_ids(self):
        return self.ids
    def set_id(self, ids):
        self.ids=ids

class OsucollectorSource(Beatmaps):
    def __init__(self, ids):
        super().__init__()
        self.ids=ids
    def get_ids(self):
        return self.ids
    def set_ids(self, ids):
        self.ids=ids

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
            all_beatmaps=scraper.get_userpage_beatmaps(source)
            source.cache_beatmaps(all_beatmaps)
        for source in self.tournament_source:
            all_beatmaps=scraper.get_tournament_beatmaps(source)
            source.cache_beatmaps(all_beatmaps)
        for source in self.mappack_source:
            all_beatmaps=scraper.get_mappack_beatmaps(source)
            source.cache_beatmaps(all_beatmaps)
        for source in self.osucollector_source:
            all_beatmaps=scraper.get_osucollector_beatmaps(source)
            source.cache_beatmaps(all_beatmaps)

        # refresh the jobs
        await data.get_jobs().refresh()
        # Update the views
        pub.sendMessage("update.sources")
        # Initiate automatic downloads
        if data.get_settings().download_on_start:
            await data.get_jobs().start_jobs()

    async def add_user_source(self, links, scope):
        key, source=misc.create_userpage_source(links, scope)
        all_beatmaps=scraper.get_userpage_beatmaps(source)
        source.cache_beatmaps(all_beatmaps)
        self.user_source[key]=source
        # refresh the jobs
        await data.get_jobs().refresh()
        # Update the views
        pub.sendMessage("update.sources")
        

    async def add_tournament_source(self, selection):
        tournament_id=selection.split(":")[0]
        key, source=misc.create_tournament_source(tournament_id, selection)
        all_beatmaps=scraper.get_tournament_beatmaps(source)
        source.cache_beatmaps(all_beatmaps)
        self.tournament_source[key]=source
        # refresh the jobs
        await data.get_jobs().refresh()
        # Update the views
        pub.sendMessage("update.sources")

    async def add_mappack_source(self, ids):
        key, source=misc.create_mappack_source(ids)
        all_beatmaps=scraper.get_mappack_beatmaps(source)
        source.cache_beatmaps(all_beatmaps)
        self.mappack_source[key]=source
        # refresh the jobs
        await data.get_jobs().refresh()
        # Update the views
        pub.sendMessage("update.sources")

    async def add_osucollector_source(self, link):
        key, source=misc.create_osucollector_source(link)
        all_beatmaps=scraper.get_osucollector_beatmaps(source)
        source.cache_beatmaps(all_beatmaps)
        self.osucollector_source[key]=source
        # refresh the jobs
        await data.get_jobs().refresh()
        # Update the views
        pub.sendMessage("update.sources")

# Job
class Job:
    # source_key is the key used to get source by data.get_sources().get_source()
    def __init__(self, source_key, downloads):
        self.job_source_key=source_key
        self.job_downloads=downloads
    def get_job_downloads_cnt(self):
        return len(self.job_downloads)
    def get_job_downloads(self):
        return self.job_downloads
    def set_job_downloads(self, downloads):
        self.job_downloads=downloads
    def get_job_source_key(self):
        return self.job_source_key
    def set_job_source_key(self, source):
        self.job_source_key=source

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
            downloads=misc.diff_local_and_source(source)
            job_queue.append(Job(source_key, downloads))

        self.job_queue=job_queue
        pub.sendMessage("update.activity")

    def get_job_cnt(self):
        return len(self.job_queue)

    async def start_jobs(self):
        # refresh --> job_queue.pop() -> download(maps) -> write_collections -> progressbar+=1 
        initial_job_cnt=self.get_job_cnt()
        success=1
        while self.get_job_cnt() > 0:
            job=self.job_queue.pop(0)
            pub.sendMessage("update.progress", value=0, range=0, progress_message=f"Downloading {job.get_job_source_key()} ({initial_job_cnt-self.get_job_cnt()}/{initial_job_cnt} jobs)")
            success=await misc.do_job(job)
            if data.cancel_jobs_toggle:
                break # Terminate all jobs
            pub.sendMessage("update.activity")
        # Check last success to see if we should show the No pending downloads
        if success:
            pub.sendMessage("update.progress", value=None, range=None, progress_message=f"{initial_job_cnt} jobs completed successfully")
            pub.sendMessage("update.activity")
        else:
            data.cancel_jobs_toggle=False
            pub.sendMessage("update.progress", value=None, range=None, progress_message=f"Cancelled running job")
            await self.refresh()
            pub.sendMessage("update.activity")
            pub.sendMessage("enable.job_toggle_button")


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