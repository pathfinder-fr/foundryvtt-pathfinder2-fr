#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

#
# cette fonction retourn vrai si les deux textes sont identiques
# (ignore les retours à la ligne)
#
def equals(val1, val2):
  return val1.replace('\n','').strip() == val2.replace('\n','').strip()

#
# cette fonction tente une extraction d'une valeur dans un objet
# Ex: data.level.value => obj["data"]["level"]["value"]
#
def getValue(obj, path):
  element = obj
  for p in path.split('.'):
    if p in element:
      element = element[p]
    else:
      print("Error with path %s in %s" % (path, obj))
      exit(1)
  
  if element.isdigit():
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
    
    for line in content:
      if line.startswith("Name:"):
        data['nameEN'] = line[5:].strip()
      elif line.startswith("Nom:"):
        data['nameFR'] = line[4:].strip()
      elif line.startswith("État:"):
        data['status'] = line[5:].strip()
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
  
  return data

#
# cette fonction écrit
#
def dataToFile(data, filepath):

  if os.path.isfile(filepath):
    
    with open(filepath, 'w') as df:
      df.write('Name: ' + data['nameEN'] + '\n')
      df.write('Nom: ' + data['nameFR'] + '\n')
      df.write('État: ' + data['status'] + '\n\n')
      df.write('------ Description (en) ------' + '\n')
      df.write(data['descrEN'] + '\n')
      df.write('------ Description (fr) ------' + '\n')
      if len(data['descrFR']) > 0:
        df.write(data['descrFR'] + '\n')
    
  else:
    print("Invalid path: %s" % filepath)
    exit(1)
  
  return data
