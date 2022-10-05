# pip install bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

# pip install fuzzywuzzy
from fuzzywuzzy import process

# pip install choice
import choice

from nba_api import *

from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players

# Basic Request
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)


custom_headers = {
    'Host': 'stats.nba.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

# Only available after v1.1.0
# Proxy Support, Custom Headers Support, Timeout Support (in seconds)
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544, proxy='127.0.0.1:80', headers=custom_headers, timeout=100)



# asking for player's name
def askname():
    playerNameInput = input(str("Enter the player's name -> "))
    return playerNameInput

def askStat():
    userDataStat = input("Enter the statistic you'd like to see")
    return userDataStat

# Get all player IDs
player_df = pd.read_csv(
    'https://www.basketball-reference.com/short/inc/sup_players_search_list.csv', header=None)
player_df = player_df.rename(columns={0: 'id',
                                      1: 'playerName',
                                      2: 'years'})
playersList = list(player_df['playerName'])

# asks user for player name
playerNameInput = askname()
userDataStat = askStat()


# Find closest matches

# process.extra(f'{WHAT TO LOOK FOR}', WHERE TO LOOK) Checks playersList (19-25) for the player name given
# matchscore uses fuzzywuzzy to find the closest to given name

search_match = pd.DataFrame(process.extract(f'{playerNameInput}', playersList))
search_match = search_match.rename(columns={0: 'playerName', 1: 'matchScore'})

matches = pd.merge(search_match, player_df, how='inner',
                   on='playerName').drop_duplicates().reset_index(drop=True)
choices = [': '.join(x) for x in list(
    zip(matches['playerName'], matches['years']))]

# Choice the match
playerChoice = choice.Menu(choices).ask()
playerName, years = playerChoice.split(': ')

# Get that match players id
match = player_df[(player_df['playerName'] == playerName)
                  & (player_df['years'] == years)]

baseUrl = 'https://www.basketball-reference.com/players'
playerId = match.iloc[0]['id']

url = f'{baseUrl}/{playerId[0]}/{playerId}.html'




html = requests.get(url).text.replace('<!--', '').replace('-->', '')
soup = BeautifulSoup(html, 'html.parser')
statList = [userDataStat,'fga_per_mp', 'fg3_per_mp', 'ft_per_mp']
for stat in statList:
    try:
        statTd = soup.find('td', {'data-stat': stat})
        print("Projected",statTd['data-stat'], statTd.text)
    except:
        print(f'{stat} stat not found')

# tests


