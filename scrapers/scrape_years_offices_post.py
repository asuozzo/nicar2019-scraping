#!/usr/bin/env python

"""
Scrape years and offices from the multi-step results form.

Outputs a CSV with one year/office pair per row.

Example:
    ./scrapers-solutions/scrape_years_offices_post.py http://127.0.0.1:5000/5

"""

import csv
import sys

from bs4 import BeautifulSoup
import requests


def scrape_years(url):
    """Returns list of years scraped from the form."""
    years = []
    
    # FILL IN THE BLANK: Load the first page, create a 
    # soup object and get the list of years from the 
    # option menu.


    return years

def scrape_offices(url, year):
    """Returns list of offices scraped from the form."""
    offices = []
    
    # FILL IN THE BLANK: Request the second page of the 
    # form and scrape the list of offices.



    return offices


if __name__ == '__main__':
    # We're going to get the same dropdown data from this 
    # form as we did on the last page we scraped. Because
    # of the way this form retrieves data, though, we're 
    # going to have to break it into a couple steps.
    start_url = sys.argv[1]

    writer = csv.writer(sys.stdout)
    columns = ['year', 'office']

    writer.writerow(columns)

    # First, pass the url to the main page of the form
    years = scrape_years(start_url)

    for year in years:
        # Submit the form for each year to get the lists of offices from the
        # second form.
        offices = scrape_offices(start_url, year)

        for office in offices:
            writer.writerow([year, office])