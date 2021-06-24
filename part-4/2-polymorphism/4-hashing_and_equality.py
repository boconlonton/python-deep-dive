# print(repr(dir(object)))


class Person:
    pass


p1 = Person()
p2 = Person()
print(hash(p1), hash(p2))  # hash() uses object id()


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """Read-only since we want the hash is immutable"""
        return self._name

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"Person(name='{self.name}')"


p1 = Person('John')
p2 = Person('John')
p3 = Person('Eric')
d = {
    p1: 'Eric'
}
print(d)
