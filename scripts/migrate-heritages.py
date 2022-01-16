#!/usr/bin/python3
# -*- coding: utf-8 -*-

##
## Ce script migre les traductions de ancestries vers heritages
## Voir commit anglophone  : https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/commit/98f77b7986a0379254fea9f2f1f81c554d780179
##
## Message de rectulo : 15 janvier 12:05 (EST)
##
import json
import yaml
import os
import re

from libdata import readFolder, dataToFile, getPacks, getValue, getList, equals, print_error, print_warning

ROOT="../"

# ==========================
# read all available entries
# ==========================
# [0] : existing (by id)
# [1] : existing (by name)
# [2] : errors
heritageData = readFolder("%sdata/heritages/" % (ROOT))
ancestriesData = readFolder("%sdata/ancestryfeatures/" % (ROOT))

for name in heritageData[1]:
  # look for an existing match in ancestryfeatures
  if not name in ancestriesData[1]:
    print("No match found for : %s" % name)
    exit(1)

  # merge name and description into heritage
  oldEntry = ancestriesData[1][name]
  newEntry = heritageData[1][name]

  newEntry["nameFR"] = oldEntry["nameFR"]
  newEntry["descrFR"] = oldEntry["descrFR"]
  newEntry["status"] = oldEntry["status"]

  dataToFile(newEntry, "%sdata/heritages/%s" % (ROOT, newEntry["filename"]))

exit(1)

      #

# =======================
# search deleted elements
# =======================
for id in existing:
  if not id in entries:
    filename = "%sdata/%s/%s" % (ROOT, pack_id, existing[id]['filename'])
    if existing[id]['status'] != 'aucune':
      print_warning("File cannot be safely removed! %s, please fix manually!" % filename)

    os.remove(filename)

