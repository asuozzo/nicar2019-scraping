#!/usr/bin/env python
"""
Fetch HTML from all candidate profile urls and write to local HTML

Example:
    ./scrapers-solutions/fetch_candidate_profiles.py data/results.csv\
    http://127.0.0.1:5000 data/src
"""

import csv
import os
import re
import sys
from urllib.parse import urljoin

import requests


def get_absolute_url(base_url, profile_url):
    """
    Returns the absolute URL for a candidate profile.

    This is needed because the links in the HTML do not include the domain,
    e.g.  `/3/BERNIE%20SANDERS`.


    Args:

        base_url: URL of results page.
        profile_url: Relative URL of profile.

    """
    return urljoin(base_url, profile_url)


def fetch_url(url):
    """
    Returns the HTML of the page at URL.

    Raises:
        ValueError: Raised if the request fails, for example, if a profile
            does not exist.

    """
    # FILL IN THE BLANK: Return the HTML for the specified URL.
    # Be sure to check for failed requests.
    r = requests.get(url)

    if r.status_code == 200:
        return r.text

    raise ValueError("Could not retrieve profile at URL '{0}'".format(url))


def get_candidate_profile_filename(candidate_name):
    """
    Returns a standardized filename for the candidate profile HTML.

    For example, for the candidate Folasade Adeluola this function
    returns `candidate_profile_folsade_adeluola.html`.
    """
    # In a production scraper, we would probably want to move this to a module
    # since it is used in multiple scripts.
    candidate_name_slug = candidate_name.strip().lower()

    candidate_name_slug = re.sub(r'[^a-zA-Z\s]', '', candidate_name_slug)

    candidate_name_slug = re.sub(r'\s+', '_', candidate_name_slug)

    return 'candidate_profile_{0}.html'.format(candidate_name_slug)


if __name__ == '__main__':
    # The first positional argument is the path to the results CSV scraped
    # using `parse_candidate_profiles_table.py`.
    results_path = sys.argv[1]
    # The second positional argument is the URL of the results page.
    # This is needed to build full URLs from the relative URLs in  we scraped
    # earlier.
    results_url = sys.argv[2]
    # The third positional argument is the directory where the HTML file
    # for each candidate profile will be saved.
    output_dir = sys.argv[3]

    with open(results_path) as f:
        results = csv.DictReader(f)

        for result in results:
            url = get_absolute_url(results_url, result['Link'])

            try:
                html = fetch_url(url)

            except ValueError as e:
                # Something went wrong with fetching the URL.
                continue

            profile_filename = get_candidate_profile_filename(
                result['Candidate']
            )
            output_path = os.path.join(output_dir, profile_filename)

            with open(output_path, "w") as f_out:
                f_out.write(html)
