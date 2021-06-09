#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import json
import urllib.request
import pandas as pd


# In[ ]:





# In[46]:


#url = 'https://patents.google.com/patent/AU2016304408B2/en'
#url = 'https://patents.google.com/patent/US8560271B2/en?assignee=Roche&after=priority:20010602&type=PATENT&num=100&sort=new'
url = 'https://patents.google.com/patent/EP3017304B1/en'
#url = 'https://patents.google.com/patent/US8560271B2/en?assignee=Roche&after=priority:20010602&type=PATENT&num=100&sort=new'
main_url="https://patents.google.com/"
params="?assignee=Pfizer&after=priority:20010602&type=PATENT&num=100"
#page = requests.get(url).content
soup = BeautifulSoup(requests.get(url).content, 'html.parser')


# In[42]:


# get first claim
claims = [soup.select_one("li.claim, li.claim-dependent, div.claim, claim")]

# (optionally) add any claim dependent to output
for claim_dependent in soup.select("li.claim-dependent"):
    if claim_dependent.find_previous("li", class_="claim") == claims[0]:
        claims.append(claim_dependent)

# print all
out = " ".join(c.get_text(strip=True) for c in claims)
out.replace(" ", "")
print(out)


# In[51]:


abstract = soup.find(class_="abstract")
if abstract is None:
    abstract = ""
print(abstract)


# In[5]:


## UNNECESSARY

with urllib.request.urlopen("http://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/locus_groups/protein-coding_gene.json") as url:
    data = json.loads(url.read().decode())
    print(data["symbol"])


# In[4]:


### GENE LIST

response = requests.get("http://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/locus_groups/protein-coding_gene.json")
data = response.json()
#symbols = [i['symbol'] for i in data['response']['docs']]

df = pd.DataFrame(data['response']['docs'])
symbols = df['symbol'].tolist()
print(df)


# In[33]:


### SCRAPE CLAIM

results = soup.find(class_="claim")
claim_texts = results.find_all('div',{'class':'claim-text'})
fullStr = ' '.join([x.text for x in claim_texts])
fullStr.replace(" ", "")
#for a in soup.find(class_="claim", num="1"):
    #text = a.find(class_="claim-text")
 #   print(a)
#print(results.prettify())


# In[29]:


print(fullStr)


# In[12]:


# import HTMLSession from requests_html

res=requests.get("https://patents.google.com/xhr/query?url=assignee%3DPfizer%26after%3Dpriority%3A20010602%26type%3DPATENT%26num%3D100&exp=")



# In[13]:


main_data=res.json()
data=main_data['results']['cluster']
i = 0


# In[14]:


for i in range(len(data[0]['result'])): 
    i += 1
    num=data[0]['result'][i]['patent']['publication_number']
    print(num)
    print(main_url+"patent/"+num+"/en"+params)


# In[11]:





# In[ ]:


https://patents.google.com/xhr/query?url=assignee%3DRoche%26after%3Dpriority%3A20110602%26type%3DPATENT%26num%3D100&exp=
https://patents.google.com/xhr/query?url=assignee%3DRoche%26after%3Dpriority%3A20110602%26type%3DPATENT%26num%3D100%26page%3D1&exp=
https://patents.google.com/xhr/query?url=assignee%3DRoche%26after%3Dpriority%3A20110602%26type%3DPATENT%26num%3D100%26page%3D2&exp=
    
https://patents.google.com/xhr/query?url=assignee%3DPfizer%26after%3Dpriority%3A20010602%26type%3DPATENT%26num%3D100&exp=


# In[ ]:





# In[ ]:




