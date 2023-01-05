import requests
from bs4 import BeautifulSoup

# Make a request to the website


abbv_nameMatch = {
    "Hawks": "ATL",
    "Celtics": "BOS",
    "Nets": "BKN",
    "Hornets": "CHA",
    "Bulls": "CHI",
    "Cavaliers": "CLE",
    "Mavericks": "DAL",
    "Nuggets": "DEN",
    "Pistons": "DET",
    "Warriors": "GSW",
    "Rockets": "HOU",
    "Pacers": "IND",
    "Clippers": "LAC",
    "Lakers": "LAL",
    "Grizzlies": "MEM",
    "Heat": "MIA",
    "Bucks": "MIL",
    "Timberwolves": "MIN",
    "Pelicans": "NOP",
    "Knicks": "NYK",
    "Thunder": "OKC",
    "Magic": "ORL",
    "76ers": "PHI",
    "Suns": "PHX",
    "Trail Blazers": "POR",
    "Kings": "SAC",
    "Spurs": "SAS",
    "Raptors": "TOR",
    "Jazz": "UTA",
    "Wizards": "WAS"
}


def defineTeamCat():
    global one_teams,two_teams,three_teams
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



    one_teams = teamNamesList[:8]
    two_teams = teamNamesList[8:16]
    three_teams = teamNamesList[16:29]
    return one_teams,two_teams,three_teams

defineTeamCat()


"""
This creates three new lists using list comprehensions, which iterate over the items in one,two and three_teams and look up the corresponding abbreviation
 in the dictionary using the team name as a key. The resulting lists contain the abbreviations for each team, in the same order as the teams in the original lists.
"""

def turntoAbbv(top, middle, bottom):
    global top_teams,middle_teams,bottom_teams
    all_Lists = [top, middle, bottom]
    top_teams = [abbv_nameMatch[team] for team in top]
    middle_teams = [abbv_nameMatch[team] for team in middle]
    bottom_teams = [abbv_nameMatch[team] for team in bottom]

    return top_teams, middle_teams, bottom_teams


turntoAbbv(one_teams,two_teams,three_teams)

