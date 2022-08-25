#!/bin/bash
# Updates the osu wiki used to extract all official tournament data
if [ ! -d "osu-wiki" ]; then
    git clone https://github.com/ppy/osu-wiki
    cd osu-wiki
else
    cd osu-wiki
    if ! git pull | grep -q 'Already up to date'; then
        
    fi  
fi