#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import os            
import datetime

from libdata import *


#TRANSL={
  #'pf2e.spells-srd': { 'label': "Sorts" },
  #'pf2e.feats-srd': { 'label': "Dons" },
  #'pf2e.equipment-srd': { 'label': "Équipement" },
  #'pf2e.conditionspf2e': { 'label': "Conditions" },
  #'pf2e.actionspf2e': { 'label': "Actions" },
  #'pf2e.archetypes': { 'label': "Archétypes" },
  ##'pf2e.pathfinder-bestiary': { 'label': "Bestiaire" },
  ##'pf2e.pathfinder-bestiary-2': { 'label': "Bestiaire 2" },
  ##'pf2e.hazards': { 'label': "Dangers" },
  ##'pf2e.age-of-ashes-bestiary': { 'label': "Bestiaire AoA" },
  ##'pf2e.extinction-curse-bestiary': { 'label': "Bestiaire EC" },
  ##'pf2e.fall-of-plaguestone-bestiary': { 'label': "Bestiaire FoP" },
  ##'pf2e.iconics': { 'label': "Personnages prétirés iconiques" },
  ##'pf2e.iconics': { 'label': "Personnages prétirés iconiques" },
  ##'pf2e.npc-gallery': { 'label': "Gallerie NPJ" },
  #'pf2e.ancestryfeatures': { 'label': "Ascendances" },
  #'pf2e.classfeatures': { 'label': "Capacités de classe" },
  ##'pf2e.rollable-tables': { 'label': "Tables aléatoires" },
  #'pf2e.backgrounds': { 'label': "Backgrounds" },
  ##'pf2e.deities': { 'label': "Divinités" },
  ##'pf2e.gmg-srd': { 'label': "Guide du MJ" },
  ##'pf2e.gmg-srd': { 'label': "Guide du MJ" },
  #'pf2e.classes': { 'label': "Classes" },
  ##'pf2e.criticaldeck': { 'label': "Critiques" },
  ##'pf2e.pf2e-macros': { 'label': "Macros PF2e" },
  #'pf2e.bestiary-ability-glossary-srd': { 'label': "Bestiaires (aptitudes)" },
  ##'pf2e.pathfinder-society-boons': { 'label': "Aubaines de société" },
  #'pf2e.boons-and-curses': { 'label': "Bénédictions et malédications" },
#}



BABELE="../babele/fr/"
BABELE_VF_VO="../babele-alt/vf-vo/fr/"
BABELE_VO_VF="../babele-alt/vo-vf/fr/"
BABELE_VO="../babele-alt/vo/fr/"

packs = getPacks()
translations = {}

for p in packs:   
  
  key = "%s.%s" % (p["module"],p["name"])  
  translations[p["id"]] = []
  packName = p["transl"]
  
  path = "../data/%s/" % p["id"]
  all_files = os.listdir(path)

  babele     = { 'label': packName, 'entries': [] }
  babeleVfVo = { 'label': packName, 'entries': [] }
  babeleVoVf = { 'label': packName, 'entries': [] }
  babeleVo   = { 'label': packName, 'entries': [] }

  count = { "aucune": 0, "libre": 0, "officielle": 0, "changé": 0, "doublon": 0 }
  
  # read all files in folder
  for fpath in all_files:
    
    data = fileToData(path + fpath)
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


  print("Statistiques: " + packName);
  print(" - Traduits: %d (officielle) %d (libre)" % (count["officielle"], count["libre"]));
  print(" - Changé: %d" % count["changé"]);
  print(" - Non-traduits: %d" % count["aucune"]);



# ==========================
# génération du dictionnaire
# ==========================
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
  
  
  
