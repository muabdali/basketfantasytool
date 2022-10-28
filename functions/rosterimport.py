# pull player from espn team

from fileinput import filename
import json
from discord import Team
import requests
from settingsImport import importSettings
from playerTeamlists import teamListReset 

path = './'
fileName = 'members'
leagueID = 454981630


teamListDict = {
    'Team1': 0,
    'Team2':0,
    'Team3':0,
    'Team4':0,
    'Team5':0,
    'Team6':0,
    'Team7':0,
    'Team8':0,
    'Team9':0,
    'Team10': 0
}   

#teamListReset()
# dictionary that only holds player names
rosterPlayer_list=[]
# function to count teams
# teamNumber is amount of teams
def TeamCount(givenLeagueID):
    global teamNumber
    teamNumber = 0
    curl = f'https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/{givenLeagueID}?view=mSettings&view=mRoster&view=mTeam&view=modular&view=mNav'
    p = requests.get(curl, headers = {"User-Agent": "Mozilla/5.0"})
    for e in p.json()['members']:
        teamNumber = teamNumber + 1

'''
STAT ID LEGEND

Rebound = statID : 6
Turnover = statID : 11
Field Goal Made = statID : 13
Field Goal Attempted = statID : 14
3 Point Made = statID : 15
Free Throw Missed = statID : 16
Point = statID : 0
Free Throw made = statID : 17
Steal = statID : 1
Block = statID : 2
Assist = statID : 3

'''


# assigns corresponding order on json as a value to the firstName + lastName as the key and stores it in a dictionary
def teamNamed(givenLeagueID):
    global teamNamedict
    url = f'https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/{givenLeagueID}?view=mSettings&view=mRoster&view=mTeam&view=modular&view=mNav'
    r = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})
    teamAssignCount = 0
    # leave empty to start
    teamNamedict = {
     
    }    
    for t in r.json()['members']:
        firstName = t['firstName']
        lastName = t['lastName']
        playerName = f'{firstName} {lastName}'
        teamNamedict[playerName] = teamAssignCount
        teamAssignCount = teamAssignCount + 1
    
    
    return


teamNamed(leagueID)

#counts amount of players so that PlayerGrab() has the right amount of loops to do
def playerCount(givenLeagueID, teamID):
    global numOfPlayers
    numOfPlayers = 0
    teamID = teamID
    mrl = f'https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/{givenLeagueID}?forTeamId={teamID}&scoringPeriodId=1&view=mRoster'
    p = requests.get(mrl, headers = {"User-Agent": "Mozilla/5.0"})
    for t in p.json()['teams'][0]['roster']['entries']:
        numOfPlayers = numOfPlayers + 1
    return(numOfPlayers)

# accesses scoringItems and returns values. All the point values are hidden under a dataID system. See line 30 or statID.md for more info.

# function that grabs players from each team, updating the URL and is called by TeamRoster() for each team in the league
def PlayerGrab(givenLeagueID, teamID):
    numOfPlayer_Count = 0
    teamID = teamID
    mrl = f'https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/{givenLeagueID}?forTeamId={teamID}&scoringPeriodId=1&view=mRoster'
    p = requests.get(mrl, headers = {"User-Agent": "Mozilla/5.0"})
    playerCount(givenLeagueID, teamID)
    for t in p.json()['teams'][0]['roster']['entries']:
            rosterPlayer_list.append(t['playerPoolEntry']['player']['fullName'])
            playerNameinLoop = (t['playerPoolEntry']['player']['fullName'])
            numOfPlayer_Count = numOfPlayer_Count + 1
            if numOfPlayer_Count == numOfPlayers:
                currentPlayerlist = rosterPlayer_list
                finallistNumber = (f'Team{teamID}')
                teamListDict[finallistNumber] = currentPlayerlist
                print(teamListDict[finallistNumber])
                rosterPlayer_list.clear()


# gets each team name then calles playerGrab to get the players to that team name.
def TeamRoster(givenLeagueID):
    global lastName_Print
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

        

def mainFunction(givenLeagueID):
    importSettings(givenLeagueID)
    TeamCount(givenLeagueID)
    TeamRoster(givenLeagueID)
    print("All Done")
    return

mainFunction(leagueID)




"""
TEAM ID CORRESPONDS WITH ORDER ON https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/454981630?view=mSettings&view=mRoster&view=mTeam&view=modular&view=mNav

ROSTER INFORMATION ON EACH INDIVIDUAL TEAM ID IS AT https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/454981630?view=mSettings&view=mRoster&view=mTeam&view=modular&view=mNav

e.g 4th team under members[] has TeamId = 4.

"""