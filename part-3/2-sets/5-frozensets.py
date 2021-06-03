"""
Frozensets
"""
from copy import deepcopy
from functools import lru_cache


s1 = {'a', 'b', 'c'}
s2 = frozenset('abc')  # Hashable as long as all elements are hashable
print(hash(s2))
s2 = {frozenset({'a', 'b'}), frozenset({1, 2, 3})}

# Copy frozenset
t1 = (1, 2, [3, 4])
t2 = tuple(t1)
print(id(t1), id(t2))  # same

l1 = [1, 2, 3]
l2 = l1.copy()
print(id(l1), id(l2))  # different

s1 = {1, 2, 3}
s2 = set(s1)
print(s1 is s2)  # False

s1 = frozenset([1, 2, 3])
s2 = frozenset(s1)
print(s1 is s2)  # True

s2 = deepcopy(s1)
print(s1 is s2)  # False

# Set operations
s1 = frozenset('ab')
s2 = {1, 2}
s3 = s1 | s2  # Type follow the type of first operand
print(s3)
s4 = s2 | s1
print(s4)

# Equality, Identity
s1 = {1, 2}
s2 = set(s1)
print(s1 is s2)
print(s1 == s2)


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __repr__(self):
        return f'Person(name={self._name}, age={self._age}'

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def key(self):
        return frozenset({self.name, self.age})


p1 = Person('John', 78)
p2 = Person('Eric', 75)
d = {
    p1.key(): p1,
    p2.key(): p2
}
print(d[frozenset(['John', 78])])


# Use case: Memoization
# Drawback of lru_cache
@lru_cache()
def my_func(*, a, b):
    print('calculating a+b...')
    return a+b


print(my_func(a='a', b='b'))
print(my_func(a='a', b='b'))
print(my_func(a='a', b='b'))


# Rewrite lru_cache
def memoizer(fn):
    cache = {}

    def inner(*args, **kwargs):
        key = (*args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
        return result

    return inner


@memoizer
def my_func(*, a, b):
    print('calculating a + b...')
    return a+b


print(my_func(a=1, b=2))
print(my_func(b=2, a=1))


# Rewrite memoization with key as frozenset
# Use when order is NOT matter
def memoizer(fn):
    cache = {}

    def inner(*args, **kwargs):
        key = frozenset(args) | frozenset(kwargs.items())
        if key in cache:
            return cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
        return result

    return inner


@memoizer
def adder(*args):
    print('calculating...')
    return sum(args)


print(adder(1, 2, 3))
print(adder(2, 1, 3))
print(adder(3, 2, 1))
