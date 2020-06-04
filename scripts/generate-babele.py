#!/usr/bin/python3
# -*- coding: utf-8 -*-

BABELE="../babele/fr/"

TRANSL={
  'pf2e.actionspf2e': { 'label': "Actions", 'path': "../data/actions/" },
  'pf2e.classes': { 'label': "Classes", 'path': "../data/classes/" },
  'pf2e.equipment-srd': { 'label': "Équipement", 'path': "../data/equipment/" },
  'pf2e.feats-srd': { 'label': "Dons", 'path': "../data/feats/" },
  'pf2e.spells-srd': { 'label': "Sorts", 'path': "../data/spells/" },
  'pf2e.backgrounds': { 'label': "Backgrounds", 'path': "../data/backgrounds/" },
  'pf2e.ancestryfeatures': { 'label': "Ascendances", 'path': "../data/ancestryfeatures/" },
  'pf2e.classfeatures': { 'label': "Capacités de classe", 'path': "../data/classfeatures/" },
  'pf2e.conditionspf2e': { 'label': "Conditions", 'path': "../data/conditions/" },
}

import json
import os             

for key in TRANSL: 
  path = TRANSL[key]['path']
  all_files = os.listdir(path)

  data = { 
    'label': TRANSL[key]['label'],
    'entries': []
  }

  count = { "non": 0, "libre": 0, "officielle": 0, "changé": 0 }
    
  # read all files in folder
  for fpath in all_files:
    
    # read all lines in f
    with open(path + fpath, 'r') as f:
      content = f.readlines()
    
    nameEN = ""
    nameFR = ""
    descr = ""
    status = ""
    isDesc = False  
    
    for line in content:
      if isDesc:
        descr += line
      elif line.startswith("Name:"):
        nameEN = line[5:].strip()
      elif line.startswith("Nom:"):
        nameFR = line[4:].strip()
      elif line.startswith("État:"):
        status = line[5:].strip()
      elif line.startswith("------ Description (fr) ------"):
        isDesc = True

    if len(nameFR) == 0 and len(descr.replace('\n','').strip()) == 0:
      count["non"]+=1
      continue
    
    if status == "libre":
      count["libre"]+=1
    elif status == "officielle":
      count["officielle"]+=1
    elif status == "changé":
      count["changé"]+=1
    elif status == "doublon":
      continue
    elif status == "aucune":
      continue
    else:
      print("Status error for : %s (%s.%s)" % (nameEN, key, fpath));
      exit(1)
    
    entry = { 'id': nameEN }
    if len(nameFR) > 0:
      entry['name'] = nameFR
    if len(descr.replace('\n','').strip()) > 0:
      entry['description'] = descr
    data['entries'].append(entry)
        

  with open(BABELE + key + ".json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

  print("Statistiques: " + TRANSL[key]['label']);
  print(" - Traduits: %d (officielle) %d (libre)" % (count["officielle"], count["libre"]));
  print(" - Changé: %d" % count["changé"]);
  print(" - Non-traduits: %d" % count["non"]);
