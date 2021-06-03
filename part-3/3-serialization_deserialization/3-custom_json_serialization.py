from datetime import datetime
import json
from functools import singledispatch
from decimal import Decimal
from fractions import Fraction


def format_iso(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')


def format_general(arg):
    return 'Unknown serialization'


@singledispatch
def json_format(arg):
    try:
        return arg.to_json()
    except AttributeError:
        try:
            return vars(arg)
        except TypeError:
            return str(arg)


@json_format.register(datetime)
def _(arg):
    return arg.isoformat()


@json_format.register(set)
def _(arg):
    return list(arg)


@json_format.register(Decimal)
def _(arg):
    return f'Decimal({str(arg)})'


current = datetime.utcnow()
'''YYYY-MM-DDTHH:MM:SS'''
print(str(current))
print(format_iso(current))
print(current.isoformat())

log_record = {
    'time': datetime.utcnow().isoformat(),
    'msg': 'testing'
}

print(json.dumps(log_record, indent=2))

# Custom JSON encoder
log_record = {
    'time': datetime.utcnow(),
    'msg': 'testing',
    "args": {
        10,
        "test"
    }
}
print(json.dumps(log_record, default=format_general))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def to_json(self):
        return vars(self)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x},y={self.y})'


pt1 = Point(1, 2)
p = Person('John', 79)

log_record = dict(
    time=datetime.utcnow(),
    message='Created New Point',
    point=pt1,
    created_by=p
)
print(json.dumps(log_record, indent=2, default=json_format))

d = dict(
    a=1+1j,
    b=Decimal('0.5'),
    c=Fraction(1, 3),
    p=Person('Python', 27),
    pt=Point(0, 0),
    time=datetime.utcnow()
)

print(json.dumps(d, indent=2, default=json_format))
