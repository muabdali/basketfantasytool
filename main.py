from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.basketball-reference.com/leagues/NBA_2021_per_game.html').text

soup = BeautifulSoup(source, 'lxml')

article = soup.findAll(class_='right')
print(article)