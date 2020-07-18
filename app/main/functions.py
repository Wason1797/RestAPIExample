from .models import db
from .models import CurrencyExchangeRates

import sys
import logging
import requests
import datetime
import traceback


class CurrencyConverterApiFunctions:
    ENDPOINT = 'https://free.currconv.com/api/v7/convert'  # Using another free API since yahoo finance was deprecated
    API_KEY = 'bf783618439a5d70b0cc'  # Idealy we get this from the env variables or a .env file

    @staticmethod
    def make_prefix(base: str, quote: str) -> str:
        return f'{base}_{quote}'

    @classmethod
    def inject_url_attributes(cls, args: dict) -> str:
        return f'{cls.ENDPOINT}?{"&".join(["=".join(pair) for pair in args.items()])}'

    @classmethod
    def get_current_exchange_rate(cls, base: str, quote: str):
        prefix = cls.make_prefix(base, quote)
        endpoint = cls.inject_url_attributes({
            'q': prefix,
            'compact': 'ultra',
            'apiKey': cls.API_KEY,
        })
        try:
            api_response = requests.get(endpoint).json()
            return api_response.get(prefix)
        except Exception:
            exec_info = sys.exc_info()
            logging.error(traceback.format_exception(*exec_info))

    @classmethod
    def get_exchange_rate_by_date_range(cls, base: str, quote: str, start_date: str, end_date: str) -> list:
        prefix = cls.make_prefix(base, quote)
        endpoint = cls.inject_url_attributes({
            'q': prefix,
            'compact': 'ultra',
            'apiKey': cls.API_KEY,
            'date': start_date,
            'endDate': end_date
        })
        try:
            api_response = requests.get(endpoint).json()
            return [{'quote': quote,
                     'base': base,
                     'rate': rate,
                     'date': date} for date, rate in api_response.get(prefix).items()] if prefix in api_response else []
        except Exception:
            exec_info = sys.exc_info()
            logging.error(traceback.format_exception(*exec_info))


class WebhookApiFunctions:
    ENDPOINT = 'https://webhook.site/6f7c6822-4237-4e18-899b-87aaedf728a3'

    @classmethod
    def post_payload(cls, payload: dict) -> requests.Response:
        return requests.post(cls.ENDPOINT, json=payload)


class PopulateDatabaseFunctions:

    @staticmethod
    def populate(data: list, source='API'):
        if data:
            try:
                db.session.add_all((
                    CurrencyExchangeRates(
                        base_currency=item.get('quote'),
                        quote_currency=item.get('base'),
                        exchange_date=datetime.datetime.strptime(item.get('date'), r'%Y-%m-%d'),
                        exchange_rate=item.get('rate'),
                        source=source
                    ) for item in data))
                db.session.commit()
            except Exception:
                exec_info = sys.exc_info()
                logging.error(traceback.format_exception(*exec_info))
