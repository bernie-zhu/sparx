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


class PatentTargets:

    def __init__(self, company):
        self.company = company

    def targetsforpatents(self, frequency, aliases, pages):
        driver = webdriver.Firefox(
            executable_path=r"C:\Python\Python38\geckodriver.exe")  # make sure this exists somewhere in a local, varies from user to user, and copy the path here

        page = 0
        numberOfPages = pages
        populartargets = []

        while page < numberOfPages:
            main_url = "https://patents.google.com/"
            params = "?assignee=" + self.company + "&after=priority:20110609&type=PATENT&num=10&sort=new&page=" + str(
                page)

            res = requests.get(
                "https://patents.google.com/xhr/query?url=assignee%3D" + self.company + "%26after%3Dpriority"
                                                                                        "%3A20110609%26type"
                                                                                        "%3DPATENT%26num%3D1"
                                                                                        "&exp=")
            main_data = res.json()
            data = main_data['results']['cluster']

            for i in range(len(data[0]['result'])):
                num = data[0]['result'][i]['patent']['publication_number']
                driver.get(main_url + "patent/" + num + "/en" + params)
                time.sleep(5)
                populartargets.append(Parsers.ParsePatent.parse(driver, aliases, frequency))

            page += 1

        driver.close()
        flattentargets = [val for sublist in populartargets for val in sublist]
        targetdict = dict(Counter(flattentargets))
        return targetdict


def targetintodict():
    targetfrequency = int(input("Enter Target Limit: "))
    pages = int(input("How many pages of patents do you want to search through: "))
    allCompanies = companyNames.companies
    del companyNames.companies
    del companyNames.names
    gc.collect
    #diseases, aliases = TargetInformation.targetinformation()
    aliases = TargetInformation.aliaslists

    for company, links in allCompanies.items():
        targets = PatentTargets(company)
        allCompanies[company] = targets.targetsforpatents(targetfrequency, aliases, pages)

    return allCompanies
