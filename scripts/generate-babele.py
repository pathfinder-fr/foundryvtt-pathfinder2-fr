#!/usr/bin/python3
# -*- coding: utf-8 -*-

BABELE="../babele/fr/"
BABELE_VF_VO="../babele-alt/vf-vo/fr/"
BABELE_VO_VF="../babele-alt/vo-vf/fr/"
BABELE_VO="../babele-alt/vo/fr/"

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
import datetime

from libdata import *


for key in TRANSL:   
  path = TRANSL[key]['path']
  all_files = os.listdir(path)

  babele     = { 'label': TRANSL[key]['label'], 'entries': [] }
  babeleVfVo = { 'label': TRANSL[key]['label'], 'entries': [] }
  babeleVoVf = { 'label': TRANSL[key]['label'], 'entries': [] }
  babeleVo   = { 'label': TRANSL[key]['label'], 'entries': [] }

  count = { "aucune": 0, "libre": 0, "officielle": 0, "changé": 0, "doublon": 0 }
  TRANSL[key]['data'] = []  
  
  # read all files in folder
  for fpath in all_files:
    
    data = fileToData(path + fpath)
    count[data['status']] += 1
    
    # prepare data
    match = re.search('/([^/]+/[^/]+\.htm)$', path + fpath)
    if not match:
      print("Invalid filename %s" % path + fpath)
      exit(1)
      
    TRANSL[key]['data'].append({ 
      'file': match.group(1),
      'name': data['nameEN'], 
      'nom': data['nameFR'] if 'nameFR' in data else "-",
      'link': "@Compendium[%s.%s]" % (key, data['id'])
    })
    
    if data['status'] == 'aucune':
      continue
    elif not isValid(data):
      print("Skipping invalid entry %s" % path + fpath)
      continue
        
    # default (all translations in french
    entry = { 'id': data['nameEN'], 'name': data['nameFR'], 'description': data['descrFR'] }
    babele['entries'].append(entry)
    # vf-vo
    entry = { 'id': data['nameEN'], 'name': ("%s (%s)" % (data['nameFR'], data['nameEN'])), 'description': data['descrFR'] }
    babeleVfVo['entries'].append(entry)
    # vo-vf
    entry = { 'id': data['nameEN'], 'name': ("%s (%s)" % (data['nameEN'], data['nameFR'])), 'description': data['descrFR'] }
    babeleVoVf['entries'].append(entry)
    # vo
    entry = { 'id': data['nameEN'], 'name': data['nameEN'], 'description': data['descrFR'] }
    babeleVo['entries'].append(entry)

  with open(BABELE + key + ".json", 'w', encoding='utf-8') as f:
    json.dump(babele, f, ensure_ascii=False, indent=4)
  with open(BABELE_VF_VO + key + ".json", 'w', encoding='utf-8') as f:
    json.dump(babeleVfVo, f, ensure_ascii=False, indent=4)
  with open(BABELE_VO_VF + key + ".json", 'w', encoding='utf-8') as f:
    json.dump(babeleVoVf, f, ensure_ascii=False, indent=4)
  with open(BABELE_VO + key + ".json", 'w', encoding='utf-8') as f:
    json.dump(babeleVo, f, ensure_ascii=False, indent=4)


  print("Statistiques: " + TRANSL[key]['label']);
  print(" - Traduits: %d (officielle) %d (libre)" % (count["officielle"], count["libre"]));
  print(" - Changé: %d" % count["changé"]);
  print(" - Non-traduits: %d" % count["aucune"]);



# ==========================
# génération du dictionnaire
# ==========================
content = "# Bibliothèque\n\n"
content += "\n\nDernière mise à jour: %s *(heure de Canada/Montréal)*" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
content += "\n\nCe fichier est généré automatiquement. NE PAS MODIFIER!"
  
for key in TRANSL: 
  content += "\n\n## %s\n\n" % TRANSL[key]['label']
  
  sortedList = sorted(TRANSL[key]['data'], key=lambda k: k['name'])
  for el in sortedList:
    content += "|[%s](%s)|%s|%s|\n" % (el['file'], el['name'], el['nom'], el['link'])
  
with open("../data/dictionnaire.md", 'w', encoding='utf-8') as f:
  f.write(content)
  
  
  
