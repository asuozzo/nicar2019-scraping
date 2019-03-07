#!/usr/bin/env python

"""
Join results file with candidate profiles file

Example:

    python join_results_candidate_profiles.py data/results.csv \
    data/profiles.csv > data/results_with_profile.csv

"""

import csv
import sys

if __name__ == '__main__':

    resultscsv = csv.reader(open(sys.argv[1], "r"))
    profilescsv = csv.reader(open(sys.argv[2], "r"))

    # skip header row on both files
    next(resultscsv, None)
    next(profilescsv, None)

    # read the profiles into a list so we can loop through multiple times
    profiles = list(profilescsv)

    columns = ["Office", "Candidate", "Party", "Votes", "Funds Raised", "Bio"]
    joinfile = csv.writer(sys.stdout)
    joinfile.writerow(columns)

    for result in resultscsv:
        row = result[0:4]
        for profile in profiles:
            if (result[1] == profile[0]) and (len(row))<6:
                row = row + profile[1:]
        joinfile.writerow(row)
