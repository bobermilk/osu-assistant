import entity as e

class Sources():
    def __init__(self):
        self.user_source={}
        self.osucollector_source={}
        self.mappack_source={}
        self.tournament_source={}

        # Create mock data
        self.user_source["User: played=all bobermilk"]=e.UserSource(["https://osu.ppy.sh/users/15656848"],[0,1,1,0,0,0,0,0])
        self.user_source["User: played=top&fav status=r&gp&p&g Polyester"]=e.UserSource(["https://osu.ppy.sh/users/11106874/mania"],[1,1,0,1,0,1,1,1])
        self.user_source["User: status=r&l&gp&p&g -mint- riunosk"]=e.UserSource(["https://osu.ppy.sh/users/5594381", "https://osu.ppy.sh/users/8976576"],[0,0,0,1,1,1,1,1])

        self.tournament_source["Tournament: osu!mania 4K World Cup 2022"]=e.TournamentSource("MWC-2022")
        self.tournament_source["Tournament: Springtime Osu!mania Free-for-all Tournament 4"]=e.TournamentSource("SOFT-4")

        self.mappack_source["Mappack: size=51 mode=m status=r"]=e.MappackSource(51, 1, 4)

        self.osucollector_source["Osucollector: DT SPEED"]=e.OsucollectorSource(4869)

sources=Sources()