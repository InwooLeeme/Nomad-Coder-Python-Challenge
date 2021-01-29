import requests
from bs4 import BeautifulSoup

indeed_url = "https://www.indeed.com/jobs?q=python&limit=50"

indeed_result = requests.get(indeed_url)

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("a", {"class": "jobtitle"})

pages = pagination('a')

print(pagination)
