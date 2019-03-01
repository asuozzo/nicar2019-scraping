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
    # so we can't just look for the table element.

    # First, grab the headers from the first table for column names.
    # since we're pulling multiple tables into one document, we'll 
    # also want to add a first column to note which office each 
    # candidate was running for.
    columns = ["Office"]
    header_cols = soup.find("table").find('thead').find_all('th')
    for header_col in header_cols:
        columns.append(header_col.string)

    writer = csv.writer(sys.stdout)
    # Write those columns to a csv.
    writer.writerow(columns)

    # Let's first find each header, and then save the text to 
    # the "office" variable.
    for header in soup.find_all("h2"):
        office = header.text

    # Then find the table after the header and loop through 
    # its rows. We've done this step before!
        table = header.find_next("table")
        for tr in table.find_all('tr'):
            row = []
            for td in tr.find_all('td'):
                row.append(td.string)
            
    # ignore blank rows
            if len(row)>0:
    
    # add the name of the office to the beginning of the row.
                row.insert(0, office)
                writer.writerow(row)