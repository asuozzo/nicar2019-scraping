#!/usr/bin/env python
"""
Get list of params from form and save out html files for all combinations
"""

import csv
import requests

from bs4 import BeautifulSoup

def fetch_url(url, payload):
    r = requests.get(url, params=payload)
    if r.status_code != 404:
        soup = BeautifulSoup(r.content, 'html.parser')

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
    else:
        return None, False


if __name__ == '__main__':

    url = "http://localhost:5000/4"
    soup = BeautifulSoup(open('output/params-form.html'), 'html.parser')

    office_select = soup.find('select', {'id': 'office'})
    offices = [office.text for office in office_select.find_all('option')]

    year_select = soup.find('select', {'id': 'year'})
    years = [year.text for year in year_select.find_all('option')]

    for office in offices:
        for year in years:
            page = 1
            next_page = True
            while next_page:
                payload = {
                    'year': year,
                    'office': office,
                    'page':page
                }
                results, next_page = fetch_url(url, payload)
                if results:
                    filename = "output/params_{0}_{1}_{2}.html".format(year,office,page)
                    print(filename)
                    with open(filename, "w") as f:
                        f.write(results)
                page += 1