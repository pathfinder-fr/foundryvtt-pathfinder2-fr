#!/bin/bash
echo "Downloading latest packs..."
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/actions.db > ../packs/actions.db
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/classes.db > ../packs/classes.db
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/feats.db > ../packs/feats.db
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/spells.db > ../packs/spells.db
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/equipment.db > ../packs/equipment.db
curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/dist/packs/classfeatures.db > ../packs/classfeatures.db

echo "Extracting data and updating translation files"
./extract.py

echo "Generating Babele file"
./generate-babele.py

echo "Updating status pages"
./generate-status.py

echo "Done"
