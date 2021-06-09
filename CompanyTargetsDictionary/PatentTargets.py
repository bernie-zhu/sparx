import requests
from CompanyTargetsDictionary import companyNames
import gc


class PatentTargets:

    def __init__(self, company):
        self.company = company

    def linksforpatents(self, pages):
        page = 0
        numberOfPages = pages
        populartargets = []

        while page < numberOfPages:
            main_url = "https://patents.google.com/"
            params = "?assignee=" + self.company + "&after=priority:20110602&type=PATENT&num=100&sort=new&page=" + str(
                page)

            res = requests.get(
                "https://patents.google.com/xhr/query?url=assignee%3D" + self.company + "%26after%3Dpriority"
                                                                                        "%3A20110602%26type"
                                                                                        "%3DPATENT%26num%3D1"
                                                                                        "&exp=")
            main_data = res.json()
            data = main_data['results']['cluster']

            for i in range(len(data[0]['result'])):
                num = data[0]['result'][i]['patent']['publication_number']
                # urls.append(main_url + "patent/" + num + "/en" + params)
                populartargets.append(parse(main_url + "patent/" + num + "/en" + params))

            page += 1

        return populartargets


def linksintodict():
    pages = int(input("How many pages do you want to search through: "))
    allCompanies = companyNames.companies
    del companyNames.companies
    del companyNames.names
    gc.collect

    for company, links in allCompanies.items():
        links = PatentTargets(company)
        allCompanies[company] = links.linksforpatents(pages)

    return allCompanies
