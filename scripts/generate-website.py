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
  
  if p["name"] == "actionspf2e":
    
    translations = {}
    
    #############################################
    # read all available data for specified pack
    #############################################
    path = "../data/%s/" % p["id"]
    all_files = os.listdir(path)
    for fpath in all_files:
      
      data = fileToData(path + fpath)
      if data['status'] == 'aucune':
        continue
          
      # default (all translations in french)
      translations[data['id']] = { 'name': data['nameFR'], 'description': data['descrFR'], 'status': data['status'] }

    #############################################
    # read original data from pf2 Foundry system
    #############################################
    with open(PACKS + p["id"] + ".db", 'r') as f:
      content = f.readlines()

    count = 0
    for line in content:
      count += 1
      try:
        obj = json.loads(line)
      except:
        print("Invalid json %s at line %d" % (FILE, count))
        continue
      
      if '$$deleted' in obj:
        continue
    
      # get translations
      obj['translations'] = { 'fr': { 'status': 'aucune' } }
      if obj['_id'] in translations:
        el =  translations[obj['_id']]
        obj['translations']['fr']['status'] = el['status']
        obj['translations']['fr']['name'] = el['name']
        obj['translations']['fr']['description'] = el['description']
        
      list.append(obj)

    with open(WEBSITE_DATA + "actions.json", 'w') as outfile:
      json.dump(list, outfile)
