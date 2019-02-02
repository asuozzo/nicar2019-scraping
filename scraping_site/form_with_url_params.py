from flask import Blueprint, render_template, request, url_for

from .data_api import get_race_results, get_years_offices, paginate


bp = Blueprint('form_with_url_params', __name__)


@bp.app_template_global('url_for_other_page')
def url_for_other_page(page):
    args = request.args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)


@bp.route('/4')
def form_with_url_params():
    """Form that selects race from dropdown. Submitting form shows table with race as URL param"""
    year = request.args.get('year')
    office = request.args.get('office')

    if year is not None and office is not None:
        results = get_race_results(year, office)
        page = int(request.args.get('page', 1))
        paginated, next_page, total_pages = paginate(results, page)

        return render_template(
            'results-paged.html',
            results=paginated,
            year=year,
            office=office,
            page=page,
            next_page=next_page,
            total_pages=total_pages
        )

    years, offices = get_years_offices()
    return render_template(
        'results-form.html',
        years=years,
        offices=offices
    )
