#!/bin/bash
##
## Script simple à exécuter après l'exécution de build-manual.sh
## pour remettre toutes les données à zéro
##
git reset ../data
rm -rf ../data
git checkout ../data

git reset ../babele*
rm -rf ../babele*
git checkout ../babele*

git reset ../module.json
git checkout ../module.json

git status
