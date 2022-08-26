#!/bin/bash
# Updates the osu wiki used to extract all official tournament data
if [ ! -d "osu-wiki" ]; then
    git clone https://github.com/ppy/osu-wiki
    cd osu-wiki
    echo -n 1
else
    cd osu-wiki
    if git pull | grep -q 'Already up to date'; then
        echo -n 0
    else
        echo -n 1
    fi
fi