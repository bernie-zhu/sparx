#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from bs4 import BeautifulSoup
import time


def checkgeneexists(cookiezi):
    
    driver = webdriver.Firefox(executable_path=r'C:\Users\Kevin\geckodriver-v0.29.1-win64\geckodriver.exe')
                                 #if not working (not in env variables), paste in executable path to geckodriver.exe file
                                 #executable_path=r'C:\Users\Kevin\geckodriver-v0.29.1-win64\geckodriver.exe'
        
    replace = "https://www.genecards.org/cgi-bin/carddisp.pl?gene=" + cookiezi
    driver.get(replace)
    time.sleep(2)
    
    dog = driver.find_elements_by_id("aliases_descriptions")
    
    cat = 0
    vaxei = "Target found"

    if not dog:
        driver.get("https://www.genecards.org/Search/Keyword?queryString=" + cookiezi)
        time.sleep(5)
        check = driver.find_elements_by_class_name("gc-gene-symbol")
        if check:
            replace = "https://www.genecards.org/cgi-bin/carddisp.pl?gene=" + driver.find_element_by_class_name("gc-gene-symbol").text
            vaxei = driver.find_element_by_class_name("gc-gene-symbol").text
            driver.get(replace)
            cat = 1
        else:
            vaxei = "Target does not exist, nor does it have related targets! Try again"
            cat = 2

    
    return replace, driver, cat, vaxei


########################################################################################


def genecards(osugame): #osugame input will be a gene name
    #Test links:
    
    #driver = webdriver.Firefox(executable_path=r'C:\Users\Kevin\geckodriver-v0.29.1-win64\geckodriver.exe')
        
    source =  "https://www.genecards.org/cgi-bin/carddisp.pl?gene=" + osugame   

    source, driver, alternatesearch, newtarget = checkgeneexists(osugame)
    n = 0
    
    if alternatesearch != 2:
        table = driver.find_element_by_id("aliases_descriptions")
        aliasnames = table.find_elements_by_tag_name("li")
        title = driver.find_element_by_tag_name("strong").text

        ensembl = ""
        mrekk = []
        check = 0
        
        
        for cat in aliasnames:
            cow = 0
            numbers = ""
            sups = cat.find_elements_by_tag_name("sup")
            if not sups:
                sups = cat.find_elements_by_class_name("gc-ga-link")
                cow = 1
            #print(cow)
            
        
            if cow == 0:
                for fish in sups:
                    numbers = numbers + " " + fish.text
            elif cow == 1:
                if ":" not in cat.text:
                    for fish in sups:
                        numbers = numbers + ", " + fish.text
                numbers = numbers[2:]
                numbers = " (" + numbers + ")"
            #print(cat.text)
            #print(numbers)
            if numbers!= "" and numbers!=" ()":
                #print(cat.text.split(numbers)[0])
                mrekk.append(cat.text.split(numbers)[0])


            if "Ensembl" in cat.text: 
                ensembl = cat.text
                check = 1
            elif check == 0:
                ensembl = "ENSEMBL NOT FOUND"

        #print()
        ensembl = ensembl.split()[1]

        #driver.close()

        return ensembl,mrekk,title, driver, source, alternatesearch, newtarget
    
    else:
        
        return "","","", driver, "", alternatesearch, newtarget
    

############################################################################################

 
def getopentargets(genename): #genename will be a gene name

    ensemblname, aliases,name, nd, genecardslink, searchno, target2 = genecards(genename)
    link = ""
    woof = 0
    if searchno !=2:
        conditions = []
        if ensemblname == "NOT":
            nd.get("https://platform.opentargets.org/search?q=" + name + "&page=1")
            time.sleep(2)
            link = nd.find_element_by_class_name("jss28").get_attribute("href")
            woof = 1
        #print(link)
        
        driver = nd #webdriver.Firefox() #executable_path=r'C:\Users\Kevin\geckodriver-v0.29.1-win64\geckodriver.exe' #make sure this exists somewhere in a local, varies from user to user, and copy the path here
        
        if woof == 0:
            opentargetslink = "https://platform.opentargets.org/target/" + ensemblname + "/associations"
        else:
            opentargetslink = link
        
        driver.get(opentargetslink)
        time.sleep(5)

        results = driver.find_elements_by_class_name("MuiTableRow-root")
        results.pop(0)

        for result in results:
            product_name = result.find_element_by_tag_name('span')
            #print("                        " + product_name.text)
            conditions.append(product_name.text)

        search = ""
        if searchno == 1:
            search = "Original target not found, closest target found: " + target2
        elif searchno == 0:
            search = target2
        
        
        if len(conditions)>10:
            conditions = conditions[:10]
        
        
        driver.close()

        return conditions, aliases, name, genecardslink, opentargetslink, search
    else:
        
        nd.close()
        return "DNE", "DNE", "DNE", "DNE", "DNE", target2


# In[ ]:


#getopentargets test

diseaseconditions, names, genename, link1, link2, closestpossibletarget = getopentargets("hoxa4") #change input string to a gene name
print(closestpossibletarget)
    
print(genename + " is also known as:")
for rafis in names:
    print("                        " + rafis)
print()
print("Source: "  + link1)
print()    

print(genename + " top associated diseases/conditions/states:")
for result in diseaseconditions:
    print("                        " + result)
print()
print("Source: " + link2)


# In[ ]:


#genecards test

ensembl,names,genename, driver, link1, alternatesearch, closestpossibletarget = genecards("grep1") #change input string to a gene name
print(closestpossibletarget)
    
print(genename + " is also known as:")
for rafis in names:
    print("                        " + rafis)
print()
print("Source: "  + link1)


print(ensembl)


driver.close()


# In[ ]:




