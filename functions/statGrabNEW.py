from bs4 import BeautifulSoup
import requests
import pandas as pd
from fuzzywuzzy import process
import choice
from nba_api import *



def player_DFform(playerNameInput):
    global playerName, years
    player_df = pd.read_csv(
        'https://www.basketball-reference.com/short/inc/sup_players_search_list.csv', 
        header=None)
    player_df = player_df.rename(columns={0: 'id',
                                      1: 'playerName',
                                      2: 'years'})
    playersList = list(player_df['playerName'])
    playerMatch = pd.DataFrame(process.extract(f'{playerNameInput}', playersList, limit=1))
    search_match = playerMatch.rename(columns={0: 'playerName', 1: 'matchScore'})
    givenPlayerMatch = playerMatch.iloc[0][0]
    matches = pd.merge(search_match, player_df, how='inner',
                   on='playerName').drop_duplicates().reset_index(drop=True)
    choices = [': '.join(x) for x in list(
        zip(matches['playerName'], matches['years']))]
    playerName, years = choices[0].split(':')



class player_DFForm():
    def __init__(self, name):
            global playerName, years
            self.player_df = pd.read_csv(
                'https://www.basketball-reference.com/short/inc/sup_players_search_list.csv', 
                header=None)
            self.player_df = self.player_df.rename(columns={0: 'id',
                                            1: 'playerName',
                                            2: 'years'})
            self.playersList = list(self.player_df['playerName'])
            self.playerMatch = pd.DataFrame(process.extract(f'{name}', self.playersList, limit=1))
            search_match = self.playerMatch.rename(columns={0: 'playerName', 1: 'matchScore'})
            self.givenPlayerMatch = self.playerMatch.iloc[0][0]
            self.matches = pd.merge(search_match, self.player_df, how='inner',
                        on='playerName').drop_duplicates().reset_index(drop=True)
            self.choices = [': '.join(x) for x in list(
                zip(self.matches['playerName'], self.matches['years']))]
            self.playerName, self.years = self.choices[0].split(':')



Test = player_DFForm("Kawhi Leonard")
thePlayersName = Test.years

print(thePlayersName)