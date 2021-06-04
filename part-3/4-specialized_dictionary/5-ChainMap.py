"""ChainMap"""
from collections import ChainMap


d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

d = {**d1, **d2, **d3}  # Last update wins
d = ChainMap(d1, d2, d3)  # First comes first serve
print(isinstance(d, dict))  # False
print(d)
print(d['a'])

# Dictionary views of ChainMap
for k, v in d.items():
    print(k, v)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)
d['z'] = 100
print(d)
d3['x'] = 500
print(d['x'])

# Add member of ChainMap
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d, d3)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d3, d)

# ChainMap operations
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d1, d2)

d3 = {'d': 400, 'e': 5}
d = d.new_child(d3)  # Add d3 to the beginning of the chain
print(d)

print(d.parents)  # Returns all dictionaries except the first

print(d.maps)  # Returns all dictionaries of the chain (child-parent)

# Directly mutate the ChainMap member through d.maps
d3 = {'e': 5, 'f': 6}
d.maps.append(d3)
print(d)
print(d['f'])

del d.maps[0]
print(d)

# USE CASE: multi-environment configuration settings
config = {
    'host': 'prod.deepdive.com',
    'port': 5432,
    'database': 'deepdive',
    'user_id': '$pg_user',
    'user_pwd': '$pg_pwd'
}

local_config = ChainMap({}, config)
local_config['user_id'] = 'test'
local_config['user_pwd'] = 'test'
print(local_config)
