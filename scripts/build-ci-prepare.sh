#!/bin/bash

set -e

echo "Test stdout"
./test-ci.py

echo "Extracting data and updating translation files"
./prepare.py

echo "Done"
