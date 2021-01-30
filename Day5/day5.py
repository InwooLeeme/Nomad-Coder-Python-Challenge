import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

request = requests.get(url)

html = BeautifulSoup(request.text, "html.parser")

table = html.find("table")

rows = table.find_all("tr")[1:]

countries = []

for row in rows:
    td = row.find_all("td")
    country = td[0].text
    currency = td[1].text
    code = td[2].text
    if(country and code):
        if(currency != "No universal currency"):
            country = {
                "name": country,
                "code": code
            }
            countries.append(country)

countries = enumerate(countries)
for index, key in countries:
    country_name = key["name"]
    print(f"#{index} : {country_name}")
