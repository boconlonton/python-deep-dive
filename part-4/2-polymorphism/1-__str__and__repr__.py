"""
No define of __str__, looks for __repr__
using __str__ whenever possible
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        print('__repr__ called')
        return f"Person=(name'{self.name}', age={self.age})"

    def __str__(self):
        print('__str__ called')
        return self.name


p = Person('Python', 30)
print(repr(p))  # __repr__
print(p)  # __str__
str(p)  # __str__
print(f'The person is {p}')  # __str__
