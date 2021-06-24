from datetime import datetime, date


a = 0.1
print(format(a, '.20f'))

print(format(datetime.now(), '%a %Y-%m-%d %I:%M %p'))


class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __repr__(self):
        return f"Person(name='{self.name}', dob={self.dob})"

    def __str__(self):
        return f"Person({self.name})"

    def __format__(self, date_format_spec):
        dob = format(self.dob, date_format_spec)
        return f"Person(name='{self.name}', dob={dob})"


p = Person('Alex', date(1900, 10, 20))
print(format(p, '%B %d, %Y'))
