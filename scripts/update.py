#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import yaml
import os
import datetime

from libdata import *


DIRS = ["actions", "classes", "equipment", "spells"]
ROOT=".."

for D in DIRS:
  compendium = "%s/packs/%s.db" % (ROOT, D)
  dirpath= "%s/data/%s" % (ROOT, D)
  
  # read compendiums
  with open(compendium, 'r') as f:
    content = f.readlines()
  
  # read entries in compendiums
  for line in content:
    obj = json.loads(line)
    
    # skip invalid entries
    if not 'name' in obj or not 'data' in obj:
      continue
    
    # check if file exists
    path = os.path.join(dirpath,"%s.htm" % obj['_id'])
    if not os.path.isfile(path):
      print("File not found: %s" % path)
      exit(1)
  
    # check content has not changed
    data = fileToData(path)
    newName = obj['name']
    newDesc = obj['data']['description']['value']
    
    if not equals(data['nameEN'],newName) or not equals(data['descrEN'], newDesc):
      
      data['nameEN'] = newName
      data['descrEN'] = newDesc
      
      if data['status'] == "aucune":
        dataToFile(data, path)
      else:
        data['status'] = "changé"
        dataToFile(data, path)
    
    
