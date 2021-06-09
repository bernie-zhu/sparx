import requests
from bs4 import BeautifulSoup

import companyNames
import gc

class CompanyLinks:

    def __init__(self, setCompany):
        self.company = setCompany


    def GetCompanyLinks(self):
        page = 0
        numberOfPages = 1
        urls = []

        while page < numberOfPages:
            main_url = "https://patents.google.com/"
            params = "?assignee=" + self.company + "&after=priority:20010602&type=PATENT&num=1&sort=new&page=" + str(page)

            res = requests.get(
                "https://patents.google.com/xhr/query?url=assignee%3D" + self.company + "%26after%3Dpriority"
                                                                               "%3A20010602%26type"
                                                                               "%3DPATENT%26num%3D1"
                                                                               "&exp=")
            main_data = res.json()
            data = main_data['results']['cluster']

            for i in range(len(data[0]['result'])):
                num = data[0]['result'][i]['patent']['publication_number']
                urls.append(main_url + "patent/" + num + "/en" + params)

            page += 1

        return urls


def CompanyLinksToClaims():
    allCompanies = companyNames.companies
    del companyNames.companies
    del companyNames.names
    gc.collect

    for company, links in allCompanies.items():
        links = CompanyLinks(company)
        allCompanies[company] = links.GetCompanyLinks()
        print(allCompanies[company])

        for i in range(len(allCompanies[company])):
            soup = BeautifulSoup(requests.get(allCompanies[company][i]).content, 'html.parser')

            # get first claim
            claims = [soup.select_one("li.claim, li.claim-dependent, div.claim, claim")]

            # (optionally) add any claim dependent to output
            for claim_dependent in soup.select("li.claim-dependent"):
                if claim_dependent.find_previous("li", class_="claim") == claims[0]:
                    claims.append(claim_dependent)

            if claims[0] == None:
                claim = ""
            else:
                claim = " ".join(c.get_text(strip=True) for c in claims)

            # print all
            print(claim)
            allCompanies[company][i] = claim

    return allCompanies
