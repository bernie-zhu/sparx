def parse(driver, l, genes, target_frequency):
    results = []
    count = [0] * len(l)

    titleStr = driver.title.split(" - ")[1].strip()

    # print(titleStr)
    ## SWITCH CASE
    for x in l:
        for y in x:
            # y=str(y).lower()
            if len(str(y)) >= 3:
                # print("entered")
                if " " + str(y) + " " in titleStr:
                    count[l.index(x)] += titleStr.count(" " + str(y) + " ")
                    results.append(x[0])
                    break
                if " " + str(y) + "." in titleStr:
                    count[l.index(x)] += titleStr.count(" " + str(y) + ".")
                    results.append(x[0])
                    break
                if " " + str(y) + "," in titleStr:
                    count[l.index(x)] += titleStr.count(" " + str(y) + ",")
                    results.append(x[0])
                    break
                if " " + str(y) + "'" in titleStr:
                    count[l.index(x)] += titleStr.count(" " + str(y) + "'")
                    results.append(x[0])
                    break
                if " " + str(y) + "/" in titleStr:
                    count[l.index(x)] += titleStr.count(" " + str(y) + "/")
                    results.append(x[0])
                    break
                if "/" + str(y) + " " in titleStr:
                    count[l.index(x)] += titleStr.count("/" + str(y) + " ")
                    results.append(x[0])
                    break
                if " " + str(y) + ":" in titleStr:
                    count[l.index(x)] += titleStr.count(" " + str(y) + ":")
                    results.append(x[0])
                    break

    # ABSTRACT
    # abstractStr = driver.find_element_by_id("abstract").text
    abstractStr = driver.find_element_by_id("abstract").text

    if not abstractStr:
        abstractStr = driver.find_element_by_tag_name("patent-text").text
    # print(abstractStr)

    for x in l:
        # y=str(y).lower()
        for y in x:
            y = str(y).lower()
            if len(str(y)) >= 3:
                # print("entered")
                if " " + str(y) + " " in abstractStr:
                    count[l.index(x)] += abstractStr.count(" " + str(y) + " ")
                elif " " + str(y) + "." in abstractStr:
                    count[l.index(x)] += abstractStr.count(" " + str(y) + ".")
                elif " " + str(y) + "," in abstractStr:
                    count[l.index(x)] += abstractStr.count(" " + str(y) + ",")
                elif " " + str(y) + "'" in abstractStr:
                    count[l.index(x)] += abstractStr.count(" " + str(y) + "'")
                elif " " + str(y) + "/" in abstractStr:
                    count[l.index(x)] += abstractStr.count(" " + str(y) + "/")
                elif "/" + str(y) + " " in abstractStr:
                    count[l.index(x)] += abstractStr.count("/" + str(y) + " ")
                elif " " + str(y) + ":" in abstractStr:
                    count[l.index(x)] += abstractStr.count(" " + str(y) + ":")

    # CLAIMS
    claims = driver.find_elements_by_class_name("claims")

    claimList = []
    temp = 0
    for x in claims:
        if temp == 10:
            break
        claimList.append(x.text + "\n")
        temp += 1

    claimStr = ""
    for x in claimList:
        claimStr += x

    # print(claimStr)

    for x in l:
        for y in x:
            if len(str(y)) >= 3:
                # print("entered")
                if " " + str(y) + " " in claimStr:
                    count[l.index(x)] += claimStr.count(" " + str(y) + " ")
                elif " " + str(y) + "." in claimStr:
                    count[l.index(x)] += claimStr.count(" " + str(y) + ".")
                elif " " + str(y) + "," in claimStr:
                    count[l.index(x)] += claimStr.count(" " + str(y) + ",")
                elif " " + str(y) + "'" in claimStr:
                    count[l.index(x)] += claimStr.count(" " + str(y) + "'")
                elif " " + str(y) + "/" in claimStr:
                    count[l.index(x)] += claimStr.count(" " + str(y) + "/")
                elif "/" + str(y) + " " in claimStr:
                    count[l.index(x)] += claimStr.count("/" + str(y) + " ")
                elif " " + str(y) + ":" in claimStr:
                    count[l.index(x)] += claimStr.count(" " + str(y) + ":")

    #print(count)
    count = [float(x) for x in count]
    test = zip(count,genes)
    for x in test:
        print(x)
    r = sorted(zip(count, l), reverse=True)[:3]
    for x in r:
        if x[0] >= target_frequency:
            results.append(x[1][0])

    # print(r)

    return results