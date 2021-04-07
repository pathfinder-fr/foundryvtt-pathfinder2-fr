#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import yaml
import os
import re

from libdata import *
  
ROOT="../"

packs = getPacks()

for p in packs:
  
  FILE=ROOT + "packs/" + p["id"] + ".db"
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
      'name': getValue(obj, p['paths']['name']), 
      'desc': getValue(obj, p['paths']['desc'], False, ""), 
      'type1': getValue(obj, p['paths']['type1']) if 'type1' in p['paths'] else None,
      'type2': getValue(obj, p['paths']['type2'], False) if 'type2' in p['paths'] else None,
      'lists': {}
    }
    
    ## additional lists
    if "lists" in p:
      for key in p["lists"]:
        list = getList(obj, p["lists"][key], False)
        if len(list) == 0:
          list = getList(obj, p["lists"][key] + ".value", False)
        entries[obj['_id']]['lists'][key] = list
  
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
  folderData = readFolder("%sdata/%s/" % (ROOT, p["id"]))
  existing = folderData[0]
  existingByName = folderData[1]
  
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
    filepath = "%sdata/%s/%s" % (ROOT, p["id"], filename)
    
    # data exists for id
    if id in existing:

      # rename file if filepath not the same
      if existing[id]['filename'] != filename:
        pathFrom = "%sdata/%s/%s" % (ROOT, p["id"], existing[id]['filename'])
        pathTo = "%sdata/%s/%s" % (ROOT, p["id"], filename)
        os.rename(pathFrom, pathTo)
      
      # check status from existing file
      if not existing[id]["status"] in ("libre", "officielle", "doublon", "aucune", "changé", "auto-trad"):
        print("Status error for : %s" % filepath);
        exit(1)
       
      # QUICK FIX pour: https://discord.com/channels/@me/757146858828333077/815954577219780728
      change = False
      #if p["name"] == "feats-srd":
      #  change = True 
      
      if change or not equals(existing[id]['nameEN'],source['name']) or not equals(existing[id]['descrEN'], source['desc']) or not equals(existing[id]['listsEN'], source['lists']):
        existing[id]['nameEN'] = source['name']
        existing[id]['descrEN'] = source['desc']
        existing[id]['listsEN'] = source['lists']
        
        if existing[id]['status'] != "aucune" and existing[id]['status'] != "changé":
          existing[id]['oldstatus'] = existing[id]['status']
          existing[id]['status'] = "changé"
          
        dataToFile(existing[id], filepath)
      
      elif 'oldstatus' in existing[id] and existing[id]['status'] != 'changé':
        del existing[id]['oldstatus']
        dataToFile(existing[id], filepath)
      
    # file doesn't exist
    else:
      
      # check if other entry exists with same name => means that ID has changed for the same element
      if source['name'] in existingByName and not source['name'] in ("Shattering Strike", "Chilling Spray"):
        oldEntry = existingByName[source['name']]
        # rename file
        pathFrom = "%sdata/%s/%s" % (ROOT, p["id"], oldEntry['filename'])
        pathTo = "%sdata/%s/%s" % (ROOT, p["id"], filename)

        if oldEntry['id'] in existing:
          del existing[oldEntry['id']]
        os.rename(pathFrom, pathTo)
      
      # create new
      else:
        tradDesc = dirtyTranslate(source['desc'])
        data = { 
          'nameEN': source['name'],
          'nameFR': "",
          'status': 'auto-trad',
          'descrEN': source['desc'],
          'descrFR': tradDesc,
          'listsEN': source['lists'],
          'listsFR': {} }
        dataToFile(data, filepath)
    
    
  

  # =======================
  # search deleted elements
  # =======================
  for id in existing:
    if not id in entries:
      filename = "%sdata/%s/%s" % (ROOT, p["id"], existing[id]['filename'])
      if existing[id]['status'] != 'aucune':
        print("File cannot be safely removed! %s" % filename)
        print("Please fix manually!")
        #exit(1)
        os.remove(filename)
      else:
        os.remove(filename)
  
  
  
  
