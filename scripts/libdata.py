#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import re
import requests
import json


SUPPORTED = {
  "spells":                         { 'transl': "Sorts", "paths": { 'name': "name", 'desc': "data.description.value", 'type1': "data.school.value", 'type2': "data.level.value" } },
  "feats":                          { 'transl': "Dons",  "paths": { 'name': "name", 'desc': "data.description.value", 'type1': "data.featType.value", 'type2': "data.level.value" } },
  "equipment":                      { 'transl': "Équipement", "paths": { 'name': "name", 'desc': "data.description.value", 'type1': "type", 'type2': "data.level.value" } },
  "conditionspf2e":                 { 'transl': "Conditions", "paths": { 'name': "name", 'desc': "content" } },
  "conditionitems":                 { 'transl': "Conditions", "paths": { 'name': "name", 'desc': "data.description.value" } },
  "actions":                        { 'transl': "Actions", "paths": { 'name': "name", 'desc': "data.description.value" } },
  "archetypes":                     { 'transl': "Archétypes", "paths": { 'name': "name", 'desc': "content" } },
  "pathfinder-bestiary":            { 'transl': "Bestiaire", "paths": { 'name': "name", 'desc': "data.details.flavorText" } },
  "pathfinder-bestiary-2":          { 'transl': "Bestiaire 2", "paths": { 'name': "name", 'desc': "data.details.flavorText" } },
  "hazards":                        { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "data.details.description" } },
  #"age-of-ashes-bestiary":          { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "content" } },
  #"extinction-curse-bestiary":      { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "content" } },
  #"fall-of-plaguestone-bestiary":   { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "content" } },
  #"iconics":                        { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "content" } },
  #"npc-gallery":                    { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "content" } },
  "ancestryfeatures":               { 'transl': "Ascendances", "paths": { 'name': "name", 'desc': "data.description.value", 'type1': "type", 'type2': "data.level.value" } },
  "classfeatures":                  { 'transl': "Capacités de classe", "paths": { 'name': "name", 'desc': "data.description.value", 'type1': "data.traits.value", 'type2': "data.level.value" } },
  #"rollable-tables":                { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "content" } },
  "backgrounds":                    { 'transl': "Backgrounds", "paths": { 'name': "name", 'desc': "content" } },
  #"deities":                        { 'transl': "Divinités", "paths": { 'name': "name", 'desc': "content" } },
  "gmg-srd":                        { 'transl': "Guide du MJ", "paths": { 'name': "name", 'desc': "content" } },
  "classes":                        { 'transl': "Classes", "paths": { 'name': "name", 'desc': "content" } },
  #"criticaldeck":                   { 'transl': "Critiques", "paths": { 'name': "name", 'desc': "content" } },
  #"pf2e-macros":                    { 'transl': "Macros PF2e", "paths": { 'name': "name", 'desc': "content" } },
  "bestiary-ability-glossary-srd":  { 'transl': "Aptitudes du Bestiaire", "paths": { 'name': "name", 'desc': "data.description.value" } },
  "pathfinder-society-boons":       { 'transl': "Macros PF2e", "paths": { 'name': "name", 'desc': "data.description.value" } },
  "boons-and-curses":               { 'transl': "Bénédictions et malédictions", "paths": { 'name': "name", 'desc': "data.description.value" } },
}

#
# cette fonction lit le fichier system.json et extrait les informations sur les packs
#
def getPacks(): 
  response = json.loads(requests.get("https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/system.json").text)
  packs = []
  for p in response["packs"]:
    match = re.search('packs/([-\w]+)\.db', p['path'])
    if match:
      p['id'] = match.group(1).strip()
    else:
      print("Error parsing ID from %s" % p['path'])
      exit(1)
    
    if p['id'] in SUPPORTED:
      packs.append({ **p, **SUPPORTED[p['id']]})
    else:
      print("Skippping %s" % p["id"])
      
  return packs;

#
# cette fonction retourn vrai si les deux textes sont identiques
# (ignore les retours à la ligne)
#
def equals(val1, val2):
  return val1.replace('\n','').replace('\r', '').strip() == val2.replace('\n','').replace('\r', '').strip()

#
# cette fonction tente une extraction d'une valeur dans un objet
# Ex: data.level.value => obj["data"]["level"]["value"]
#
def getValue(obj, path, exitOnError = True, defaultValue = None):
  element = obj
  for p in path.split('.'):
    if p in element:
      element = element[p]
    elif exitOnError:
      print("Error with path %s in %s" % (path, obj))
      exit(1)
    else:
      print("Path %s not found for %s!" % (path, obj['name']))
      return defaultValue
  
  if element is None:
    return defaultValue
  elif isinstance(element, int):
    return "%02d" % element
  elif isinstance(element, list):
    if len(element) == 0:
      return defaultValue
    if len(element) > 1:
      print("List has more than 1 element for '%s'! %s" % (element, path))
      exit(1)
    return element[0]
  elif element.isdigit():
    return "%02d" % int(element)
  else:
    return element

#
# cette fonction extrait l'information d'un fichier
#
def fileToData(filepath):

  data = {}
  if os.path.isfile(filepath):
    
    # read all lines in f
    with open(filepath, 'r') as f:
      content = f.readlines()
      
    nameEN = ""
    nameFR = ""
    descrEN = ""
    descrFR = ""
    status = ""
    isDescEN = False  
    isDescFR = False  
    
    match = re.search('(\w{16})\.htm', filepath)
    if not match:
      print("Invalid filename %s" % filepath)
      exit(1)
    data['id'] = match.group(1)  
    
    for line in content:
      if line.startswith("Name:"):
        data['nameEN'] = line[5:].strip()
      elif line.startswith("Nom:"):
        data['nameFR'] = line[4:].strip()
      elif line.startswith("État:"):
        data['status'] = line[5:].strip()
      elif line.startswith("État d'origine:"):
        data['oldstatus'] = line[15:].strip()
      elif line.startswith("------ Description (en) ------"):
        isDescEN = True
        isDescFR = False
        continue
      elif line.startswith("------ Description (fr) ------"):
        isDescFR = True
        isDescEN = False
        continue
      
      if isDescEN:
        descrEN += line
      elif isDescFR:
        descrFR += line
      
      
    data['descrEN'] = descrEN.strip()
    data['descrFR'] = descrFR.strip()
    
  else:
    print("Invalid path: %s" % filepath)
    exit(1)
  
  if not 'nameEN' in data or not 'descrEN' in data:
    print("Invalid data: %s" % filepath)
    exit(1)
  
  return data

#
# cette fonction écrit
#
def dataToFile(data, filepath):

  with open(filepath, 'w') as df:
    df.write('Name: ' + data['nameEN'] + '\n')
    df.write('Nom: ' + data['nameFR'] + '\n')
    df.write('État: ' + data['status'] + '\n')
    if 'oldstatus' in data:
      df.write('État d\'origine: ' + data['oldstatus'] + '\n')
    df.write('\n')
    df.write('------ Description (en) ------' + '\n')
    df.write(data['descrEN'] + '\n')
    df.write('------ Description (fr) ------' + '\n')
    if len(data['descrFR']) > 0:
      df.write(data['descrFR'] + '\n')

  return data

#
# retourne vrai si l'entrée est valide
#
def isValid(data):
  return data['nameFR'] and len(data['nameFR']) > 0


#
# cette fonction lit tous les fichiers d'un répertoire (data)
# et génère un dictionnaire basé sur les identifiants
#
def readFolder(path):
  
  resultById = {}
  resultByName = {}
  all_files = os.listdir(path)
  
  # read all files in folder
  for fpath in all_files:
    
    data = fileToData(path + fpath)
    data['filename'] = fpath
    
    if data['id'] in resultById:
      print("Duplicate data %s %s" % (path + resultById[data['id']]['filename'], path + data['filename']))
      print("Please fix it manually!")
      exit(1)
      
    resultById[data['id']] = data
    resultByName[data['nameEN']] = data
    
  return [resultById, resultByName]
    
    
    
