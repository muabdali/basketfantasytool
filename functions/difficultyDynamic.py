import requests
from bs4 import BeautifulSoup

# Make a request to the website
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
    print(teamName_text)


