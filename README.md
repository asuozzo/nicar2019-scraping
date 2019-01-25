# NICAR 2019: Scraping with Python

This project contains the activities and supporting code for a hands-on workshop on web scraping with Python for the 2019 NICAR conference.


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
FLASK_APP=scraping-site/hello.py pipenv run flask run
```

TODO: Can we streamline this at all, especially the environment variable setting?
