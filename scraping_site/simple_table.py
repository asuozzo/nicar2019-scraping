from flask import Blueprint, render_template

bp = Blueprint('simple_table', __name__)

@bp.route('/1')
def simple_table():
    return render_template('simple-table.html')