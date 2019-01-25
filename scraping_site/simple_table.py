from flask import Blueprint, render_template
from . import data_api

bp = Blueprint('simple_table', __name__)

@bp.route('/1')
def simple_table():
    sen_results = data_api.get_race_results(2018, "US SENATOR")
    return render_template('simple-table.html', results=sen_results)