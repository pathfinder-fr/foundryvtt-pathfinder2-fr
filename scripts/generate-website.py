#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import os            
import datetime

from libdata import *

PACKS        = "../packs/"
WEBSITE_DATA = "../../pf2-data-fr/"

packs = getPacks()

for p in packs:   
  
  list = []
    
  translations = {}
  
  #############################################
  # read all available data for specified pack
  #############################################
  path = "../data/%s/" % p["id"]
  all_files = os.listdir(path)
  for fpath in all_files:
    
    data = fileToData(path + fpath)

    if data['status'] == 'aucune' or data['status'] == "auto-trad" \
      or data['status'] == "auto-googtrad"  or data['status'] == "vide":
      continue

    # pack id (ancestries, actionspf2e, ...)
    data_id = data['id']

    # default (all translations in french)
    translation = {
      'status': data['status'],
      'name': data['nameFR'],
      'description': data['descrFR']
     }

    # specific treatments by data type
    if data_id == 'ancestries':
      # translation['test'] = data['machin']
      pass
    elif data_id == 'classes':
      # translation['test'] = data['machin']
      pass

    # store translation
    translations[data_id] = translation

  #############################################
  # read original data from pf2 Foundry system
  #############################################
  filename = PACKS + p["id"] + ".db"
  descPathParts = p['paths']['desc'].split('.')

  with open(filename, 'r', encoding='utf8') as f:
    content = f.readlines()

  count = 0
  for line in content:
    count += 1
    try:
      enJson = json.loads(line)
    except:
      print("Invalid json %s at line %d" % (FILE, count))
      continue
    
    if '$$deleted' in enJson:
      continue

    # by default only id and name are copied
    dataJson = {
      '_id': enJson['_id'],
      'name': enJson['name']
    }
    
    # retrive description based on pack desc path
    node = enJson
    i = 0
    while i < len(descPathParts) and descPathParts[i] in node:
      node = node[descPathParts[i]]
      i = i + 1
    if i == len(descPathParts):
      dataJson['description'] = node

    # add custom properties based on type
    data_id = p['id']

    # ancestries
    if data_id == 'ancestries':
      dataJson['additionalLanguages'] = enJson['data']['additionalLanguages']['value']
      dataJson['hp'] = enJson['data']['hp']
      dataJson['languages'] = enJson['data']['languages']['value']
    elif data_id == 'spells-srd':
      dataJson['school'] = enJson['data']['school']['value']
  
    # add translations
    dataJson['translations'] = { 'fr': { 'status': 'aucune' } }
    if dataJson['_id'] in translations:
      frJson =  translations[dataJson['_id']]
      dataJson['translations']['fr'] = frJson
      
    list.append(dataJson)

  with open(WEBSITE_DATA + p['name'] + ".json", 'w') as outfile:
    json.dump(list, outfile, indent=3)
