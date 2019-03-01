#!/usr/bin/env python

"""Get table data from form with URL params and output CSV to standard output"""

import csv
import sys

import requests
from bs4 import BeautifulSoup

def get_params_lists(content):
    soup = BeautifulSoup(content, 'html.parser')

    office_select = soup.find("select", {"id":"office"})
    offices = [office.text for office in office_select.find_all("option")]
    
    year_select = soup.find("select", {"id": "year"})
    years = [year.text for year in year_select.find_all("option")]

    return offices, years

def get_results(url, year, office):
    payload = {'year':year, "office":office}
    r = requests.get(url, params=payload)

    if r.status_code == 404:
        return None
    else:
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find("table")
        
        columns = []
        header_cols = table.find('thead').find_all('th')
        for header_col in header_cols:
            columns.append(header_col.string)

        results = []
        for tr in table.find_all('tr'):
            row = {}
            i=0
            for td in tr.find_all('td'):
                row[columns[i]] = td.string
                i += 1
            if len(row) > 0:
                row["Year"] = year
                row["Office"] = office
                results.append(row)

        return results

if __name__ == "__main__":
    
    url = sys.argv[1]
    r = requests.get(url)
    
    offices, years = get_params_lists(r.content)

    results = []
    for year in years:
        for office in offices:
            race_results = get_results(url, year, office)
            if race_results:
                results += race_results

    columns = ["Year","Office","Candidate","Party","Votes"]
    writer = csv.DictWriter(sys.stdout, fieldnames=columns)
    writer.writeheader()
    for result in results:
        writer.writerow(result)




