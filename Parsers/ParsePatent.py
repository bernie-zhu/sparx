from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import time


def parse(driver, l, target_frequency):
    results = []
    count = [0] * len(l)

    # TITLE
    titleStr = driver.find_element_by_id("title").text

    # print(titleStr)

    for x in l:
        for y in x:
            if y in titleStr:
                count[l.index(x)] += titleStr.count(y)
                results.append(x[len(x) - 1])
                break

    # ABSTRACT
    abstractStr = driver.find_element_by_id("abstract").text

    # print(abstractStr)

    for x in l:
        for y in x:
            if y in abstractStr:
                count[l.index(x)] += abstractStr.count(y)

    # CLAIMS
    claims = driver.find_elements_by_class_name("claims")

    claimList = []

    for x in claims:
        claimList.append(x.text + "\n")
    claimStr = ""
    for x in claimList:
        claimStr += x

    # print(claimStr)

    for x in l:
        for y in x:
            if y in claimStr:
                count[l.index(x)] += claimStr.count(y)

    # ADD TO RESULTS
    # temp = count
    # c = 0
    # while c<3:
    #    t = l[l.index(max(count))][len(l[l.index(max(count))])-1]
    #    if t not in results:
    #        results.append(t)
    #        count.remove(max(count))
    #    c+=1

    # for y in l:
    #    if count[l.index(y)]>=3 and l[l.index(y)][len(l[l.index(y)])-1] not in results:
    #        results.append(y[len(y)-1])

    r = sorted(zip(count, l), reverse=True)[:3]
    for x in r:
        if x[0] >= target_frequency:
            results.append(x[1][len(x[1]) - 1])

    # c = 0
    # if len(results)==0:
    #    for y in l:
    #        if count[l.index(y)]!=0 and c<2:
    #            results.append(y[len(y)-1])
    #            count+=1

    # for x in count:
    #    print("Target: "+l[count.index(x)][len(l[count.index(x)])-1])
    #    print("#s of times seen: "+str(x)+"\n")
    # list = list[:3]
    return results
