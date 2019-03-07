#!/usr/bin/env python

"""
Parse a single HTML table and output CSV to standard output

Example:
    python fetch_html.py http://127.0.0.1:5000/1 | \
    python parse_single_table.py > data/results.csv

"""

import csv
import sys

from bs4 import BeautifulSoup


if __name__ == "__main__":
    # This implementation is pretty simple, so it's all in the main
    # body of this script. For a more complicated scraper, it's important
    # to break the steps into multiple functions.

    # Create a parser object. We'll read the HTML from standard input.
    soup = BeautifulSoup(sys.stdin, 'html.parser')

    # There's only one table on the page, so it's easy to select it as an
    # object that we can use to traverse the table structure.
    table = soup.find('table')

    # Read the column names from the table header.
    # This could also be implemented more concisely using a list comprehension.
    columns = []
    header_cols = table.find('thead').find_all('th')
    for header_col in header_cols:
        columns.append(header_col.string)

    # Create an object that we'll use to write CSV.
    # We'll write to standard output. If we want to output this to a file, we
    # can just use the shell's redirection.
    writer = csv.writer(sys.stdout)

    # Write the columns as the first row.
    writer.writerow(columns)

    # Read the results from the rest of the table row by row.
    for tr in table.find_all('tr'):
        # Make a list of column values for each row.
        # This could also be implemented more concisely as a list
        # comprehension.
        row = []
        for td in tr.find_all('td'):
            row.append(td.string)

        writer.writerow(row)
