def parse(driver, l, target_frequency):
    results = []
    count = [0] * len(l)

    # claims = driver.find_elements_by_class_name("claims")

    # dog = ""

    # for x in claims:
    #    dog = dog + x.text + "\n"

    # print(dog)
    # claim = dog

    # TITLE
    # titleStr = driver.find_element_by_id("title").text
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

    for x in claims:
        claimList.append(x.text + "\n")
    claimStr = ""
    for x in claimList:
        claimStr += x

    # print(claimStr)

    for x in l:
        for y in x:
            # y=str(y).lower()
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
    print(count)
    r = sorted(zip(count, l), reverse=True)[:3]
    for x in r:
        if x[0] >= target_frequency:
            results.append(x[1][0])

    # print(r)

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