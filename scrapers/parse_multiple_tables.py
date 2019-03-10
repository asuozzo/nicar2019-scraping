#!/usr/bin/env python

"""
Parse a page with multiple HTML tables and output CSV to standard output

Example:

    python ./scrapers/fetch_html.py http://127.0.0.1:5000/2 | \
    python ./scrapers/parse_multiple_tables.py > data/results.csv

"""

import csv
import sys

from bs4 import BeautifulSoup


if __name__ == "__main__":

    # Just like last time around, we'll get the html we fetched
    # and create a parser object
    soup = BeautifulSoup(sys.stdin, 'html.parser')

    # This is the same thing we did in the single table file — 
    # they all have the same header row, so we only need to grab
    # the column names
    columns = []
    header_cols = soup.find("table").find('thead').find_all('th')
    for header_col in header_cols:
        columns.append(header_col.string)

    # If we're going to scrape all these tables into one file, 
    # we'll need to keep track of which table each row came from. 
    # Let's put in a column called "Office".
    columns.append("Office")

    # UNCOMMENT THESE ROWS when you're ready to write the csv.
    # writer = csv.writer(sys.stdout)
    # writer.writerow(columns)

    # FILL IN THE BLANK: Loop through each header on this table
    # and create a variable "office". Save the header value to
    # that variable.

    
    # FILL IN THE BLANK: Now you can find each table and parse it
    # like you did with just one table. Within the same for loop, 
    # find the table immediately after each header.
    # 
    # (Hint: What does the Beautiful Soup command find_next() do?)



    # FILL IN THE BLANK: Now, iterate through those table rows
    # like you did in the last script. Add the variable "office"
    # to the end of your row, then write the whole thing to 
    # a file.