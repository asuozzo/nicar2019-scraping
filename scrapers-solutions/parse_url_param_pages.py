#!/usr/bin/env python

"""Open each year/office result file and write info to csv"""

import csv
import sys
from glob import glob

from bs4 import BeautifulSoup


if __name__ == '__main__':

    param_files = glob("output/params_*.html")

    columns = ["Year", "Office", "Candidate", "Party", "Votes"]

    writer = csv.writer(open("output/params_results.csv", "w"))
    writer.writerow(columns)

    for param_file in param_files:
        filename_list = param_file.split("_")
        year = filename_list[1]
        office = filename_list[2]

        soup = BeautifulSoup(open(param_file), 'html.parser')

        table = soup.find('table')
        for tr in table.find_all('tr'):
            row = []
            for td in tr.find_all('td'):
                row.append(td.string)
            if len(row) > 0:
                row = [year, office] + row
                writer.writerow(row)


