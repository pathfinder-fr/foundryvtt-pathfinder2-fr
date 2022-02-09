#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import re
import requests
import json
import html
import time
import logging
from dataclasses import dataclass

##########################################
# Packs
##########################################
#
# Liste des packs supportés, avec les réglages de traduction
#
#
# transl    Nom du pack traduit en français
# paths     Dictionnaire contenant le chemin des informations principales dans le json anglais
#   name    Nom de la propriété contenant le nom de la donnée
#   desc    Chemin de la propriété contenant la description à traduire
#   type1   Chemin de la donnée à utiliser comme première partie du nom de fichier. Si absent c'est uniquement l'id qui servira à nommer le fichier. Le fichier sera nommé type1-id.htm
#   type2   Chemin de la seconde données. Si type2 est présent, type1 doit l'être aussi. Le fichier sera nommé avec type1-type2-id.htm
# extract   Dictionnaire contenant la liste des champs supplémentaires à extraire dans la section ------- Data et à traduire.
#           La clé correspondra au nom du champ auquel sera ajouté FR et EN
# lists     Dictionnaire contenant la liste des champs supplémentaires à extraire sous forme de liste, dont les différentes valeurs seront extraites avec un "|" comme séparateur, et à traduire.
SUPPORTED = {
    "spells": {
        'transl': "Sorts",
        "paths": {
            'name': "name",
            'desc': "data.description.value",
            'type1': "data.school.value",
            'type2': "data.level.value"
        },
        "extract": {
            'Areasize': "data.areasize.value",
            'Range': "data.range.value",
            'Material': "data.materials.value",
            'Target': "data.target.value",
            'SecondaryCaster': "data.secondarycasters.value",
            'PrimaryCheck': "data.primarycheck.value",
            'SecondaryCheck': "data.secondarycheck.value",
        }
    },
    "feats": {
        'transl': "Dons",
        "paths": {
            'name': "name",
            'desc': "data.description.value",
            'type1': "data.featType.value",
            'type2': "data.level.value"
        },
        "lists": {
            'Prereq': "data.prerequisites.value"
        }
    },
    "equipment": {
        'transl': "Équipement",
        "paths": {
            'name': "name",
            'desc': "data.description.value",
            'type1': "type",
            'type2': "data.level.value"
        }
    },
    "conditionspf2e": {'transl': "Conditions", "paths": {'name': "name", 'desc': "content"}},
    "conditionitems": {'transl': "Conditions", "paths": {'name': "name", 'desc': "data.description.value"}},
    "actions": {'transl': "Actions", "paths": {'name': "name", 'desc': "data.description.value"}},
    "archetypes": {'transl': "Archétypes", "paths": {'name': "name", 'desc': "content"}},
    "pathfinder-bestiary": {'transl': "Bestiaire", "paths": {'name': "name", 'desc': "data.details.publicNotes"}},
    "pathfinder-bestiary-2": {'transl': "Bestiaire 2", "paths": {'name': "name", 'desc': "data.details.publicNotes"}},
    "pathfinder-bestiary-3": {'transl': "Bestiaire 3", "paths": {'name': "name", 'desc': "data.details.publicNotes"}},
    "hazards": {
      'transl': "Dangers",
      "paths": {
        'name': "name", 'desc': "data.details.description"
      },
      "extract": {
        'Disable': "data.details.disable",
        'Reset': "data.details.reset",
        'Routine': "data.details.routine",
        'Target': "data.target.value",
        'ItemsDescription': "items.data.description.value",
      }
    },
    # "age-of-ashes-bestiary":          { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "content" } },
    # "extinction-curse-bestiary":      { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "content" } },
    # "fall-of-plaguestone-bestiary":   { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "content" } },
    # "iconics":                        { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "content" } },
    # "npc-gallery":                    { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "content" } },
    "ancestryfeatures": {
        'transl': "Ascendances (aptitudes)",
        "paths": {
            'name': "name",
            'desc': "data.description.value",
            'type1': "type",
            'type2': "data.level.value"
        }
    },
    "classfeatures": {
        'transl': "Capacités de classe",
        "paths": {
            'name': "name",
            'desc': "data.description.value",
            'type1': "data.traits.value",
            'type2': "data.level.value"
        }
    },
    # "rollable-tables":                { 'transl': "Dangers", "paths": { 'name': "name", 'desc': "content" } },
    "backgrounds": {'transl': "Backgrounds", "paths": {'name': "name", 'desc': "data.description.value"}},
    # "deities":                        { 'transl': "Divinités", "paths": { 'name': "name", 'desc': "content" } },
    "gmg-srd": {'transl': "Guide du MJ", "paths": {'name': "name", 'desc': "content"}},
    "classes": {'transl': "Classes", "paths": {'name': "name", 'desc': "data.description.value"}},
    # "criticaldeck":                   { 'transl': "Critiques", "paths": { 'name': "name", 'desc': "content" } },
    # "pf2e-macros":                    { 'transl': "Macros PF2e", "paths": { 'name': "name", 'desc': "content" } },
    "bestiary-ability-glossary-srd": {
        'transl': "Aptitudes du bestiaire",
        "paths": {'name': "name", 'desc': "data.description.value"}
    },
    "pathfinder-society-boons": {'transl': "Macros PF2e", "paths": {'name': "name", 'desc': "data.description.value"}},
    "boons-and-curses": {'transl': "Bénédictions et malédictions", "paths": {'name': "name", 'desc': "data.description.value"}},
    "familiar-abilities": {'transl': "Aptitudes des familiers", "paths": {'name': "name", 'desc': "data.description.value", 'type1': "data.level.value"}},
    "spell-effects": {'transl': "Effets des sorts", "paths": {'name': "name", 'desc': "data.description.value", 'type1': "data.level.value"}},
    "ancestries": {'transl': "Ascendances", "paths": {'name': "name", 'desc': "data.description.value"}},
    "bestiary-family-ability-glossary": {
        'transl': "Capacités des familles de monstre",
        "paths": {'name': "name", 'desc': "data.description.value"}
    },
    "criticaldeck": {
        'transl': "Cartes critiques",
        "paths": {'name': "name", 'desc': "content"}
    },
    "heritages": {
        'transl': "Héritages",
        "paths": {'name': "name", 'desc': "data.description.value"}
    }
}


class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR


def print_error(message):
    print(bcolors.FAIL + message + bcolors.RESET)


def print_warning(message):
    print(bcolors.WARNING + message + bcolors.RESET)

#
# cette fonction lit le fichier system.json et extrait les informations sur les packs
#


def getPacks():
    response = json.loads(requests.get(
        "https://gitlab.com/hooking/foundry-vtt---pathfinder-2e/-/raw/master/system.json").text)
    packs = []

    for p in response["packs"]:
        match = re.search('packs/([-\w]+)\.db', p['path'])
        if match:
            p['id'] = match.group(1).strip()
        else:
            print("Error parsing ID from %s" % p['path'])
            exit(1)

        if p['id'] in SUPPORTED:
            packs.append({**p, **SUPPORTED[p['id']]})

    return packs

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
            list1 = []
            list2 = []
            try:
                list1 = [e.strip() for e in val1[k] if len(e.strip()) > 0]
            except AttributeError:
                for item in val1[k]:
                    for e in item.values():
                        if len(e.strip()) > 0:
                            list1 += [e.strip()]
            try:
                list2 = [e.strip() for e in val2[k] if len(e.strip()) > 0]
            except AttributeError:
                for item in val2[k]:
                    for e in item.values():
                        if len(e.strip()) > 0:
                            list2 += [e.strip()]
            if list1 != list2:
                return False
        return True
    else:
        return val1.replace('\n', '').replace('\r', '').strip() == val2.replace('\n', '').replace('\r', '').strip()


#
# cette fonction tente une extraction d'une valeur dans un objet
# Ex: data.level.value => obj["data"]["level"]["value"]
#
def getObject(obj, path, exitOnError=True):
    element = obj
    for p in path.split('.'):
        if p in element:
            element = element[p]
        elif exitOnError:
            print_error("Error with path %s in %s" % (path, obj))
            exit(1)
        else:
            # print("Path %s not found for %s!" % (path, obj['name']))
            return None

    return element


def getValue(obj, path, exitOnError=True, defaultValue=None):
    element = getObject(obj, path, exitOnError)
    if element is None:
        return defaultValue
    elif isinstance(element, int):
        return "%02d" % element
    elif isinstance(element, list):
        if len(element) == 0:
            return defaultValue
        if len(element) > 1:
            print_warning(
                "List has more than 1 element for '%s'! %s" % (element, path))
            return element[len(element) - 1]
        return element[0]
    elif element.isdigit():
        return "%02d" % int(element)
    else:
        return element


def getList(obj, path, exitOnError=True):
    element = getObject(obj, path, exitOnError)
    if element is None:
        return []
    elif not isinstance(element, list):
        if exitOnError:
            print_error("Element at '%s' is not a list! %s" % (path, element))
            exit(1)
        return []
    else:
        return element


#
# Cette fonction extrait l'information d'un fichier .htm sous forme d'un tableau contenant les différens attributs
# au format nom: Valeur
#
# Liste des valeurs renvoyées :
#
# id            identifiant unique complet (ex: skill-15-Vk7BzAb3D9r226sI), obtenu à partir du nom de fichier sans le .htm
# nameEN        nom anglais (Name)
# nameFR        nom français (Nom)
# status        état de la traduction (État)
# oldstatus     état d'origine de la traudction (État d'origine)
# benefitsEN    avantage (du don?) en anglais (Benefits)
# benefitsFR    avantage (du don?) en français (Avantage)
# spoilersEN    Balise SpoilersEN
# spoilersFR    Balise SpoilersFR
#
# descrFR/EN    Description en français/anglais
# dataEN/FR     Tableau des différentes données stockées dans la partie ------ Data
# listsEN/FR    Tableau des différentes listes
#               Ces lis
def fileToData(filepath):
    data = {}
    if os.path.isfile(filepath):

        # read all lines in f
        with open(filepath, 'r', encoding='utf8') as f:
            content = f.readlines()

        descrEN = ""
        descrFR = ""
        summEN = ""
        summFR = ""
        spoilers = ""
        isDescEN = False
        isDescFR = False
        isData = False
        listsEN = {}
        listsFR = {}
        dataEN = {}
        dataFR = {}

        match = re.search('(\w{16})\.htm', filepath)
        if not match:
            print_error("Invalid filename %s" % filepath)
            exit(1)

        data['id'] = match.group(1)
        data['misc'] = {}

        for line in content:
            if line.startswith("Name:"):
                data['nameEN'] = line[5:].strip()
            elif line.startswith("Nom:"):
                data['nameFR'] = line[4:].strip()
            elif line.startswith("État:"):
                data['status'] = line[5:].strip()
            elif line.startswith("État d'origine:"):
                data['oldstatus'] = line[15:].strip()

            # Champs gérés en dur
            # Nécessaire qd le champ : n'est pas dans Data, se termine par EN ou FR et n'est pas une liste
            elif line.startswith("Benefits:"):
                data['benefitsEN'] = line[9:].strip()
            elif line.startswith("Avantage:"):
                data['benefitsFR'] = line[9:].strip()
            elif line.startswith("SpoilersEN:"):
                data['spoilersEN'] = line[11:].strip()
            elif line.startswith("SpoilersFR:"):
                data['spoilersFR'] = line[11:].strip()

            elif line.startswith("------ Benefits") or line.startswith("------ Spoilers"):
                isData = False
                continue
            elif line.startswith("------ Data"):
                isData = True
            elif line.startswith("------ Description (en) ------"):
                isData = False
                isDescEN = True
                isDescFR = False
                continue
            elif line.startswith("------ Description (fr) ------"):
                isData = False
                isDescFR = True
                isDescEN = False
                continue
            elif not isDescEN and not isDescFR and len(line.strip()) > 0:
                # tente de lire toutes les propriétés restantes comme des traduction FR/EN

                # on commence par rechercher le ':' en fin du mot
                sep = line.find(":")
                if sep < 0:
                    print(bcolors.FAIL + "Invalid data '%s' in file %s " %
                          (line, filepath) + bcolors.RESET)
                    exit(1)
                key = line[0:sep]
                value = line[sep+1:].strip()
                # on prend tous les attributs qui finissent par FR ou EN
                if key.endswith("EN") or key.endswith("FR"):
                    key = key[0:-2]
                    lang = line[sep-2:sep]
                    if isData:
                        # si la donnée se trouve dans la section "------- Data"
                        # on l'ajoute au dictionnaire des données
                        # dataEN ou dataFR
                        if lang == "EN":
                            dataEN[key] = value.replace("\\n","\n")
                        elif lang == "FR":
                            dataFR[key] = value.replace("\\n","\n")
                    else:
                        # sinon, on considère que c'est une liste et on ajoute les éléments de cette liste dans le dictionnaire de données
                        # listsEN ou listsFR
                        liste = [e.strip() for e in value.split('|')]
                        liste = [e.strip()
                                 for e in liste if len(e.strip()) > 0]
                        if lang == "EN":
                            listsEN[key] = liste
                        elif lang == "FR":
                            listsFR[key] = liste
                else:
                    # on stocke toutes les clés inconnues qui ne finissent pas par EN ou FR dans une propriété 'misc' du résultat
                    data['misc'][key] = value

            if isDescEN:
                descrEN += line
            elif isDescFR:
                descrFR += line

        data['descrEN'] = descrEN.strip()
        data['descrFR'] = descrFR.strip()
        data['listsEN'] = listsEN
        data['listsFR'] = listsFR
        data['dataEN'] = dataEN
        data['dataFR'] = dataFR

    else:
        print("Invalid path: %s" % filepath)
        exit(1)

    if not 'nameEN' in data or not 'descrEN' in data:
        print_error("Invalid data: %s" % filepath)
        exit(1)

    return data


#
# cette fonction écrit les datas avec le benefits en plus
#
def dataToFile(data, filepath):
    with open(filepath, 'w', encoding='utf8') as df:
        df.write('Name: ' + data['nameEN'] + '\n')
        df.write('Nom: ' + data['nameFR'] + '\n')

        if data['listsEN']:
            for key in data['listsEN']:
                try:
                    df.write("%sEN: %s\n" %
                             (key, "|".join(data['listsEN'][key])))
                except TypeError:
                    values = ""
                    for item in data['listsEN'][key]:
                        for e in item.values():
                            values += "|" + e
                    df.write("%sEN: %s\n" % (key, values))
                try:
                    df.write("%sFR: %s\n" % (key, "|".join(
                        data['listsFR'][key]) if key in data['listsFR'] else ""))
                except TypeError:
                    values = ""
                    for item in data['listsFR'][key]:
                        for e in item.values():
                            values += "|" + e
                    df.write("%sFR: %s\n" % (key, values))

        df.write('État: ' + data['status'] + '\n')
        if 'oldstatus' in data:
            df.write('État d\'origine: ' + data['oldstatus'] + '\n')
        df.write('\n')
        if 'benefitsEN' in data or 'benefitsFR' in data:
            df.write('------ Benefits ----' + '\n')
            if 'benefitsEN' in data:
                df.write("Benefits: %s\n" % data['benefitsEN'])
            if 'benefitsFR' in data:
                df.write("Avantage: %s\n" % data['benefitsFR'])
        if 'spoilersEN' in data or 'spoilersFR' in data:
            df.write('------ Spoilers ----' + '\n')
            if 'spoilersEN' in data:
                df.write("SpoilersEN: %s\n" % data['spoilersEN'])
            if 'spoilersFR' in data:
                df.write("SpoilersFR: %s\n" % data['spoilersFR'])

        if data['dataEN']:
            df.write('------ Data ------' + '\n')
            for key in data['dataEN']:
                if data['dataEN'][key] and len(data['dataEN'][key]) > 0:
                    df.write("%sEN: %s\n" % (key, data['dataEN'][key].replace("\n","\\n")))
                    if 'dataFR' in data and key in data['dataFR'] and data['dataFR'][key] and len(data['dataFR'][key]) > 0:
                        df.write("%sFR: %s\n" % (
                            key, data['dataFR'][key].replace("\n","\\n") if key in data['dataFR'] else ""))
                    else:
                        df.write("%sFR: \n" % key)

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
    has_errors = False

    # read all files in folder
    for fpath in all_files:

        if fpath[0] != ".":
            data = fileToData(path + fpath)
            data['filename'] = fpath

            if data['id'] in resultById:
                print_error("Duplicate data %s and %s, please fix it manually!" % (
                    path + resultById[data['id']]['filename'], path + data['filename']))
                has_errors = True
            else:
                resultById[data['id']] = data
                resultByName[data['nameEN']] = data

    return [resultById, resultByName, has_errors]

#
# Vérifie si la chaîne text est vide, et renvoie None si c'est le cas
#


def emptyAsNull(value, empty=None):
    if value is None:
        return None
    if empty is not None and value == empty:
        return None
    if isinstance(value, str) and len(value) == 0:
        return None
    if isinstance(value, list) and len(value) == 0:
        return None
    return value

#
# Tente de convertir la valeur donnée sous forme d'entier
# Si la conversion est impossible, renvoie la valeur telle quelle sans la modifier
#


def tryIntOrNone(value):
    # si la valeur vaut None on renvoie None
    if value is None:
        return None

    # si la valeur est une chaine correspondant à un nombre signe - au début puis des chiffres
    # on la transfore en int
    if isinstance(value, str) and re.match('^-?\d+$', value):
        return int(value)

    # sinon on ne fait rien
    return value

#
# tente de charger un élément du dictionnaire imbriqué correspondant aux différentes propriétés données.
# renvoie None dès qu'une clé n'est pas présente dans le dictionnaire.
#
# alternative aux indexeurs [''] pour ne pas planter
#
# ex: tryGetDict(dict, 'data', 'name', 'value')
#     équivaut à dict['data']['name']['value'] en renvoyant None si le dictionnaire ne contient pas l'une des clés
#


def tryGetDict(dict: dict, *args: str):
    i = 0
    node = dict
    while i < len(args) and node is not None and args[i] in node:
        node = node[args[i]]
        i = i + 1
    if i != len(args):
        return None
    return node

#
# ajoute un élément key de valeur value au dictionaire dict uniquement si la valeur ne vaut pas None
#


def addIfNotNull(dict: dict, key: str, value: any):
    if value is None:
        return
    dict[key] = value
