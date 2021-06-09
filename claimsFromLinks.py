import requests
from bs4 import BeautifulSoup
import json

class ClaimFromLinks:
    def __init__(self, allCompanyLinks):
        self.companyLinks = allCompanyLinks

    def convertLinksToClaims(self):
        url = 'https://patents.google.com/patent/EP3017304B1/en'
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')

        # get first claim
        claims = [soup.select_one("li.claim, li.claim-dependent")]

        # (optionally) add any claim dependent to output
        for claim_dependent in soup.select("li.claim-dependent"):
            if claim_dependent.find_previous("li", class_="claim") == claims[0]:
                claims.append(claim_dependent)

        # print all
        claim = " ".join(c.get_text(strip=True) for c in claims)
        print(claim)
