import json
from pprint import pprint
from datetime import datetime
from fractions import Fraction
from decimal import Decimal


j = '''
{
    "name": "Python",
    "age": 27,
    "versions": ["2.x", "3.x"]
}
'''
print(json.loads(j))

p = '''
{
    "time": {
        "objecttype": "datetime",
        "value": "2018-10-21T09:14:00"
    },
    "message": "created this json string"
}
'''
d = json.loads(p)
pprint(d)

for k, v in d.items():
    if (isinstance(v, dict) and
            'objecttype' in v and
            v['objecttype'] == 'datetime'):
        d[k] = datetime.strptime(v['value'], '%Y-%m-%dT%H:%M:%S')

pprint(d)


# Usage of object_hook
def custom_decoder(arg):
    print('decoding: ', arg)
    return arg


j = '''
{
    "a": 1,
    "b": 2,
    "c": {
        "c.1": 1,
        "c.2": 2,
        "c.3": {
            "c.3.1": 1,
            "c.3.2": 2
        }
    }
}
'''
print('-----object_hook--------')
d = json.loads(j, object_hook=custom_decoder)

print('-----object_hook 2--------')
p = '''
{
    "time": {
        "objecttype": "datetime",
        "value": "2018-10-21T09:14:00"
    },
    "message": "created this json string"
}
'''


def custom_decoder_1(arg):
    if 'objecttype' in arg and arg['objecttype'] == 'datetime':
        return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
    else:
        return arg


def custom_decoder_2(arg):
    if 'objecttype' in arg:
        if arg['objecttype'] == 'datetime':
            return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
        elif arg['objecttype'] == 'fraction':
            return Fraction(arg['n'], arg['d'])
    return arg


print(json.loads(p, object_hook=custom_decoder_1))

print('-----object_hook 3--------')


class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __repr__(self):
        return f'Person(name={self.name},ssn={self.ssn})'


def custom_decoder_2(arg):
    if 'objecttype' in arg:
        if arg['objecttype'] == 'datetime':
            return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
        elif arg['objecttype'] == 'fraction':
            return Fraction(arg['n'], arg['d'])
        elif arg['objecttype'] == 'person':
            return Person(arg['name'], arg['ssn'])
    return arg


print('-----object_hook 4--------')


def make_decimal(arg):
    print('Received: ', type(arg), arg)
    return Decimal(arg)


def make_int_binary(arg):
    return bin(int(arg))


def make_const_none(arg):
    return None


j = '''
{
    "a": 100,
    "b": 0.2,
    "c": 0.5,
    "e": true,
    "f": null
}
'''

# d = json.loads(j, parse_float=make_decimal)
# print(d)
#
# d = json.loads(j, parse_float=make_decimal, parse_int=make_int_binary)
# print(d)

d = json.loads(j, parse_float=make_decimal, parse_constant=make_const_none)
print(d)

print('-----object_pairs_hook--------')

j = '''
{
    "a": 1,
    "b": 2,
    "c": {
        "c.1": 1,
        "c.2": 2,
        "c.3": {
            "c.3.1": 1,
            "c.3.2": 2
        }
    }
}
'''


def custom_pairs_decode(arg):
    print('decoding: ', arg, type(arg))
    return {
        k: v
        for k, v in arg
    }


print(json.loads(j, object_pairs_hook=custom_pairs_decode))

j = '''
{
    "a": [1, 2, 3, 4, 5],
    "b": 100,
    "c": 10.5,
    "d": NaN,
    "e": null,
    "f": "python"
}
'''


def float_hanlder(arg):
    print('float handler ', type(arg), arg)
    return float(arg)


def int_hanlder(arg):
    print('int handler ', type(arg), arg)
    return int(arg)


def const_hanlder(arg):
    print('const handler ', type(arg), arg)
    return None


def obj_hook(arg):
    print('obj hook', arg)
    return arg


json.loads(
    j,
    object_hook=obj_hook,
    parse_float=float_hanlder,
    parse_int=int_hanlder,
    parse_constant=const_hanlder
)
