import entity as e

class Sources(e.Sources):
    def __init__(self):
        super().__init__(self)
        # Create mock data
        self.user_source["User: played=all bobermilk"]=e.UserSource(["https://osu.ppy.sh/users/15656848"],[False,True,True,False,False,False,False,False])
        self.user_source["User: played=top&fav status=r&gp&p&g Polyester"]=e.UserSource(["https://osu.ppy.sh/users/11106874/mania"],[True,True,False,True,False,True,True,True])
        self.user_source["User: status=r&l&gp&p&g -mint- riunosk"]=e.UserSource(["https://osu.ppy.sh/users/5594381", "https://osu.ppy.sh/users/8976576"],[False,False,False,True,True,True,True,True])

        self.tournament_source["Tournament: osu!mania 4K World Cup 2022"]=e.TournamentSource("MWC-2022")
        self.tournament_source["Tournament: Springtime Osu!mania Free-for-all Tournament 4"]=e.TournamentSource("SOFT-4")

        self.mappack_source["Mappack: size=51 mode=m status=r"]=e.MappackSource(1,0,51)

        self.osucollector_source["Osucollector: DT SPEED"]=e.OsucollectorSource(4869)

Sources=Sources()