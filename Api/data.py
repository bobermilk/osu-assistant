
# Data
tournaments_data={}
mappack_data={}

# We need to pause serving all requests when the update happens
async def write(_tournament_data, _mappack_data):
    global tournament_data
    global mappack_data
    tournament_data=_tournament_data
    mappack_data=_mappack_data

def update_tournaments():
    return {"foo":"tournament"}
def update_mappacks():
    return {"foo": "beatconnect"}