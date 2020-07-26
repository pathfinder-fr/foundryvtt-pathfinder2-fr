#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from libdata import *

packs = getPacks()

os.system("rm ../packs/*")
for p in packs:
  id = p['id']
  os.system("curl -s https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/static/packs/%s.db > ../packs/%s.db" % (id, id))
  print("Pack %s downloaded!" % id)
