from bs4 import BeautifulSoup, SoupStrainer
import requests
import time
import json

def pausechamp(r):
    if r.status_code != 200:
        raise Exception()
    time.sleep(5)

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
    
with open("mappacks.json", "w") as f:
    f.write(json.dumps(mappacks))
