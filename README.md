# NICAR 2019: Scraping with Python

This project contains the activities and supporting code for a hands-on workshop on web scraping with Python for the 2019 NICAR conference.

## To do

* [ ] Mock an initial version of the data and create Python abstractions around it
* [ ] Implement the single-table version
* [ ] Define next steps/division of labor

* [ ] Mock robots.txt
* [ ] Mock malformed HTML
* [ ] Tipsheet
  - Other parsers
  - Other challenging sites (and solutions)
* [] Mock or implement additional cases for
  - Data as JSON
  - Multi-stage form where state is saved in cookie/session

## Assumptions

- Python 3.6+
- Pipenv

## Installation

Create a virtualenv for the project and install Python dependencies using Pipenv:

```
pipenv install
```

## Running the mock scraping site

In order to make this workshop able to run, even if conference Internet access is sketchy, we decided to implement a mock site that has many features of actual sites we've scraped as a Flask app. To run this app, run the following command:

```
FLASK_APP=scraping_site pipenv run flask run
```

TODO: Can we streamline this at all, especially the environment variable setting?
