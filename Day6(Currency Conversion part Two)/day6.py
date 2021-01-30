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

print("Welcome to CurrencyConvert PRO 2000")


def convert_coins(first, second):
    try:
        convert_coin = int(input(
            f"How many {countries[first]['name']} do you want to convert to {countries[second]['name']}?\n"))
        convert_url = f"https://transferwise.com/gb/currency-converter/{countries[first]['code'].lower()}-to-{countries[second]['code'].lower()}-rate?amount={convert_coin}"
        print(convert_url)

    except ValueError:
        print("That was not the number.")
        convert_coins(first, second)


def ask_country():
    try:
        print("Where are you from? Choose a country by number.\n")
        first_country = int(input("#: "))
        if(first_country <= len(countries)):
            print(f"{countries[first_country]['name']}\n")
            print("Now choose another country.\n")
            second_country = int(input("#: "))
            print(f"{countries[second_country]['name']}\n")
            if(second_country <= len(countries)):
                convert_coins(first_country, second_country)
            else:
                print("That was not in the list.")
                ask_country()
        else:
            print("That was not in the list.")
            ask_country()
    except ValueError:
        print("That was not the number.")
        ask_country()


ask_country()

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

#print(format_currency(5000, "KRW", locale="ko_KR"))
