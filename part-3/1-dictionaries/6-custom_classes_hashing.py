class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age}'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.age))

    # __hash__ = None


p1 = Person('John', 78)
p2 = Person('Eric', 75)
persons = {p1: 'John obj', p2: 'Eric obj'}
print(p1 is p2)  # False
print(p1 == p2)  # True
# print(hash(p1))
print(persons[Person('John', 78)])


class Number:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        if isinstance(other, Number):
            return self.x == other.x
        else:
            return False

    def __hash__(self):
        return hash(self.x)


# Usage of Custom hashes

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.x}, {self.y}'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))


points = {
    Point(0, 0): 'origin',
    Point(1, 1): 'second pt'
}

print(points[Point(0, 0)])
