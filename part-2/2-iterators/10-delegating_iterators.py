"""
Delegating Iterators: Reuse an existed iterator
"""
from collections import namedtuple

Person = namedtuple('Person', 'first last')


class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [
                person.first.capitalize()
                + ' ' + person.last.capitalize()
                for person in persons
            ]
        except (TypeError, AttributeError):
            self._persons = []

    def __iter__(self):
        # return ListIterator
        return iter(self._persons)


# Usage
persons = [Person('michalE', 'paLin'),
           Person('eRic', 'iDle'),
           Person('john', 'cheese')]
person_names = PersonNames(persons)
for name in person_names:
    print(name)
