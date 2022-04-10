#!/usr/bin/python3
# -*- coding: utf-8 -*-

print('Starting imports')
import json
import yaml
import os
import re
import logging

from libdata import readFolder, dataToFile, getPacks, getValue, getList, equals, print_error, print_warning, checkItems

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
  FILE=p["pack"] + "/" + pack_id + ".db" if "pack" in p else ROOT + "packs/" + pack_id + ".db"
  entries = {}

  # =================================
  # read pack files and generate dict
  # =================================
  with open(FILE, 'r', encoding='utf8') as f:
    content = f.readlines()

  obj_items = {}
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

    ## items
    if "items" in p:
      items = getList(obj, "items", False)
      for item in items:
        # Attaques, Passifs, Actions
        if item['type'] in ["melee", "action"]:
          obj_items[item['_id']] = {
            "_id": getValue(item, '_id', False),
            "name": getValue(item, 'name', False),
            "desc": getValue(item, 'data.description.value', False),
            'type1': None,
            'type2': None,
            'lists': {},
            'data': {}
          }
        # Compétences avec variantes uniquement
        elif item['type'] == 'lore' and 'variants' in item['data'] and len(item['data']['variants']) > 0:
          data_variants = {}
          for key in item['data']['variants']:
            data_variants[key+'.label'] = item['data']['variants'][key]["label"]
          obj_items[item['_id']] = {
            "_id": getValue(item, '_id', False),
            "name": getValue(item, 'name', False),
            "desc": getValue(item, 'data.description.value', False, ""),
            'type1': None,
            'type2': None,
            'lists': {},
            'data': data_variants
          }


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
  has_errors = checkItems(entries, folderPath)

  # =============
  # process items
  # =============
  if len(obj_items) > 0:
    folderPath = "%sdata/%s/" % (ROOT, p["items"]["folder"])
    has_errors = checkItems(obj_items, folderPath, False)

# à réactiver pour autotrad
# # fermeture de la connexion a DeepL Translator
# if driver:
#   driver.quit()
if has_errors:
  print_error("Au moins une erreur survenue durant la préparation, échec")
  exit(1)