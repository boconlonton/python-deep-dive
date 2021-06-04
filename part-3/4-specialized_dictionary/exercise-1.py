"""
Use defaultdict & Counter to create a dictionary that merges all the input dictionaries
"""
from collections import defaultdict, Counter
from functools import reduce


d1 = {
    'python': 10,
    'java': 3,
    'c#': 8,
    'javascript': 15
}

d2 = {
    'java': 10,
    'c++': 10,
    'c#': 4,
    'go': 9,
    'python': 6
}

d3 = {
    'erlang': 5,
    'haskell': 2,
    'python': 1,
    'pascal': 1
}


def merge_using_defaultdict(*dicts):
    result = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            result[k] += v
    return result


def merge_using_counter(*dicts):
    result = Counter()
    for d in dicts:
        result += Counter(**d)
    return result


def merge_using_counter_1(*dicts):
    result = Counter()
    for d in dicts:
        result.update(d)
    return result


def merge_using_counter_2(*dicts):
    temps = (Counter(**d) for d in dicts)
    return reduce(lambda x, y: x + y, temps)


defaultdict_demo = merge_using_defaultdict(d1, d2, d3)
print(defaultdict_demo)
counter_demo = merge_using_counter(d1, d2, d3)
print(counter_demo)
counter_demo_1 = merge_using_counter_1(d1, d2, d3)
print(counter_demo_1)
counter_demo_2 = merge_using_counter_2(d1, d2, d3)
print(counter_demo_2)
