#!/bin/bash

set -e

echo "Downloading latest foundry pack"
mkdir .ci/ || true
wget -q https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/jobs/artifacts/release-v9/download?job=build -O .ci/pf2e.zip
unzip -q -o -d .ci/ .ci/pf2e.zip
mv .ci/pf2e/packs ../packs

echo "Done"
