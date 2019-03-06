#!/usr/bin/env python

"""
Parse a page with multiple HTML tables and output CSV to standard output

Example:

    python fetch_html.py http://localhost:5000/2 | \
    python parse_multiple_tables.py > data/results.csv

"""

import csv
import sys

from bs4 import BeautifulSoup


if __name__ == "__main__":

    # Just like last time around, we'll get the html we fetched
    # and create a parser object
    soup = BeautifulSoup(sys.stdin, 'html.parser')

    # If we're going to scrape all these tables into one file, 
    # we'll need to keep track of which table each row came from. 
    # Let's put in a first column called "Office".
    columns = ["Office"]

    # This is the same thing we did in the single table file — 
    # they all have the same header row, so we only need to grab
    # the column names
    header_cols = soup.find("table").find('thead').find_all('th')
    for header_col in header_cols:
        columns.append(header_col.string)

    writer = csv.writer(sys.stdout)
    writer.writerow(columns)

    # FILL IN THE BLANK: Find each header on this table, and create 
    # a for loop that iterates through them and grabs the name of 
    # the office. Save it to the variable "office".

    
    # FILL IN THE BLANK: Now you can find each table and parse it
    # like you did with just one table. Within the same for loop, 
    # find the table immediately after each header.
    # 
    # (Hint: See what find_next() does)



    # Now, just iterate through those table rows like you did in 
    # the last script. We're starting that list for each row with
    # the office variable we set before. Write the whole thing to 
    # a file.
        for tr in table.find_all('tr'):
            row = [office]
            for td in tr.find_all('td'):
                row.append(td.string)

            row.insert(0, office)
            writer.writerow(row)

