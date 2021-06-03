"""
Write a function that will create and return a dictionary from another dictionary but sorted by value
"""


def dictionary_constructor1(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x: x[1]))


def dictionary_constructor2(dictionary):
    return {
        k: v
        for k, v in sorted(dictionary.items(), key=lambda x: x[1])
    }


d1 = {'a': 2, 'b': 1, 'c': 4}
d2 = dictionary_constructor1(d1)
print(d2)
d3 = dictionary_constructor2(d1)
print(d3)
