from .models import db, CurrencyExchangeRates

import sys
import logging
import traceback


class ExchangeRateQueries:

    model = CurrencyExchangeRates

    @staticmethod
    def bulk_add(exchange_rates: list):
        try:
            db.session.add_all(exchange_rates)
            db.session.commit()
        except Exception:
            exec_info = sys.exc_info()
            logging.error(traceback.format_exception(*exec_info))

    @classmethod
    def get_latest_exchange(cls, base: str, quote: str, source: str = 'API'):
        return db.session.query(cls.model).filter((
            (cls.model.base_currency == base) &
            (cls.model.quote_currency == quote) &
            (cls.model.source == source))
        ).order_by(db.desc('exchange_date')).first()

    @classmethod
    def get_exchange_by_date(cls, base: str, quote: str, date: str, end_date: str = None, source: str = 'API'):
        return db.session.query(cls.model).filter((
            (cls.model.base_currency == base) &
            (cls.model.quote_currency == quote) &
            (cls.model.source == source) &
            (cls.model.exchange_date == db.func.DATE(date))
            if date and not end_date else
            (cls.model.exchange_date.between(db.func.DATE(date), db.func.DATE(end_date))))
        ).order_by(db.asc('exchange_date'))
