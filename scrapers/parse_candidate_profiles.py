#!/usr/bin/env python

"""
Open each candidate profile file and write info to csv

Example:
    python parse_candidate_profiles.py data/src/profiles_candidate_*.html > \
    data/profiles.csv

"""

import csv
import os
import re
import sys

from bs4 import BeautifulSoup


def parse_profile_html(profile_path):
    """Returns a list of funds raised and the candidate bio."""
    with open(profile_path) as f:
        soup = BeautifulSoup(f, 'html.parser')
        funds_raised = None
        bio = None

        # FILL IN THE BLANK: Use Beautiful Soup to scrape the bio text and the
        # amount of funds raised.

        return [funds_raised, bio]


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
    # The second positional argument is the directory where the HTML file
    # for each candidate profile was saved.
    output_dir = sys.argv[2]

    columns = ["Candidate", "Funds Raised", "Bio"]

    writer = csv.writer(sys.stdout)
    writer.writerow(columns)

    with open(results_path, "r") as f:
        results = csv.DictReader(f)

        for result in results:
            # Get the standardized profile filename for the candidate.
            # We use the same function as in our script that downloaded all
            # the files.
            profile_filename = get_candidate_profile_filename(
                result['Candidate']
            )
            profile_html_path = os.path.join(output_dir, profile_filename)

            try:
                candidate_data = parse_profile_html(profile_html_path)

                row = [result['Candidate']] + candidate_data

                writer.writerow(row)

            except FileNotFoundError:
                # There might not be a profile for every candidate. If the
                # file doesn't exist, just skip it.
                pass
