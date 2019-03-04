#!/usr/bin/env python
"""
Learn to use BeautifulSoup and Requests
"""

import requests
from bs4 import BeautifulSoup


if __name__=="__main__":
    
    # print("Hello! This is a simple Python program that you'll edit for scraping practice.")

    # FILL IN THE BLANK! Make a GET request to get the content of the
    # homepage. Its url is http://localhost:5000/
    r = requests.get("http://localhost:5000/")


    # FILL IN THE BLANK! The request will return a status code to tell 
    # you if the request was successful. Print out "good to go!" if
    # r.status_code is 200.
    if r.status_code == 200:
        print("good to go!")

    # FILL IN THE BLANK! Output the HTML of the page you just retrieved.
    # Once you have that working, comment this out — you won't need it 
    # for the next step.
    print(r.text)

    # FILL IN THE BLANK! Create a BeautifulSoup object named soup. 
    # Find and print the first h1 header on the page.
    soup = BeautifulSoup(r.text, 'html.parser')

    heading = soup.find("h1")
    print(heading)

    # FILL IN THE BLANK! Now, print out just the text from that 
    # heading.
    print(heading.text)

    # FILL IN THE BLANK! Find all the links on the page.
    links = soup.find_all("a")
    print(links)

    # FILL IN THE BLANK! Print out the url for each link on 
    # the page.
    for link in links:
        print(link["href"])

    # FILL IN THE BLANK! Print the url for the Vermont 
    # Secretary of State.
    data_section = soup.find("section", {"id":"data"})
    sos_link = data_section.find("a")
    print(sos_link["href"])