#!/usr/bin/env python

"""
Parse an HTML table with links. Output CSV to standard output

Example:
    python ./scrapers/parse_candidate_profiles_table.py data/src/profiles_main.html \
    > data/results.csv

"""

import csv
import sys

from bs4 import BeautifulSoup

def get_result_office(soup):
    """
    Returns office for results table.

    Args:
        soup: BeautifulSoup object representing results page HTML.

    """
    return soup.find('h2').text

def get_result_field_names(table):
    """
    Returns list of columns in the results table.

    Args:
        table: Beautiful Soup `Tag` object representing the results table.

    """
    field_names = []
    for th in table.find('thead').find_all('th'):
        field_names.append(th.string)

    return field_names
    # You could also use a list comprehension, e.g.
    #return [th.string for th in table.find('thead').find_all('th')]


def parse_results(table):
    """
    Returns list of results scraped from table.

    Each list item is a list representing a candidate result.
    The list should have these items in the following order:

    - Candidate name
    - Party
    - Votes
    - URL to candidate profile

    Args:
        table: Beautiful Soup `Tag` object representing an HTML table of
            results.

    """
    results = []

    # FILL IN THE BLANK: Read each row from the table and append it to
    # `results` as a list. Be sure to also get the `href` value of the link
    # to the profile and include as the last element of each result list.

    return results


if __name__ == '__main__':
    # The first positional argument is the path to the file containing the
    # results HTML.
    results_html_path = sys.argv[1]

    with open(results_html_path) as f:
        soup = BeautifulSoup(f, 'html.parser')

        # Find the office name and table on the page
        office = get_result_office(soup)
        results_table = soup.find('table')

        # Get the field names for our results from the table header.
        # This should be familiar from the previous scrapers that we wrote.
        columns = ["Office"] + get_result_field_names(results_table) + ['Link']

        writer = csv.writer(sys.stdout)
        writer.writerow(columns)

        for result in parse_results(results_table):
            # We have to add the office to each row since it's not in the table
            # itself.
            writer.writerow([office] + result)
