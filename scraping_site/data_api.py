import csv
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
RESULTS_PATH = os.path.join(DATA_DIR, 'results.csv')

def get_race_results(year, office):
    with open(RESULTS_PATH) as f:
        return [
            result for result in csv.DictReader(f)
            if result['office'] == office
        ]

def get_candidate_info(candidate_name):
    filename = os.path.join(DATA_DIR, 'candidateprofiles.csv')
    with open(filename) as f:
        return next((result for result in csv.DictReader(f)
            if result['candidate'] == candidate_name), None)
