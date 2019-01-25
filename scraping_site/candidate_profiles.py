from flask import Blueprint, render_template

bp = Blueprint('candidate_profiles', __name__)

@bp.route('/3')
def candidate_profiles():
    return render_template('candidate-profiles.html')


@bp.route("/3/<candidate_name>")
def candidate_profile(candidate_name):
    # TODO: get candidate info from data_api
    try:
        return render_template('candidate-profile.html', 
                    candidate_name=candidate_name,
                    candidate_info=candidate_info)
    except NameError:
        return render_template('candidate-missing.html', candidate_name=candidate_name)
        
