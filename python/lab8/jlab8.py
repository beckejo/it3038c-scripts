import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.reebok.com/us/smiley-club-c-85-mens-shoes/GV9492.html").content
soup = BeautifulSoup(data, 'html.parser') 
span = soup.find("h1", {"class":"name___120FN"})
title = span.text
span = soup.find("h1", {"class":"gl-price-item notranslate"})
price = span.text
print("Item %s has price %s" % (title, price))