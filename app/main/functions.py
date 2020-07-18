import sys
import logging
import requests
import traceback


class CurrencyConverterApiFunctions:
    ENDPOINT = 'https://free.currconv.com/api/v7/convert'  # Using another free API sins yahoo finance was deprecated
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
