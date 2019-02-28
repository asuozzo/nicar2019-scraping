#!/usr/bin/env python

"""Parse an HTML table and follow links. Output CSV to standard output"""

import csv
import sys

from bs4 import BeautifulSoup

def fetch_profile(url):
    pass
    # request - check for 404
    # if not 404, then soup
    # return list of components
    # [description, funds raised]

if __name__ == "__main__":

    soup = BeautifulSoup(sys.stdin, 'html.parser')

    # find the office name and table on the page
    office = soup.find("h2").text
    table = soup.find("table")

    columns = []
    
    # for each row in table:
    # fetch description and funds from url
    # write column names with description and funds
    # write each row to stdout
