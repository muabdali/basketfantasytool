import requests
from bs4 import BeautifulSoup

# Make a request to the website



def defineTeamCat():
    url = "https://www.cbssports.com/nba/powerrankings/"
    page = requests.get(url)

    # Parse the HTML of the page
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find all the elements with the class "teamname"
    teamname_elements = soup.find_all(class_="team-name")
    teamNamesList = []


    # Print the text of each element
    for element in teamname_elements:
        teamName_text = element.get_text()
        teamNamesList.append(teamName_text)



    top_teams = teamNamesList[:8]
    middle_teams = teamNamesList[8:16]
    bottom_teams = teamNamesList[16:29]
    return bottom_teams,top_teams,middle_teams


defineTeamCat()
