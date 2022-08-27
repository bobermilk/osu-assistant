import scraper, entity

all_beatmaps=scraper.get_userpage_beatmaps(entity.UserpageSource({(2520707,"mania")},[True,False,False,False,False,False,False,False]))

print(all_beatmaps)