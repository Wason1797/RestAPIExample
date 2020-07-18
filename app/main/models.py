from .plugins import db


class CurrencyExchangeRates(db.Model):
    _id = db.Column(db.Integer, prmary_key=True)
    base_currency = db.Column(db.String(20), nullable=False)
    quote_currency = db.Column(db.String(20), nullable=False)
    exchange_date = db.Column(db.Date(timezone=False))
    exchange_rate = db.Column(db.Numeric(8, 8))

    __table_args__ = (db.UniqueConstraint('base_currency', 'quote_currency', 'date'), )
