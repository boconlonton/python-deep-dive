"""Set Operation"""

# Intersection
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
temp = s1.intersection(s2)
print(s1, s2)
print(temp)
temp = s1.intersection(s2, s3)
print(temp)
print(s1 & s2 & s3)

# Union
temp = s1.union(s2)
print(temp)
print(s1.union(s2, s3))
print(s1 | (s2 | s3))  # s1 | s2 | s3

# disjoint
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {30, 40, 50}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
if s1 & s2:
    print('Not disjoint')
else:
    print('disjoint')
if s1 & s3:
    print('Not disjoint')
else:
    print('disjoint')

# Truth value
print(bool(set()))
print(bool({0}))

# Differences
print(s1 - s2)
print(s2 - s1)  # Different

s1 = {1, 2, 3}
s2 = {3, 4}
s3 = {3, 4}
print(s1 - s2 - s3)
print((s1 - s2) - s3)
print(s1 - (s2 - s3))
print(s1.difference(s2, s3))

# Symmetric difference
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

# Subset & Superset
s1 = {1, 2, 3}
s2 = {1, 2, 3}
s3 = {1, 2, 3, 4}
s4 = {10, 20, 30}
print(s1.issubset(s2))  # True
print(s1 <= s2)  # True
print(s1 < s2)  # False

print(s3.issuperset(s1))  # True
print(s3 > s1)  # True

# Special case
# {1, 2} & [2, 3]  # Error
print({1, 2}.intersection([2, 3]))
