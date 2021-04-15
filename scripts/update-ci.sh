#!/bin/bash

set -e

#echo "Downloading latest packs..."
#./download-db.py

echo "Extracting data and updating translation files"
./extract.py

echo "Generating Babele file"
./generate-babele.py

echo "Updating status pages"
./generate-status.py

echo "Updating website data",
./generate-website.py

echo "Change version"
./change-version-ci.sh

echo "Done"