from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def sport():
    return 'Hello Flask'
