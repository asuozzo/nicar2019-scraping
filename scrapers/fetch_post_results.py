#!/usr/bin/env python

"""
Fetches HTML results that requires an HTTP POST of form to view results.

Example:
    python fetch_post_results.py http://127.0.0.1:5000/5 years_offices.csv \
    data/src/

"""

import csv
import os
import sys

import requests


def get_output_filename(year, office):
    """Returns a normalized filename for the results HTML."""
    office_slug = office.lower().replace('')
    office_slug = office.lower().replace(' ', '_')
    return '{0}__{1}.html'.format(year, office_slug)


def fetch_results_html(base_url, year, office):
    """Returns HTML of results for a particular race."""
    # FILL IN THE BLANK: Make a request using the url, year and 
    # office variables that will get you to a page with a table.




    return r.text


if __name__ == '__main__':
    # This program takes three positional arguments:
    #
    # The first argument to this program is the URL that accepts the HTTP POST
    # to retrieve the results.
    base_url = sys.argv[1]
    # The second argument is the path to a CSV file that contains the list of
    # years and offices. This file can be created using the
    # `scrape_years_offices.py` script.
    years_offices_csv_path = sys.argv[2]
    # The third argument is the path to a directory where the downloaded HTML
    # files will be stored.
    output_dir = sys.argv[3]


    with open(years_offices_csv_path) as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Each row of the CSV includes an election year and an office
            output_filename = get_output_filename(row['year'], row['office'])
            # Get the local path where we'll store the HTML for the results.
            output_path = os.path.join(output_dir, output_filename)

            if os.path.exists(output_path):
                # Only fetch the results HTML if the file doesn't already exist.
                # This lets  us re-run the program if a request fails without
                # re-making a bunch of requests.
                # This is kind to the remote webserver and also saves us time.
                continue

            # Do the HTTP request to get the results HTML.
            results_html = fetch_results_html(base_url, row['year'], row['office'])

            # Save the results HTML to disk.
            with open(output_path, 'w') as fout:
                fout.write(results_html)