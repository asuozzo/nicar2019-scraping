#!/usr/bin/env python

"""
Scrape years and offices from the multi-step results form.

Outputs a CSV with one year/office pair per row.

Example:
    ./scrapers-solutions/scrape_years_offices.py http://127.0.0.1:5000/5

"""

import csv
import sys

from bs4 import BeautifulSoup
import requests


def scrape_years(url):
    """Returns list of years scraped from the form."""

    r = requests.get(start_url)

    soup = BeautifulSoup(r.text, 'html.parser')

    form = soup.select_one('form')
    year_select = form.select_one('select#year')

    years = [opt.text for opt in year_select.select('option')]

    return years


def scrape_offices(url, year):
    """Returns list of offices scraped from the form."""

    data = {'year': year}

    r = requests.post(url, data=data)

    soup = BeautifulSoup(r.text, 'html.parser')

    form = soup.select_one('form')
    office_select = form.select_one('select#office')

    offices = [opt.text for opt in office_select.select('option')]

    return offices


if __name__ == '__main__':
    # This program takes one positional argument, the URL of the initial
    # results form with the year select element.
    start_url = sys.argv[1]

    writer = csv.writer(sys.stdout)
    columns = ['year', 'office']

    writer.writerow(columns)

    # Scrape the years from the initial form.
    years = scrape_years(start_url)

    for year in years:
        # Submit the form for each year to get the lists of offices from the
        # second form.
        offices = scrape_offices(start_url, year)
        for office in offices:
            # Then, output the years and offices for each form.
            writer.writerow([year, office])
