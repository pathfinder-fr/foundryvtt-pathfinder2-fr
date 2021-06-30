#!/bin/bash

set -e

chmod a+x test-ci.py
echo "Test stdout python inline"
python3 test-ci.py
echo "Test stdout"
./test-ci.py

echo "Extracting data and updating translation files"
./prepare.py

echo "Done"
