#!/usr/bin/env python
"""
Fetch HTML from all candidate profile urls and write to local HTML

Example:
    python fetch_candidate_profiles.py data/results.csv data/src

"""

import sys
import csv
import requests

def fetch_url(url):
    r = requests.get(url)
    if r.status_code != 404:
        return r.text
    else:
        return None


if __name__ == '__main__':

    output_dir = sys.argv[2]

    results = csv.DictReader(open(sys.argv[1], "r"))

    for result in results:
        html = fetch_url(result["Link"])
        if html:
            filename = "{0}/profiles_candidate_{1}.html".format(output_dir, result["Candidate"])
            with open(filename, "w") as f:
                f.write(html)