from flask import Blueprint, render_template

bp = Blueprint('form_with_url_params', __name__)

@bp.route('/4')
def form_with_url_params():
     """Form that selects race from dropdown. Submitting form shows table with race as URL param"""
     # Also think about pagination here
     return "TODO: Implement this"