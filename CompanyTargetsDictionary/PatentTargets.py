from datetime import time
from collections import Counter
import requests
from selenium.webdriver.firefox import webdriver
import Parsers.ParsePatent
from selenium import webdriver
import time
import pandas as pd
import xlrd
import xlwt
from xlwt import Workbook
import xlsxwriter

import testFile


class PatentTargets:

    def __init__(self, company):
        self.company = company

    def targetsforpatents(self, frequency, genes, aliases, pages, claimNumber):
        driver = webdriver.Firefox(
            executable_path=r"C:\Python\Python38\geckodriver.exe")  # make sure this exists somewhere in a local, varies from user to user, and copy the path here

        page = 0
        numberOfPages = pages
        populartargets = []
        patents = []
        firstlist = {}

        while page < numberOfPages:
            main_url = "https://patents.google.com/"
            params = "?assignee=" + self.company + "&country=US&after=priority:20110101&type=PATENT&num=10&sort=new&page=" + str(
                page)
            # params = "?q=(tp53)&num=10&oq=(tp53)"
            res = requests.get(
                "https://patents.google.com/xhr/query?url=assignee%3D" + self.company + "%26country%3DUS%26after%3Dpriority%3A20110101%26type%3DPATENT%26num%3D10%26sort%3Dnew&exp=")
            # res = requests.get("https://patents.google.com/xhr/query?url=q%3D(tp53)%26num%3D10%26oq%3D(tp53)&exp=")

            main_data = res.json()
            data = main_data['results']['cluster']

            for i in range(len(data[0]['result'])):
                num = data[0]['result'][i]['patent']['publication_number']
                driver.get(main_url + "patent/" + num + "/en" + params)
                time.sleep(3)
                print(firstlist)

            page += 1

        driver.close()
        return firstlist

def TopGenesInPatents(targets):

    my_dict = {i:targets.count(i) for i in targets}
    sor = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    sor = list(sor)

    targetList = []
    amountList = []
    total = 0
    for target in sor:
        target = list(target)
        targetList.append(target[0])
        amountList.append(target[1])
        total += target[1]

    df = pd.DataFrame.from_dict({'Column1': targetList, 'Column2': amountList})
    writer = pd.ExcelWriter('Popular2.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Genes', index=False)
    writer.save()

    return sor

def RunningCompanyData(company):
    patents = PatentsFromFile()
    #patents = testFile.manual_patents

    return testmanual(patents, company)

def RunningCompanyFinal(info):
    diseases = diseasesfromfile()

    return TopGenesInPatents(info)

def testmanual(patents, company):
    newPatents = []

    for patent in patents:
        patent = str(patent)
        newPatent = patent.replace('-', '')

        if len(str(newPatent)) == 14:
            newPatent = newPatent[0:6] + "0" + newPatent[6:]
        newPatents.append(newPatent)

    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, company + ":")
    i = 0
    driver = webdriver.Firefox(
        executable_path=r"C:\Python\Python38\geckodriver.exe")

    aliases = newaliasesfromfile()
    genes = genesfromfile()
    firstlist = {}

    while i < len(newPatents):
        driver.get("https://patents.google.com/patent/" + newPatents[i])
        time.sleep(5)

        targets = Parsers.ParsePatent.parse(driver, aliases, genes, 3, 10)
        k = 0

        if len(targets) > 13:
            i = i + 1
            continue

        sheet1.write(i + 1, 0, newPatents[i])

        for target in targets:
            sheet1.write(i + 1, k + 1, target)
            k = k + 1
        wb.save('RocheData2.xls')

        firstlist[newPatents[i]] = targets
        print(i)
        i = i + 1

    driver.close
    return firstlist


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

def PatentsFromFile():
    pepega = pd.read_excel(r"C:\Users\zaids\PycharmProjects\sparx\CompanyTargetsDictionary\Novartis_Patent_Data.xls")
    firstColumn = pepega["search URL:"]
    firstColumn.pop(0)

    return firstColumn

def CompanyGenesFromFile():
    pepega = pd.read_excel(r"C:\Users\zaids\Downloads\NovartisData.xls")
    firstColumn = list(pepega["Unnamed: 1"]) + list(pepega["Unnamed: 2"]) + list(pepega["Unnamed: 3"]) + list(pepega["Unnamed: 4"]) + list(pepega["Unnamed: 5"]) + list(pepega["Unnamed: 6"]) + list(pepega["Unnamed: 7"]) + list(pepega["Unnamed: 8"]) + list(pepega["Unnamed: 9"]) + list(pepega["Unnamed: 10"])

    newlist = [x for x in firstColumn if pd.isnull(x) == False and x != 'nan']

    return newlist