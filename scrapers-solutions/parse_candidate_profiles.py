#!/usr/bin/env python

"""
Open each candidate profile file and write info to csv

Example:
    python parse_candidate_profiles.py data/src/profiles_candidate_*.html > \
    data/profiles.csv

"""

import csv
import sys

from bs4 import BeautifulSoup

def parse_html(f):

    soup = BeautifulSoup(open(f), 'html.parser')

    bio = soup.find('p', {'class': 'bio'})
    funds_raised = bio.find_next('p').text
    funds_raised = funds_raised[funds_raised.find('$') + 1:]
    bio = bio.text

    return [funds_raised, bio]


if __name__ == '__main__':

    profile_files = sys.argv[1:]

    columns = ["Candidate","Funds Raised","Bio"]

    writer = csv.writer(sys.stdout)
    writer.writerow(columns)

    for profile_file in profile_files:
        candidate = profile_file.split("_")[2][:-5]

        candidate_data = parse_html(profile_file)
        candidate_data.insert(0,candidate)

        writer.writerow(candidate_data)






