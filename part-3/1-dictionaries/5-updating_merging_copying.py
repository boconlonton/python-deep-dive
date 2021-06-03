"""Updating, Merging & Copying"""

# Update dictionary
d1 = {'a': 1, 'b': 2}
d1.update(b=20, x=40, c=30)
print(d1)

d1.update([['c', 2], ['d', 3]])  # update(iterables)
print(d1)

d1 = {'a': 1, 'b': 2}
d1.update((k, ord(k)) for k in 'python')
print(d1)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = {**d1, **d2}
print(d)

# Example of use case of updating dictionary
conf_defaults = dict.fromkeys(('host', 'port',
                               'user', 'pwd', 'database'), None)
conf_global = {
    'port': 5432,
    'database': 'deepdive'
}
conf_dev = {
    'host': 'localhost',
    'user': 'test',
    'pwd': 'test'
}

conf_prod = {
    'host': 'prod.deepdive.com',
    'user': 'prod_user',
    'pwd': 'prod_pwd',
    'database': 'deepdive_prod'
}

conf = {**conf_defaults, **conf_global, **conf_dev}
conf = {**conf_defaults, **conf_global, **conf_prod}
