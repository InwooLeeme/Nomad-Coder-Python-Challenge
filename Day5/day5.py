import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

request = requests.get(url)

country_list = BeautifulSoup(
    request.text, "html.parser").select("td:nth-child(1)")

code_list = BeautifulSoup(
    request.text, "html.parser").select("td:nth-child(3)")

country_name = []
code_name = []

for name in country_list:
    country_name.append(name.text)
country_list = country_name
