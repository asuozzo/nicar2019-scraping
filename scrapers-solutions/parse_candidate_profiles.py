#!/usr/bin/env python

"""Parse an HTML table and follow links. Output CSV to standard output"""

import csv
import sys

import requests
from bs4 import BeautifulSoup

def fetch_profile(url):
    r = requests.get(url)
    
    # make sure to check whether the page returned is a 404
    if r.status_code != 404:
        soup = BeautifulSoup(r.content, 'html.parser')
        bio = soup.find("p", {"class": "bio"})
        funds_raised = bio.find_next("p").text
        funds_raised = funds_raised[funds_raised.find("$")+1:]
        return [bio.text,funds_raised]
    
    # if it is a 404, return a list of blank values
    else:
        return [None, None]

def get_row_data(tr):
    row = []
    candidate_info = []
    for td in tr.find_all('td'):
        
        # if there's a link in the cell, get the 
        # cell's text, then follow the link
        if td.find("a"):
            row.append(td.string)
            link = td.find("a")["href"]
            candidate_info = fetch_profile(
                "http://localhost:5000" + link
                )
        
        else:
            row.append(td.string)
    
    # make sure the row isn't empty
    if len(row)>0:
        
        # add office name to the beginning of the row, 
        # then add candidate bio info to the end
        row.insert(0, office)
        row = row + candidate_info
        return row


if __name__ == "__main__":

    soup = BeautifulSoup(sys.stdin, 'html.parser')

    # find the office name and table on the page
    office = soup.find("h2").text
    table = soup.find("table")

    columns = ["Office"]
    header_cols = soup.find("table").find('thead').find_all('th')
    for header_col in header_cols:
        columns.append(header_col.string)    
    
    # these columns are where we'll put our candidate 
    # profile info
    columns.extend(["Bio", "Funds Raised"])

    writer = csv.writer(sys.stdout)
    writer.writerow(columns)
    
    # for each row in table, grab candidate info
    for tr in table.find_all('tr'):
        row = get_row_data(tr)
        if row:
            writer.writerow(row)
