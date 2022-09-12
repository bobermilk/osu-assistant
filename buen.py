import os
import data
import database
import misc
import shutil
from strings import generate_random_name, generate_collection_name

# Walks the specified subdirectory to a specified level
def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

# Buen
def generate_beatmap(selections, current_collections):
        settings=data.Settings
        osudb=database.create_osudb2()
        new_folder=os.path.join(settings.osu_install_folder, "Songs", generate_random_name(8))
        while os.path.isdir(new_folder):
            new_folder=os.path.join(settings.osu_install_folder, "Songs", generate_random_name(8))
            
        os.mkdir(new_folder)
        if len(selections) > 0:
            for i, collection in enumerate(current_collections["collections"]):
                if i in selections:
                    for checksum in collection["hashes"]:
                        beatmap_id, song_title, mapper, folder = osudb[checksum]
                        for dirpath, dirnames, filenames in misc.walklevel(os.path.join(settings.osu_install_folder, "Songs", folder)):
                            for filename in filenames:
                                filename=str(filename)
                                if filename.endswith(".osu"):
                                    lines=None # file lines
                                    audio_file=None # AudioFilename
                                    title=(None, None) # Title, TitleUnicode
                                    artist=(None, None) # Artist, ArtistUnicode
                                    diff_name=None # Version
                                    found=False
                                    with open(os.path.join(settings.osu_install_folder, "Songs", folder, filename), "r") as f:
                                        lines=f.readlines()
                                        if "BeatmapID" and beatmap_id in lines:
                                            found=True
                                        if "Title" and song_title[0] in lines and "Creator" and mapper in lines:
                                            found=True
                                        # Now we extract the data
                                        if found:
                                            for line in lines:
                                                line=line.replace(":", " ")
                                                l=line.split() # l[0] = key, l[-1]=value

                                                if len(l)>1:
                                                    if l[0]=="AudioFilename":
                                                        audio_file=l[-1]
                                                    if l[0]=="Title":
                                                        title[0]=l[-1]
                                                    if l[0]=="TitleUnicode":
                                                        title[1]=l[-1]
                                                    if l[0]=="Artist":
                                                        artist[0]=l[-1]
                                                    if l[0]=="ArtistUnicode":
                                                        artist[1]=l[-1]
                                                    if l[0]=="Version":
                                                        diff_name=l[-1]
                                    print(audio_file, title, artist, diff_name)
                                    # if found and title!=None and audio_file!=None and artist!=None and diff_name!=None :
                                    #     dest=os.path.join(settings.osu_install_folder, "Songs", new_folder)
                                    #     while os.path.isfile(generate_random_name())
                                    #     shutil.copyfile(os.path.join(settings.osu_install_folder, "Songs", folder, audio_file),os.path.join(dest, ))
                                    #     with open(os.path.join(dest, f"{artist} - {title} (osu-assistant) {diff_name}"), "w+") as f:
                                    #         for line in lines:
                                    #             line=line.replace(":", " ")
                                    #             l=line.split() # l[0] = key, l[-1]=value
                                                
                                    #             if len(l)>1:
                                    #                 if l=="AudioFilename:":
                                                    
                                    #                 if l=="Title:":
                                                    
                                    #                 if l=="TitleUnicode:":
                                                    
                                    #                 if l=="Creator:":
                                                    
                                    #                 if l=="BeatmapID:":
                                    #                     f.write("BeatmapID:0")
                                                    
                                    #                 if l=="BeatmapSetID:":
                                    #                     f.write("BeatmapSetID:-1")