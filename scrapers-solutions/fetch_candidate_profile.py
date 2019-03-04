#!/usr/bin/env python
"""
Fetch HTML from all candidate profile urls and write info to csv
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

    results = csv.DictReader(open("output/results.csv", "r"))

    for result in results:
        html = fetch_url(result["Link"])
        if html:
            filename = "output/candidate_{0}.html".format(result["Candidate"])
            with open(filename, "w") as f:
                f.write(html)