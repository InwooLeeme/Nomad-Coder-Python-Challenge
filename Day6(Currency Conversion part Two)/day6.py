#import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

# os.system("clear")

url = "https://www.iban.com/currency-codes"

request = requests.get(url)

html = BeautifulSoup(request.text, "html.parser")

table = html.find("table")

rows = table.find_all("tr")[1:]

countries = []

for row in rows:
    td = row.find_all("td")
    name = td[0].text
    currency = td[1].text
    code = td[2].text
    if(name and code):
        if(currency != "No universal currency"):
            country = {
                "name": name,
                "code": code
            }
            countries.append(country)

for index, key in enumerate(countries):
    print(f"#{index} : {key['name']}")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

#print(format_currency(5000, "KRW", locale="ko_KR"))
