#!/bin/bash

set -e

echo "Generating Babele file"
./update-babele.py

echo "Updating status pages"
./update-status.py

echo "Increment module version"
CURVER=`grep "version" ../module.json | awk -F'.' '{print $2}'`
NEWVER="$(($CURVER+1))"
VERSION="v-0.$NEWVER.0"
cat ../module.template.json | sed "s/VERSION/0.$NEWVER.0/g" > ../module.json

echo "Commit module update"
git add ../data ../babele* ../module.json
git commit -m $VERSION
git tag $VERSION
git push --tags -o ci.skip https://root:$ACCESS_TOKEN@gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr.git HEAD:master
# useless ??
git push        -o ci.skip https://root:$ACCESS_TOKEN@gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr.git HEAD:master 

echo "Done"