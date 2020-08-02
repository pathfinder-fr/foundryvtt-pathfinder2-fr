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
  content += "\n## Liste des traductions complétés\n\n"
  content += statusContentOK
  
  with open("%s/data/status-%s.md" % (ROOT, D), 'w', encoding='utf-8') as f:
    f.write(content)
    
    
