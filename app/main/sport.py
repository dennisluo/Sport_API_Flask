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




if __name__ == '__main__':
    main.run(debug=True)
