# pull player from espn team

from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.request, json 

# default url https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/***LEAGUEID***



leagueID = '454981630'
league_URL = f'https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/{leagueID}'

# gets json from webpage also 
with urllib.request.urlopen(league_URL) as url:
    data = json.load(url)
    dataJSON = json.loads(data)


print(dataJSON)

