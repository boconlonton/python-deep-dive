"""MappingProxyType"""
from types import MappingProxyType

d = {'a': 1, 'b': 2}
mp = MappingProxyType(d)

# Read-only
print(list(mp.keys()))
print(list(mp.values()))

print(mp.get('a'))
print(mp.get('c', 'not found'))

# Immutable
# del mp['a']  # TypeError
# mp['a'] = 100  # TypeError

# Mutate the original dictionary
d['a'] = 100
d['c'] = 'new item'
del d['b']

print(mp)  # Reflect the changes in original dictionary
