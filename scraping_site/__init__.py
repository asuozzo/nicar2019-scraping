from flask import Flask, render_template
from . import simple_table, multiple_tables, candidate_profiles, form_with_url_params, form_with_post_request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    
    app.register_blueprint(simple_table.bp)
    app.register_blueprint(multiple_tables.bp)
    app.register_blueprint(candidate_profiles.bp)
    app.register_blueprint(form_with_url_params.bp)
    app.register_blueprint(form_with_post_request.bp)

    @app.route('/')
    def intro():
        return render_template('intro.html')

    return app