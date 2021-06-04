"""defaultdict"""
from collections import defaultdict, namedtuple
from datetime import datetime
from functools import partial, wraps


counts = defaultdict(lambda: 0)
sentence = "able was I ere I saw elba"
for c in sentence:
    counts[c] += 1
print(counts)
print(isinstance(counts, defaultdict))  # True
print(isinstance(counts, dict))  # True

# Factory function
c = defaultdict(int)  # equals to defaultdict(lambda: 0)
print(bool())
print(list())
print(str())

# Usage of defaultdict
persons = {
    'john': {'age': 20, 'eye_color': 'blue'},
    'jack': {'age': 25, 'eye_color': 'brown'},
    'jill': {'age': 22, 'eye_color': 'blue'},
    'eric': {'age': 35},
    'michael': {'age': 27}
}

eye_colors = {}
for person, details in persons.items():
    if 'eye_color' in details:
        color = details['eye_color']
    else:
        color = 'unknown'
    if color in eye_colors:
        eye_colors[color].append(person)
    else:
        eye_colors[color] = [person]
print(eye_colors)

eye_colors = {}
for person, details in persons.items():
    color = details.get('eye_color', 'unknown')
    person_list = eye_colors.get(color, [])
    person_list.append(person)
    eye_colors[color] = person_list
print(eye_colors)

eye_colors = defaultdict(list)
for person, details in persons.items():
    color = details.get('eye_color', 'unknown')
    eye_colors[color].append(person)
print(eye_colors)

persons = {
    'john': defaultdict(lambda: 'unknown',
                        age=20, eye_color='blue'),
    'jack': defaultdict(lambda: 'unknown',
                        age=20, eye_color='brown'),
    'jill': defaultdict(lambda: 'unknown',
                        age=22, eye_color='blue'),
    'eric': defaultdict(lambda: 'unknown', age=35),
    'michael': defaultdict(lambda: 'unknown', age=27)
}
eye_colors = defaultdict(lambda: [])
for person, details in persons.items():
    eye_colors[details['eye_color']].append(person)
print(eye_colors)

eyedict = partial(defaultdict, lambda: 'unknown')
# eyedict1 = lambda *args, **kwargs: defaultdict(lambda: 'unknown', *args, **kwargs)
persons = {
    'john': eyedict(age=20, eye_color='blue'),
    'jack': eyedict(age=20, eye_color='brown'),
    'jill': eyedict(age=22, eye_color='blue'),
    'eric': eyedict(age=35),
    'michael': eyedict(age=27)
}
eye_colors = defaultdict(lambda: [])
for person, details in persons.items():
    eye_colors[details['eye_color']].append(person)
print(eye_colors)


# Additional arguments of defaultdict()
d = defaultdict(lambda: ' ', k1=100, k2=200)
print(d)


# Factory function NOT need to be a deterministic function
def function_stats():
    d = defaultdict(lambda: {"count": 0, "first_called": datetime.utcnow()})
    Stats = namedtuple('Stats', 'decorator data')

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            d[fn.__name__]['count'] += 1
            return fn(*args, **kwargs)
        return wrapper
    return Stats(decorator, d)


stats = function_stats()


@stats.decorator
def func_1():
    pass


@stats.decorator
def func_2():
    pass


func_1()
func_2()
func_1()
print(stats.data)
