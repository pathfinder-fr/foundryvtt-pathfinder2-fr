#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import yaml
import os
import datetime

from libdata import *


DIRS = ["feats"]
ROOT=".."

for D in DIRS:
  dirpath= "%s/data/%s" % (ROOT, D)

  statusContent = "| Fichier   | Nom (EN)    | État |\n" + "|-----------|-------------|:----:|\n"
    
  files = [f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]
  files = sorted(files, key=str.casefold)
  stats = {}
  
  for f in files:
    data = fileToData(os.path.join(dirpath,f))
    status = '<span style="color:red">%s</span>' % data['status'] if data['status'] == "aucune" else data['status']
    statusContent += "|[%s](%s/%s)|%s|%s|\n" % (f, D, f, data['nameEN'], status)
    if data['status'] in stats:
      stats[data['status']]+=1
    else:
      stats[data['status']]=1

  header = "# État de la traduction (%s)\n\n" % D
  for s in stats:
    header += " * **%s**: %d\n" % (s, stats[s])
  
  header += "\n\nDernière mise à jour: %s *(heure de Canada/Montréal)*" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
  header += "\n## Liste détaillée\n\n"
  
  with open("%s/data/status-%s.md" % (ROOT, D), 'w', encoding='utf-8') as f:
    f.write(header)
    f.write(statusContent)
    
    
