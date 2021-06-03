"""
Dictionary Views
"""

# d = dict(zip('abc', range(1, 4)))
# for k, v in d.items():
#     print(k, v)
#     del[k]

# d = dict(zip('abc', range(1, 4)))
# for k, v in d.items():
#     print(k, v)
#     d['z'] = 100

# d = dict(zip('abc', range(1, 4)))
# for k, v in d.items():
#     print(k, v)
#     d[k] = 1000

d = dict.fromkeys('python', 0)
print(d)
for k in d:
    print(k)
d_iter = iter(d)
for k in d_iter:
    print(k)
