# ESPN Fantasy league settings import
# accesses scoringItems and returns values. All the point values are hidden under a dataID system. See statID.md for more info.

from fileinput import filename
import json
from discord import Team
import numpy as np
import requests


path = './'
fileName = 'members'
leagueID = 454981630

# includes dictionary for all key value pairs (points, steals etc)
# for legend on keys (0 = points, 6 = rounds etc) check statID.md
def importSettings(givenLeagueID):
    global statsDict
    url = f'https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/{givenLeagueID}?view=mSettings&view=mRoster&view=mTeam&view=modular&view=mNav'
    p = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})
    statsDict = {
        '0' :[],
        '1' :[],
        '6' :[],
        '11' :[],
        '13' :[],
        '14' :[],
        '15' :[],
        '16' :[],
        '17' :[],
        '2' :[],
        '3' :[]
            }
    for t in p.json()['settings']['scoringSettings']['scoringItems']:
        statID = (t['statId'])
        pointValue = (t['points'])
        statsID = str(statID)
        statsDict[statsID].append(pointValue)



importSettings(leagueID)