
# pip install bs4
from email.policy import default
from bs4 import BeautifulSoup
import requests
import pandas as pd

# pip install fuzzywuzzy
from fuzzywuzzy import process

# pip install choice
import choice

from nba_api import *
# import endpoints
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import PlayerNextNGames


import pandas as pd
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
# more endpoints
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import MatchupsRollup
player_dict = players.get_active_players()


#gamelog_bron = playergamelog.PlayerGameLog(player_id='2544', season = '2022')

nextgame_bron = PlayerNextNGames(number_of_games=5, player_id=2544)

df = nextgame_bron.get_data_frames()[0]
print(df)


def fixtureFind():
    i = 0
    while i < 5:
        nextFixture = df.iat[i,7]
        if nextFixture == "LAL":
            nextFixture = df.iat[i,6]
            print(nextFixture)
            i = i + 1
        else:
            print(nextFixture)
            i = i + 1

fixtureFind()

#a = df.iat[0,7]

#print(a)