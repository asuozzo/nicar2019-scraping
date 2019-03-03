#!/usr/bin/env python

"""Open each candidate profile file and write info to csv"""

import csv
import sys
from glob import glob

from bs4 import BeautifulSoup


if __name__ == '__main__':

    profile_files = glob("output/candidate_*.html")

    columns = ["Candidate","Funds Raised","Bio"]

    writer = csv.writer(open("output/candidate_bios.csv", "w"))
    writer.writerow(columns)

    for profile_file in profile_files:
        candidate = profile_file.split("_")[1][:-5]

        soup = BeautifulSoup(open(profile_file), 'html.parser')

        bio = soup.find('p', {'class': 'bio'})
        funds_raised = bio.find_next('p').text
        funds_raised = funds_raised[funds_raised.find('$') + 1:]
        bio = bio.text

        writer.writerow([candidate, funds_raised, bio])






