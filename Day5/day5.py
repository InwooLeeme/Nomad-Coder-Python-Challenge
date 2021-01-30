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

print("Hello! Please choose select a country by number:\n")
for index, key in enumerate(countries):
    country_name = key["name"]
    print(f"#{index} : {country_name}")


def ask():
    try:
        user = int(input("#:"))
        if(user <= len(countries)):
            print(f"You chose {countries[user]['name']}")
            print(f"The currency code is {countries[user]['code']}")
        else:
            print("Chose the number from the list.")
            ask()
    except ValueError:
        print("That was not a number.")
        ask()


ask()
