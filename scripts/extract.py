#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import yaml
import os


FILES = ["actions", "classes", "equipment", "feats", "spells"]
ROOT="../"

for F in FILES:
  FILE=ROOT + "packs/" + F + ".db"

  # read file
  with open(FILE, 'r') as f:
    content = f.readlines()


  for line in content:
    obj = json.loads(line)
    
    filepath = ROOT + 'data/' + F + '/' + obj['_id'] + ".htm"
    if os.path.isfile(filepath):
      with open(filepath, 'r') as df:
        content = df.read()
        metadata = yaml.load(content.split('------ Description (en) ------')[0])
        if metadata['État'] != 'aucune':
          continue
    
    if not 'name' in obj:
        continue
      
    with open(filepath, 'w') as df:
      df.write('Name: ' + obj['name'] + '\n')
      df.write('Nom: ' + '\n')
      df.write('État: aucune\n\n')
      df.write('------ Description (en) ------' + '\n')
      
      if F in ("actions", "equipment", "feats", "spells"):
        df.write(obj['data']['description']['value'] + '\n')
      
      elif F == "classes":
        df.write(obj['content'] + '\n')
      df.write('------ Description (fr) ------' + '\n')
