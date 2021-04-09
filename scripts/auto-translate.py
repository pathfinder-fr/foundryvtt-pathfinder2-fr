#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
from libdata import *

logging.basicConfig(filename='translation.log', level=logging.INFO)


ROOT = "../"

driver = translator_driver()

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
            logging.info("Translating "+name)
            toTrad = existing[id]['descrEN']
            try:
                translated = dirtyTranslate(driver, toTrad)
                existing[id]['descrFR'] = translated
                existing[id]['status'] = "auto-trad"
                dataToFile(existing[id], filepath)
                logging.info("Success !")
            except Exception as e:
                exception_name = type(e).__name__
                logging.error("Error while translating %s : %s" % (filename, exception_name))
                if exception_name=="TimeoutException":
                    logging.error("Fichier %s : le texte est très long et le délai pour la \
                    traduction automatique a été dépassé" % filename)
                else: 
                    filename = name.lower().replace(" ", "-")+".json"
                    logging.error("File %s in pack %s -> %s" % (filename, p["id"], e.message))
driver.quit()