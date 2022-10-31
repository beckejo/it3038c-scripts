import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.reebok.com/us/smiley-shaq-attaq-basketball-shoes/GX2250.html?cm_sp=SLOT-2.1-_-HOME_%3F_%3F_HOME_%3F-_-PRODUCTSELECTIONCAROUSEL-PRODUCT-CARD-_-957910").content 
soup = BeautifulSoup(data, 'html.parser') 
span = soup.find("h1", {"class":"product_information_title___2rG9M product_title gl-heading gl-heading--m"}) 
title = span.text
span = soup.find("span", {"class":"gl-price__value gl-price__value--sale"}) 
price = span.text
print("Item %s has price %s" % (title, price))
