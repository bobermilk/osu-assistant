import os
import json
import time
import requests
import subprocess
from bs4 import BeautifulSoup, SoupStrainer
from urlextract import URLExtract

# Data
tournament_json={}
mappack_json={}
mappack_data={}
mappack_latest=1

def update_tournaments():
    print("updating")
    global tournament_json
    urlextractor=URLExtract()
    proc=subprocess.run([os.path.join(os.getcwd(), 'osu_wiki.sh')], check=True, capture_output=True, text=True)
    should_update=bool(proc.stdout)
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
        tournament_json=json.dumps(tournaments)

def update_mappacks():
    global mappack_data
    global mappack_latest
    global mappack_json
    old_mappack_latest=mappack_latest
    while True:
        beatmaps=[]
        r=requests.get("https://osu.ppy.sh/beatmaps/packs/{}/raw".format(mappack_latest))
        if mappack_latest==100:
            break
        if r.status_code != 200:
            mappack_latest-=1
            break
        time.sleep(0.5)
        soup=BeautifulSoup(r.text, "lxml", parse_only=SoupStrainer('a'))
        urls=[x['href'] for x in soup if x.has_attr('href')]
        urls.pop(0) # remove mediafire link
        for url in urls:
            url=url.split('/')
            beatmaps.append(url[-1])
        
        mappack_data[mappack_latest]=beatmaps
        mappack_latest+=1
    if old_mappack_latest<mappack_latest:
        mappack_json=json.dumps(mappack_data)