import time

import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import time
import pandas as pd
import xlrd

from selenium.webdriver.firefox import webdriver
from datetime import time
from collections import Counter
import requests
from selenium.webdriver.firefox import webdriver
import Parsers.ParsePatent
import TargetInformation
from CompanyTargetsDictionary import companyNames
import gc
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import time
import xlrd
import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import time
import pandas as pd
import xlrd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def newParser():
    driver = webdriver.Firefox(executable_path=r"C:\Python\Python38\geckodriver.exe")
    driver.get("https://patents.google.com/patent/WO2016141185A1/en")
    time.sleep(5)

    titleStr = driver.title.split(" - ")[1].strip()

   # print(titleStr)
    print()
    print("__")

    abstractStr = driver.find_element_by_id("abstract").text

    if not abstractStr:
        abstractStr = driver.find_element_by_tag_name("patent-text").text

    #print(abstractStr)

    print()
    print("__")

    claims = driver.find_elements_by_class_name("claims")

    dog = ""

    for x in claims:
        dog = dog + x.text + "\n"

    #print(dog)

    print()
    print("__")

    '''
    concepts = driver.find_elements_by_class_name("tbody")

    if not concepts:
        print("WTGFFF")

    concepts = concepts[len(concepts)-1].text.split("Show all concepts from the description section")[0]
    print(concepts)

    print()
    print("__")

    '''

    #dog = driver.find_element_by_tag_name("dropdown-menu")

    #dog.click()

    #html = driver.find_element_by_tag_name('html')
   # html.send_keys(Keys.END)

    #doge = dog.find_elements_by_tag_name("div")

   # for uwu in doge:
        #if uwu.text == "Human genes" or uwu.text == "Proteins" and not uwu.is_selected():
            # print("HUMAN GENES SELECT")
            #uwu.click()
    #for uwu in doge:
       # if uwu.is_selected() and not "Human genes" in uwu.text:
            # print(uwu.text + "WAS SELECTED< WILL DESELECT NOW")
           # uwu.click()

   # concepts2 = []
    #concepts3 = driver.find_elements_by_tag_name("concept-mention")
    #for dog in concepts3:
        #concepts2.append(dog.text)

    #while ("" in concepts2):
        #concepts2.remove("")

    #concepts2.pop(0)

    #seen = set()
    #result = []
    #for item in concepts2:  # remove recurring values
       # if item not in seen:
            #seen.add(item)
           # result.append(item)
    #concepts2 = result
    #print(concepts2)

    #print()
    #print("__")


    t0 = time.time()

    pepega = pd.read_excel(r"C:\Users\zaids\PycharmProjects\sparx\CompanyTargetsDictionary\Gene_Aliases_All.xls")
    # print(pepega["Unnamed: 0"].values[0])
    # print(pepega.values[0])
    poogers = []
    for dog in range(len(pepega.values)):
        peepo = []
        for cow in range(len(pepega.values[dog]) - 1):
            if pd.isnull(pepega.values[dog][cow]):
                break
            if len(str(pepega.values[dog][cow])) <= 2:
                continue
            peepo.append(pepega.values[dog][cow])
        poogers.append(peepo)

    t1 = time.time()
    total = t1 - t0

    #print(total)

    t0 = time.time()

    testlist = "The present invention relates to combination therapies employing anti-CD20/anti-CD3 bispecific antibodies and 4-1BB (CD137) agonists, in particular 4-1BBL trimer containing antigen binding molecules, the use of these combination therapies for the treatment of cancer and methods of using the combination therapies."
    #testlist = testlist.split()
    #print(testlist)

    titleStr = " " + titleStr + " "

    for dardog in poogers:
        for alias in dardog:
            alias = str(alias).lower()
            if " " + str(alias) + " " in titleStr:
                print(alias)
                print(dardog[0])
            elif  " " + str(alias) + "." in titleStr:
                print(dardog[0])
            elif  " " + str(alias) + "," in titleStr:
                print(dardog[0])
            elif  " " + str(alias) + "'" in titleStr:
                print(dardog[0])
            elif  " " + str(alias) + "/" in titleStr:
                print(dardog[0])
            elif  "/" + str(alias) + " " in titleStr:
                print(dardog[0])

    t1 = time.time()
    total = t1 - t0

    #print(total)
    driver.close()