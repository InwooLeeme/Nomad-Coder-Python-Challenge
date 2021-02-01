#import os
import csv
import requests
from bs4 import BeautifulSoup

# os.system("clear")
alba_url = "http://www.alba.co.kr"

alba_request = requests.get(alba_url)

abla_html = BeautifulSoup(alba_request.text, "html.parser")

alba_ul = abla_html.find_all("ul", {"class": "goodsBox"})[1:]

print(alba_ul)
