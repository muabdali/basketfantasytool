
# pip install bs4
from email.policy import default
from logging import PlaceHolder
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

name = "Lebron James"

def findPlayerFunc(find):
    global findPlayer
    findPlayer = players.find_players_by_full_name(find)
    return findPlayer



findPlayerFunc(name)

pf = pd.DataFrame(findPlayer)
playerTeamID = "PlaceHolder"


pf.to_csv('file_name.csv')



#gamelog_bron = playergamelog.PlayerGameLog(player_id='2544', season = '2022')

#NEXT
players_ID = 2544 

def findPlayerID():
    return


nextgame_bron = PlayerNextNGames(number_of_games=5, player_id=players_ID)

df = nextgame_bron.get_data_frames()[0]
print(df)

# list of next 5 games
game_List = []

hard_List = [ 'BOS', 'PHX', 'LAC', 'PHI', 'MKW', 'GSW']
med_List = ['DEN','BKN','MEM', 'DAL', 'CLE', 'MIA', 'TOR', 'ATL', 'MIN']
easy_List = ['NOP', 'CHI', 'LAL', 'POR', 'NYK', 'CHA', 'SAC', 'WAS', 'DET', 'IND', 'HOU', 'ORL', 'UTA', 'OKC', 'SAS']




# function that repeats 5 times, finds the opposing team's abbriviation on the 7th coloumn. 
# if the player's team is on the 7th coloum, it switches to the 6th and takes that instead.
# it then appends the diffculty_List list to include all 5 fixtures.
def fixtureFind_abbv(playersTeam_Abbv):
    i = 0
    while i < 5:
        nextFixture = df.iat[i,7]
        if nextFixture == playersTeam_Abbv:
            nextFixture = df.iat[i,6]
            print(nextFixture)
            game_List.append(nextFixture)
            i = i + 1
        else:
            print(nextFixture)
            game_List.append(nextFixture)
            i = i + 1



def fixtureFind_visID():
    b = 0
    while b < 5:
        nextFixture = df.iat[b, 3]
        if nextFixture == playerTeamID:
            nextFixture = df.iat[b, 2]
            print(nextFixture)


playerAbbv = str("LAL")
fixtureFind_abbv(playerAbbv)


print(game_List)

def matchupDecide():
    for team in game_List:
        c = 0
        while c < 6:
            if team == hard_List[c]:
                print(team + " - Hard Matchup")
                c = c + 1
            elif team == med_List[c]:
                print(team + " - Medium Matchup")
                c = c + 1
            elif team == easy_List[c]:
                print(team + " - Easy Matchup")
                c = c + 1
            else:
                c = c + 1

matchupDecide()
