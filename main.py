from bs4 import BeautifulSoup
import requests
import pandas as pd

#pip install fuzzywuzzy
from fuzzywuzzy import process

#pip install choice
import choice



def askname():
    playerNameInput = input(str("Enter the player's name -> "))
    return playerNameInput


# Get all player IDs
player_df = pd.read_csv('https://www.basketball-reference.com/short/inc/sup_players_search_list.csv', header=None)
player_df = player_df.rename(columns={0:'id',
                                      1:'playerName',
                                      2:'years'})
playersList = list(player_df['playerName'])

# asks user for player name
playerNameInput = askname()


# Find closest matches
search_match = pd.DataFrame(process.extract(f'{playerNameInput}', playersList))
search_match = search_match.rename(columns={0:'playerName',1:'matchScore'})

matches = pd.merge(search_match, player_df, how='inner', on='playerName').drop_duplicates().reset_index(drop=True)
choices = [': '.join(x) for x in list(zip(matches['playerName'], matches['years']))]

# Choice the match
playerChoice = choice.Menu(choices).ask()
playerName, years = playerChoice.split(': ')

# Get that match players id
match = player_df[(player_df['playerName'] == playerName) & (player_df['years'] == years)]

baseUrl = 'https://www.basketball-reference.com/players'
playerId = match.iloc[0]['id']

url = f'{baseUrl}/{playerId[0]}/{playerId}.html'


html = requests.get(url).text.replace('<!--', '').replace('-->', '')
soup = BeautifulSoup(html, 'html.parser')
statList = ['fga_per_mp', 'fg3_per_mp', 'ft_per_mp', 'random']
for stat in statList:
    try:
        statTd = soup.find('td', {'data-stat':stat})
        print(statTd['data-stat'], statTd.text)
    except:
        print(f'{stat} stat not found')

# test