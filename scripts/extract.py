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
  {'id': "classfeatures", 'name': "name", 'desc': "data.description.value", 'type1': "data.traits.value", 'type2': "data.level.value" },
  {'id': "conditions", 'name': "name", 'desc': "content" },
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

  count = 0
  for line in content:
    count += 1
    try:
      obj = json.loads(line)
    except:
      print("Invalid json %s at line %d" % (FILE, count))
      continue
    
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
  
  # ==========================
  # read all available entries
  # ==========================
  existing = readFolder("%sdata/%s/" % (ROOT, F['id']))
  
  # ========================
  # create or update entries
  # ========================
  for id in entries:
    source = entries[id]
    if not source:
      continue

    # build filename
    filename =  "%s.htm" % id
    if source['type2']:
      filename = "%s-%s-%s" % (source['type1'], source['type2'], filename)
    elif source['type1']:
      filename = "%s-%s" % (source['type1'], filename)
    filepath = "%sdata/%s/%s" % (ROOT, F['id'], filename)
    
    # data exists for id
    if id in existing:

      # rename file if filepath not the same
      if existing[id]['filename'] != filename:
        pathFrom = "%sdata/%s/%s" % (ROOT, F['id'], existing[id]['filename'])
        pathTo = "%sdata/%s/%s" % (ROOT, F['id'], filename)
        os.rename(pathFrom, pathTo)
      
      # check status from existing file
      if not existing[id]["status"] in ("libre", "officielle", "doublon", "aucune", "changé"):
        print("Status error for : %s" % filepath);
        exit(1)
        
      if not equals(existing[id]['nameEN'],source['name']) or not equals(existing[id]['descrEN'], source['desc']):
        existing[id]['nameEN'] = source['name']
        existing[id]['descrEN'] = source['desc']
        
        if existing[id]['status'] != "aucune":
          existing[id]['oldstatus'] = existing[id]['status']
          existing[id]['status'] = "changé"
          
        dataToFile(existing[id], filepath)
      
      elif 'oldstatus' in existing[id] and existing[id]['status'] != 'changé':
        del existing[id]['oldstatus']
        dataToFile(existing[id], filepath)
      
    # file doesn't exist => create new
    else:
      data = { 
        'nameEN': source['name'],
        'nameFR': "",
        'status': 'aucune',
        'descrEN': source['desc'],
        'descrFR': "" }
      dataToFile(data, filepath)
    
    continue
  

  # =======================
  # search deleted elements
  # =======================
  for id in existing:
    if not id in entries:
      filename = "%sdata/%s/%s" % (ROOT, F['id'], existing[id]['filename'])
      if existing[id]['status'] != 'aucune':
        print("File cannot be safely removed! %s" % filename)
        print("Please fix manually!")
        exit(1)
      else:
        os.remove(filename)
  
  
  
  
