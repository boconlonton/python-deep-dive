class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        print('deleter called...')
        del self._name


p = Person('Alex')
print(p.__dict__)
del p.name
print(p.__dict__)

