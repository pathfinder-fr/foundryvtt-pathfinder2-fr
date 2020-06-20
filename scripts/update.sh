#!/bin/bash

set -e

echo "Downloading latest packs..."
rm ../packs/*
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/actions.db > ../packs/actions.db
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/classes.db > ../packs/classes.db
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/feats.db > ../packs/feats.db
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/spells.db > ../packs/spells.db
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/backgrounds.db > ../packs/backgrounds.db
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/ancestryfeatures.db > ../packs/ancestryfeatures.db
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/equipment.db > ../packs/equipment.db
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/classfeatures.db > ../packs/classfeatures.db
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/conditionspf2e.db > ../packs/conditions.db

echo "Extracting data and updating translation files"
./extract.py

echo "Generating Babele file"
./generate-babele.py

echo "Updating status pages"
./generate-status.py

echo "Change version"
./change-version.sh

echo "Ready for commit"
git add ../data ../babele* ../module.json

echo "Done"
