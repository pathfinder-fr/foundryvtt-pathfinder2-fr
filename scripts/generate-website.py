#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import os            
import datetime

from libdata import *

PACKS        = "../packs/"
WEBSITE_DATA = "../pf2-data-fr/"

packs = getPacks()

for pack in packs:   
  
  list = []
    
  translations = {}
  
  #############################################
  # read all available data for specified pack
  #############################################
  path = "../data/%s/" % pack["id"]
  all_files = os.listdir(path)
  for fpath in all_files:
    
    data = fileToData(path + fpath)

    if data['status'] == 'aucune' or data['status'] == "auto-trad" \
      or data['status'] == "auto-googtrad"  or data['status'] == "vide":
      continue

    # item id
    data_id = data['id']

    # default (all translations in french)
    translation = {
      'status': data['status'],
      'name': data['nameFR'],
      'description': data['descrFR']
     }

    # specific treatments by data type
    if pack["id"] == 'feats':
      addIfNotNull(translation, 'avantage', emptyAsNull(tryGetDict(data, 'misc', 'Avantage')))

    # store translation
    translations[data_id] = translation

  #############################################
  # read original data from pf2 Foundry system
  #############################################
  filename = PACKS + pack["id"] + ".db"
  descPathParts = pack['paths']['desc'].split('.')

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
    data_id = pack['id']

    try:
      # actions
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/actions.db
      if data_id == 'actions':
        dataJson['actionType'] = enJson['data']['actionType']['value']

      # ancestries
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/ancestries.db
      if data_id == 'ancestries':
        dataJson['additionalLanguages'] = enJson['data']['additionalLanguages']['value']
        dataJson['hp'] = enJson['data']['hp']
        dataJson['languages'] = enJson['data']['languages']['value']

      # ancestryfeatures
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/ancestryfeatures.db
      if data_id == 'ancestryfeatures':
        dataJson['traits'] = enJson['data']['traits']['value']
        # inutile à priori, car toujours identique
        # dataJson['featType'] = enJson['data']['featType']['value']
        # dataJson['level'] = enJson['data']['level']['value']
        # dataJson['actionType'] = enJson['data']['actionType']['value']

      # équipement
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/equipment.db
      if data_id == 'equipment':
        data_type = dataJson['type'] = enJson['type']
        dataJson['price'] = enJson['data']['price']['value']
        dataJson['traits'] = enJson['data']['traits']['value']
        dataJson['rarity'] = enJson['data']['traits']['rarity']['value']
        if data_type == 'armor':
          # champs spécifiques aux armures
          dataJson['level'] = int(enJson['data']['level']['value'])
          dataJson['armor'] = int(enJson['data']['armor']['value'])
          dataJson['armorType'] = enJson['data']['armorType']['value']
          # propriétés que l'on ne souhaite pas recopier si elles n'ont pas de valeur (= 0 ou vide)
          addIfNotNull(dataJson, 'armorMaxDex', tryIntOrNone(emptyAsNull(enJson['data']['dex']['value'], '0')))
          addIfNotNull(dataJson, 'armorCheck', tryIntOrNone(emptyAsNull(enJson['data']['check']['value'], '0')))
          addIfNotNull(dataJson, 'armorStrength', tryIntOrNone(emptyAsNull(enJson['data']['strength']['value'], '0')))
          addIfNotNull(dataJson, 'armorEquippedBulk', tryIntOrNone(emptyAsNull(enJson['data']['equippedBulk']['value'])))
          addIfNotNull(dataJson, 'armorGroup', emptyAsNull(enJson['data']['group']['value']))

      # classes
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/classes.db
      if data_id == 'classes':
        # aucune propriété particulière, on préfèrera générer les pages de classes manuellement pour l'instant
        pass
      
      # class features
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/classfeatures.db
      if data_id == 'classfeatures':
        dataJson['level'] = int(enJson['data']['level']['value'])
        dataJson['traits'] = enJson['data']['traits']['value']
        pass

      # spells
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/spells.db
      if data_id == 'spells-srd':
        dataJson['school'] = enJson['data']['school']['value']

      # feats
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/feats.db
      if data_id == 'feats-srd':
        dataJson['featType'] = enJson['data']['featType']['value']
        dataJson['level'] = tryIntOrNone(enJson['data']['level']['value'])
        dataJson['traits'] = enJson['data']['traits']['value']

    except Exception as ex:
      print("Unable to convert data from %s at line %d : %s" % (filename, count, ex))
  
    # add translations
    dataJson['translations'] = { 'fr': { 'status': 'aucune' } }
    if dataJson['_id'] in translations:
      frJson =  translations[dataJson['_id']]
      dataJson['translations']['fr'] = frJson
      
    list.append(dataJson)

  with open(WEBSITE_DATA + pack['name'] + ".json", 'w') as outfile:
    json.dump(list, outfile, indent=3)
