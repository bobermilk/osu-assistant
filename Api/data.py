import os
import json
import subprocess
from urlextract import URLExtract

# Data
tournaments_data={}
mappack_data={}

def update_tournaments():
    global tournament_data
    urlextractor=URLExtract()
    proc=subprocess.run([os.path.join(os.getcwd(), 'osu_wiki.sh')], check=True, capture_output=True, text=True)
    should_update=bool(proc.stdout)
    should_update=1
    if should_update:
        # How to parse markdown 101
        # list of (tournament_name, beatmaps)
        tournaments={}
        with open("test.md", "r") as f:
            items=[x for x in f.read().split("\n") if len(x)>3 and x[:3]=='| [']
            for item in items:
                item=item.split("](")
                beatmaps=[]
                tournament_name=item[0][3:]
                tournament_tag=item[1][:item[1].find(")")]
                tournament_source_key=tournament_tag.replace('/', '-')
                dir=os.path.join(os.getcwd(),"osu-wiki", "wiki", "Tournaments", tournament_tag)
                fcontent=open(os.path.join(dir, "en.md")).read()
                urls=urlextractor.find_urls(fcontent)
                osu_urls=[x for x in urls if "beatmapsets" in x]
                beatconnect_urls=[x for x in urls if "beatconnect" in x]
                for url in osu_urls:
                    url=url.replace('#', '/').split("/")
                    beatmaps.append((url[-3], url[-1], url[-2])) # beatmapset_id, beatmap_id, gamemode
                for url in beatconnect_urls:
                    beatmaps.append((url.split("/")[-2], None, None))
                tournaments[tournament_source_key]=[tournament_name, beatmaps]
        tournament_data=json.dumps(tournaments)

def update_mappacks():
    return {"foo": "beatconnect"}

update_tournaments()
with open("test.txt", "w") as f:
    f.write(tournament_data)