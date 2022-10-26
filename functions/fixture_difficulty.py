
# pip install bs4
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

name = "Kyle Lowry"

def findPlayerFunc(find):
    global findPlayer
    findPlayer = players.find_players_by_full_name(find)
    return findPlayer



findPlayerFunc(name)

pf = pd.DataFrame(findPlayer)
playerTeamID = "PlaceHolder"

#saves playerinfo df as csv
playerCSVDataFrame = pf.to_csv('file_name.csv')
print(pf)



#gamelog_bron = playergamelog.PlayerGameLog(player_id='2544', season = '2022')


# extracts playerID from df (pf)
#def findPlayerID():

# reads playerinfo dataframe and extracts id as playerID_Spec and full name and player id as pfRead


def playerID_Pull():
    global playerID_Spec, pfName_playerID
    dataset = pd.read_csv('file_name.csv')
    cols = [1,2]
    pfName_playerID = dataset[dataset.columns[cols]]
    playerID_Spec = pf.iat[0,0]
    print(playerID_Spec)
    return



playerID_Pull()

# VARIABLE SWAP VERY IMPORTANT
players_ID = playerID_Spec 
print(players_ID)

teamABBV = commonplayerinfo.CommonPlayerInfo(player_id=players_ID)
abbvDF = teamABBV.get_data_frames()[0]
getAbbv = abbvDF.iat[0, 20]
print(getAbbv)

nextgame_bron = PlayerNextNGames(number_of_games=5, player_id=players_ID)

df = nextgame_bron.get_data_frames()[0]
print(df)

# list of next 5 games
game_List = []

hard_List = [ 'BOS', 'PHX', 'LAC', 'PHI', 'MKW', 'GSW']
med_List = ['MIA','TOR','DEN','BKN','MEM', 'DAL','CLE','MIA','ATL', 'MIN']
easy_List = ['HOU', 'OKC','SAC','NOP', 'CHI', 'LAL', 'POR', 'NYK', 'CHA', 'WAS', 'DET', 'IND', 'ORL', 'UTA', 'SAS']




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


playerAbbv = str(getAbbv)
fixtureFind_abbv(playerAbbv)


print(game_List)

def matchupDecide():
    c = 0
    while c < 5:
        for team in game_List:
            if team in hard_List:
                print(team + " - Hard Matchup")
                c = c + 1
            elif team in med_List:
                print(team + " - Medium Matchup")
                c = c + 1
            elif team in easy_List:
                print(team + " - Easy Matchup")
                c = c + 1

matchupDecide()