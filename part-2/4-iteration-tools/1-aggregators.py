"""Aggregators"""

# Example 1: Testing if all element of an iterable meet a condition

from numbers import Number

l = [10, 20, 30, 'hello']

# 1st way: map()
pred_l = map(lambda x: isinstance(x, Number), l)
print(all(pred_l))

# 2nd way: generator expression
pred_l = (lambda x: isinstance(x, Number) for x in l)

# 3rd way
all(map(lambda x: isinstance(x, Number), l))

# Example 2:
with open('car-brands.txt', encoding='latin-1') as f:
    # 1st way
    result1 = all((len(row) >= 4 for row in f))
    # 2nd way
    result2 = all(map(lambda row: len(row) >= 4, f))

print(result1)
print(result2)
