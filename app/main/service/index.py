from flask import Blueprint, jsonify
from app.http_methods import GET


index = Blueprint('index', __name__)


@index.route('/', methods=GET)
def _index():
    return jsonify({'message': 'hello from mock api'})
