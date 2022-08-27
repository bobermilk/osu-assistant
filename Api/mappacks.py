from bs4 import BeautifulSoup, SoupStrainer
import requests
import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Actual shit
def setup_webdriver(headless):
    chrome_install = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(service=chrome_install, options=chrome_options)

mappacks={}
sites = [
    "https://osu.ppy.sh/beatmaps/packs?type=standard&page={}",
    "https://osu.ppy.sh/beatmaps/packs?type=chart&page={}",
    "https://osu.ppy.sh/beatmaps/packs?type=theme&page={}",
    "https://osu.ppy.sh/beatmaps/packs?type=artist&page={}",
]

driver = setup_webdriver(headless=False)
for i, site in enumerate(sites):
    response = requests.get(site.format(1)).content
    soup = BeautifulSoup(response, "html.parser")
    page_cnt = int(soup.find_all("a", {"class": "pagination-v2__link"})[-2].text)
    pack_ids=[]
    for page_num in range(1, page_cnt + 1):
        # get pack titles

        driver.get(site.format(page_num))
        time.sleep(5)
        actions = ActionChains(driver)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        pack_urls = soup.find_all("a", {"class", "beatmap-pack__header js-accordion__item-header"})
        for pack_url in pack_urls:
            pack_ids.append(pack_url)
    mappacks[i]=pack_ids
    
with open("mappacks.json", "w") as f:
    f.write(json.dumps(mappacks))
