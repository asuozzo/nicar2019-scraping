from flask import Blueprint, render_template, request

from .data_api import get_race_results, get_years_offices


bp = Blueprint('form_with_post_request', __name__)


@bp.route('/5', methods=['GET', 'POST'])
def form_with_post_request():
    year = request.values.get('year')
    office = request.values.get('office')

    if year is not None and office is not None:
        results = get_race_results(year, office)

        return render_template(
            'simple-table-multistep.html',
            results=results,
            path=request.path
        )

    years, offices = get_years_offices(year=year)
    return render_template(
        'results-form-multistep.html',
        year=year,
        years=years,
        offices=offices,
    )
