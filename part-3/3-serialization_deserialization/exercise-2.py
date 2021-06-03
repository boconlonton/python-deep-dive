"""
Write a custom JSONDecoder class to deserialize
"""

from json import JSONEncoder, dumps, JSONDecoder, loads
from functools import singledispatchmethod
from datetime import datetime, date
from decimal import Decimal, InvalidOperation


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


class CustomDecoder(JSONDecoder):
    base_decoder = JSONDecoder(parse_float=Decimal)

    def decode(self, arg):
        obj = self.base_decoder.decode(arg)
        if isinstance(obj, dict):
            obj = {
                k: self.handler(v)
                for k, v in obj.items()
            }
        return obj

    @singledispatchmethod
    def handler(self, obj):
        return obj

    @handler.register(list)
    def _(self, obj):
        for position, item in enumerate(obj):
            obj[position] = self.handler(item)
        return obj

    @handler.register(dict)
    def _(self, obj):
        if obj.get('object', None) == 'stock':
            obj['date'] = datetime.strptime(obj.get('date'), '%Y-%m-%d').date()
            obj['high'] = Decimal(obj.get('high'))
            obj['low'] = Decimal(obj.get('low'))
            obj['open_'] = Decimal(obj.get('open_'))
            obj['close'] = Decimal(obj.get('close'))
            obj.pop('object', None)
            return Stock(**obj)
        elif obj.get('object', None) == 'trade':
            obj['timestamp'] = datetime.strptime(obj.get('timestamp'), '%Y-%m-%dT%H:%M:%S')
            obj['price'] = Decimal(obj.get('price'))
            obj['commission'] = Decimal(obj.get('commission'))
            obj.pop('object', None)
            return Trade(**obj)


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

activity = loads(data, cls=CustomDecoder)
print(activity)
