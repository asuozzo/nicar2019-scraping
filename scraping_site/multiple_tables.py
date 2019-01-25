from flask import Blueprint, render_template
from . import data_api

bp = Blueprint('multiple_tables', __name__)

@bp.route('/2')
def multiple_tables():
    results_by_race = [
        data_api.get_race_results(2018, "US SENATOR"),
        data_api.get_race_results(2018, "REPRESENTATIVE TO CONGRESS"),
        data_api.get_race_results(2018, "GOVERNOR"),
    ]
    
    return render_template('multiple-tables.html', results_by_race=results_by_race)