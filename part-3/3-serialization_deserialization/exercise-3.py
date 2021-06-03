"""
Write serializer & deserializer with marshmallow
"""
from marshmallow import Schema, fields, post_load
from datetime import datetime, date
from decimal import Decimal


class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open_ = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def as_dict(self):
        return {
            'symbol': self.symbol,
            'date': self.date,
            'open_': self.open_,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'volume': self.volume
        }


class StockSerializer(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open_ = fields.Decimal(as_string=True)
    high = fields.Decimal(as_string=True)
    low = fields.Decimal(as_string=True)
    close = fields.Decimal(as_string=True)
    volume = fields.Integer()

    @post_load
    def save(self, data, **kwargs):
        return Stock(**data)


class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.volume = volume
        self.commission = commission

    def as_dict(self):
        return dict(
            symbol=self.symbol,
            timestamp=self.timestamp,
            order=self.order,
            price=self.price,
            volume=self.volume,
            commission=self.commission
        )


class TradeSerializer(Schema):
    symbol = fields.Str()
    timestamp = fields.DateTime()
    order = fields.Str()
    price = fields.Decimal(as_string=True)
    volume = fields.Integer()
    commission = fields.Decimal(as_string=True)

    @post_load
    def save(self, data, **kwargs):
        return Trade(**data)


class ItemSerializer(Schema):
    quotes = fields.Nested(StockSerializer, many=True)
    trades = fields.Nested(TradeSerializer, many=True)


activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22),
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22),
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22),
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],

    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}

item_schema = ItemSerializer()
stock_schema = StockSerializer()
encode = item_schema.dumps(activity)
decode = item_schema.loads(encode)
print(decode)
