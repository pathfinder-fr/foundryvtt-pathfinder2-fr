#!/bin/bash

# Script local de mise à jour des données babele et pf2-data-fr
#
# Ce script n'est pas forcément à jour, car utilisé uniquement manuellement.
#
# Les scripts à jours sont ceux du service d'intégration continue :
# - prepare-ci.sh
# - update-ci-module.sh
# - update-ci-pf2-data-fr.sh

set -e

#echo "Downloading latest packs..."
#./download-db.py

echo "Extracting data and updating translation files"
./prepare.py

echo "Generating Babele file"
./update-babele.py

echo "Updating status pages"
./update-status.py

echo "Updating pf2-data-fr repository",
./update-pf2datafr.py

echo "Increment module version"
CURVER=`grep "version" ../module.json | awk -F'.' '{print $2}'`
NEWVER="$(($CURVER+1))"
VERSION="v-1.$NEWVER.0"
cat ../module.template.json | sed "s/VERSION/1.$NEWVER.0/g" > ../module.json

echo "Change version"
CURVER=`grep "version" ../module.json | awk -F'.' '{print $2}'`
NEWVER="$(($CURVER+1))"
cat ../module.template.json | sed "s/VERSION/1.$NEWVER.0/g" > ../module.json
VERSION="v-1.$NEWVER.0"

echo "Ready for commit"
git add ../data ../babele* ../module.json

# on affiche uniquement la commande git à exécuter, on laisse l'utilisateur le faire
echo "git commit -m \"$VERSION\" && git tag \"$VERSION\" && git push --tags"

echo "Done"
