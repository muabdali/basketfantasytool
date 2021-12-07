from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.basketball-reference.com/leagues/NBA_2021_per_game.html').text

soup = BeautifulSoup(source, 'lxml')
tbody = soup.find("div", {"id": "all_per_game_stats"})
fullt = tbody.find('tbody')

# data = fullt.find("player")
# use soup.get to get obscure attributes other than class_=
data = fullt.findAll('tr', class_="full_table")

#print(tbody)
print(data)