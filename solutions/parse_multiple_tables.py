#!/usr/bin/env python

"""Parse a page with multiple HTML tables and output CSV to standard output"""

import csv
import sys

from bs4 import BeautifulSoup


if __name__ == "__main__":

    # Just like last time around, we'll get the html we fetched
    # and create a parser object
    soup = BeautifulSoup(sys.stdin, 'html.parser')

    # This time, though, we've got a page with multiple tables,
    # so we can't just look for the table element. Instead,
    # let's look specifically for the table header we want
    # (Representative to Congress) and find the next table
    # element on the page.
    header = soup.find("h2", text="Representative To Congress")
    table = header.find_next("table")

    # Now that we've got our table, it's all stuff we already know.
    # First, grab the headers.
    columns = []
    header_cols = table.find('thead').find_all('th')
    for header_col in header_cols:
        columns.append(header_col.string)

    # Then write everything to a csv.
    writer = csv.writer(sys.stdout)
    writer.writerow(columns)

    for tr in table.find_all('tr'):
        row = []
        for td in tr.find_all('td'):
            row.append(td.string)

        writer.writerow(row)