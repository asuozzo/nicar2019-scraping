from flask import Blueprint, render_template
from . import data_api

bp = Blueprint('candidate_profiles', __name__)

@bp.route('/3')
def candidate_profiles():
    results = data_api.get_race_results(2018, "US SENATOR")
    return render_template(
        'candidate-profiles.html',
        results=results
        )


@bp.route("/3/<candidate_name>")
def candidate_profile(candidate_name):
    candidate_info = data_api.get_candidate_info(candidate_name)
    if candidate_info:
        return render_template('candidate-profile.html', 
                    candidate_info=candidate_info)
    else:
        return render_template('candidate-missing.html', candidate_name=candidate_name)
        
