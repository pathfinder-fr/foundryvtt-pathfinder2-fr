#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import re
import requests
import json

from libdata import *


path = "../data/conditionspf2e/"
all_files = os.listdir(path)

conditions = {}
conditionsById = {}
newConditions = {}

# read all old conditions files
for fpath in all_files:
  data = fileToData(path + fpath)
  conditions[data['nameEN']] = data
  conditionsById[data['id']] = data
  
# convert old conditions to new
path = "../data/conditionitems/"
all_files = os.listdir(path)
for fpath in all_files:
  data = fileToData(path + fpath)
  if data['nameEN'] in conditions:
    c = conditions[data['nameEN']]
    data['nameFR'] = c['nameFR']
    data['status'] = c['status']
    data['descrFR'] = c['descrFR'].replace("pf2e.conditionspf2e", "pf2e.conditionitems")
    dataToFile(data, path + fpath)
    
  else:
    print("not found: %s" % data['nameEN'])
  
