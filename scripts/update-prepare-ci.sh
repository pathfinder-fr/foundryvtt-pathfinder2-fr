#!/bin/bash

set -e

#echo "Downloading latest packs..."
#./download-db.py

echo "Extracting data and updating translation files"
./extract.py

echo "Done"