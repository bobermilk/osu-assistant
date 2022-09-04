import json
maps={}
maps_entry=["Springtime Osu!mania Free-for-all Tournament 6"]
mapplist=[]
with open("extras.txt", "r") as f:
    links=[x.split()[0] for x in f.readlines()]
    for link in links:
        l=link.replace("#", "/").split("/")
        mapplist.append([l[-3], l[-1], l[-2]])
maps_entry.append(mapplist)
maps["SOFT-6"]=maps_entry
with open("extras.json", "w") as f:
    json.dump(maps,f)

