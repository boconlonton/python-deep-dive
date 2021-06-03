"""
Write a custom JSONEncoder class to serialize dictionaries that contain instances of these particular classes
"""
from json import JSONEncoder, dumps
from functools import singledispatchmethod
from datetime import datetime, date
from decimal import Decimal


class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def as_dict(self):
        return {
            'symbol': self.symbol,
            'date': self.date,
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'volume': self.volume
        }


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


class CustomEncoder(JSONEncoder):
    @singledispatchmethod
    def default(self, arg):
        print(arg)
        return arg

    @default.register(Stock)
    def _(self, arg):
        obj = arg.as_dict()
        obj.setdefault('object', 'stock')
        return obj

    @default.register(Trade)
    def _(self, arg):
        obj = arg.as_dict()
        obj.setdefault('object', 'trade')
        return obj

    @default.register(date)
    def _(self, arg):
        return arg.isoformat()

    @default.register(Decimal)
    def _(self, arg):
        return str(arg)

    @default.register(int)
    def _(self, arg):
        return int(arg)

    @default.register(list)
    def _(self, arg):
        return [
            self.default(instance)
            for instance in arg
        ]


# s1 = Stock('TSLA', date(2018, 11, 22), Decimal('338.19'), Decimal('338.64'), Decimal('337.60'),
#            Decimal('338.19'), 365_607)
# data = dumps(s1.as_dict(), cls=CustomEncoder)
# print(data)

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
data = dumps(activity, cls=CustomEncoder)
print(data)
