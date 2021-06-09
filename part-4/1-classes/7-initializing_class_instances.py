class Person:
    def __init__(self):
        print(f'Initializing a new Person object: {self}')


p = Person()
print(hex(id(p)))


class Person:
    def __init__(self, name):
        self.name = name


p = Person('Eric')


class Person:
    def init(self, name):
        self.name = name


p = Person()
print(p.__dict__)
p.init('Eric')
print(p.__dict__)
