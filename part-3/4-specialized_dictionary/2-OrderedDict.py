"""OrderedDict"""
from collections import OrderedDict, deque

# Not good since prior to 3.6, order is not guaranteed
d = OrderedDict(a=10, b=20)
print(d)

# Best
d = OrderedDict()
d['z'] = 'hello'
d['y'] = 'world'
d['a'] = 'python'
print(d)

# Reversed Iteration
for key in reversed(d):
    print(key)

d = OrderedDict()
d['first'] = 10
d['second'] = 20
d['third'] = 30
d['fourth'] = 40

# popitem() - Remove and return the last item
print(d.popitem())
print(d)

# popitem(last=False) - Remove and return the first item
print(d.popitem(last=False))
print(d)

d = OrderedDict()
d['first'] = 10
d['second'] = 20
d['third'] = 30
d['fourth'] = 40

# move_to_end(key) - Move key to the last position
d.move_to_end('second')
print(d)

# move_to_end(key, last=False) - Move key to the beginning
d.move_to_end('third', last=False)
print(d)

# OrderedDict compare to OrderedDict
d1 = OrderedDict()
d1['a'] = 10
d1['b'] = 20
d2 = OrderedDict()
d1['b'] = 20
d1['a'] = 10
print(d1 == d2)  # False since no match of key order

# OrderedDict compare to dict
d3 = dict()
d3['b'] = 20
d3['a'] = 10
print(d1 == d3)  # True since order of key NOT matter


# Usage of OrderedDict as stack/queue
def create_ordereddict(n=100):
    d = OrderedDict()
    for i in range(n):
        d[str(i)] = i
    return d


def create_deque(n=100):
    return deque(range(n))


def pop_all_ordered_dict(n=1000, last=True):
    d = create_ordereddict(n)
    while True:
        try:
            d.popitem(last=last)
        except KeyError:
            break


def pop_all_deque(n=1000, last=True):
    dq = create_deque(n)
    if last:
        pop = dq.pop
    else:
        pop = dq.popleft
    while True:
        try:
            pop()
        except IndexError:
            break
