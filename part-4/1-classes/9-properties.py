"""Properties"""


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value.strip()
        else:
            raise ValueError('name must be a non-empty string')


p = Person('Alex')
print(p.__dict__)
p.set_name('Eric')
print(p.__dict__)
print(p.get_name())
print(property())


# Usage of property class
class Person:
    """This is a Person object"""

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value.strip()
        else:
            raise ValueError('name must be a non-empty string')

    def del_name(self):
        print('deleter called...')
        del self._name

    name = property(get_name, set_name, del_name, doc="The person's name")


p = Person('Alex')
print(p.name)
p.name = 'Eric'
print(p.name)
print(p.__dict__)

print(getattr(p, 'name'))

p = Person('Alex')
print(p._name)

del p.name

help(Person.name)
