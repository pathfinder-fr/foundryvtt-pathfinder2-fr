#!/bin/bash
CURVER=`grep "version" ../module.json | awk -F'.' '{print $2}'`
NEWVER="$(($CURVER+1))"
cat ../module.template.json | sed "s/VERSION/0.$NEWVER.0/g" > ../module.json
VERSION="v-0.$NEWVER.0"
echo "git commit -m \"$VERSION\" && git tag \"$VERSION\" && git push && git push --tags"

