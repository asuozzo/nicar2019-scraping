# NICAR 2019: Scraping with Python

## Useful links for NICAR participants

- [Slides](https://docs.google.com/document/d/1-APtsKXlB4cjHz2jPUYNZ-7FnXEWbV61Hd47q1JA-9Q/edit?usp=sharing)
- [Technical Cheat Sheet](blob/master/reference_cheatsheet.md)

## What is this?

This project contains the activities and supporting code for a [hands-on workshop](https://www.ire.org/events-and-training/event/3190/4093) on web scraping with Python for the 2019 NICAR conference.

## What's in here?

- `Pipfile`: Defines Python dependencies for this project. See [Pipenv](https://github.com/pypa/pipenv) [documentation](https://pipenv.readthedocs.io/en/latest/).
- `data`: Place to store your the output of your scrapers.
- `data/src`: Place to store your raw HTML.
- `reference_cheatsheet.md`: Quick technical reference.
- `scrapers`: Directory that contains the files you'll edit in these exercises.
- `scrapers-solutions`: Directory that contains versions of the scripts in `scrapers` with the blank sections filled in.
- `scraping_site`: Flask app that implements our mock scraping site.

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
pipenv shell
FLASK_ENV=development FLASK_APP=scraping_site flask run
```
