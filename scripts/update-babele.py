#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import os            
import datetime

from libdata import *

BABELE="../babele/fr/"
BABELE_VF_VO="../babele-alt/vf-vo/fr/"
BABELE_VO_VF="../babele-alt/vo-vf/fr/"
BABELE_VO="../babele-alt/vo/fr/"


#
# cette fonction ajoute dynamiquement les champs de listes
#
def addLists(pack, data, entry):
  if "lists" in pack and "listsFR" in data:
    for k in pack["lists"]:
      if len(data["listsFR"][k]) > 0:
        if k == "Prereq":
          json_array = []
          for item in data["listsFR"][k]:
            json_array += [{ "value": item }]
          entry[k.lower()] = json_array
        else:
          entry[k.lower()] = data["listsFR"][k]

  if "extract" in pack:
    for k in pack["extract"]:
      if k in data["dataFR"] and len(data["dataFR"][k].strip()) > 0:
        entry[k.lower()] = data["dataFR"][k]

packs = getPacks()
translations = {}

for p in packs:   

  key = "%s.%s" % ("pf2e",p["name"])  
  translations[p["id"]] = []
  packName = p["transl"]
  
  path = "../data/%s/" % p["id"]
  all_files = os.listdir(path)

  babele     = { 'label': packName, 'entries': [], 'mapping': {} }
  babeleVfVo = { 'label': packName, 'entries': [], 'mapping': {} }
  babeleVoVf = { 'label': packName, 'entries': [], 'mapping': {} }
  babeleVo   = { 'label': packName, 'entries': [], 'mapping': {} }

  count = { "aucune": 0, "libre": 0, "officielle": 0, "changé": 0, "doublon": 0, 
           "auto-trad": 0, "auto-googtrad": 0, "vide": 0 }
  
  # add mappings
  if 'desc' in p['paths']:
    babele['mapping']["description"] = p['paths']['desc']
    babeleVfVo['mapping']["description"] = p['paths']['desc']
    babeleVoVf['mapping']["description"] = p['paths']['desc']
    babeleVo['mapping']["description"] = p['paths']['desc']

  if "lists" in p:
    for k in p["lists"]:
      babele['mapping'][k.lower()] = p["lists"][k]
      babeleVfVo['mapping'][k.lower()] = p["lists"][k]
      babeleVoVf['mapping'][k.lower()] = p["lists"][k]
      babeleVo['mapping'][k.lower()] = p["lists"][k]
  
  if "extract" in p:
    for k in p["extract"]:
      babele['mapping'][k.lower()] = p["extract"][k]
      babeleVfVo['mapping'][k.lower()] = p["extract"][k]
      babeleVoVf['mapping'][k.lower()] = p["extract"][k]
      babeleVo['mapping'][k.lower()] = p["extract"][k]

  # read all files in folder
  for fpath in all_files:
    
    data = fileToData(path + fpath)
    if data['status'] == "auto-trad":
      data['descFr'] = ""
    count[data['status']] += 1
    
    # prepare data
    match = re.search('/([^/]+/[^/]+\.htm)$', path + fpath)
    if not match:
      print("Invalid filename %s" % path + fpath)
      exit(1)
      
    translations[p["id"]].append({ 
      'file': match.group(1),
      'name': data['nameEN'], 
      'nom': data['nameFR'] if 'nameFR' in data else "-",
      'link': "@Compendium[%s.%s]" % (key, data['id'])
    })
    
    if data['status'] == 'aucune' or data['status'] == "auto-trad" \
      or data['status'] == "auto-googtrad"  or data['status'] == "vide":
      continue
    elif not isValid(data):
      print("Skipping invalid entry %s" % path + fpath)
      continue
        
    # default (all translations in french)
    entry = { 'id': data['nameEN'], 'name': data['nameFR'], 'description': data['descrFR'] }
    addLists(p, data, entry)
    babele['entries'].append(entry)
    # vf-vo (names in both languages, vf first)
    entry = { 'id': data['nameEN'], 'name': ("%s (%s)" % (data['nameFR'], data['nameEN'])), 'description': data['descrFR'] }
    addLists(p, data, entry)
    babeleVfVo['entries'].append(entry)
    # vo-vf (names in both languages, vo first)
    entry = { 'id': data['nameEN'], 'name': ("%s (%s)" % (data['nameEN'], data['nameFR'])), 'description': data['descrFR'] }
    addLists(p, data, entry)
    babeleVoVf['entries'].append(entry)
    # vo (only descriptions in french)
    entry = { 'id': data['nameEN'], 'name': data['nameEN'], 'description': data['descrFR'] }
    addLists(p, data, entry)
    babeleVo['entries'].append(entry)


  print(BABELE + key + ".json")
  with open(BABELE + key + ".json", 'w', encoding='utf-8') as f:
    json.dump(babele, f, ensure_ascii=False, indent=4)
  with open(BABELE_VF_VO + key + ".json", 'w', encoding='utf-8') as f:
    json.dump(babeleVfVo, f, ensure_ascii=False, indent=4)
  with open(BABELE_VO_VF + key + ".json", 'w', encoding='utf-8') as f:
    json.dump(babeleVoVf, f, ensure_ascii=False, indent=4)
  with open(BABELE_VO + key + ".json", 'w', encoding='utf-8') as f:
    json.dump(babeleVo, f, ensure_ascii=False, indent=4)


  print("Statistiques: " + packName);
  print(" - Traduits: %d (officielle) %d (libre)" % (count["officielle"], count["libre"]));
  print(" - Changé: %d" % count["changé"]);
  print(" - Non-traduits: %d - Auto-générés: %d" % (count["aucune"], count['auto-trad']+count['auto-googtrad']));
  print(" - Vides: %d" % count["vide"]);


# ===============================
# génération du dictionnaire (EN)
# ===============================
content = "# Bibliothèque\n\n"
content += "\n\nDernière mise à jour: %s *(heure de Canada/Montréal)*" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
content += "\n\nCe fichier est généré automatiquement. NE PAS MODIFIER!\n\n"

packs = sorted(packs, key=lambda k: k['transl'])

for p in packs:
  packName = p["transl"]
  content += " * [%s](#%s)\n" % (packName, packName.lower().replace(' ', '-'))

  
for p in packs: 
  packName = p["transl"]
  content += "\n\n## %s\n\n" % packName
  content += "| Nom (EN)   | Nom (FR)    | Lien compendium |\n"
  content += "|------------|-------------|-----------------|\n"
  
  sortedList = sorted(translations[p["id"]], key=lambda k: k['name'])
  for el in sortedList:
    content += "|[%s](%s)|%s|`%s`|\n" % (el['name'], el['file'], el['nom'], el['link'])
  
with open("../data/dictionnaire.md", 'w', encoding='utf-8') as f:
  f.write(content)
  

# ===============================
# génération du dictionnaire (FR)
# ===============================

content = "# Bibliothèque\n\n"
content += "\n\nDernière mise à jour: %s *(heure de Canada/Montréal)*" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
content += "\n\nCe fichier est généré automatiquement. NE PAS MODIFIER!\n\n"

packs = sorted(packs, key=lambda k: k['transl'])

for p in packs:
  packName = p["transl"]
  content += " * [%s](#%s)\n" % (packName, packName.lower().replace(' ', '-'))


for p in packs:
  packName = p["transl"]
  content += "\n\n## %s\n\n" % packName
  content += "| Nom (FR)   | Nom (EN)    | Lien compendium |\n"
  content += "|------------|-------------|-----------------|\n"

  sortedList = sorted(translations[p["id"]], key=lambda k: k['nom'])
  for el in sortedList:
    content += "|[%s](%s)|%s|`%s`|\n" % (el['nom'], el['file'], el['name'], el['link'])

with open("../data/dictionnaire-fr.md", 'w', encoding='utf-8') as f:
  f.write(content)

