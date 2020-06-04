#!/usr/bin/python3
# -*- coding: utf-8 -*-

BABELE="../babele/fr/"

TRANSL={
  'pf2e.actionspf2e': { 'label': "Actions", 'path': "../data/actions/" },
  'pf2e.classes': { 'label': "Classes", 'path': "../data/classes/" },
  'pf2e.equipment-srd': { 'label': "Équipement", 'path': "../data/equipment/" },
  'pf2e.feats-srd': { 'label': "Dons", 'path': "../data/feats/" },
  'pf2e.spells-srd': { 'label': "Spells", 'path': "../data/spells/" }
}

import json
import os             

from libdata import *

output = {}

for key in TRANSL: 
  path = TRANSL[key]['path']
  all_files = os.listdir(path)

  typeKey = TRANSL[key]['label']
  output[typeKey] = {}

  count = { "non": 0, "libre": 0, "officielle": 0 }
    
  # read all files in folder
  for fpath in all_files:
    
    if os.path.isfile(path + fpath):
      data = fileToData(path + fpath)
      output[typeKey][data['nameEN']] = data['descrEN']

with open("../i18n/en_US/translations.json", 'w', encoding='utf-8') as f:
  json.dump(output, f, ensure_ascii=False, indent=4)

