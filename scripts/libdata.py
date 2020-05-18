#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

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
    descr = ""
    status = ""
    isDesc = False  
    
    for line in content:
      if isDesc:
        descr += line
      elif line.startswith("Name:"):
        data['nameEN'] = line[5:].strip()
      elif line.startswith("Nom:"):
        data['nameFR'] = line[4:].strip()
      elif line.startswith("État:"):
        data['status'] = line[5:].strip()
      elif line.startswith("------ Description (fr) ------"):
        isDesc = True
    
    data['description'] = descr.replace('\n','').strip()
    
  else:
    print("Invalid path: %s" % filepath)
    exit(1)
  
  return data
