#!/usr/bin/env /usr/local/bin/python3

import sys

import requests
from bs4 import BeautifulSoup

URL = "https://www.live-footballontv.com/freeview-football-on-tv.html"
data = requests.get(URL)
soup = BeautifulSoup(data.text, features="html.parser")


def print_data(limit=100):
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

        if idx > limit:
            break


def main():
    args = sys.argv

    if len(args) <= 1:
        # No args provided so just do the default behaviour.
        print_data()
        return

    if args[1] == "bitbar":
        # Being called in BitBar mode, so print a header and limit output.
        print("F")
        print("---")
        print_data(limit=5)

if __name__ == "__main__":
    main()
