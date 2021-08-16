from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://www.nba.com/stats/")

stats = response.text

soup = BeautifulSoup(stats, "lxml")

print(soup.prettify())