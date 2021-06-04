"""OrderedDict vs Python 3.6 Plain Dicts"""
from collections import OrderedDict


d1 = OrderedDict(a=1, b=2, c=3, d=4)
d2 = dict(a=1, b=2, c=3, d=4)

for k in reversed(d1):
    print(k)

# Reversed iteration with dict
for k in reversed(list(d2.keys())):
    print(k)

# Get the first key of dict
first_key = next(iter(d2.keys()))
print(d2)
print(first_key)

# Get the last key of dict
d1 = OrderedDict(a=1, b=2, c=3, d=4)
d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
print(d2.popitem())
print(d2)


def popitem(d, last=True):
    """Remove and return the first/last key of dict"""
    if last:
        return d.popitem()
    else:
        first_key = next(iter(d.keys()))
        return first_key, d.pop(first_key)


# Remove and return last item
d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
print(popitem(d2))
print(d2)

# Remove and return first item
d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
print(popitem(d2, last=False))
print(d2)


# move_to_end with dict
def move_to_end(obj_dict, key, beginning=False):
    obj_dict[key] = obj_dict.pop(key)
    if beginning:
        for key in list(obj_dict.keys())[:-1]:
            print(key)
            obj_dict[key] = obj_dict.pop(key)


d = dict(a=1, b=2, c=3, d=4, e=5, f=6)
print(d)
move_to_end(d, key='c')
print(d)
move_to_end(d, key='c', beginning=True)
print(d)

# Equality with order matter
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 3, 'a': 1}


def dict_equality_sensitive(d1, d2):
    if d1 == d2:
        for k1, k2 in zip(d1, d2):
            if k1 != k2:
                return False
        return True
    else:
        return False


def dict_equality_sensitive_improved_1(d1, d2):
    if d1 == d2:
        return all(k1 == k2 for k1, k2 in zip(d1, d2))
    else:
        return False


def dict_equality_sensitive_improved_2(d1, d2):
    if d1 == d2:
        return all(map(lambda el: el[0] == el[1], zip(d1, d2)))
    else:
        return False
