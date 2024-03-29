from bs4 import BeautifulSoup, SoupStrainer
import requests
import time
import json
import subprocess
import os
from bs4 import BeautifulSoup, SoupStrainer
from urlextract import URLExtract

def pausechamp(r):
    if r.status_code != 200:
        print("missing pack but what the hell lol")
    time.sleep(10)

urlextractor=URLExtract()
sync_cnt=0
try:
    while True:
        sync_cnt+=1
        print("ouscollection sync #{}".format(sync_cnt))
        # server
        # proc=subprocess.run(['bash', 'osu_wiki.sh'], check=True, capture_output=True, text=True)
        # should_update=proc.stdout
        should_update="1"
        if should_update == "1":
            # How to parse markdown 101
            # list of (tournament_name, beatmaps)
            with open("extras.json", "r") as f:
                tournaments=json.load(f)
            tournament_dir=os.path.join(os.getcwd(),"osu-wiki", "wiki", "Tournaments")
            with open(os.path.join(tournament_dir,"en.md"), "r") as f:
                items=[x for x in f.read().split("\n") if len(x)>3 and x[:3]=='| [']
                # Peppy didnt update the wiki :sadge:
                items.append("| [Springtime osu!mania Free-for-all Tournament 4](SOFT/4) |")
                items.append("| [Springtime osu!mania Free-for-all Tournament 5](SOFT/5) |")
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
                    if len(osu_urls)>0:
                        for url in osu_urls:
                            url=url.replace('#', '/').split("/")
                            if url[-3]!="osu.ppy.sh":
                                beatmaps.append((url[-3], url[-1], url[-2])) # beatmapset_id, beatmap_id, gamemode
                            else:
                                beatmaps.append((url[-1], None, None))
                        for url in beatconnect_urls:
                            beatmaps.append((url.split("/")[-2], None, None))
                        tournaments[tournament_source_key]=[tournament_name, beatmaps]
            try:
                with open("tournament.json", "w") as f:
                    json.dump(tournaments, f)
            except:
                pass
        print("updated tournament.json")

        # server
        # with open("mappack.json", "r") as f:
            #  mappacks=json.load(f)
        mappacks=dict()
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
            # server
            # pack_ids=mappacks[str(i)]
            pack_ids=dict()
            stop=False
            for page_num in range(1, page_cnt + 1):
                if stop:
                    break
                # get pack titles
                r=requests.get(site.format(page_num))
                pausechamp(r)
                soup = BeautifulSoup(r.text, "html.parser")
                packs = soup.find_all("a", {"class", "beatmap-pack__header js-accordion__item-header"})
                for pack in packs:
                    beatmaps=[]
                    try:
                        soup=BeautifulSoup(r.text, "lxml", parse_only=SoupStrainer('a'))
                        mappack_id=pack['href'].split("/")[-1]
                        if str(mappack_id) in pack_ids.keys():
                            # We can stop here, we got the rest
                            stop=True
                            break
                        r=requests.get("https://osu.ppy.sh/beatmaps/packs/{}/raw".format(mappack_id))
                        pausechamp(r)
                        soup=BeautifulSoup(r.text, "lxml", parse_only=SoupStrainer('a'))
                        urls=[x['href'] for x in soup if x.has_attr('href')]
                        urls.pop(0) # remove mediafire link
                        for url in urls:
                            url=url.replace('#', '/').split("/")
                            # if url[-3]!="osu.ppy.sh":
                            #     beatmaps.append((url[-3], url[-1], url[-2])) # beatmapset_id, beatmap_id, gamemode
                            # else:
                            #     beatmaps.append((url[-1], None, None))
                            if url[-1]!="Game_modifier":
                                beatmaps.append(int(url[-1]))
                        pack_ids[mappack_id]=[pack.find("div", {"class", "beatmap-pack__name"}).getText(), beatmaps]
                    except:
                        raise Exception(f"{pack['href']} mappack failed, the script will now terminate")
            mappacks[i]=pack_ids
        try:
            with open("mappack.json", "w") as f:
                json.dump(mappacks, f)
        except:
            pass
        print("updated mappack.json")

        # server
        # time.sleep(86400) # one day
        break
except Exception as e:
   raise e 
