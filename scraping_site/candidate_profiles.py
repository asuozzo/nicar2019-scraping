from flask import Blueprint, render_template

bp = Blueprint('candidate_profiles', __name__)

@bp.route('/3')
def candidate_profiles():
    return render_template('candidate-profiles.html')