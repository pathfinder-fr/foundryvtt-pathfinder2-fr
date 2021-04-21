#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
import logging
import os
import json
from bs4 import BeautifulSoup
from libdata import readFolder, translator_driver, full_trad, dataToFile
from dataclasses import dataclass
logging.basicConfig(filename='translation.log', level=logging.INFO)

@dataclass
class Feat:
    name: str
    benefits: str
    spoiler: str


PATH = "../data/feats/"


def get_data():
    with open("feats-benefits-links-list.json", "r") as feats_json:
        feats_json = json.load(feats_json)
        for el in feats_json:
            print("Requesting %s" % feats_json[el])
            req = requests.get(feats_json[el])
            if req.status_code == 200:
                html_doc = req.content

            soup = BeautifulSoup(html_doc, 'html.parser')

            with open("feats.html", "a") as file:
                file.write(soup.prettify())
                file.write("\n")



def get_stripped_text(full_text):
    full_text = full_text.get_text().strip().replace("\n", "")
    return re.sub("[\s]{2,}", " ", full_text)



def trad_benefits(benefitsEN):
    translation_attempt = full_trad(driver, benefitsEN)
    return translation_attempt.data


def add_benefits_and_spoil(data, feat):
    try:
        if len(data['benefitsFR'])<=1:
            raise Exception
    except Exception:
        logging.info("Translating %s - %s" % (data['filename'], data['nameEN']))
        benefitsFR = trad_benefits(feat.benefits)
        data["benefitsFR"] = benefitsFR
    data["benefitsEN"] = feat.benefits
    data['spoilers'] = feat.spoiler
    dataToFile(data, PATH + data['filename'])


try:
    if os.stat("feats.html").st_size <= 10:
        get_data()
except FileNotFoundError:
    get_data()

with open("feats.html", "r") as html_doc:
    soup = BeautifulSoup(html_doc, 'html.parser')
    names = soup.select("td:nth-child(1) u > a")
    summaries = soup.select("td:nth-child(5)")
    spoilers = soup.select("td:nth-child(6)")
    values = []
    for name, benefits, spoiler in zip(names, summaries, spoilers):
        values += [Feat(get_stripped_text(name), get_stripped_text(benefits), get_stripped_text(spoiler))]


data = readFolder(PATH)[1]
exceptions = {"Virtuosic": [], "Specialty": [],
              "Impeccable": [], "Terrain": [],
              "Counterspell": [], "Soulsight": []}
for f in data:
    if f.__contains__("Virtuosic"):
        exceptions["Virtuosic"] += [f]
    elif f.__contains__("Specialty"):
        exceptions["Specialty"] += [f]
    elif f.__contains__("Impeccable"):
        exceptions["Impeccable"] += [f]
    elif f.__contains__("Terrain Expertise"):
        exceptions["Terrain"] += [f]
    elif f.__contains__("Counterspell"):
        exceptions["Counterspell"] += [f]
    elif f.__contains__("Soulsight"):
        exceptions["Soulsight"] += [f]

driver = translator_driver()
weirdquotes = []
for feat in values:
    name = feat.name.title()\
        .replace(" Of The ", " of the ")\
        .replace("'S", "'s")\
        .replace("'T", "'t")\
        .replace("'Re", "'re")\
        .replace("Side By Side", "Side by Side")
    #Et c'est parti pour l'horreur...
    if name == "Quick Climber":
        name = "Quick Climb"
    elif name == "Glad-hand":
        name = "Glad-Hand"
    elif name == "Numb To Death":
        name = "Numb to Death"
    elif name == "Scare To Death":
        name = "Scare to Death"
    elif name == "Avenge In Glory":
        name = "Avenge in Glory"
    elif name == "Kneel For No God":
        name = "Kneel for No God"
    elif name == "Roll With It":
        name = "Roll with It"
    elif name == "Unbreakable-Er Goblin":
        name = "Unbreakable-er Goblin"
    elif name == "Eyes of the Night":
        name = "Eyes Of Night"
    elif name == "To The Ends of the Earth":
        name = "To the Ends of the Earth"
    elif name == "Tongue of the Sun And Moon":
        name = "Tongue of Sun and Moon"
    elif name == "Tide-Hardened":
        name = "Tide-hardened"
    elif name == "Follow-Up Assault":
        name = "Follow-up Assault"
    elif name == "Hydraulic Maneuvers":
        name = "Hydraulic Amneuvers"
    elif name == "Saberteeth":
        name = "Saber Teeth"
    elif name == "Speak With Kindred":
        name = "Speak with Kindred"
    elif name == "Revivification Protocal":
        name = "Revivification Protocol"
    elif name == "Derring-Do":
        name = "Derring-do"
    elif name == "Precise Debilitation":
        name = "Precise Debilitations"
    elif name == "Bloody Debilitations":
        name = "Bloody Debilitation"
    elif name == "Critical Debilitations":
        name = "Critical Debilitation"
    elif name == "Deepvision":
        name = "Deep Vision"
    elif name == "Captivating Curosity":
        name = "Captivating Curiosity"
    elif name == "Know-It-All":
        name = "Know-It-All (Bard)"
    elif name == "Heatwave":
        name = "Heat Wave"
    elif name == "Shake It Off":
        name = "Shake it Off"
    elif name == "Stella's Stab And Snag":
        name = "Stella's Stab and Snag"
    elif name == "Incredible Luck":
        name = "Incredible Luck (Halfling)"
    elif name == "Tusks":
        name = "Tusks (Orc)"
    elif name == "Symphony of the Muses":
        name = "Symphony of the Muse"
    elif name == "Twist The Knife":
        name = "Twist the Knife"
    elif name == "Metal-Veined Strikes":
        name = "Metal-veined Strikes"
    elif name == "Rkoan Arts":
        name = "Rokoan Arts"
    elif name == "Ru-Shi":
        name = "Ru-shi"
    elif name == "Suli-Jann":
        name = "Suli-jann"
    elif name == "Leave An Opening":
        name = "Leave an Opening"
    elif name == "Spring From The Shadows":
        name = "Spring from the Shadows"
    elif name == "Finishing Follow-Through":
        name = "Finishing Follow-through"
    try:
        if name.__contains__("Specialty"):
            for p in exceptions["Specialty"]:
                add_benefits_and_spoil(data[p], feat)
        elif name.__contains__("Virtuosic"):
            for p in exceptions["Virtuosic"]:
                add_benefits_and_spoil(data[p], feat)
        elif name.__contains__("Impeccable"):
            for p in exceptions["Impeccable"]:
                add_benefits_and_spoil(data[p], feat)
        elif name.__contains__("Terrain Expertise"):
            for p in exceptions["Terrain"]:
                add_benefits_and_spoil(data[p], feat)
        elif name.__contains__("Counterspell"):
            for p in exceptions["Counterspell"]:
                add_benefits_and_spoil(data[p], feat)
        elif name.__contains__("Soulsight"):
            for p in exceptions["Soulsight"]:
                add_benefits_and_spoil(data[p], feat)
        else:
            add_benefits_and_spoil(data[name], feat)
    except KeyError as e: 
        if name.__contains__("'"): 
            name = name.replace("'", "’")
            try:
                add_benefits_and_spoil(data[name], feat)
                continue
            except:
                logging.error("Error : erreur pour les avantages de la feat %s" % name)
                print("Not weirdquote %s" % name)
        if name.__contains__("of the"):
            name = name.replace("of the", "Of The")
            try:
                add_benefits_and_spoil(data[name], feat)
            except:
                logging.error("Error : erreur pour les avantages de la feat %s" % name)
                print("Not 'of the' %s" % name)
        elif name.__contains__("Of"):
            name = name.replace("Of", "of")
            try:
                add_benefits_and_spoil(data[name], feat)
            except:
                logging.error("Error : erreur pour les avantages de la feat %s" % name)
                print("Not 'Of' %s" % name)
        elif name.__contains__("And"):
            name = name.replace("And", "and")
            try:
                add_benefits_and_spoil(data[name], feat)
            except:
                logging.error("Error : erreur pour les avantages de la feat %s" % name)
                print("Not 'And' %s" % name)
        elif name.__contains__("In"):
            name = name.replace("In", "in")
            try:
                add_benefits_and_spoil(data[name], feat)
            except:
                logging.error("Error : erreur pour les avantages de la feat %s" % name)
                print("Not 'And' %s" % name)
        else:
            logging.error("Error : erreur pour les avantages de la feat %s" % name)
            print(name)
        continue

driver.quit()