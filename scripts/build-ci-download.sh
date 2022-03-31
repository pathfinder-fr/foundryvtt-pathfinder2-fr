#!/bin/bash

set -e

echo "Downloading latest foundry packs"
mkdir .ci/ || true
wget -q https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/jobs/artifacts/release-v9/download?job=build -O .ci/pf2e.zip
unzip -o -d .ci/ .ci/pf2e.zip # ZIP initial ne contient qu'un autre ZIP (pf2e.zip et le manifest JSON)
unzip -o -d .ci/ .ci/pf2e.zip # ZIP du système
mv .ci/pf2e/packs ../packs
rm -rf .ci/

echo "Downloading animal companions packs"
mkdir .ci/ || true
wget -q https://github.com/TikaelSol/PF2e-Animal-Companions/archive/refs/heads/main.zip -O .ci/animal.zip
unzip -o -d .ci/ .ci/animal.zip
ls .ci/PF2e-Animal-Companions-main/
mv .ci/PF2e-Animal-Companions-main/packs ../packs-animal
rm -rf .ci/

echo "Done"
