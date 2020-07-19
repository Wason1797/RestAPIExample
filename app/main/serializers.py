from .plugins import ma
from .models import CurrencyExchangeRates


class CurrencyExchangeRatesSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = CurrencyExchangeRates
        fields = ('base_currency',
                  'quote_currency',
                  'exchange_date',
                  'exchange_rate')

    exchange_date = ma.DateTime(format=r'%Y-%m-%d')
