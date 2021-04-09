#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
from libdata import *

logging.basicConfig(filename='translation.log', level=logging.INFO)


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
        if existing[id]["status"] == "auto-trad":
            name = existing[id]["nameEN"]
            logging.info("Translating "+name)
            toTrad = existing[id]['descrEN']
            try:
                translated = dirtyTranslate(toTrad)
                existing[id]['descrFR'] = translated
                existing[id]['status'] = "auto-trad"
                dataToFile(existing[id], filepath)
                logging.info("Success !")
            except Exception as e:
                logging.error("Error while translating "+name+" : "+type(e).__name__)
                logging.error(e)