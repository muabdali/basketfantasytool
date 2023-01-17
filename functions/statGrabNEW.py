from bs4 import BeautifulSoup
import requests
import pandas as pd
from fuzzywuzzy import process
import choice
from nba_api import *


class NBA_PlayerStats():
    def __init__(self, name):
        self.name = name
        self.playerDF = pd.read_csv('https://www.basketball-reference.com/short/inc/sup_players_search_list.csv', header=None)
        self.playerDF = self.playerDF.rename(columns={0: 'id',
                                      1: 'playerName',
                                      2: 'years'})
        self.playersList = list(self.playerDF['playerName'])
        return self.playersList

NBA_PlayerStats("Kawhi Leonard")

