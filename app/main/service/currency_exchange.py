from app.http_methods import GET
from flask import Blueprint, jsonify, request
from app.main.queries import ExchangeRateQueries
from app.main.functions import WebhookApiFunctions
from app.main.serializers import CurrencyExchangeRatesSerializer


currency_exchange = Blueprint('currency_exchange', __name__)


@currency_exchange.route('v1/latest', methods=GET)
def get_exchange_rate():
    base_currency = request.args.get('base')
    quote_currency = request.args.get('quote')

    exchange = CurrencyExchangeRatesSerializer().dump(
        ExchangeRateQueries.get_latest_exchange(base_currency, quote_currency))\
        if base_currency and quote_currency else {}

    WebhookApiFunctions.post_payload(exchange)

    return jsonify(exchange)


@currency_exchange.route('v1/range', methods=GET)
def get_exchange_rate_by_dates():
    base_currency = request.args.get('base')
    quote_currency = request.args.get('quote')
    date = request.args.get('date')
    end_date = request.args.get('end_date')

    exchange = CurrencyExchangeRatesSerializer(many=True).dump(
        ExchangeRateQueries.get_exchange_by_date(base_currency, quote_currency, date, end_date))\
        if base_currency and quote_currency and date else {}

    WebhookApiFunctions.post_payload(exchange)

    return jsonify(exchange)
