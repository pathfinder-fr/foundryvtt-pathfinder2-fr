#!/bin/bash
CURVER=`grep "version" ../module.json | awk -F'.' '{print $2}'`
NEWVER="$(($CURVER+1))"
cat ../module.template.json | sed "s/VERSION/0.$NEWVER.0/g" > ../module.json
git add ../module.json
VERSION="v-0.$NEWVER.0"
echo "Ready for commit"
git add ../data ../babele* ../module.json
git commit -m \"$VERSION\" && git tag \"$VERSION\" && git push -o ci-skip https://root:$ACCESS_TOKEN@gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr.git  HEAD:master && git push --tags

