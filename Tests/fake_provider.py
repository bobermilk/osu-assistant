import entity as e
import os
import Utilities.sensitive_data as sensitive_data

class Sources(e.Sources):
    def __init__(self):
        super().__init__()
        # Create mock data
        self.user_source["User: played=all bobermilk"]=e.UserpageSource(["https://osu.ppy.sh/users/15656848"],[False,True,True,False,False,False,False,False])
        self.user_source["User: played=top&fav status=r&gp&p&g mode=m Polyester"]=e.UserpageSource(["https://osu.ppy.sh/users/11106874/mania"],[True,True,False,True,False,True,True,True])
        self.user_source["User: status=r&l&gp&p&g mode=m -mint- riunosk"]=e.UserpageSource(["https://osu.ppy.sh/users/5594381", "https://osu.ppy.sh/users/8976576"],[False,False,False,True,True,True,True,True])

        self.tournament_source["Tournament: osu!mania 4K World Cup 2022"]=e.TournamentSource("MWC-2022")
        self.tournament_source["Tournament: Springtime Osu!mania Free-for-all Tournament 4"]=e.TournamentSource("SOFT-4")

        self.mappack_source["Mappack: mode=m #109 #108"]=e.MappackSource({109, 108},4)

        self.osucollector_source["Osucollector: DT SPEED"]=e.OsucollectorSource(4869)

class Jobs(e.Jobs):
    def __init__(self):
        super().__init__()
        job_queue=[]
        job_queue.append(e.Job("User: played=all bobermilk", [1727891, 1825575, 1622277]))
        job_queue.append(e.Job("User: played=top&fav status=r&gp&p&g Polyester", [1701223, 1772954]))
        job_queue.append(e.Job("User: status=r&l&gp&p&g -mint- riunosk", [1622277]))
        job_queue.append(e.Job("Tournament: osu!mania 4K World Cup 2022", [1806117, 1753715]))
        job_queue.append(e.Job("Tournament: Springtime Osu!mania Free-for-all Tournament 4", [1738470, 1707554]))
        job_queue.append(e.Job("Mappack: mode=m #109 #108", [1765297, 1501294]))
        job_queue.append(e.Job("Osucollector: DT SPEED", [1734430]))

        self.job_queue=job_queue

class Settings(e.Settings):
    def __init__(self):
        super().__init__()
        self.osu_install_folder=os.getcwd()
        self.oauth=(sensitive_data.oauth_client_id, sensitive_data.oauth_client_secret)
        self.xsrf_token=sensitive_data.xsrf_token
        self.osu_session=sensitive_data.osu_session
        self.download_from_osu=True
        self.download_interval=2000

Sources=Sources()
Jobs=Jobs()
Settings=Settings()