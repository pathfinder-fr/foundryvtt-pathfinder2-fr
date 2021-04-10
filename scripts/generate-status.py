#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import yaml
import os
import datetime

from libdata import *


ROOT=".."

for D in SUPPORTED:
  dirpath= "%s/data/%s" % (ROOT, D)

  statusContentOK = "| Fichier   | Nom (EN)    | Nom (FR)    | État |\n" + "|-----------|-------------|-------------|:----:|\n"
  statusContentChanged = "| Fichier   | Nom (EN)    | État |\n" + "|-----------|-------------|:----:|\n"
  statusContentEmpty = "| Fichier   | Nom (EN)    | État |\n" + "|-----------|-------------|:----:|\n"
  statusContentAT = "| Fichier   | Nom (EN)    | État |\n" + "|-----------|-------------|:----:|\n"
  statusContentNOK = "| Fichier   | Nom (EN)    |\n" + "|-----------|-------------|\n"
    
  files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]
  files = sorted(files, key=str.casefold)
  stats = {}
  
  for f in files:
    data = fileToData(os.path.join(dirpath,f))
    
    if data['status'] in stats:
      stats[data['status']]+=1
    else:
      stats[data['status']]=1
    
    if data['status'] == "aucune":
      statusContentNOK += "|[%s](%s/%s)|%s|\n" % (f, D, f, data['nameEN'])
    elif data['status'] == "auto-trad" or data['status'] == "auto-googtrad":
      statusContentAT += "|[%s](%s/%s)|%s|%s|\n" % (f, D, f, data['nameEN'], data['status'])
    elif data['status'] == "changed":
      statusContentChanged += "|[%s](%s/%s)|%s|%s|\n" % (f, D, f, data['nameEN'], data['status'])
    elif data['status'] == "vide":
      statusContentEmpty += "|[%s](%s/%s)|%s|%s|\n" % (f, D, f, data['nameEN'], data['status'])
    else:
      statusContentOK += "|[%s](%s/%s)|%s|%s|%s|\n" % (f, D, f, data['nameEN'], data['nameFR'], data['status'])
    

  content = "# État de la traduction (%s)\n\n" % D
  for s in stats:
    content += " * **%s**: %d\n" % (s, stats[s])
  
  content += "\n\nDernière mise à jour: %s *(heure de Canada/Montréal)*" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
  content += "\n\nCe fichier est généré automatiquement. NE PAS MODIFIER!"
  if "aucune" in stats and stats["aucune"] > 0:
    content += "\n## Liste des traductions à faire\n\n"
    content += statusContentNOK
  if "auto-trad" in stats and stats["auto-trad"] > 0 or "auto-googtrad" in stats and stats["auto-googtrad"] > 0:
    content += "\n## Liste des traductions automatiques à corriger/retraduire\n\n"
    content += statusContentAT
  if "changed" in stats and stats["changed"] > 0:
    content += "\n## Liste des éléments changés en VO et devant être vérifiés\n\n"
    content += statusContentChanged
  if "vide" in stats and stats["vide"] > 0:
    content += "\n## Liste des éléments vides ne pouvant pas être traduits\n\n"
    content += statusContentEmpty
  content += "\n## Liste des traductions complétés\n\n"
  content += statusContentOK
  
  with open("%s/data/status-%s.md" % (ROOT, D), 'w', encoding='utf-8') as f:
    f.write(content)
    
    
