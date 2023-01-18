from bs4 import BeautifulSoup
import requests
import pandas as pd
from fuzzywuzzy import process
import choice
from nba_api import *



def player_DFform(playerNameInput):
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
    print(choices)

# NEXT STEP, FOLLOW LINE 50 in ORIGINAL statGrab.py



player_DFform('Kawhi Leonard')





        

