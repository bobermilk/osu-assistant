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

def update_tournaments():
    global tournament_json
    urlextractor=URLExtract()
    proc=subprocess.run([os.path.join(os.getcwd(), 'osu_wiki.sh')], check=True, capture_output=True, text=True)
    should_update=proc.stdout
    if should_update == "1":
        # How to parse markdown 101
        # list of (tournament_name, beatmaps)
        tournaments={}
        tournament_dir=os.path.join(os.getcwd(),"osu-wiki", "wiki", "Tournaments")
        with open(os.path.join(tournament_dir,"en.md"), "r") as f:
            items=[x for x in f.read().split("\n") if len(x)>3 and x[:3]=='| [']
            for item in items:
                item=item.split("](")
                beatmaps=[]
                tournament_name=item[0][3:]
                tournament_tag=item[1][:item[1].find(")")]
                tournament_source_key=tournament_tag.replace('/', '-')
                dir=os.path.join(tournament_dir, tournament_tag)
                fcontent=open(os.path.join(dir, "en.md")).read()
                urls=urlextractor.find_urls(fcontent)
                osu_urls=[x for x in urls if "beatmapsets" in x]
                beatconnect_urls=[x for x in urls if "beatconnect" in x]
                for url in osu_urls:
                    url=url.replace('#', '/').split("/")
                    if url[-3]!="osu.ppy.sh":
                        beatmaps.append((url[-3], url[-1], url[-2])) # beatmapset_id, beatmap_id, gamemode
                    else:
                        beatmaps.append((url[-1], None, None))
                for url in beatconnect_urls:
                    beatmaps.append((url.split("/")[-2], None, None))
                tournaments[tournament_source_key]=[tournament_name, beatmaps]
        tournament_json=json.dumps(tournaments)

    with open("tournament.json", "w") as f:
        f.write(json.dumps(tournament_json))

def pausechamp(r):
    if r.status_code != 200:
        raise Exception()
    time.sleep(5)

def update_mappacks():
    global mappack_json
    mappacks={}
    sites = [
        "https://osu.ppy.sh/beatmaps/packs?type=standard&page={}",
        "https://osu.ppy.sh/beatmaps/packs?type=chart&page={}",
        "https://osu.ppy.sh/beatmaps/packs?type=theme&page={}",
        "https://osu.ppy.sh/beatmaps/packs?type=artist&page={}",
    ]

    for i, site in enumerate(sites):
        r = requests.get(site.format(1))
        pausechamp(r)
        soup = BeautifulSoup(r.text, "html.parser")
        page_cnt = int(soup.find_all("a", {"class": "pagination-v2__link"})[-2].text)
        pack_ids=[]
        for page_num in range(1, page_cnt + 1):
            # get pack titles
            r=requests.get(site.format(page_num))
            pausechamp(r)
            soup = BeautifulSoup(r.text, "html.parser")
            packs = soup.find_all("a", {"class", "beatmap-pack__header js-accordion__item-header"})
            beatmaps=[]
            for pack in packs:
                try:
                    soup=BeautifulSoup(r.text, "lxml", parse_only=SoupStrainer('a'))
                    mappack_id=pack['href'].split("/")[-1]
                    r=requests.get("https://osu.ppy.sh/beatmaps/packs/{}/raw".format(mappack_id))
                    pausechamp(r)
                    soup=BeautifulSoup(r.text, "lxml", parse_only=SoupStrainer('a'))
                    urls=[x['href'] for x in soup if x.has_attr('href')]
                    urls.pop(0) # remove mediafire link
                    for url in urls:
                        url=url.replace('#', '/').split("/")
                        if url[-3]!="osu.ppy.sh":
                            beatmaps.append((url[-3], url[-1], url[-2])) # beatmapset_id, beatmap_id, gamemode
                        else:
                            beatmaps.append((url[-1], None, None))
                except:
                    pass
                beatmaps.append([pack.find("div", {"class", "beatmap-pack__name"}).getText(), beatmaps])
                    
            pack_ids.append(beatmaps)
        mappacks[i]=pack_ids
    mappack_json=json.dumps(mappacks)
    with open("mappack.json", "w") as f:
        f.write(json.dumps(mappacks))