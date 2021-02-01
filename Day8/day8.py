#import os
import csv
import requests
from bs4 import BeautifulSoup

# os.system("clear")
alba_url = "http://www.alba.co.kr"

url_list = []

data_list = []

alba_request = requests.get(alba_url)

abla_html = BeautifulSoup(alba_request.text, "html.parser")

main_brand = abla_html.find("div", {"id": "MainSuperBrand"})

ul = main_brand.find("ul", {"class": "goodsBox"})

li = ul.find_all("li", {"class": "impact"})

for a in li:
    links = a.find("a", {"class": "goodsBox-info"}).get('href')
    company = a.find("span", {"class": "company"}).get_text()
    url_dict = {
        "url": links,
        "company": company
    }
    url_list.append(url_dict)

for item in url_list:
    print(f"Now scrapping on {item['company']}")
    each_url = item['url']
    request = requests.get(each_url)
    each_html = BeautifulSoup(request.text, "html.parser")
    tr = each_html.find("tbody").find_all("tr", {"class": ""})
    for td in tr:
        location = td.find("td", {"class": "local"}, recurive=False)
        if(location is None):
            location = "None"
            continue
        else:
            real_local = location.get_text().replace("\xa0", " ")
        title = td.find("span", {"class": "company"})
        if(title is None):
            title = "None"
            continue
        during = td.find("td", {"class": "data"})
        if(during is None):
            during = "None"
            continue
        pay = td.find("span", {"class": "number"})
        if(pay is None):
            pay = "None"
            continue
        up_time = td.find("td", {"class": "last"})
        if(up_time is None):
            up_time = "None"
            continue
        alba_dict = {
            "place": real_local,
            "title": title.text,
            "time": during.text,
            "pay": pay.text,
            "date": up_time.text
        }
        company_name = item['company'].replace("/", " ")
        file = open(f"{company_name}.csv", mode="w", encoding="utf-8")
        writer = csv.writer(file)
        writer.writerow(list(alba_dict.values()))
