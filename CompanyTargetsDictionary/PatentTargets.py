from datetime import time
from collections import Counter
import requests
from selenium.webdriver.firefox import webdriver
import Parsers.ParsePatent
import TargetInformation
import testFile
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


class PatentTargets:

    def __init__(self, company):
        self.company = company

    def targetsforpatents(self, frequency, genes, aliases, pages, diseases, claimNumber):
        driver = webdriver.Firefox(
            executable_path=r"C:\Python\Python38\geckodriver.exe")  # make sure this exists somewhere in a local, varies from user to user, and copy the path here

        page = 0
        numberOfPages = pages
        populartargets = []

        while page < numberOfPages:
            main_url = "https://patents.google.com/"
            params = "?assignee=" + self.company + "&after=priority:20110609&type=PATENT&num=10&sort=new&page=" + str(
                page)
            # params = "?q=(tp53)&num=10&oq=(tp53)"

            res = requests.get(
                "https://patents.google.com/xhr/query?url=assignee%3D" + self.company + "%26after%3Dpriority"
                                                                                        "%3A20110609%26type"
                                                                                        "%3DPATENT%26num%3D1"
                                                                                        "&exp=")
            # res = requests.get("https://patents.google.com/xhr/query?url=q%3D(tp53)%26num%3D10%26oq%3D(tp53)&exp=")

            main_data = res.json()
            data = main_data['results']['cluster']

            for i in range(len(data[0]['result'])):
                num = data[0]['result'][i]['patent']['publication_number']
                driver.get(main_url + "patent/" + num + "/en" + params)
                time.sleep(3)
                populartargets.append(Parsers.ParsePatent.parse(driver, aliases, genes, frequency, claimNumber))
                print(num + ":" + populartargets)

            page += 1

        driver.close()

        flattentargets = [val for sublist in populartargets for val in sublist]
        targetdict = dict(Counter(flattentargets))
        sor = sorted(targetdict.items(), key=lambda x: x[1], reverse=True)
        sor = list(sor[:3])
        finishedList = []

        returnList = []
        for target in sor:
            target = list(target)
            for disease in diseases:
                if target[0] == disease[0]:
                    returnList.append(target[0])
                    returnList.append(disease[1:])
                    break

        return sor


def targetintodict():
    targetfrequency = int(input("Enter Target Limit: "))
    pages = int(input("How many pages of patents do you want to search through: "))
    claim = int(input("How many claims do you want to search through:"))

    allCompanies = companyNames.companies
    aliases = newaliasesfromfile()
    genes = genesfromfile()
    diseases = diseasesfromfile()

    for company, links in allCompanies.items():
        targets = PatentTargets(company)
        allCompanies[company] = targets.targetsforpatents(targetfrequency, genes, aliases, pages, diseases, claim)

    return allCompanies


def testparser():
    targets = []
    driver = webdriver.Firefox(
        executable_path=r"C:\Python\Python38\geckodriver.exe")  # make sure this exists somewhere in a local, varies from user to user, and copy the path here
    driver.get("https://patents.google.com/patent/US2018222985A1")
    time.sleep(3)
    aliases = newaliasesfromfile()
    genes = genesfromfile()
    diseases = diseasesfromfile()
    targets.append(Parsers.ParsePatent.parse(driver, aliases, genes, 2))
    driver.close
    flattentargets = [val for sublist in targets for val in sublist]
    targetdict = dict(Counter(flattentargets))
    sor = sorted(targetdict.items(), key=lambda x: x[1], reverse=True)
    sor = sor[:3]
    return sor

def testmanual():
    i = 0
    driver = webdriver.Firefox(
        executable_path=r"C:\Python\Python38\geckodriver.exe")  # make sure this exists somewhere in a local, varies from user to user, and copy the path here

    while i < len(testFile.manual_patents):
        targets = []
        patentsubstring = testFile.manual_patents[i][0:6]
        patentendstring = testFile.manual_patents[i][6:]

        if (len(testFile.manual_patents[i]) < 14):
            driver.get("https://patents.google.com/patent/" + testFile.manual_patents[i])
        else:
            driver.get("https://patents.google.com/patent/" + patentsubstring + "0" + patentendstring)

        time.sleep(3)

        aliases = newaliasesfromfile()
        genes = genesfromfile()
        diseases = diseasesfromfile()

        targets.append(Parsers.ParsePatent.parse(driver, aliases, genes, 2, 10))
        flattentargets = [val for sublist in targets for val in sublist]
        targetdict = dict(Counter(flattentargets))
        sor = sorted(targetdict.items(), key=lambda x: x[1], reverse=True)
        sor = sor[:3]
        print(str(testFile.manual_patents[i]) + " - " + str(sor))
        i = i + 1

    driver.close
    return sor


def aliasesfromfile():
    wb = xlrd.open_workbook(
        r"C:\Users\zaids\PycharmProjects\sparx\CompanyTargetsDictionary\Gene_Aliases_All.xls")  # read all genes from excel sheet
    ws = wb.sheet_by_index(0)
    x = len(ws.col_values(0))

    genelist = ws.col_values(0)
    genelist.pop(0)  # genelist = list of all target names
    aliases = []
    for dog in range(x):
        x = ws.row_values(dog)
        x[:] = [y for y in x if y]
        x = x[1:]
        x = str(x)
        aliases.append(x)
    return aliases


def newaliasesfromfile():
    pepega = pd.read_excel(r"C:\Users\zaids\PycharmProjects\sparx\CompanyTargetsDictionary\Gene_Aliases_All.xls")
    # print(pepega["Unnamed: 0"].values[0])
    # print(pepega.values[0])
    poogers = []
    for dog in range(len(pepega.values)):
        peepo = []
        for cow in range(len(pepega.values[dog]) - 1):
            if pd.isnull(pepega.values[dog][cow]):
                break
            peepo.append(pepega.values[dog][cow])
        poogers.append(peepo)
    return poogers


def genesfromfile():
    pepega = pd.read_excel(r"C:\Users\zaids\PycharmProjects\sparx\CompanyTargetsDictionary\Gene_Aliases_All.xls")
    return pepega["Unnamed: 0"]


def diseasesfromfile():
    pepega = pd.read_excel(r"C:\Users\zaids\PycharmProjects\sparx\CompanyTargetsDictionary\Gene_Conditions_All.xls")
    # print(pepega["Unnamed: 0"].values[0])
    # print(pepega.values[0])
    poogers = []
    for dog in range(len(pepega.values)):
        peepo = []
        for cow in range(len(pepega.values[dog]) - 1):
            if pd.isnull(pepega.values[dog][cow]):
                break
            peepo.append(pepega.values[dog][cow])
        poogers.append(peepo)
    return poogers


def diseasesFromTarget(foundTarget, diseases):

    for target in diseases:
        if target[0] == foundTarget:
            return target[1:]
