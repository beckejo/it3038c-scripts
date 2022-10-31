import requests, re
from bs4 import BeautifulSoup

r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/computers").content
soup = BeautifulSoup(r, 'html.parser')
tags = soup.findAll("div", {"class": re.compile('(ratings)')})
i = 1
for p in tags:
    a = p.findAll("p", {"class": "pull-right"})
    print("Computer " + str(i) + " has " + a[0].string)
    i = i + 1
