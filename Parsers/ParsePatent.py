def parse(driver, alias_list, genes, target_frequency):
    results = []
    count = [0] * len(alias_list)

    # TITLE
    # titleStr = driver.find_element_by_id("title").text
    titleStr = driver.title.split(" - ")[1].strip()

    # print(titleStr)
    for aliases in alias_list:
        for cur in aliases:
            if len(str(cur)) >= 3:
                # print("entered")
                if str(cur) in titleStr:
                    countTitle = (titleStr.count(" " + str(cur) + " ") + titleStr.count(" " + str(cur) + ".") + \
                                  titleStr.count(" " + str(cur) + ",") + titleStr.count(" " + str(cur) + "'") + \
                                  titleStr.count(" " + str(cur) + "/") + titleStr.count("/" + str(cur) + " ") + \
                                  titleStr.count(" " + str(cur) + ":") + titleStr.count("-" + str(cur) + " "))
                    if countTitle != 0:
                        results.append(aliases[0])
                        count[alias_list.index(aliases)] += countTitle
                        break

    # ABSTRACT
    abstractStr = driver.find_element_by_id("abstract").text

    if not abstractStr:
        abstractStr = driver.find_element_by_tag_name("patent-text").text
    # print(abstractStr)

    ## aliases - list of aliases for current gene
    ## cur - the current alias that is being looked for in the text
    for aliases in alias_list:
        for cur in aliases:
            # y=str(y).lower()
            if len(str(cur)) >= 3:
                # print("entered")
                if str(cur) in abstractStr:
                    countAbstract = 3 * (
                                abstractStr.count(" " + str(cur) + " ") + abstractStr.count(" " + str(cur) + ".") + \
                                abstractStr.count(" " + str(cur) + ",") + abstractStr.count(" " + str(cur) + "'") + \
                                abstractStr.count(" " + str(cur) + "/") + abstractStr.count("/" + str(cur) + " ") + \
                                abstractStr.count(" " + str(cur) + ":") + abstractStr.count("-" + str(cur) + " "))
                    count[alias_list.index(aliases)] += countAbstract
                    # print(str(temp) + " gene: "+ str(y))

    # CLAIMS
    claimList = []

    claims = driver.find_elements_by_class_name("claim-text")
    num_claims = 0
    for x in claims:
        if num_claims >= 10:
            break
        claimList.append(x.text + "\n")
        num_claims += 1

    # print(claimList)
    claimStr = ""
    for x in claimList:
        claimStr += x

    # print(claimStr)
    for aliases in alias_list:
        for cur in aliases:
            if len(str(cur)) >= 3:
                # print("entered")
                if str(cur) in claimStr:
                    count[alias_list.index(aliases)] += claimStr.count(" " + str(cur) + " ") + claimStr.count(
                        " " + str(cur) + ".") + \
                                                        claimStr.count(" " + str(cur) + ",") + claimStr.count(
                        " " + str(cur) + "'") + \
                                                        claimStr.count(" " + str(cur) + "/") + claimStr.count(
                        "/" + str(cur) + " ") + \
                                                        claimStr.count(" " + str(cur) + ":") + claimStr.count(
                        "-" + str(cur) + " ")

    sort = sorted(zip(count, genes), reverse=True)
    count = 0
    r = []
    print_stuff = []
    for x in sort:
        if count >= 3:
            break
        elif x[1] not in results:
            r.append(x)
            print_stuff.append(x)
            count += 1
        elif x[1] in results:
            print_stuff.append(x)

    for x in r:
        if x[0] >= target_frequency:
            results.append(x[1])
        elif x[0] > 0 and len(results) == 0:
            results.append(x[1])
            break

    return results