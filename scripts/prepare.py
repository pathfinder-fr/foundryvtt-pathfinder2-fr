#!/usr/bin/python3
# -*- coding: utf-8 -*-

print('Starting imports')
import json
import yaml
import os
import re
import logging

from libdata import readFolder, dataToFile, getPacks, getValue, getList, equals, print_error, print_warning

# à réactiver pour autotrad
# from libselenium import translator_driver, full_trad

print('Preparing translation')
logging.basicConfig(filename='translation.log', level=logging.INFO)
  
ROOT="../"

# à réactiver pour autotrad
# # ouverture de la connexion a DeepL Translator
# print('Opening DeepL Translator connection')
# driver = translator_driver()

print('Loading packs...')
packs = getPacks()
has_errors = False

for p in packs:
  pack_id = p["id"]
  print('Preparing %s.db pack' % (pack_id))
  FILE=ROOT + "packs/" + pack_id + ".db"
  entries = {}

  # =================================
  # read pack files and generate dict
  # =================================
  with open(FILE, 'r', encoding='utf8') as f:
    content = f.readlines()

  count = 0
  for line in content:
    count += 1
    try:
      obj = json.loads(line)
    except:
      print_error("Invalid json %s at line %d" % (FILE, count))
      continue
    
    if '$$deleted' in obj:
      continue
    
    entries[obj['_id']] = { 
      'name': getValue(obj, p['paths']['name']), 
      'desc': getValue(obj, p['paths']['desc'], False, "") if 'desc' in p['paths'] else "NE PAS TRADUIRE",
      'type1': getValue(obj, p['paths']['type1']) if 'type1' in p['paths'] else None,
      'type2': getValue(obj, p['paths']['type2'], False) if 'type2' in p['paths'] else None,
      'lists': {},
      'data': {}
    }
    
    ## additional lists
    if "lists" in p:
      for key in p["lists"]:
        list = getList(obj, p["lists"][key], False)
        if len(list) == 0:
          list = getList(obj, p["lists"][key] + ".value", False)
        entries[obj['_id']]['lists'][key] = list
    
    ## other extractions
    if "extract" in p:
      for key in p["extract"]:
          value = getValue(obj, p["extract"][key], False)
          if value and len(value) > 0:
              entries[obj['_id']]['data'][key] = value
  
  # ==============================
  # search for duplicates in names
  # ==============================
  duplic = {}
  for id in entries:
    if entries[id]['name'] in duplic:
      print_warning("Duplicated name: %s (%s)\e[0m" % (entries[id]['name'], id))
      #entries[id] = None
    else:
      duplic[entries[id]['name']] = id
  
  # ==========================
  # read all available entries
  # ==========================
  folderPath = "%sdata/%s/" % (ROOT, pack_id)
  if not os.path.isdir(folderPath):
    os.mkdir(folderPath)

  folderData = readFolder(folderPath)
  existing = folderData[0]
  existingByName = folderData[1]
  pack_has_errors = folderData[2]

  # si le pack contient au moins une erreur à la lecture, on arrête de l'examiner
  if pack_has_errors == True:
    print_warning("Invalid data in pack %s, skipping" % (pack_id))
    has_errors = True
    continue
  
  # ========================
  # create or update entries
  # ========================
  for id in entries:
    source = entries[id]
    if not source:
      continue

    # build filename
    filename =  "%s.htm" % id
    if source['type2']:
      filename = "%s-%s-%s" % (source['type1'], source['type2'], filename)
    elif source['type1']:
      filename = "%s-%s" % (source['type1'], filename)
    filepath = "%sdata/%s/%s" % (ROOT, pack_id, filename)
    
    # data exists for id
    if id in existing:

      # rename file if filepath not the same
      if existing[id]['filename'] != filename:
        pathFrom = "%sdata/%s/%s" % (ROOT, pack_id, existing[id]['filename'])
        pathTo = "%sdata/%s/%s" % (ROOT, pack_id, filename)
        os.rename(pathFrom, pathTo)
      
      # check status from existing file
      if not existing[id]["status"] in ("libre", "officielle", "doublon", "aucune", "changé", "auto-trad", "auto-googtrad", "vide"):
        print_error("Status error for : %s" % filepath);
        has_errors = True
        continue
       
      # QUICK FIX pour: https://discord.com/channels/@me/757146858828333077/815954577219780728
      change = False
      #if p["name"] == "feats-srd":
      #  change = True 

      if change or not equals(existing[id]['nameEN'],source['name']) or not equals(existing[id]['descrEN'], source['desc']) or not equals(existing[id]['listsEN'], source['lists']) or not equals(existing[id]['dataEN'], source['data']):
        existing[id]['nameEN'] = source['name']
        existing[id]['descrEN'] = source['desc']
        existing[id]['listsEN'] = source['lists']
        existing[id]['dataEN'] = source['data']
        
        if existing[id]['status'] != "aucune" and existing[id]['status'] != "changé":
          existing[id]['oldstatus'] = existing[id]['status']
          existing[id]['status'] = "changé"
          
        dataToFile(existing[id], filepath)
      
      elif 'oldstatus' in existing[id] and existing[id]['status'] != 'changé':
        del existing[id]['oldstatus']
        dataToFile(existing[id], filepath)
      
    # file doesn't exist
    else:
      
      # check if other entry exists with same name => means that ID has changed for the same element
      if source['name'] in existingByName and not source['name'] in ("Shattering Strike", "Chilling Spray"):
        oldEntry = existingByName[source['name']]
        # rename file
        pathFrom = "%sdata/%s/%s" % (ROOT, pack_id, oldEntry['filename'])
        pathTo = "%sdata/%s/%s" % (ROOT, pack_id, filename)

        if oldEntry['id'] in existing:
          del existing[oldEntry['id']]
        os.rename(pathFrom, pathTo)
      
      # create new
      else:
        name = source["name"]
        if len(source['desc']) > 0:
          # Automatic translation
          logging.info("Translating %s" % name)
          #print("Translating %s" % name)
          #translation_data = full_trad(driver, source['desc'])
          #tradDesc = translation_data.data
          #status = translation_data.status
          # FIX : auto-trad trop longue pour le bestiaire 3
          status="aucune"
          tradDesc = ""
        else:
          tradDesc = ""
          status = "vide"
            
        data = { 
          'nameEN': name,
          'nameFR': "",
          'status': status,
          'descrEN': source['desc'],
          'descrFR': tradDesc,
          'listsEN': source['lists'],
          'dataEN': source['data'],
          'listsFR': {} }
        dataToFile(data, filepath)

  # =======================
  # search deleted elements
  # =======================
  for id in existing:
    if not id in entries:
      filename = "%sdata/%s/%s" % (ROOT, pack_id, existing[id]['filename'])
      if existing[id]['status'] != 'aucune':
        print_warning("File cannot be safely removed! %s, please fix manually!" % filename)
      
      os.remove(filename)

# à réactiver pour autotrad
# # fermeture de la connexion a DeepL Translator
# if driver:
#   driver.quit()

if has_errors:
  print_error("Au moins une erreur survenue durant la préparation, échec")
  exit(1)
