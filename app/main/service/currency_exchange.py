from app.http_methods import GET
from flask import Blueprint, jsonify, request


currency_exchange = Blueprint('currency_exchange', __name__)


@currency_exchange.route('/v1', methods=GET)
def get_exchange_rate():
    source_currency = request.args.get('source')
    quote_currency = request.args.get('quote')

    if source_currency and quote_currency:
        return jsonify({'message': f'{source_currency}{quote_currency}'})

    return jsonify({'message': 'hello from mock api'})
