#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import re
import requests
import json
import html
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


SUPPORTED = {
  "spells":                         { 'transl': "Sorts", "paths": { 'name': "name", 'desc': "data.description.value", 'type1': "data.school.value", 'type2': "data.level.value" } },
  "feats":                          { 'transl': "Dons",  "paths": { 'name': "name", 'desc': "data.description.value", 'type1': "data.featType.value", 'type2': "data.level.value" }, "lists": { 'Prereq' : "data.prerequisites" } },
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
  "ancestryfeatures":               { 'transl': "Ascendances (aptitudes)", "paths": { 'name': "name", 'desc': "data.description.value", 'type1': "type", 'type2': "data.level.value" } },
  "classfeatures":                  { 'transl': "Capacités de classe", "paths": { 'name': "name", 'desc': "data.description.value", 'type1': "data.traits.value", 'type2': "data.level.value" } },
  #"rollable-tables":                { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "content" } },
  "backgrounds":                    { 'transl': "Backgrounds", "paths": { 'name': "name", 'desc': "data.description.value" } },
  #"deities":                        { 'transl': "Divinités", "paths": { 'name': "name", 'desc': "content" } },
  "gmg-srd":                        { 'transl': "Guide du MJ", "paths": { 'name': "name", 'desc': "content" } },
  "classes":                        { 'transl': "Classes", "paths": { 'name': "name", 'desc': "data.description.value" } },
  #"criticaldeck":                   { 'transl': "Critiques", "paths": { 'name': "name", 'desc': "content" } },
  #"pf2e-macros":                    { 'transl': "Macros PF2e", "paths": { 'name': "name", 'desc': "content" } },
  "bestiary-ability-glossary-srd":  { 'transl': "Aptitudes du bestiaire", "paths": { 'name': "name", 'desc': "data.description.value" } },
  "pathfinder-society-boons":       { 'transl': "Macros PF2e", "paths": { 'name': "name", 'desc': "data.description.value" } },
  "boons-and-curses":               { 'transl': "Bénédictions et malédictions", "paths": { 'name': "name", 'desc': "data.description.value" } },
  "familiar-abilities":             { 'transl': "Aptitudes des familiers", "paths": { 'name': "name", 'desc': "data.description.value", 'type1': "data.level.value" } },
  "spell-effects":                  { 'transl': "Effets des sorts", "paths": { 'name': "name", 'desc': "data.description.value", 'type1': "data.level.value" } },
  "ancestries":                     { 'transl': "Ascendances", "paths": { 'name': "name", 'desc': "data.description.value" } },

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
#    else:
#      print("Skippping %s" % p["id"])
      
  return packs;

#
# cette fonction retourn vrai si les deux textes sont identiques
# (ignore les retours à la ligne)
#
def equals(val1, val2):
  if isinstance(val1, dict) and isinstance(val2, dict):
    keys1 = list(val1.keys())
    keys2 = list(val2.keys())
    if len(keys1) != len(keys2):
      return False
    # comparer le contenu de chaque clé
    for k in keys1:
      if not k in keys2:
        return False
      # contenu est une liste
      # retirer les vides des listes
      list1 = [e.strip() for e in val1[k] if len(e.strip()) > 0]
      list2 = [e.strip() for e in val2[k] if len(e.strip()) > 0]
      if list1 != list2:
        return False
    return True
  else:
    return val1.replace('\n','').replace('\r', '').strip() == val2.replace('\n','').replace('\r', '').strip()

#
# cette fonction tente une extraction d'une valeur dans un objet
# Ex: data.level.value => obj["data"]["level"]["value"]
#
def getObject(obj, path, exitOnError = True):
  element = obj
  for p in path.split('.'):
    if p in element:
      element = element[p]
    elif exitOnError:
      print("Error with path %s in %s" % (path, obj))
      exit(1)
    else:
      #print("Path %s not found for %s!" % (path, obj['name']))
      return None
  
  return element


def getValue(obj, path, exitOnError = True, defaultValue = None):
  element = getObject(obj, path, exitOnError)
  if element is None:
    return defaultValue
  elif isinstance(element, int):
    return "%02d" % element
  elif isinstance(element, list):
    if len(element) == 0:
      return defaultValue
    if len(element) > 1:
      print("List has more than 1 element for '%s'! %s" % (element, path))
      return element[len(element)-1]
    return element[0]
  elif element.isdigit():
    return "%02d" % int(element)
  else:
    return element

def getList(obj, path, exitOnError = True):
  element = getObject(obj, path, exitOnError)
  if element is None:
    return []
  elif not isinstance(element, list):
    if exitOnError:
      print("Element at '%s' is not a list! %s" % (path, element))
      exit(1)
    return []
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
      
    descrEN = ""
    descrFR = ""
    isDescEN = False  
    isDescFR = False
    listsEN = {}
    listsFR = {}
    
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
      elif not isDescEN and not isDescFR and len(line.strip()) > 0:
        sep = line.find(":")
        if sep < 0:
          print("Invalid data '%s' in file %s " % (line, filepath));
          exit(1)
        key = line[0:sep-2]
        lang = line[sep-2:sep]
        value = line[sep+1:].strip()
        liste = [e.strip() for e in value.split('|')]
        liste = [e.strip() for e in liste if len(e.strip()) > 0]
        if lang == "EN": 
          listsEN[key] = liste
        elif lang == "FR":
          listsFR[key] = liste
        else:
          print("Invalid key '%s' in file %s " % (key, filepath));
          exit(1)        
      
      if isDescEN:
        descrEN += line
      elif isDescFR:
        descrFR += line
      
    data['descrEN'] = descrEN.strip()
    data['descrFR'] = descrFR.strip()
    data['listsEN'] = listsEN
    data['listsFR'] = listsFR
    
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
    
    if data['listsEN']:
      for key in data['listsEN']:
        df.write("%sEN: %s\n" % (key, "|".join(data['listsEN'][key])))
        df.write("%sFR: %s\n" % (key, "|".join(data['listsFR'][key]) if key in data['listsFR'] else "" ))
    
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


#
# Cette fonction crée un driver Selenium pour la connexion à DeepL Translator
#
def translator_driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    try:
        driver.get("https://www.deepl.com/en/translator#en/fr/thing")
        time.sleep(3)
        return driver
    except Exception as e:
        print(e)
        driver.quit()
        raise


#
# Cette fonction tente une traduction automatique 
# sur DeepL Translator
#
def dirtyTranslate(driver, data):
    length = len(data)
    if (length<10):
      raise EmptyDescriptionException()
      return ""
    inputer = driver.find_element_by_class_name('lmt__source_textarea')
    inputer.clear()
    inputer.send_keys(html.escape(data))
    WebDriverWait(driver, 100).until(
        ExpectedConditions.text_to_be_present_in_element_value((By.CLASS_NAME, 'lmt__target_textarea'), ";"))
    if(length>8000):
      time.sleep(82)
    elif(length>1000):
      time.sleep(22)
    output = driver.find_element_by_class_name('lmt__target_textarea')
    transData = html.unescape(cleanTrad(output.get_attribute("value")))
    output.clear()
    return transData



#
# Nettoie la traduction en corrigeant les termes mal-traduits ou
# qui ne devaient pas être traduits
#
def cleanTrad(data):
    data = data.replace("&gt ;", "&gt")
    data = data.replace("Activate", "Activation")
    data = data.replace("Interact", "Interagir")
    data = data.replace("60 feet", "18 mètres")
    data = data.replace("30 feet", "9 mètres")
    data = data.replace("Traduit avec www.DeepL.com/Translator (version gratuite)", "")
    return data


#
# Cette fonction tente une traduction automatique 
# sur Google Translate
#
def dirtyGoogleTranslate(data):
  length = len(data)
  if (length<10):
    raise EmptyDescriptionException()
    return ""
  options = webdriver.FirefoxOptions()
  options.add_argument("--headless")
  driver = webdriver.Firefox(options=options)
  driver.get("https://translate.google.com/?sl=en&tl=fr&format=html&op=translate")
  inputer = driver.find_element_by_xpath("//textarea[@jsname='BJE2fc']")
  inputer.send_keys(data)
  output = WebDriverWait(driver, timeout=120).until(lambda d: d.find_element_by_xpath("//div[@class='J0lOec']"))
  transData = output.text
  driver.quit()
  transData = cleanGoogleTrad(transData)
  return transData


#
# Nettoie la traduction en corrigeant les termes mal-traduits ou
# qui ne devaient pas être traduits
#
def cleanGoogleTrad(data):
  data = data.replace("</ ", "</")
  data = data.replace("<Strong>", "<strong>")
  data = data.replace("</Strong>", "</strong>")
  data = re.sub("<[f,F]+ort[e]{0,1}>", "<strong>", data)
  data = re.sub("</[f,F]+ort[e]{0,1}>", "</strong>", data)
  data = re.sub("[0-9]+D[0-9]+", lambda s: s.group(0).replace("D", "d"), data)
  data = data.replace("</P>", "</p>")
  data = data.replace("[[/ R", "[[/r")
  data = data.replace("accroître", "Intensifié")
  data = data.replace("#feu", "#fire")
  data = data.replace("#acide", "#acid")
  return data


class EmptyDescriptionException(Exception):
  """
  Exception levée si l'item traduit n'a pas de description
  """
  def __init__(self, message="There is no description in this file. Check for missing data."):
    self.message = message