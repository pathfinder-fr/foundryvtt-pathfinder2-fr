#!/usr/bin/python3
# -*- coding: utf-8 -*-

from libdata import *

ROOT = "../"
packs = getPacks()

for p in packs:
    folderData = readFolder("%sdata/%s/" % (ROOT, p["id"]))
    existing = folderData[0]
    existingByName = folderData[1]

    # ========================
    # create or update entries
    # ========================
    for id in existing:
        filename = existing[id]["filename"]
        filepath = "%sdata/%s/%s" % (ROOT, p["id"], filename)
        if existing[id]["status"] == "aucune":
            name = existing[id]["nameEN"]
            print("Translating "+name)
            toTrad = existing[id]['descrEN']
            try:
                translated = dirtyTranslate(toTrad)
                existing[id]['descrFR'] = translated
                existing[id]['status'] = "auto-trad"
                dataToFile(existing[id], filepath)
            except Exception as e:
                print("Error while translating "+name+" : "+type(e).__name__)
