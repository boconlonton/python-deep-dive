"""Counter"""
from collections import defaultdict, Counter
import random
import re
from itertools import repeat, chain


random.seed(1)
sentence = 'the quick brown fox jumps over the lazy dog'

counter = defaultdict(int)
for c in sentence:
    counter[c] += 1

# Usage of Counter
counter = Counter()
for c in sentence:
    counter[c] += 1

c1 = Counter('able was I ere I saw elba')
print(c1)

my_list = [random.randint(0, 10) for _ in range(1000)]
c2 = Counter(my_list)
print(c2)

# Initial value
c2 = Counter(a=1, b=10)
print(c2)

c3 = Counter({'a': 1, 'b': 20})
print(c3)

# Functionality of Counter
sentence = '''
his module implements pseudo-random number generators for various distributions.

For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.

On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions. For generating distributions of angles, the von Mises distribution is available.

Almost all module functions depend on the basic function random(), which generates a random float uniformly in the semi-open range [0.0, 1.0). Python uses the Mersenne Twister as the core generator. It produces 53-bit precision floats and has a period of 2**19937-1. The underlying implementation in C is both fast and threadsafe. The Mersenne Twister is one of the most extensively tested random number generators in existence. However, being completely deterministic, it is not suitable for all purposes, and is completely unsuitable for cryptographic purposes.'''
words = re.split(r'\W', sentence)
word_count = Counter(words)

# Find the most common item
word_count.most_common(5)

# Print duplicated element
c1 = Counter('abba')
for c in c1.elements():
    print(c)

# Generate a repeated chain
l = []
for i in range(1, 11):
    for _ in range(i):
        l.append(i)

c1 = Counter()
for i in range(1, 11):
    c1[i] = i
print(list(c1.elements()))


def gen(counter):
    for key, value in counter.items():
        for _ in range(value):
            yield key


class counter_iter:
    def __init__(self, counter):
        self.counter = counter

    def __iter__(self):
        return gen(self.counter)


a = counter_iter(c1)
print(list(a))

# Additive counter from another dictionaries
c1 = Counter(a=1, b=2, c=3)
c2 = Counter(b=1, c=2, d=3)
c1.update(c2)
print(c1)  # mutating c1

# Subtract counter from another dictionaries
c1 = Counter(a=1, b=2, c=3)
c2 = Counter(a=1, b=2, c=3)
c1.subtract(c2)
print(c1)

# Additive by iterables
c1 = Counter('aabbccddee')
print(c1)
c1.update('abcdef')
print(c1)

# Add operator
c1 = Counter('aabbcc')
c2 = Counter('abc')
print(c1 + c2)  # new object
print(c1 - c2)  # When subtracting, return only > 0 frequency

# Find minimum/maximum between 2 counter
c1 = Counter(a=5, b=1)
c2 = Counter(a=2, b=10)
print(c1 & c2)  # minimum
print(c1 | c2)  # maximum

# Plus unary operator: Keep only elements has > 0 frequency
c1 = Counter(a=10, b=-10, c=0)
print(c1)
print(+c1)

# Minus unary operator: Reverse the sign & Keep only > 0
print(-c1)

# Use case
widgets = ['battery', 'charger', 'cable', 'case',
           'keyboard', 'mouse']

orders = [(random.choice(widgets), random.randint(1, 5)) for _ in range(100)]
refunds = [(random.choice(widgets), random.randint(1, 5)) for _ in range(100)]
# This equals to: repeat(*order[0]) + repeat(*order[1]) + ... + repeat(*order[n])
sold_counter = Counter(chain.from_iterable(repeat(*order) for order in orders))
refund_counter = Counter(chain.from_iterable(repeat(*refund) for refund in refunds))

# Top 3 widgets
net_counter = sold_counter - refund_counter
print(net_counter.most_common(3))
