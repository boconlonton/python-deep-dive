# Exercise 01

"""
List comprehension exercise
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""

from functools import lru_cache


@lru_cache(2**10)
def factorial_me(k):
    """k!"""
    if k <= 1:
        return 1
    else:
        return k * factorial_me(k-1)


def combination(n, k):
    """C(n, k) = n! / (k! * (n-k)!)"""
    return factorial_me(n)//(factorial_me(k)*factorial_me(n-k))


# for loop version
new_list = []
for i in range(1, 5):
    new_row = []
    for j in range(i+1):
        new_row.append(combination(i, j))
    new_list.append(new_row)


# list comprehension
new_list = [
    [combination(i, j) for j in range(i+1)]
    for i in range(1, 5)
]

# Fred solution

from math import factorial


def combo(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))


size = 10

pascal = [
    [combo(n, k) for k in range(n+1)]
    for n in range(size+1)
]

print(pascal)

# Exercise 02
"""
l1 = ['a','b','c']
l2 = ['x','y','z']

result = ['ax', 'ay', 'az', ..., 'cy', 'cz']
"""
l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']
result = [
    a+b for a in l1 for b in l2
]
print(result)

# Exercise 03: Dot product
"""
v1 = (c1, c2, c3,..., cn)
v2 = (d1, d2, d3,..., dn)

v1.v2 = c1*d1 + c2*d2 + ... + cn*dn
"""
v1 = (1, 2, 3, 4, 5, 6)
v2 = (7, 8, 9)
result = sum(i*j for i, j in zip(v1, v2))
