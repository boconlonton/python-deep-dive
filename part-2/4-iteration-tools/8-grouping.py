"""Grouping"""
import itertools
from collections import defaultdict

# Example: counting car by makes
# Approach 1
# makes = defaultdict(int)
# with open('cars_2014.csv') as f:
#     for row in f:
#         make, _ = row.strip('\n').split(',')
#         makes[make] += 1
#
# for key, value in makes.items():
#     print(f'{key}: {value}')

# Approach 2: using itertools.groupby()
data = (1, 2, 2, 3)
# print(list(itertools.groupby(data)))
# BEWARE
data = (1, 2, 2, 3, 1)
# print(list(itertools.groupby(data)))
# How groupby works
data = (1, 2, 2, 3)
# it = itertools.groupby(data)
# for group_key, sub_iter in it:
#     print(group_key, list(sub_iter))


# Calculate len of an iterable
def len_(iterable):
    return sum(1 for i in iterable)


with open('cars_2014.csv') as f:
    next(f)  # Skip the header
    make_groups = itertools.groupby(f, lambda x: x.split(',')[0])
    result = ((key, len_(sub_iter)) for key, sub_iter in make_groups)
    print(list(result))


