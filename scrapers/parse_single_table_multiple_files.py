#!/usr/bin/env python

"""
Parse HTML files containing a single results table and output CSV to standard
output.

The parsing logic is very similar to that in `parse_single_table.py` since the
results in both versions of the results site that use forms are
displayed in a single table per page.

However, this version can parse multiple files. They are discovered based on
the election years and offices scraped into a CSV. While we could just pass
the filenames as positional arguments, the year of the result is not contained
in the HTML of the results.

Example:
    python ./scrapers-solutions/parse_single_table_multiple_files.py
    data/years_offices.csv data/src

"""

import csv
import glob
import os
import re
import sys

from bs4 import BeautifulSoup


def get_output_filename_wildcard(year, office):
    """
    Returns a normalized wildcard that will match filenames for
    downloaded results HTML.

    This returns a wildcard to accomodate multiple pages of results.

    """
    office_slug = office.strip().lower()
    office_slug = re.sub(r'[^\w\s]', '', office_slug)
    office_slug = re.sub(r'\s+', '_', office_slug)

    return '{0}__{1}*.html'.format(year, office_slug)


def parse_html(f):
    """
    Returns a list of election results.

    There is one result, represented as a dictionary for each candidate.

    """
    # Create a parser object. We'll read the HTML from standard input.
    soup = BeautifulSoup(f, 'html.parser')

    # There's only one table on the page, so it's easy to select it as an
    # object that we can use to traverse the table structure.
    table = soup.find('table')

    results = []

    # Read the column names from the table header.
    # This could also be implemented more concisely using a list comprehension.
    columns = []
    header_cols = table.find('thead').find_all('th')
    for header_col in header_cols:
        columns.append(header_col.string)

    # Read the results from the rest of the table row by row.
    for tr in table.find('tbody').find_all('tr'):
        result = {}
        for i, td in enumerate(tr.find_all('td')):
            k = columns[i]
            result[k] = td.string

        results.append(result)

    return results


if __name__ == "__main__":
    # The first positional argument is the path to a CSV of years and offices
    # scraped from the form.
    years_offices_csv_path = sys.argv[1]
    # The second positional argument is the path to a directory that contains
    # downloaded HTML files.
    html_search_path = sys.argv[2]

    with open(years_offices_csv_path) as f:
        reader = csv.DictReader(f)

        # Create an object that we'll use to write CSV.
        # We'll write to standard output. If we want to output this to a file, we
        # can just use the shell's redirection.
        writer = None

        # The CSV just contains rows of years and office names.
        # Loop through them to identify filenames of scraped HTML files.
        for row in reader:
            election_year = row['year']
            office = row['office']
            # Build a wildcard that will match any HTML files that begin
            # with the slug for the election year and the office.
            output_pattern = os.path.join(
                html_search_path,
                get_output_filename_wildcard(election_year, office)
            )

            # glob.glob() returns an iterable of filenames that match a
            # pattern. We need to use this because we might have paged
            # results.
            # Not every year and office combination will have results, so
            # this iterable might be empty in some cases.
            for path in glob.glob(output_pattern):
                with open(path) as f:
                    results = parse_html(f)

                    if writer is None:
                        # We're handling the first file.
                        # Write the header of our output CSV.
                        # The year and office aren't in the HTML. So, we have
                        # to add them in.
                        fieldnames = (
                            ['Year', 'Office'] +
                            list(results[0].keys())
                        )

                        writer = csv.DictWriter(sys.stdout,
                            fieldnames=fieldnames)
                        writer.writeheader()

                    for result in results:
                        # For each row of results, write a row of CSV.
                        # Again, the results HTML doesn't include the election
                        # year or office, so we have to add it in.
                        result['Year'] = election_year
                        result['Office'] = office
                        writer.writerow(result)
