"""
Write a function that returns a dictionary with the correct counts for each eye color listed in eye_colors
"""
from collections import Counter, defaultdict
from random import seed, choices


EYE_COLORS = ("amber", "blue", "brown", "gray", "green", "hazel", "red", "violet")


class Person:
    def __init__(self, eye_color):
        self.eye_color = eye_color


def count_by_eye_color(list_people):
    gen_temp = (p.eye_color for p in list_people)
    result = Counter(dict.fromkeys(EYE_COLORS, 0))
    result.update(Counter(gen_temp))
    return result


def count_by_eye_color_fred(list_people):
    result = Counter(dict.fromkeys(EYE_COLORS, 0))
    result.update(p.eye_color for p in list_people)
    return result


seed(0)
persons = [Person(color) for color in choices(EYE_COLORS[2:], k=50)]
demo = count_by_eye_color(persons)
print(demo)
demo_fred = count_by_eye_color_fred(persons)
print(demo_fred)
