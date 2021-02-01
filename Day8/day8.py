#import os
import csv
import requests
from bs4 import BeautifulSoup

# os.system("clear")
alba_url = "http://www.alba.co.kr"

url_list = []

alba_request = requests.get(alba_url)

abla_html = BeautifulSoup(alba_request.text, "html.parser")

main_brand = abla_html.find("div", {"id": "MainSuperBrand"})

ul = main_brand.find("ul", {"class": "goodsBox"})

li = ul.find_all("li", {"class": "impact"})

for a in li:
    links = a.find("a", {"class": "goodsBox-info"}).get('href')
    url_list.append(links)
