#!/usr/bin/env python
"""
Fetch HTML from a URL and output to standard output.
"""

import sys

import requests


def fetch_url(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    # In a more complex script, or if you want error handling, you might
    # want to check out the argparse package for parsing command-line
    # arguments and options.
    # The documentation is at
    # https://docs.python.org/3/library/argparse.html
    url = sys.argv[1]
    html = fetch_url(url)
    sys.stdout.write(html)
