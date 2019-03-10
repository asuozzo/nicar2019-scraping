#!/usr/bin/env python

"""
Fetches HTML results for all form combinations.

Example:
    python ./scrapers/fetch_get_results.py http://127.0.0.1:5000/4 data/years_offices.csv \
    data/src
"""

import csv
import os
import re
import sys

import requests
from bs4 import BeautifulSoup


def get_output_filename(year, office, page):
    """Returns a normalized filename for the results HTML."""
    office_slug = office.strip().lower()
    office_slug = re.sub(r'[^\w\s]', '', office_slug)
    office_slug = re.sub(r'\s+', '_', office_slug)

    page_numeric = int(page)

    # We zero pad the page number in case there are many pages so the
    # filenames will be ordered. Otherwise page 10 would come before page
    # 2 when viewing files in our file explorer or listing them using `ls`.
    return '{0}__{1}__{2:03d}.html'.format(year, office_slug, page_numeric)


def submit_form(url, year, office, page):
    """
    Mimics a results form submission.

    Returns a `requests.Response` object for that request..
    """
    # FILL IN THE BLANK: Use `requests.get()` tommimic a form submission by
    # retrieving the form submission URL with the appropriate URL parameters.

    return None


def verify_response(r):
    """
    Returns True if the response succeeded.

    Raises:
        ValueError: Raises a ValueError if the request failed.

    """
    # FILL IN THE BLANK: Check that the form submission succeeded and if
    # it did, return `True`.
 
    if r is None:
        raise ValueError("Not a response object")

    msg = "Results could not be retrieved for URL {0}".format(r.url)
    raise ValueError(msg)


def has_next_page(soup):
    """
    Returns True if there appears to be additional pages of results

    Args:
        soup: Beautiful Soup object representing the HTML of a page of
            results that contains a pager control.

    """
    # FILL IN THE BLANK: Use Beautiful Soup to inspect the HTML to determine if
    # there is another page of results.
    
    return False


def fetch_results_html(url, year, office, page):
    """
    Returns a tuple of results HTML and whether there is another page.

    Args:
        url: URL of form that returns results.
        year: Election year for which to retrieve results.
        office: Office for which to retrieve results.
        page: page of results.

    Raises:
        ValueError: Raises a ValueError if the request failed.

    """
    r = submit_form(url, year, office, page)

    verify_response(r)

    soup = BeautifulSoup(r.text, 'html.parser')

    return r.text, has_next_page(soup)


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

                if os.path.exists(output_path):
                    page += 1
                    continue

                try:
                    results_html, next_page = fetch_results_html(
                        base_url, row['year'], row['office'], page)

                except ValueError:
                    break

                with open(output_path, 'w') as fout:
                    fout.write(results_html)

                page += 1
