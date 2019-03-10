#!/usr/bin/env python
"""
Scrape years and offices from the selection form

Output a CSV with a row for each year/office combination

Example:
    ./scrapers-solutions/scrape_years_offices_get.py http://127.0.0.1:5000/4 > \
    data/years_offices.csv

"""

import csv
import sys

from bs4 import BeautifulSoup
import requests


def get_election_years(soup):
    """
    Returns a list of election years available in a results form.

    Args:
        soup: BeautifulSoup object representing the HTML of a web page that
            includes a form for selecting an election year and office for
            which to retrieve results.

    """
    years = []

    # FILL IN THE BLANK: Scrape the years from the form.
    year_select = soup.find('select', {'id': 'year'})
    years = [year.text for year in year_select.find_all('option')]

    return years


def get_offices(soup):
    """
    Returns a list of offices available in a results form.

    Args:
        soup: BeautifulSoup object representing the HTML of a web page that
            includes a form for selecting an election year and office for
            which to retrieve results.

    """
    offices = []

    # FILL IN THE BLANK: Scrape the offices from the form.
    office_select = soup.find('select', {'id': 'office'})
    offices = [office.text for office in office_select.find_all('option')]

    return offices


if __name__ == '__main__':
    url = sys.argv[1]

    writer = csv.writer(sys.stdout)
    columns = ['year','office']

    writer.writerow(columns)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    offices = get_offices(soup)
    years = get_election_years(soup)

    for office in offices:
        for year in years:
            writer.writerow([year, office])
