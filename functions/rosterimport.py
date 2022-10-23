# pull player from espn team

from fileinput import filename
import json
from discord import Team



path = './'
fileName = 'members'

import requests
leagueID = 454981630
#teamID = 1


# dictionary that only holds player names
rosterPlayer_dict=[]
# function to count teams
# teamNumber is amount of teams
def TeamCount(givenLeagueID):
    global teamNumber
    teamNumber = 0
    curl = f'https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/{givenLeagueID}?view=mSettings&view=mRoster&view=mTeam&view=modular&view=mNav'
    p = requests.get(curl, headers = {"User-Agent": "Mozilla/5.0"})
    for e in p.json()['members']:
        teamNumber = teamNumber + 1


TeamCount(leagueID)


# function that grabs players from each team, updating the URL and is called by TeamRoster() for each team in the league
def PlayerGrab(givenLeagueID, teamID):
    teamID = teamID
    mrl = f'https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/{givenLeagueID}?forTeamId={teamID}&scoringPeriodId=1&view=mRoster'
    p = requests.get(mrl, headers = {"User-Agent": "Mozilla/5.0"})
    for t in p.json()['teams'][0]['roster']['entries']:
            #print(e['playerPoolEntry']['player']['fullName'])
            rosterPlayer_dict.append(t['playerPoolEntry']['player']['fullName'])
            playerNameinLoop = (t['playerPoolEntry']['player']['fullName'])
            print(playerNameinLoop)


# gets each team name then calles playerGrab to get the players to that team name.
def TeamRoster(givenLeagueID):
    teamID = 1
    while teamID < teamNumber:
        url = f'https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/{givenLeagueID}?view=mSettings&view=mRoster&view=mTeam&view=modular&view=mNav'
        r = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})
        for e in r.json()['members']:
            lastName = (e['lastName'])
            lastName_Print = f'Team {lastName}'
            print(lastName_Print)
            PlayerGrab(givenLeagueID, teamID)
            teamID = teamID + 1

        
#test
            
                    


TeamRoster(leagueID)
#print(rosterPlayer_dict)

"""
TEAM ID CORRESPONDS WITH ORDER ON https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/454981630?view=mSettings&view=mRoster&view=mTeam&view=modular&view=mNav

ROSTER INFORMATION ON EACH INDIVIDUAL TEAM ID IS AT https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/454981630?view=mSettings&view=mRoster&view=mTeam&view=modular&view=mNav

e.g 4th team under members[] has TeamId = 4.

"""