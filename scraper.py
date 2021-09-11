
from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://www.nba.com/stats/")

stats = response.text


# Stats page of the NBA
soup = BeautifulSoup(stats, "lxml")

# Show all entire html page
print(soup.prettify())

soup.find_all()


# grabbing all p tags
soup.currentTag('<p>')