#!/usr/bin/env python
"""
Scrape years and offices from the selection form

Output a CSV with a row for each year/office combination

Example:
    python scrape_years_offices_get.py http://localhost:5000/4 > \
    data/years_offices.csv

"""

import csv
import sys

from bs4 import BeautifulSoup
import requests

def fetch_url(url, payload):
    r = requests.get(url, params=payload)
    if r.status_code != 404:
        soup = BeautifulSoup(r.content, 'html.parser')

        # handle jinja error
        if (soup.find("h1").text).find("jinja2") >-1:
            return None, False

        page_list = soup.find("ul", {"class":"pagination"})
        next_page_btn = page_list.find_all('li')[-1]

        if "disabled" in next_page_btn["class"]:
            next_page = False
        else:
            next_page=True

        return r.text, next_page
    else:
        return None, False


if __name__ == '__main__':

    url = sys.argv[1]

    writer = csv.writer(sys.stdout)
    columns = ['year','office']

    writer.writerow(columns)

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    options = soup.find_all('select')

    office_select = soup.find('select', {'id': 'office'})
    offices = [office.text for office in office_select.find_all('option')]

    year_select = soup.find('select', {'id': 'year'})
    years = [year.text for year in year_select.find_all('option')]

    for office in offices:
        for year in years:
            writer.writerow([year, office])