"""
Create Sets
"""

s = {'a', 100, (1, 2)}

# Empty set
s = set()

# Using set constructor
s = set([1, 2, 3])
print(s)

# Works with any iterables as long as elements are Hashable
s = set(range(10))

d = {'a': 1, 'b': 2}
s = set(d)  # Set of keys

# Set comprehension
s = {c for c in 'python'}
s = set('python')

# Unpacking
s1 = {'a', 'b', 'c'}
s2 = {10, 20, 30}

s = {*s1, *s2}
print(s)


# Usage of sets
def scorer(s):
    
    alphabet = set('abcdefghjklmnopqrstuvwxyz')
    s = s.lower()
    distinct = set(s)
    effective = distinct & alphabet
    return len(effective) / len(alphabet)


print(scorer('the quick brown fox jumps over the lazy dog'))

