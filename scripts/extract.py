#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import yaml
import os
import re

from libdata import *

FILES = [
  {'id': "classes", 'name': "name", 'desc': "content" },
  {'id': "actions", 'name': "name", 'desc': "data.description.value" },
  {'id': "equipment", 'name': "name", 'desc': "data.description.value", 'type1': "type", 'type2': "data.level.value" },
  {'id': "feats",   'name': "name", 'desc': "data.description.value", 'type1': "data.featType.value", 'type2': "data.level.value" },
  {'id': "spells", 'name': "name", 'desc': "data.description.value", 'type1': "data.school.value", 'type2': "data.level.value" },
  {'id': "backgrounds", 'name': "name", 'desc': "content" },
  {'id': "ancestryfeatures", 'name': "name", 'desc': "data.description.value", 'type1': "type", 'type2': "data.level.value" },
]
  
ROOT="../"


for F in FILES:
  FILE=ROOT + "packs/" + F['id'] + ".db"

  entries = {}

  # =================================
  # read pack files and generate dict
  # =================================
  with open(FILE, 'r') as f:
    content = f.readlines()

  for line in content:
    obj = json.loads(line)
    
    if '$$deleted' in obj:
      continue
    
    entries[obj['_id']] = { 
      'name': getValue(obj, F['name']), 
      'desc': getValue(obj, F['desc']), 
      'type1': getValue(obj, F['type1']) if 'type1' in F else None,
      'type2': getValue(obj, F['type2'], False) if 'type2' in F else None
    }
  
  # ==============================
  # search for duplicates in names
  # ==============================
  duplic = {}
  for id in entries:
    if entries[id]['name'] in duplic:
      print("Duplicated name: %s (%s)" % (entries[id]['name'],id))
      #entries[id] = None
    else:
      duplic[entries[id]['name']] = id
  
  # ========================
  # create or update entries
  # ========================
  for id in entries:
    source = entries[id]
    if not source:
      continue
    
    # build filename
    filenameBase1 = "%s.htm" % id
    filenameBase2 = "%s.htm" % id
    filename = filenameBase1
    if source['type2']:
      filename = "%s-%s-%s" % (source['type1'], source['type2'], filenameBase1)
      filenameBase2 = "%s-%s" % (source['type1'], filenameBase1)
    elif source['type1']:
      filename = "%s-%s" % (source['type1'], filenameBase1)
      
    filepathBase1 = "%sdata/%s/%s" % (ROOT, F['id'], filenameBase1)
    filepathBase2 = "%sdata/%s/%s" % (ROOT, F['id'], filenameBase2)
    filepath = "%sdata/%s/%s" % (ROOT, F['id'], filename)
    if os.path.isfile(filepath):
      data = fileToData(filepath)
      
      if not data["status"] in ("libre", "officielle", "doublon", "aucune", "changé"):
        print("Status error for : %s" % filepath);
        exit(1)
      
      nameSource = source['name']
      nameDesc = source['desc']
      
      if not equals(data['nameEN'],nameSource) or not equals(data['descrEN'], nameDesc):
        
        data['nameEN'] = source['name']
        data['descrEN'] = source['desc']
        
        if data['status'] == "aucune":
          dataToFile(data, filepath)
        else:
          data['status'] = "changé"
          dataToFile(data, filepath)

    # old path2
    elif os.path.isfile(filepathBase1):
      os.rename(filepathBase1, filepath)
    elif os.path.isfile(filepathBase2):
      os.rename(filepathBase2, filepath)
    
    else:
      data = { 
        'nameEN': source['name'],
        'nameFR': "",
        'status': 'aucune',
        'descrEN': source['desc'],
        'descrFR': "" }
      
      dataToFile(data, filepath)

  # =======================
  # search deleted elements
  # =======================
  all_files = os.listdir(ROOT + "data/" + F['id'])
  for f in all_files:
    el = re.search('-?(\w+)\.htm', f)
    if el:
      if not el.group(1) in entries:
        os.remove("%sdata/%s/%s" % (ROOT, F['id'], f))
        #print("Entry %s (%s) doesn't exist anymore" % (el.group(1), F['id']))
    else:
      print("Error: invalid filename: %s" % f)
      exit(1)
  
  
  
  
