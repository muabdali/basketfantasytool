
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.basketball-reference.com/players/a/achiupr01.html').text

soup = BeautifulSoup(source, 'lxml')
tbody = soup.find('tbody')
pergame = tbody.find(class_="full_table")
classrite = pergame.find(class_="right")



data = input("what data")

find = classrite.get("datastat=" + data
                     )
first=()

last=()

def askname():
    global first
    first = input(str("First Name of Player?"))
    global last
    last = input(str("Last Name of Player?"))
    print("Confirmed, loading up " + first + " " + last)


# end