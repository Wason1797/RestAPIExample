from .plugins import db


class CurrencyExchangeRates(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    base_currency = db.Column(db.String(20), nullable=False)
    quote_currency = db.Column(db.String(20), nullable=False)
    exchange_date = db.Column(db.Date())
    exchange_rate = db.Column(db.Float())
    source = db.Column(db.String(10), nullable=False)

    __table_args__ = (db.UniqueConstraint('base_currency', 'quote_currency', 'exchange_date', 'source'), )
