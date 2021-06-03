"""
- You have text data spread across multiple servers. Each server is able to analyze this data and return a dictionary
that contains words and their frequency.
- Your job is to combine this data to create a single dictionary that contains all the words and their combined
frequencies from all these data sources
- Bonus points if you can make your dictionary sorted by frequency
"""
from itertools import chain


def combined_data(*dictionary):
    d = dict()
    for dict_temp in dictionary:
        for key in dict_temp:
            d[key] = d.setdefault(key, 0) + dict_temp[key]
    return {
        k: v
        for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True)
    }


def combined_data1(*dictionary):
    d = dict()
    for dict_temp in dictionary:
        for key in dict_temp:
            d[key] = d.setdefault(key, 0) + dict_temp[key]
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))


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

d = combined_data(d1, d2, d3)
print(d)
d1 = combined_data1(d1, d2, d3)
print(d1)
