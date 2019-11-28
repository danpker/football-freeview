#!/usr/bin/env /usr/local/bin/python3

import sys

import requests
from bs4 import BeautifulSoup

URL = "https://www.live-footballontv.com/freeview-football-on-tv.html"
data = requests.get(URL)
soup = BeautifulSoup(data.text, features="html.parser")


def parse_fixture_list(limit=100):
    """Load and parse the fixture list."""
    fixtures = {}
    for idx, match_date in enumerate(soup.find_all("div", {"class": "matchdate"})):
        day_fixtures = []
        children = match_date.findParent().next_siblings
        for i in children:
            fixture = i.find_all("div", {"class": "matchfixture"})
            if len(fixture) == 0:
                break

            competition = i.find_all("div", {"class": "competition"})
            kickofftime = i.find_all("div", {"class": "kickofftime"})
            channels = i.find_all("div", {"class": "channels"})

            day_fixtures.append(
                (
                    fixture[0].getText(),
                    competition[0].getText(),
                    kickofftime[0].getText(),
                    channels[0].getText(),
                )
            )
        fixtures[match_date.getText()] = day_fixtures

        if idx > limit:
            break

    return fixtures


def main():
    args = sys.argv

    if len(args) <= 1:
        # No args provided so just do the default behaviour.
        print(parse_fixture_list())
        return

    if args[1] == "bitbar":
        # Being called in BitBar mode, so print a header and limit output.
        print("O")
        print("---")
        all_fixtures = parse_fixture_list(limit=5)
        for day, fixtures in all_fixtures.items():
            print(day)
            for fixture in fixtures:
                print("{} - {} - {} - {}".format(*fixture))
            print("---")


if __name__ == "__main__":
    main()
