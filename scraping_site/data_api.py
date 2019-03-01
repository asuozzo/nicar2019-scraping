import csv
import math
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
RESULTS_PATH = os.path.join(DATA_DIR, 'results.csv')

def get_race_results(year, office):
    with open(RESULTS_PATH) as f:
        return [
            result for result in csv.DictReader(f)
            if (str(result['year']) == str(year) and
                result['office'] == office)
        ]


def get_candidate_info(candidate_name):
    filename = os.path.join(DATA_DIR, 'candidateprofiles.csv')
    with open(filename) as f:
        return next((result for result in csv.DictReader(f)
            if result['candidate'] == candidate_name), None)


def get_years_offices(year=None):
    years = set()
    offices = set()

    with open(RESULTS_PATH) as f:
        for result in csv.DictReader(f):
            if (year is None or
                    (year is not None and result['year'] == str(year))):
                years.add(result['year'])
                offices.add(result['office'])

        return sorted(list(years)), sorted(list(offices))


def paginate(results, page, page_size=10):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    next_page = page + 1
    total_pages = int(math.ceil(len(results) / (page_size * 1.0)))

    if end_index > len(results):
        end_index = None
        next_page = None

    return results[start_index:end_index], next_page, total_pages
