import pandas as pd
import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import process
from nba_api import *
from teamDiff import *
from difficultyDynamic import *
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import PlayerNextNGames


class NBA_PlayerFixtures():
    global players_ID, nextFiveGames, nextNumberGames
    def __init__(self, name):
        self.name = name
        self.player_dict = players.get_active_players()
        self.findPlayer = players.find_players_by_full_name(self.name)
        self.pf = pd.DataFrame(self.findPlayer)
        self.playerTeamID = "PlaceHolder"
        self.playerCSVDataFrame = self.pf.to_csv('file_name.csv')
        self.players_ID = self.playerID_pull()
        self.teamABBV = commonplayerinfo.CommonPlayerInfo(player_id=self.players_ID)
        self.abbvDF = self.teamABBV.get_data_frames()[0]
        self.getAbbv = self.abbvDF.iat[0, 20]
        self.nextFiveGames = PlayerNextNGames(number_of_games=5, player_id=self.players_ID)
        self.df = self.nextFiveGames.get_data_frames()[0]
        self.game_List = []
        players_ID = self.players_ID

    def playerID_pull(self):
        global playerID_Spec
        dataset = pd.read_csv('file_name.csv')
        cols = [1,2]
        pfName_playerID = dataset[dataset.columns[cols]]
        playerID_Spec = self.pf.iat[0,0]
        return playerID_Spec

    def fixture_find_abbv(self, playersTeam_Abbv):
        for i in range(5):
            nextFixture = self.df.iat[i,7]
            if nextFixture == playersTeam_Abbv:
                nextFixture = self.df.iat[i,6]
            self.game_List.append(nextFixture)

    def nextNumberGames(N_Games):
        p = NBA_PlayerFixtures("Kawhi Leonard")
        pes = p.players_ID
        nextNumberGamesPlain = PlayerNextNGames(number_of_games=N_Games, player_id=pes)
        nextNumberGamesDF = nextNumberGamesPlain.get_data_frames()[0]
        print(nextNumberGamesDF)
        



