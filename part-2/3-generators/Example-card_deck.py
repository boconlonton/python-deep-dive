"""Example: Card Deck"""

from collections import namedtuple

Card = namedtuple('Card', 'rank suite')
SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
RANKS = tuple(range(2, 11)) + tuple('JQKA')


def card_gen():
    # Previous
    # for i in range(len(SUITS) * len(RANKS)):
    #     rank = RANKS[i % len(RANKS)]
    #     suit = SUITS[i // len(RANKS)]
    #     yield Card(rank, suit)
    # Improvements
    for suit in SUITS:
        for rank in RANKS:
            yield Card(rank, suit)


class CardDeck:
    """CardDeck iterable"""
    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    RANKS = tuple(range(2, 11)) + tuple('JQKA')

    def __iter__(self):
        return CardDeck.card_generate()

    def __reversed__(self):
        return CardDeck.reversed_card_gen()

    @staticmethod
    def card_generate():
        for suit in CardDeck.SUITS:
            for rank in CardDeck.RANKS:
                yield Card(rank, suit)

    @staticmethod
    def reversed_card_gen():
        for suit in reversed(CardDeck.SUITS):
            for rank in reversed(CardDeck.RANKS):
                yield Card(rank, suit)


# Usage
for card in card_gen():
    print(card)

card_deck = CardDeck()
for card in card_deck:
    print(card)
for card in reversed(card_deck):
    print(card)
