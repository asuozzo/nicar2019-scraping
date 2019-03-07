#!/usr/bin/env python

"""
Fetch HTML from a URL and output to standard output.

Example:
    python fetch_html.py http://127.0.0.1:5000/1

"""

import sys

import requests

def fetch_url(url):
    # FILL IN THE BLANK: Make a request to this url 
    # and return the text.
    r = requests.get(url)
    return r.text


if __name__ == '__main__':

    # FILL IN THE BLANK: Get the url you passed in on 
    # the command line.

    # FILL IN THE BLANK: Use our fetch_url function to 
    # get this page's contents

    # FILL IN THE BLANK: Write the results to standard 
    # output so we can save it to a file or send it to 
    # another function.
