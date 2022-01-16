#!/bin/bash

set -e

echo "Downloading latest foundry pack"
mkdir .ci/ || true
wget -q https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/jobs/artifacts/release-v9/download?job=build -O .ci/pf2e.zip
unzip -o -d .ci/ .ci/pf2e.zip # ZIP initial ne contient qu'un autre ZIP (pf2e.zip et le manifest JSON)
unzip -o -d .ci/ .ci/pf2e.zip # ZIP du système
mv .ci/pf2e/packs ../packs

echo "Done"
