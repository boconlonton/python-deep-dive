"""Descriptors"""
from datetime import datetime
from random import choice


class TimeUTC:
    """This is a non-data descriptor"""

    def __get__(self, instance, owner):
        return datetime.utcnow().isoformat()


class Logger:
    current_time = TimeUTC()


print(Logger.current_time)


class Choice:
    def __init__(self, *choices):
        self.choices = choices

    def __get__(self, instance, owner):
        return choice(self.choices)


class Deck:
    suit = Choice('Spade', 'Heart', 'Diamond', 'Club')
    card = Choice(*'23456789JQKA', '10')


d = Deck()
for _ in range(10):
    print(d.card, d.suit)


class Dice:
    dice_1 = Choice(1, 2, 3, 4, 5, 6)
    dice_2 = Choice(1, 2, 3, 4, 5, 6)


dice = Dice()
for _ in range(10):
    print(dice.dice_1, dice.dice_2)
