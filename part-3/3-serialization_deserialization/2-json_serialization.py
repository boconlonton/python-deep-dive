import json
from pprint import pprint
from decimal import Decimal


d1 = {'a': 100, 'b': 200}
d1_json = json.dumps(d1)
print(d1_json)
print(json.dumps(d1, indent=4))

d2 = json.loads(d1_json)
print(d2 == d1)
print(d2 is d1)

# Keys must be string
d1 = {1: 100, 2: 200}
d1_json = json.dumps(d1)
print(d1_json)
d2 = json.loads(d1_json)
print(d2)
print(d2 == d1)
print(d2 is d1)

# Construct json manually
d_json = '''
{
    "name": "John Cleese",
    "age": 82,
    "height": 1.96,
    "walksFunny": true,
    "sketches": [
        {
            "title": "Dead Parror",
            "costars": ["Micheal Palin"]
        },
        {
            "title": "Ministry of Silly Walks",
            "costars": ["Micheal Palin"]
        }
    ],
    "boring": null
}
'''
d = json.loads(d_json)
pprint(d)


# Serialize class object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    # def to_json(self):
    #     return dict(name=self.name, age=self.age)
    def to_json(self):
        return vars(self)


p = Person('John', 82)
try:
    json.dumps(p)
except TypeError as ex:
    print(ex)

p.to_json()
print(json.dumps({'john': p.to_json()}, indent=2))
print(vars(p))
