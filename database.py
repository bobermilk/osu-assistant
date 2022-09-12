# collections and osu db

import os
import buffer, data
import shutil
import aiofiles
from pubsub import pub

def query_osudb(beatmap):
    beatmapset_id=int(beatmap[0])
    if beatmap[1] is not None and int(beatmap[1]) in data.osudb_beatmap_ids:
        return True
    if beatmap[1] is None and beatmapset_id in data.osudb_beatmapset_ids:
        return True
    return False

async def create_osudb():
    settings=data.Settings
    osu_db_directory=os.path.join(settings.osu_install_folder, "osu!.db")
    if not os.path.isfile(osu_db_directory):
        settings.valid_osu_directory=False
    else:
        settings.valid_osu_directory=True
        async with aiofiles.open(osu_db_directory, mode="rb") as db:
            await db.read(9)
            # skip this datetime shit for now (8 bytes)
            await db.read(8)
            await buffer.read_string(db, True)
            num_beatmaps = await buffer.read_uint(db)

            for i in range(num_beatmaps):
                pub.sendMessage("show.loading", msg=f"Scanning osu! in-game database ({i}/{num_beatmaps} beatmaps)")
                await buffer.read_string(db, True)
                await buffer.read_string(db, True)
                await buffer.read_string(db, True)
                await buffer.read_string(db, True)
                await buffer.read_string(db, True)
                await buffer.read_string(db, True)
                await buffer.read_string(db, True)
                await buffer.read_string(db, True)
                await buffer.read_string(db, True)
                await db.read(39)
                # skip these int double pairs, personally i dont think they're 
                # important for the purpose of this database
                i = await buffer.read_uint(db)
                for _ in range(i):
                    await db.read(14)

                i = await buffer.read_uint(db)
                for _ in range(i):
                    await db.read(14)

                i = await buffer.read_uint(db)
                for _ in range(i):
                    await db.read(14)

                i = await buffer.read_uint(db)
                for _ in range(i):
                    await db.read(14)
                
                await db.read(12)
                # skip timing points
                # i = await buffer.read_uint(db)
                for _ in range(await buffer.read_uint(db)):
                    await db.read(17)
                beatmap_id=await buffer.read_uint(db)
                beatmapset_id=await buffer.read_uint(db)
                await db.read(15)
                await buffer.read_string(db, True)
                await buffer.read_string(db, True)
                await db.read(2)
                await buffer.read_string(db, True)
                await db.read(10)
                await buffer.read_string(db, True)
                await db.read(18)
                data.osudb_beatmap_ids.add(beatmap_id)
                data.osudb_beatmapset_ids.add(beatmapset_id)
        pub.sendMessage("show.loading", msg=None)

async def collection_to_dict():
    collections = {}
    try:
        async with aiofiles.open(os.path.join(data.Settings.osu_install_folder, "collection.db"), "rb") as db:
            collections["version"] = await buffer.read_uint(db)
            collections["num_collections"] = await buffer.read_uint(db)
            collections["collections"] = []
            for i in range(collections["num_collections"]):
                collection = {}
                collection["name"] = await buffer.read_string(db)
                collection["size"] = await buffer.read_uint(db)
                collection["hashes"] = []
                for i in range(collection["size"]):
                    collection["hashes"].append(await buffer.read_string(db))
                collections["collections"].append(collection)
    except:
        # Invalid osu folder, can't write to collections
        return False
    return collections


async def update_collections(new_collections):
    if data.Settings.valid_osu_directory:
        current_collections=await collection_to_dict()
        if not isinstance(current_collections, bool):
            b = buffer.WriteBuffer()
            b.write_uint(current_collections["version"])

            # Weed out the shit we gonna replace
            existing_collections={}
            new_collection_names=["- Source {}".format(data.Sources.collection_index[x]) for x in new_collections.keys()]
            for collection in current_collections["collections"]:
                if collection["name"] not in new_collection_names:
                    existing_collections[collection["name"]]=collection["hashes"]

            b.write_uint(len(new_collections)+len(existing_collections))

            # Write the existing collections
            for name, checksums in existing_collections.items():
                b.write_string(name)
                b.write_uint(len(checksums))
                for checksum in checksums:
                    b.write_string(checksum)
                    
            # Write the new collections
            for source_key, checksums in new_collections.items():
                b.write_string("- Source {}".format(data.Sources.collection_index[source_key]))
                b.write_uint(len(checksums))
                for checksum in checksums:
                    b.write_string(checksum)
            
            osu_folder=data.Settings.osu_install_folder
            collection_file=os.path.join(osu_folder,"collection.db")
            backup_file=os.path.join(osu_folder, "collection_backup.db")
            if not os.path.isfile(backup_file) and os.path.isfile(collection_file):
                shutil.copy2(collection_file, backup_file)
            with open(collection_file, "wb") as db:
                db.write(b.data)
                db.close()

# Taken from https://github.com/jaasonw/osu-db-tools/blob/master/osu_to_sqlite.py
def create_osudb2():
    # settings=data.Settings
    # osu_db_directory=os.path.join(settings.osu_install_folder, "osu!.db")
    # beatmaps={}
    # if os.path.isfile(osu_db_directory):
    #     with open(osu_db_directory, "rb") as db:
    #         version = buffer.read_uint(db)
    #         folder_count = buffer.read_uint(db)
    #         account_unlocked = buffer.read_bool(db)
    #         # skip this datetime shit for now (8 bytes)
    #         buffer.read_uint(db)
    #         buffer.read_uint(db)
    #         name = buffer.read_string(db)
    #         num_beatmaps = buffer.read_uint(db)

    #         for _ in range(num_beatmaps):
    #             artist = buffer.read_string(db)
    #             artist_unicode = buffer.read_string(db)
    #             song_title = buffer.read_string(db)
    #             song_title_unicode = buffer.read_string(db)
    #             mapper = buffer.read_string(db)
    #             difficulty = buffer.read_string(db)
    #             audio_file = buffer.read_string(db)
    #             md5_hash = buffer.read_string(db)
    #             map_file = buffer.read_string(db)
    #             ranked_status = buffer.read_ubyte(db)
    #             num_hitcircles = buffer.read_ushort(db)
    #             num_sliders = buffer.read_ushort(db)
    #             num_spinners = buffer.read_ushort(db)
    #             last_modified = buffer.read_ulong(db)
    #             approach_rate = buffer.read_float(db)
    #             circle_size = buffer.read_float(db)
    #             hp_drain = buffer.read_float(db)
    #             overall_difficulty = buffer.read_float(db)
    #             slider_velocity = buffer.read_double(db)
    #             # skip these int double pairs, personally i dont think they're 
    #             # important for the purpose of this database
    #             i = buffer.read_uint(db)
    #             for _ in range(i):
    #                 buffer.read_int_double(db)

    #             i = buffer.read_uint(db)
    #             for _ in range(i):
    #                 buffer.read_int_double(db)

    #             i = buffer.read_uint(db)
    #             for _ in range(i):
    #                 buffer.read_int_double(db)

    #             i = buffer.read_uint(db)
    #             for _ in range(i):
    #                 buffer.read_int_double(db)

    #             drain_time = buffer.read_uint(db)
    #             total_time = buffer.read_uint(db)
    #             preview_time = buffer.read_uint(db)
    #             # skip timing points
    #             # i = buffer.read_uint(db)
    #             for _ in range(buffer.read_uint(db)):
    #                 buffer.read_timing_point(db)
    #             beatmap_id = buffer.read_uint(db)
    #             beatmapset_id = buffer.read_uint(db)
    #             thread_id = buffer.read_uint(db)
    #             grade_standard = buffer.read_ubyte(db)
    #             grade_taiko = buffer.read_ubyte(db)
    #             grade_ctb = buffer.read_ubyte(db)
    #             grade_mania = buffer.read_ubyte(db)
    #             local_offset = buffer.read_ushort(db)
    #             stack_leniency = buffer.read_float(db)
    #             gameplay_mode = buffer.read_ubyte(db)
    #             song_source = buffer.read_string(db)
    #             song_tags = buffer.read_string(db)
    #             online_offset = buffer.read_ushort(db)
    #             title_font = buffer.read_string(db)
    #             is_unplayed = buffer.read_bool(db)
    #             last_played = buffer.read_ulong(db)
    #             is_osz2 = buffer.read_bool(db)
    #             folder_name = buffer.read_string(db)
    #             last_checked = buffer.read_ulong(db)
    #             ignore_sounds = buffer.read_bool(db)
    #             ignore_skin = buffer.read_bool(db)
    #             disable_storyboard = buffer.read_bool(db)
    #             disable_video = buffer.read_bool(db)
    #             visual_override = buffer.read_bool(db)
    #             last_modified2 = buffer.read_uint(db)
    #             scroll_speed = buffer.read_ubyte(db)
    #             beatmaps[md5_hash]=(beatmap_id, (song_title, song_title_unicode), mapper, folder_name)
    # return beatmaps
    pass