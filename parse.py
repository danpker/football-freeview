#!/usr/bin/env LC_ALL=en_US.UTF-8 /usr/local/bin/python3

import requests
from bs4 import BeautifulSoup

URL = "https://www.live-footballontv.com/freeview-football-on-tv.html"
data = requests.get(URL)
soup = BeautifulSoup(data.text, features="html.parser")

print("F")
print("---")
for idx, match_date in enumerate(soup.find_all("div", {"class": "matchdate"})):
    print(match_date.getText())
    children = match_date.findParent().next_siblings
    for i in children:
        fixture = i.find_all("div", {"class": "matchfixture"})
        if len(fixture) == 0:
            break

        competition = i.find_all("div", {"class": "competition"})
        kickofftime = i.find_all("div", {"class": "kickofftime"})
        channels = i.find_all("div", {"class": "channels"})
        print("{} - {} - {} - {}".format(
            fixture[0].getText(),
            competition[0].getText(),
            kickofftime[0].getText(),
            channels[0].getText(),
        ))
    print("---")

    if idx > 5:
        break
