from flask import Blueprint, render_template

bp = Blueprint('form_with_post_request', __name__)

@bp.route('/5')
def form_with_post_request():
     # Same as form_with_url_params, but the URL doesn't change
     return "TODO: Implement this"