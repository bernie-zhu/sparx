from selenium.webdriver.firefox import webdriver

import OpenTargetsAliases
import gettinggenelist
import testFile
from OpenTargetsAliases import OpenTargetAndAliases
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import time

import TargetInformation

diseases = []
aliases = []


def targetinformation():
    print(len(testFile.g))
    count = 0
    for f in testFile.genes:
        if count == 249:
            print(f)
        count += 1

def targetinfonew():
    doggie = testFile.t
    tar = OpenTargetsAliases.OpenTargetAndAliases()
    driver = webdriver.Firefox()
    rajeevram = []  # list for diseases/conditions
    joesalisbury = []  # list for aliases
    cat = 0

    while len(doggie) != 0:
        conditions, aliases, name, genecardslink, opentargetslink, search, driver = tar.getopentargets(doggie[0], driver)
        cat = cat + 1
        rajeevram.append(conditions)
        joesalisbury.append(aliases)
        if cat % 250  == 0:
            print("Conditions:")
            print(rajeevram)
            print("\n" + "\n")
            print("Aliases:")
            print(joesalisbury)
        print(cat)
        doggie.pop(0)

    driver.close()

    print()
    print("ALiases")
    print(joesalisbury)

    print()
    print("Conditions")
    print(rajeevram)

