from flask import Blueprint, render_template

bp = Blueprint('multiple_tables', __name__)

@bp.route('/2')
def multiple_tables():
    return "multiple tables"