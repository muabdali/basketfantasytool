from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.basketball-reference.com/leagues/NBA_2021_per_game.html').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('tbody')

player = soup.find('div', class_='full_table')

print(player)
