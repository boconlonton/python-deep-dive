"""Yaml Format"""
import yaml
from datetime import date


data = '''
---
title: Parrot Sketch
actors:
    - first_name: John
      last_name: Cleese
      dob: 1939-10-27
    - first_name: Micheal
      last_name: Palin
      dob: 1943-05-05
'''

d = yaml.load(data)
print(type(d))
print(d)

d = {
    'a': 100,
    'b': False,
    'c': 10.5,
    'd': [1, 2, 3]
}

print(yaml.dump(d, default_flow_style=False))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name},age={self.age})'


p1 = Person('John Cleese', date(1939, 10, 27))
p2 = Person('Micheal Palin', date(1934, 5, 5))
print(yaml.dump({'john': p1, 'micheal': p2}))

print(yaml.safe_load(data))


class Person(yaml.YAMLObject):
    yaml_tag = '!Person'
    yaml_loader = yaml.SafeLoader

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name},age={self.age})'


print(yaml.dump(
    dict(
        john=Person('John Cleese', 79),
        micheal=Person('Micheal Palin', 74)
    )
))

yaml_data = '''
john: !Person
  age: 79
  name: John Cleese
micheal: !Person
  age: 74
  name: Micheal Palin
'''

print(yaml.safe_load(yaml_data))
