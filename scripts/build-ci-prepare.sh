#!/bin/bash

set -e

echo "Test stdout"
chmod a+x test-ci.py
./test-ci.py

echo "Extracting data and updating translation files"
./prepare.py

echo "Done"
