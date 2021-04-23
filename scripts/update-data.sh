#!/bin/bash

set -e

echo "Updating website data",
./generate-website.py

echo "Done"