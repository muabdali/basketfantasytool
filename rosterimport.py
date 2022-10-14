# pull player from espn team


import requests
leagueID = 454981630
url = f'https://fantasy.espn.com/apis/v3/games/fba/seasons/2023/segments/0/leagues/{leagueID}?forTeamId=10&scoringPeriodId=1&view=mRoster'
r = requests.get(url, headers = {"User-Agent": "Mozilla/5.0"})


# gets players from json and puts them in a dictionary
def rosterGet():
    for e in r.json()['teams'][0]['roster']['entries']:
        #print(e['playerPoolEntry']['player']['fullName'])
        rosterPlayer_dict.append(e['playerPoolEntry']['player']['fullName'])

# dictionary with all the players from linked team
rosterPlayer_dict=[]

rosterGet()
print(rosterPlayer_dict)