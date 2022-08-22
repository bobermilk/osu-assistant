import entity as e

class Sources():
    def __init__(self):
        self.user_source={}
        self.osucollector_source={}
        self.mappack_source={}
        self.tournament_source={}

        # Create mock data
        self.user_source["User: played=all bobermilk"]=e.UserSource(["https://osu.ppy.sh/users/15656848"],[False,True,True,False,False,False,False,False],[1397860, 547451])
        self.user_source["User: played=top&fav status=r&gp&p&g Polyester"]=e.UserSource(["https://osu.ppy.sh/users/11106874/mania"],[True,True,False,True,False,True,True,True], [])
        self.user_source["User: status=r&l&gp&p&g -mint- riunosk"]=e.UserSource(["https://osu.ppy.sh/users/5594381", "https://osu.ppy.sh/users/8976576"],[False,False,False,True,True,True,True,True],[132023, 123953, 120344])

        self.tournament_source["Tournament: osu!mania 4K World Cup 2022"]=e.TournamentSource("MWC-2022", [123,123,321,213])
        self.tournament_source["Tournament: Springtime Osu!mania Free-for-all Tournament 4"]=e.TournamentSource("SOFT-4", [1923, 189828])

        self.mappack_source["Mappack: size=51 mode=m status=r"]=e.MappackSource(1,0,51,[19239,1923894875, 923])

        self.osucollector_source["Osucollector: DT SPEED"]=e.OsucollectorSource(4869, [9127,9123])
        
    def read(self):
        return list(self.user_source.items()) + list(self.tournament_source.items()) + list(self.mappack_source.items()) + list(self.osucollector_source.items())

Sources=Sources()