"""Infinite Iterators"""

from itertools import count, cycle, repeat, islice
from collections import namedtuple

# count()

g = count(10)
print(list(islice(g, 5)))

g = count(1, 0.5)
print(list(islice(g, 5)))


# cycle()
def colors():
    yield 'red'
    yield 'green'
    yield 'blue'


cols = colors()
g = cycle(cols)
print(list(islice(g, 10)))


# Example cycle: Card Deck
Card = namedtuple('Card', 'rank suit')


def card_deck():
    ranks = tuple(str(num) for num in range(2, 11)) + tuple('JQKA')
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    for suit in suits:
        for rank in ranks:
            yield Card(rank, suit)


hands = [list() for _ in range(4)]
# First way to split card to hands
index = 0
for card in card_deck():
    index = index % 4
    hands[index].append(card)
    index += 1
# Second way: use cycle()
hands = [list() for _ in range(4)]
index_cycle = cycle([0, 1, 2, 3])
print(list(islice(index_cycle, 8)))
for card in card_deck():
    hands[next(index_cycle)].append(card)
# Third way: Improved second
hands = [list() for _ in range(4)]
hands_cycle = cycle(hands)
for card in card_deck():
    next(hands_cycle).append(card)

# Repeat
g = repeat('Python')
for _ in range(5):
    print(next(g))
g = repeat('Python', 4)
print(list(g))
