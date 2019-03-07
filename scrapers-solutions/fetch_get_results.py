#!/usr/bin/env python

"""
Fetches HTML results for all form combinations.

Example:
    python fetch_get_results.py http://127.0.0.1:5000/4 data/years_offices.csv \
    data/src
"""

import csv
import os
import sys

import requests
from bs4 import BeautifulSoup

def get_output_filename(year, office, page):
    """Returns a normalized filename for the results HTML."""
    office_slug = office.lower().replace(' ', '_')
    return '{0}__{1}__{2}.html'.format(year, office_slug, page)


def fetch_results_html(url, year, office, page):
    payload = {
        'year':year,
        'office':office,
        'page':page
    }
    
    r = requests.get(url, params=payload)

    if r.status_code != 404:
        soup = BeautifulSoup(r.text, 'html.parser')

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
    return None, False

if __name__ == '__main__':

    base_url = sys.argv[1]
    years_offices_csv_path = sys.argv[2]
    output_dir = sys.argv[3]

    with open(years_offices_csv_path) as f:
        reader = csv.DictReader(f)

        for row in reader:
            next_page = True
            page = 1

            while next_page:
                
                output_filename = get_output_filename(row['year'], row['office'], page)
                
                output_path = os.path.join(output_dir, output_filename)
                next_page = False

                if os.path.exists(output_path):
                    page += 1
                    continue

                results_html, next_page = fetch_results_html(base_url, row['year'], row['office'], page)

                if results_html:
                    with open(output_path, 'w') as fout:
                        fout.write(results_html)
               
                page += 1