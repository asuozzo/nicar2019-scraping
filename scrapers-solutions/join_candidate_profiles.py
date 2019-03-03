#!/usr/bin/env python

"""Join results file with candidate profiles file"""

import csv

if __name__ == '__main__':

    resultscsv = csv.reader(open("output/results.csv", "r"))
    profilescsv = csv.reader(open("output/candidate_bios.csv", "r"))

    # skip header row on both files
    next(resultscsv, None)
    next(profilescsv, None)

    # read the profiles into a list so we can loop through multiple times
    profiles = list(profilescsv)

    columns = ["Office", "Candidate", "Party", "Votes", "Funds Raised", "Bio"]
    joinfile = csv.writer(open("output/results_w_bios.csv", "w"))
    joinfile.writerow(columns)

    for result in resultscsv:
        row = result[0:4]
        for profile in profiles:
            if result[1] == profile[0]:
                row = row + profile[1:]
        joinfile.writerow(row)



