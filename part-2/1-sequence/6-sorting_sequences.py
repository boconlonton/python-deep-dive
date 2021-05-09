"""
    Implementing sorting for custom sequence type
"""


class MyClass:

    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __repr__(self):
        return f'MyClass({self.name},{self.val})'

    def __lt__(self, other):
        return self.val < other.val


c1 = MyClass('c1', 20)
c2 = MyClass('c2', 10)
c3 = MyClass('c3', 20)
c4 = MyClass('c4', 10)

print(c1 < c2)

ls = sorted([c1, c2, c3, c4])
print(ls)

l2 = [c4, c2, c3, c1]
ls = sorted(l2, key=lambda i: i.name)
print(ls)
