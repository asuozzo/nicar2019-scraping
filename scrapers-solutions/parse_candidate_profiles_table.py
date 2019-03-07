#!/usr/bin/env python

"""
Parse an HTML table with links. Output CSV to standard output

Example:
    python parse_candidate_profiles_table.py http://127.0.0.1:5000 \
    data/src/profiles_main.html > data/results.csv

"""

import csv
import sys

from bs4 import BeautifulSoup


if __name__ == '__main__':

    url = sys.argv[1]
    soup = BeautifulSoup(open(sys.argv[2]), 'html.parser')

    # find the office name and table on the page
    office = soup.find('h2').text
    table = soup.find('table')

    columns = ["Office"]
    header_cols = soup.find('table').find('thead').find_all('th')
    for header_col in header_cols:
        columns.append(header_col.string)
    columns.append("Link")

    writer = csv.writer(sys.stdout)
    writer.writerow(columns)

    for tr in table.find_all('tr'):
        row = []
        link = None
        for td in tr.find_all('td'):

        # if there's a link in the cell, get the
        # cell's text, then format the link
            if td.find('a'):
                row.append(td.string)
                link = td.find('a')['href']
                link = '{0}{1}'.format(url,link)
            else:
                row.append(td.string)

        # make sure the row isn't empty
        if len(row)>0:
            row.append(link)
            row.insert(0, office)
            writer.writerow(row)