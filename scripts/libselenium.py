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