import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

request = requests.get(url)

html = BeautifulSoup(request.text, "html.parser")

table = html.find("table")

print(table)
