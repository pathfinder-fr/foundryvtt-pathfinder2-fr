#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
from libdata import *

ROOT = "../"

driver = translator_driver()

logging.basicConfig(filename='translation.log', level=logging.INFO)

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
        if existing[id]["status"] == "aucune" or (existing[id]["status"]=="changé" and len(existing[id]["descrFR"])==0):
            name = existing[id]["nameEN"]
            logging.info("Translating "+name)
            toTrad = existing[id]['descrEN']
            translationAttempt = full_trad(driver, toTrad)
            existing[id]['descrFR'] = translationAttempt.data
            existing[id]['status'] = translationAttempt.status
            dataToFile(existing[id], filepath)
driver.quit()