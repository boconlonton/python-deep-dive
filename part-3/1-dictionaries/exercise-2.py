"""
Write a function that creates a dictionary that contains only the keys common to both dictionaries, with values being a
tuple containing the value from d1 & d2
"""
from itertools import chain


def dictionary_constructor(d1, d2):
    return {
        k: (d1[k], d2[k])
        for k in d1.keys() & d2.keys()
    }


d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}

temp = dictionary_constructor(d1, d2)
print(temp)
