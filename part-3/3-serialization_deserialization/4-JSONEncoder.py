"""Custom JSON Encoding using JSONEncoder"""
import json
from datetime import datetime


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            super().default(arg)


custom_encoder = CustomJSONEncoder()
print(custom_encoder.encode(True))
print(custom_encoder.encode(datetime.utcnow()))

print(json.dumps(
    dict(name='test', time=datetime.utcnow()),
    cls=CustomJSONEncoder))

# print(json.dumps(
#     {'a': float('infinity')},
#     allow_nan=False
# ))  # Not allow nan/infinity value

d = {
    10: 'int',
    10.5: 'float',
    (1, 1): "complex"
}
print(json.dumps(d, skipkeys=True))

d = {
    'name': 'Python',
    'age': 27,
    'created_by': 'GUido',
    'list': [1, 2, 3]
}

print(json.dumps(d, separators=(',', ':')))


class CustomEncoder2(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(skipkeys=True,
                         allow_nan=False,
                         indent='---',
                         separators=('', ' = '))

    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            return super().default(arg)


class CustomEncoder3(json.JSONEncoder):

    def default(self, arg):
        if isinstance(arg, datetime):
            obj = dict(
                datatype="datetime",
                iso=arg.isoformat(),
                date=arg.date().isoformat(),
                time=arg.time().isoformat(),
                year=arg.year,
                month=arg.month,
                day=arg.day,
                hour=arg.hour,
                minutes=arg.minute,
                seconds=arg.second
            )
            return obj
        else:
            return super().default(arg)


d = {
    'time': datetime.utcnow(),
    'name': 'Python'
}

print(json.dumps(d, cls=CustomEncoder2))
print(json.dumps(d, cls=CustomEncoder3, indent=2))
