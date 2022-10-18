# pull player from espn team


import requests
leagueID = 454981630
teamID = 1


def teamNget(givenLeagueID):
    url = f'https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/{givenLeagueID}?view=mSettings&view=mRoster&view=mTeam&view=modular&view=mNav'
    r = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})
    for e in r.json()['members']:
        lastName = (e['lastName'])
        lastName_Print = f'Team {lastName}'
        rosterTeam_dict.append(e['lastName'])

# gets players from json and puts them in a dictionary
def rosterGet(givenLeagueID, givenTeamID):
    url = f'https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/{givenLeagueID}?forTeamId={givenTeamID}&scoringPeriodId=1&view=mRoster'
    r = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})
    for e in r.json()['teams'][0]['roster']['entries']:
        #print(e['playerPoolEntry']['player']['fullName'])
        rosterPlayer_dict.append(e['playerPoolEntry']['player']['fullName'])
# dictionary with all the players from linked team
rosterPlayer_dict=[]
rosterTeam_dict=[]
teamNget(leagueID)
rosterGet(leagueID, teamID)
print(rosterTeam_dict)








"""
TEAM ID CORRESPONDS WITH ORDER ON https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/454981630?view=mSettings&view=mRoster&view=mTeam&view=modular&view=mNav

ROSTER INFORMATION ON EACH INDIVIDUAL TEAM ID IS AT https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/454981630?view=mSettings&view=mRoster&view=mTeam&view=modular&view=mNav

e.g 4th team under members[] has TeamId = 4.

"""