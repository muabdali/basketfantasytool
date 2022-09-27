from bs4 import BeautifulSoup
import requests

first = ()
first_slice = ()
last = ()


def askname():
    global first
    first = input(str("First Name of Player?"))
    global last
    last = input(str("Last Name of Player?"))
    print("Confirmed, loading up " + first + " " + last)
# asks user for player name

askname()

first_slice_result = (first[:2])
last_slice_result = (last[:5])
print(first_slice_result)
print(last_slice_result)
# slices player's name so it can match the format bref uses
first_slice_resultA = str(first_slice_result)
last_slice_resultA = str(last_slice_result)

first_last_slice = last_slice_resultA + first_slice_resultA

lower = first_last_slice.lower() + "01"

start_letter = (last[:1])
lower_letter = (start_letter.lower())
# grabs the letter bref uses for organization

print(lower)
source = requests.get('https://www.basketball-reference.com/players/' + lower_letter + '/' + lower + '.html').text

soup = BeautifulSoup(source, 'lxml')
tbody = soup.find('tbody')
pergame = tbody.find(class_="full_table")
classrite = tbody.find(class_="right")
tr_body = tbody.find_all('tr')
# lprint(pergame)

'''
# seperates data-stat, apparently you can use .get to get obscure classes
for trb in tr_body:
    print(trb.get('id'))

    th = trb.find('th')
    print(th.get_text())
    print(th.get('data-stat'))
'''
"""
    for td in trb.find_all('td'):
        print(td.get_text())
        print(td.get('data-stat'))
    
"""

for td in tbody:
    print(td.get_text)

print("done")

get = str(input("What stat?"))

for trb in tr_body:
    print(trb.get('id'))
    print("\n")

    th = trb.find('th')
    print(th.get_text())
    print(th.get('data-stat'))

    row = {}
    for td in trb.find_all('td'):
        row[td.get('data-stat')] = td.get_text()

    print(row[get])