class Person:
    pass


print(Person.__name__)


class Program:
    language = 'Python'
    version = '3.6'


print(Program.__name__)
print(type(Program))
print(Program.language)
print(Program.version)

Program.version = '3.7'
print(Program.version)

# Usage of getattr
print(getattr(Program, 'version'))
print(getattr(Program, 'x', 'N/A'))

# Usage of setattr
setattr(Program, 'version', '3.6')
print(getattr(Program, 'version'))

# Remove an attribute
Program.x = 100  # Add attribute at runtime
print(Program.__dict__)
delattr(Program, 'x')
print(Program.__dict__)
Program.y = 200
print(Program.__dict__)
del Program.y
print(Program.__dict__)

# Access class attribute directly
print(Program.__dict__['language'])
