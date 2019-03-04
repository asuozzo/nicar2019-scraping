#!/usr/bin/env python

"""
Parse a single HTML table and output CSV to standard output.

The parsing logic is very similar to that in `parse_single_table.py` since the
results in the version of the results site that requires an HTTP POST are
displayed in a single page per race with only one results table.

However, this version can parse multiple files, specified as positional
arguments to scrape results from multiple HTML files.

Example:
    ./scrapers-solutions/parse_single_table_multiple_files.py data/src/*.htm

"""

import csv
import sys

from bs4 import BeautifulSoup


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
    # This implementation is pretty simple, so it's all in the main
    # body of this script. For a more complicated scraper, it's important
    # to break the steps into multiple functions.

    if len(sys.argv) == 1:
        # No arguments, read HTML from standard input.
        files_or_paths = [sys.stdin]

    else:
        # Command line arguments. Interpret as paths to HTML files
        files_or_paths = sys.argv[1:]


    # Create an object that we'll use to write CSV.
    # We'll write to standard output. If we want to output this to a file, we
    # can just use the shell's redirection.
    writer = None

    for i, file_or_path in enumerate(files_or_paths):
        # Loop through the paths or file objects and scrape the results from
        # each.
        try:
            # Try to interpret the value as a string containing a path to an
            # HTML file.
            with open(file_or_path) as f:
                results = parse_html(f)

        except TypeError:
            # Trying to open the path failed. Assume it's already a
            # file-like-object, like sys.stdin
            results = parse_html(file_or_path)

        if i == 0:
            # We're handling the first file. Write the header of our output CSV.
            writer = csv.DictWriter(sys.stdout, fieldnames=results[0].keys())
            writer.writeheader()

        for result in results:
            # For each row of results, write a row of CSV.
            writer.writerow(result)
