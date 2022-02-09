#!/usr/bin/python3
# -*- coding: utf-8 -*-

############################################################
# Script de mise à jour du projet pf2-data-fr
# 
# Ce script a pour fonction de générer les données du projet
# pf2-data-fr et de les pousser.
#
# Il se sert des données anglaises et leur éventuelle
# traduction pour générer un fichier .json par type de
# données.
#
# Si une donnée n'est pas présente dans le projet pf2-data-fr
# C'est ce script que vous devrez modifier pour les ajouter.
#
############################################################

import json
import os            
import datetime

from libdata import *

PACKS        = "../packs/"
WEBSITE_DATA = "../../pf2-data-fr/"

packs = getPacks()

for pack in packs:   
  
  list = []
    
  # liste des données issues des fichiers de traduction FR
  frDatas = {}
  
  #############################################
  # read all available data for specified pack
  #############################################
  pack_id = pack['id']
  path = "../data/%s/" % pack_id
  all_files = os.listdir(path)
  print("Lecture données pack %s (%d fichiers)" % (pack_id, len(all_files)))
  for fpath in all_files:
    
    # le fichier data contient les données traduites selon le format spécifique documenté dans fileToData
    data = fileToData(path + fpath)

    if data['status'] == 'aucune' or data['status'] == "auto-trad" \
      or data['status'] == "auto-googtrad"  or data['status'] == "vide":
      continue

    # item id
    data_id = data['id']

    # contient les données traduites en FR
    translation = {
      'status': data['status'],
      'name': data['nameFR'],
      'description': data['descrFR']
    }

    # contient des données anglaises uniquement disponibles dans le fichier FR
    miscData = {      
    }

    # données FR
    frData = {
      'translation': translation,
      'misc': miscData
    }

    ###################################################
    # Récupération données fichier .htm français
    ###################################################
    #
    # C'est ici que l'on ajoute du contenu traduit spécifique selon le type de pack
    #
    # Si il existe un champ particulier renvoyé par fileToData dont la traduction FR nous intéresse,
    # c'est dans cette partie que l'on pourra l'ajouter dans la partie 'translation'
    #
    # Pour le format du tableau 'data', il faut aller voir la documentation de la fonction fileToData
    # du fichier libdata.py
    #
    # On peut recopier les informations dans deux endroits :
    #
    # Dans le dictionnaire 'translation' si c'est la traduction FR
    # Dans le dictionnaire 'misc' si c'est une donnée anglaise non disponible dans le JSON Foundry
    #
    # La valeur clé (ex: benefits) doit obligatoirement être identique dans le fichier de sortie
    # entre la version FR et EN.

    # feats
    # https://gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr/-/tree/master/data/feats
    if pack_id == 'feats':
      # on stocke le champ benefitsFR dans les traductions
      # et on stocke le benefitsEN dans le champ misc pour qu'il apparaisse en anglais
      addIfNotNull(translation, 'benefits', emptyAsNull(tryGetDict(data, 'benefitsFR')))
      addIfNotNull(miscData, 'benefits', emptyAsNull(tryGetDict(data, 'benefitsEN')))

    # spells
    # https://gitlab.com/pathfinder-fr/foundryvtt-pathfinder2-fr/-/tree/master/data/spells
    if pack_id == 'spells':
      addIfNotNull(translation, 'target', emptyAsNull(tryGetDict(data, 'dataFR', 'Target')))
      addIfNotNull(miscData, 'target', emptyAsNull(tryGetDict(data, 'dataEN', 'Target')))
      addIfNotNull(translation, 'range', emptyAsNull(tryGetDict(data, 'dataFR', 'Range')))
      addIfNotNull(miscData, 'range', emptyAsNull(tryGetDict(data, 'dataEN', 'Range')))
      addIfNotNull(translation, 'materials', emptyAsNull(tryGetDict(data, 'dataFR', 'Material')))
      addIfNotNull(miscData, 'materials', emptyAsNull(tryGetDict(data, 'dataEN', 'Material')))
      addIfNotNull(translation, 'secondaryCaster',  tryIntOrNone(emptyAsNull(tryGetDict(data, 'dataFR', 'SecondaryCaster'))))
      addIfNotNull(miscData, 'secondaryCaster', tryIntOrNone(emptyAsNull(tryGetDict(data, 'dataEN', 'SecondaryCaster'))))
      addIfNotNull(translation, 'primaryCheck', emptyAsNull(tryGetDict(data, 'dataFR', 'PrimaryCheck')))
      addIfNotNull(miscData, 'primaryCheck', emptyAsNull(tryGetDict(data, 'dataEN', 'PrimaryCheck')))
      addIfNotNull(translation, 'secondaryCheck', emptyAsNull(tryGetDict(data, 'dataFR', 'SecondaryCheck')))
      addIfNotNull(miscData, 'secondaryCheck', emptyAsNull(tryGetDict(data, 'dataEN', 'SecondaryCheck')))
      addIfNotNull(translation, 'areaSize', emptyAsNull(tryGetDict(data, 'dataFR', 'Areasize')))
      addIfNotNull(miscData, 'areaSize', emptyAsNull(tryGetDict(data, 'dataEN', 'Areasize')))

    # store translation
    frDatas[data_id] = frData

  #############################################
  # read original data from pf2 Foundry system
  #############################################
  filename = PACKS + pack_id + ".db"
  descPathParts = pack['paths']['desc'].split('.')

  with open(filename, 'r', encoding='utf8') as f:
    content = f.readlines()

  count = 0
  for line in content:
    count += 1
    try:
      enJson = json.loads(line)
    except:
      print("Invalid json %s at line %d" % (filename, count))
      continue
    
    if '$$deleted' in enJson:
      continue

    # by default only id and name are copied
    dataJson = {
      '_id': enJson['_id'],
      'name': enJson['name']
    }
    
    # retrive description based on pack desc path
    node = enJson
    i = 0
    while i < len(descPathParts) and descPathParts[i] in node:
      node = node[descPathParts[i]]
      i = i + 1
    if i == len(descPathParts):
      dataJson['description'] = node

    # add custom properties based on type

    try:
      ###################################################
      # Récupération données fichier json anglais
      ###################################################
      #
      # C'est ici que l'on personnalise le contenu exporté selon le type de pack (pack_id).
      #
      # La variable enJson contient les données json du fichier anglais (foundry-vtt---pathfinder-2e)
      # Le but est de recopier dans la partie dataJson (export vers pf2-data-fr) les données du fichier
      # anglais qui nous intéressent, en manipulant si possible les données pour les rendre les plus claires possibles
      #
      # Le JSON anglais a une structure spécifique, imposée par le module Foundry.
      #
      # L'intérêt de cette partie et de recopier les données intréressantes tout en faisant  disparaître les spécificités
      # du format Foundry pour rendre le JSON le plus "logique" possible.
      #
      # Ex :
      # le type d'action est stocké dans un 'data': { 'actionType': { 'value': 'xxx' } }
      # ce script simplifie la structure pour simplement stocker cette information dans un json { 'actionType': 'xxx' }


      # actions
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/actions.db
      if pack_id == 'actions':
        dataJson['actionType'] = enJson['data']['actionType']['value']

      # ancestries
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/ancestries.db
      if pack_id == 'ancestries':
        dataJson['additionalLanguages'] = enJson['data']['additionalLanguages']['value']
        dataJson['hp'] = enJson['data']['hp']
        dataJson['languages'] = enJson['data']['languages']['value']

      # ancestryfeatures
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/ancestryfeatures.db
      if pack_id == 'ancestryfeatures':
        dataJson['traits'] = enJson['data']['traits']['value']
        # inutile à priori, car toujours identique
        # dataJson['featType'] = enJson['data']['featType']['value']
        # dataJson['level'] = enJson['data']['level']['value']
        # dataJson['actionType'] = enJson['data']['actionType']['value']

      # équipement
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/equipment.db
      if pack_id == 'equipment':
        data_type = dataJson['type'] = enJson['type']
        dataJson['price'] = enJson['data']['price']['value']
        dataJson['traits'] = enJson['data']['traits']['value']
        dataJson['rarity'] = enJson['data']['traits']['rarity']['value']
        if data_type == 'armor':
          # champs spécifiques aux armures
          # on les transforme en nombres
          dataJson['level'] = int(enJson['data']['level']['value'])
          dataJson['armor'] = int(enJson['data']['armor']['value'])
          dataJson['armorType'] = enJson['data']['armorType']['value']
          # propriétés que l'on ne souhaite pas recopier si elles n'ont pas de valeur (= 0 ou vide)
          addIfNotNull(dataJson, 'armorMaxDex', tryIntOrNone(emptyAsNull(enJson['data']['dex']['value'], '0')))
          addIfNotNull(dataJson, 'armorCheck', tryIntOrNone(emptyAsNull(enJson['data']['check']['value'], '0')))
          addIfNotNull(dataJson, 'armorStrength', tryIntOrNone(emptyAsNull(enJson['data']['strength']['value'], '0')))
          addIfNotNull(dataJson, 'armorEquippedBulk', tryIntOrNone(emptyAsNull(enJson['data']['equippedBulk']['value'])))
          addIfNotNull(dataJson, 'armorGroup', emptyAsNull(enJson['data']['group']['value']))
        if data_type == "weapon":
          # champs spécifiques aux armes
          dataJson['level'] = int(enJson['data']['level']['value'])
          dataJson['weaponType'] = enJson['data']['weaponType']['value']
          dataJson['damage'] = {}
          dataJson['damage']['type'] = enJson['data']['damage']['damageType']
          dataJson['damage']['dice'] = enJson['data']['damage']['dice']
          dataJson['damage']['die'] = enJson['data']['damage']['die']
          # propriétés que l'on ne souhaite pas recopier si vides
          addIfNotNull(dataJson, 'group', tryGetDict(enJson, 'data', 'group', 'value'))
          addIfNotNull(dataJson, 'range', tryGetDict(enJson, 'data', 'range', 'value'))
          addIfNotNull(dataJson, 'weight', tryGetDict(enJson, 'data', 'weight', 'value'))

      # classes
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/classes.db
      if pack_id == 'classes':
        # aucune propriété particulière, on préfèrera générer les pages de classes manuellement pour l'instant
        pass
      
      # class features
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/classfeatures.db
      if pack_id == 'classfeatures':
        dataJson['level'] = int(enJson['data']['level']['value'])
        dataJson['traits'] = enJson['data']['traits']['value']
        pass

      # spells
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/spells.db
      if pack_id == 'spells':
        dataJson['school'] = enJson['data']['school']['value']
        dataJson['type'] = enJson['data']['category']['value'] # focus, ritual ou spell
        dataJson['level'] = tryIntOrNone(enJson['data']['level']['value'])
        dataJson['traits'] = enJson['data']['traits']['value']
        addIfNotNull(dataJson, 'traditions', emptyAsNull(enJson['data']['traditions']['value']))
        dataJson['incantation'] = {}
        dataJson['incantation']['time'] = tryIntOrNone(enJson['data']['time']['value'])
        dataJson['incantation']['components'] = enJson['data']['components']

      # feats
      # cf. https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/tree/master/packs/data/feats.db
      if pack_id == 'feats':
        dataJson['featType'] = enJson['data']['featType']['value']
        dataJson['level'] = tryIntOrNone(enJson['data']['level']['value'])
        dataJson['traits'] = enJson['data']['traits']['value']

    except Exception as ex:
      print("Unable to convert data from %s at line %d : %s" % (filename, count, ex))
  
    #############################################
    # Ajout données de traductions
    #############################################
    # 
    # Par défaut on marque qu'il n'y a aucune traduction dans le json :
    # "translations": { "fr": { "status": "aucune", ... } }
    translation = { 'status': 'aucune' }

    # On recopie dans "fr" l'intégralité des informations de traduction
    if dataJson['_id'] in frDatas:
      frData = frDatas[dataJson['_id']]

      # recopie des données 'translation' dans la partie traduction
      translation = frData['translation']

      # on écrase les données EN avec les éventuelles propriétés stockées dans misc
      misc = frData['misc']
      for key, value in misc.items():
        dataJson[key] = value

    # on ajoute la translation à la fin, pour que les autres propriétés soient toujours avant
    dataJson['translations'] = { 'fr': translation }
      
    list.append(dataJson)

  with open(WEBSITE_DATA + pack['name'] + ".json", 'w') as outfile:
    json.dump(list, outfile, indent=3)
