import requests
from bs4 import BeautifulSoup

# Make a request to the website

abbv_nameMatch = {
    "Toronto":"TOR",
    "Miami":"MIA",
    'Denver':"DEN",
    "Brooklyn" : "BKN",
    "Memphis": "MEM",
    'Dallas':"DAL",
    "Cleveland":"CLE",
    "Atlanta":"ATL",
    "Minnisota":"MIN"

    }

def defineTeamCat():
    global top_teams, middle_teams, bottom_teams
    url = "https://www.cbssports.com/nba/powerrankings/"
    page = requests.get(url)

    # Parse the HTML of the page
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find all the elements with the class "teamname"
    teamname_elements = soup.find_all(class_="team-name")
    teamNamesList = []
    top_teams = []
    middle_teams = []
    bottom_teams = []


    # Print the text of each element
    for element in teamname_elements:
        teamName_text = element.get_text()
        teamName_text = teamName_text.strip()
        teamNamesList.append(teamName_text)



    top_teams = teamNamesList[:8]
    middle_teams = teamNamesList[8:16]
    bottom_teams = teamNamesList[16:29]
    return top_teams,middle_teams,bottom_teams

defineTeamCat()


def turnToAbbv(top, mid, bot):
    list_of_teams = [top,mid,bot]
    for team_list in list_of_teams:
        for element in team_list:
