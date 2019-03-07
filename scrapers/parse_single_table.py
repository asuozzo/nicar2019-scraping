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

    # FILL IN THE BLANK: Create a Beautiful Soup object 
    # from standard input (sys.stdin)


    # FILL IN THE BLANK: There's only one table on this 
    # page. Find it.



    columns = []
    # FILL IN THE BLANK: Next, we want to fill this list 
    # with column names from the table. Check it out in the 
    # page source. Is there a way to select each column's name?


    # Here, we'll create a csv writer that writes to standard
    # output. This writes output to the terminal unless we 
    # redirect the output to a filename. 
    # That way, we can pass in lists (like our list of columns) 
    # with writer.writerow(LIST) to add new rows to the file.
    
    # UNCOMMENT THESE ROWS when you're ready to write the csv.
    # writer = csv.writer(sys.stdout)
    # writer.writerow(columns)


    # FILL IN THE BLANK: Write a "for" loop that goes through 
    # each table row and writes each cell value to a list. 
    # Then use "writer.writerow()" to write that list to a file.

