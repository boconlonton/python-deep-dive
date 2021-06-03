"""Views: keys, values and items"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}

# Set operations
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = dict(zip('cde', [30, 4, 5]))

# Views are dynamic
keys = d1.keys()
d1['d'] = 0
print(set(keys))

# Set operations on views
union = d1.keys() | d2.keys()
print(union)  # The order are NOT guaranteed

intersection = d1.keys() & d2.keys()
print(intersection)

union_1 = d1.items() | d2.items()
print(union_1)

# Usage of set operations on views

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 50}
# union = d1.keys() | d2.keys()
# intersection = d1.keys() & d2.keys()
# keys = union - intersection

results = {}
for key in (d1.keys() ^ d2.keys()):
    results[key] = d1.get(key) or d2.get(key)
print(results)
