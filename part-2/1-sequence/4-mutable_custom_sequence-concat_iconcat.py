"""This defines a sample custom mutable sequence
    - __add__(self,b)
    - __iadd__(self,b)
"""


class MyClass:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Myclass(name={self.name})'

    def __add__(self, other):
        """Define how a + b works:
        - This SHOULD return new object
        """
        if isinstance(other, MyClass):
            return MyClass(self.name + other.name)
        else:
            raise TypeError('Must be the same type')

    def __iadd__(self, other):
        """Define how a += b works
        - This SHOULD mutate the current object
        """
        if isinstance(other, MyClass):
            self.name += other.name
        else:
            self.name += other
        return self

    def __mul__(self, n):
        """Define how a * n works
        - This should return new object
        """
        return MyClass(self.name * n)

    def __rmul__(self, n):
        """Define how n * a works
        - This should return new object
        """
        return self.__mul__(n)

    def __imul__(self, n):
        """Define how a *= n works
        - This should mutate the original object
        """
        self.name *= n
        return self

    def __contains__(self, value):
        """Define how value in self works"""
        return value in self.name


# Usage of Concat/IConcat
print('USAGE OF CONCAT/ICONCAT')
c1 = MyClass('Eric')
c2 = MyClass('Idle')
print(id(c1))
print(id(c2))
result = c1 + c2
print(id(result))  # New object
print(result)

c1 += c2
print(id(c1))  # Mutate the original object
print(c1)

# Usage of Concat/IConcat
print('\nUSAGE OF MUL/IMUL')
c1 = MyClass('Eric')
print(id(c1))
result = c1 * 3
print(id(result))  # New object
print(result)

c1 *= 3
print(id(c1))  # Mutate the original object
print(c1)

c1 = MyClass('Eric')
print(id(c1))
result = 3 * c1
print(result)
print(id(result))  # New object

print('\nUSAGE OF __contains__')
c1 = MyClass('Eric Idle')
print('Eric' in c1)
