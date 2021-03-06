# NICAR 2019: Scraping with Python

## Useful links for NICAR participants

- [Slides](https://docs.google.com/presentation/d/1WZmdW1lcXvo1gLQ_VanjWkCFTJVvu8T0md0is-2Sg60/edit?usp=sharing)
- [Technical Cheat Sheet](reference_cheatsheet.md)
- [Tipsheet](tipsheet.md)

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

- Python 3.6+. If you don't have Python, you may want to follow the instructions at [Installing Python the IRE Way](https://docs.google.com/document/d/1cYmpfZEZ8r-09Q6Go917cKVcQk_d0P61gm0q8DAdIdg/edit)
- [Pipenv](https://pipenv.readthedocs.io/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)
- A basic knowledge of Python programming. These are good resources:
  - [Intermediate Python — Python Tips](http://book.pythontips.com/en/latest/)
  - [How to Think like a Computer Scientist: Interactive Edition](https://interactivepython.org/courselib/static/thinkcspy/index.html)
  - [Dive Into Python 3](https://www.diveinto.org/python3/)
  - [Django Girls Tutorial](https://tutorial.djangogirls.org/en/) - This is Django-specific, but there is a good intro to the command line and Python section.

## Installation

### Clone this repository

```
git clone https://github.com/asuozzo/nicar2019-scraping.git
```

### Change directory to the project directory

```
cd nicar2019-scraping
```

#### Install Python dependencies

#### Pipenv

Create a virtualenv for the project and install Python dependencies using Pipenv:

```
pipenv install
```

#### Virtualenvwrapper

Create a virtualenv for the project and install Python dependencies using Virtualenvwrapper:

```
mkvirtualenv nicar2019-scraping
workon nicar2019-scraping
pip install -r requirements.txt 
```

## Running the mock scraping site

In order to make this workshop able to run, even if conference Internet access is sketchy, we decided to implement a mock site that has many features of actual sites we've scraped as a Flask app. To run this app, run the following command:

```
pipenv shell
FLASK_ENV=development FLASK_APP=scraping_site flask run
```
