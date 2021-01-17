from flask import Blueprint, request
from datetime import datetime
from app.api_call import api_call
import json

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
@main.route('/sport_api/v1', methods=['GET'])
def sport():
    # Call api and retrieve all match results
    games = api_call()
    games = json.dumps(games)

    return games


# End_point that returns bpl data
@main.route('/sport_api/v1/bpl', methods=['GET'])
def bpl():
    # Call api and retrieve bpl results
    games = api_call()

    bpl_results = games['bpl_games']

    # Query data for additional params
    query_parameters = request.args
    page = query_parameters.get('page')
    date = query_parameters.get('date')

    # Sort data with most recent game first in json
    bpl_results_filtered = [x for x in bpl_results
                            if datetime.strptime(x['utcDate'], '%Y-%m-%dT%H:%M:%SZ') <= datetime.utcnow()]
    sorted_bpl_results = sorted(bpl_results_filtered,
                                key=lambda x: datetime.strptime(x['utcDate'], '%Y-%m-%dT%H:%M:%SZ'),
                                reverse=True)

    # If page param passed then filter results for specified page results
    current_page = 40 if not page else (int(page) * 40)

    sorted_bpl_results = sorted_bpl_results[current_page - 40:current_page]

    # Query current results if date param passed
    if date:
        date_filter = datetime.strptime(date, '%Y-%m-%d').date()
        sorted_bpl_results = [x for x in sorted_bpl_results
                              if datetime.strptime(x['utcDate'], '%Y-%m-%dT%H:%M:%SZ').date() == date_filter]

    sorted_bpl_results = json.dumps(sorted_bpl_results)
    return sorted_bpl_results



if __name__ == '__main__':
    print(sport())
