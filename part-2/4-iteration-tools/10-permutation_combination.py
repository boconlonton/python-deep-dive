"""Permutation: Order matter"""
import fractions
import itertools
from collections import namedtuple
import fractions

l1 = 'abc'
# By default, size of permutation = len(iterable)
print(list(itertools.permutations(l1)))
# P(r, n)
print(list(itertools.permutations(l1, r=2)))

"""Combination: Order NO matter"""
# C(r, n)
# Keep the original ordering
# This is combination without replacement
print(list(itertools.combinations([1, 2, 3, 4], r=2)))
# This is combination with replacement
print(list(itertools.combinations_with_replacement([1, 2, 3, 4], 2)))

# Example: Calculate the odds of drawing 4 consecutive Ace cards
# Brute-forced way
SUITS = 'SHDC'
RANKS = tuple(map(str, range(2, 11))) + tuple('JQKA')
# dec = (
#     rank + suit
#     for suit in SUITS for rank in RANKS
# )
Card = namedtuple('Card', 'rank suit')
dec = (
    Card(rank, suit)
    for suit, rank in itertools.product(SUITS, RANKS)
)
# Sample space of 4 card, without repetition
sample_space = itertools.combinations(dec, 4)
total = 0
acceptable = 0
for outcome in sample_space:
    total += 1
    for card in outcome:
        if card.rank != 'A':
            break
    else:  # nobreak
        acceptable += 1

print(f'total={total}, accceptable={acceptable}')
print(f'odds ={fractions.Fraction(acceptable, total)}')
print('odds = {:.10f}'.format(acceptable/total))

# Improved
dec = (
    Card(rank, suit)
    for suit, rank in itertools.product(SUITS, RANKS)
)
sample_space = itertools.combinations(dec, 4)
total = 0
acceptable = 0
for outcome in sample_space:
    total += 1
    if all(map(lambda x: x.rank == 'A', outcome)):
        acceptable += 1
print(f'total={total}, accceptable={acceptable}')
print(f'odds ={fractions.Fraction(acceptable, total)}')
print('odds = {:.10f}'.format(acceptable/total))
