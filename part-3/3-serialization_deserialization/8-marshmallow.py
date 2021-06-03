"""Marshmallow"""
from datetime import date
from marshmallow import Schema, fields, post_load
from collections import namedtuple


class Person:
    def __init__(self, first_name, last_name, dob, height):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.height = height

    def __repr__(self):
        return f'Person({self.first_name}, {self.last_name}, {self.dob})'


class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()
    height = fields.Int()


p1 = Person('John', 'Cleese', date(1939, 10, 27), 182)
person_schema_2 = PersonSchema()
data = person_schema_2.dumps(p1)
print(data)
PT = namedtuple('PT', 'first_name, last_name, dob, height')
p2 = PT('Eric', 'Idle', date(1943, 3, 29), 178)
data = person_schema_2.dumps(p2)

# Not full field as in schema
PT2 = namedtuple('PT2', 'first_name, last_name, age')
p3 = PT2('Micheal', 'Palin', 70)
data = person_schema_2.dumps(p3)
print(data)

# Partial schema
person_partial = PersonSchema(only=('first_name', 'last_name'))
data = person_schema_2.dumps(p1)
print(data)
data = person_partial.dumps(p1)
print(data)

person_partial_2 = PersonSchema(exclude=['dob'])
data = person_partial_2.dumps(p1)
print(data)

# Bad input
# p4 = Person(100, None, 200, 'abc')
# data = person_schema_2.dumps(p4)
# print(data)


# multiple objects in a field with marshmallow
class Person:
    def __init__(self, first_name, last_name, dob, height):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.height = height

    def __repr__(self):
        return f'Person({self.first_name}, {self.last_name}, {self.dob})'


class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()


class Movie:
    def __init__(self, title, year, actors):
        self.title = title
        self.year = year
        self.actors = actors


class MovieSchema(Schema):
    title = fields.Str()
    year = fields.Integer()
    actors = fields.Nested(PersonSchema, many=True)


parrot = Movie('Parrot Sketch', 1989, [p1, PT('Micheal', 'Palin', date(1943, 5, 5), 177)])
print(parrot)
print(MovieSchema().dumps(parrot))


# Object generation from json
class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()
    height = fields.Int()

    @post_load
    def make_person(self, data, **kwargs):
        return Person(**data)


person_schema = PersonSchema()
print(person_schema.load(
    dict(
        first_name='John',
        last_name='Cleese',
        dob='1939-10-27',
        height=178
    )
))


class Movie:
    def __init__(self, title, year, actors):
        self.title = title
        self.year = year
        self.actors = actors


class MovieSchema(Schema):
    title = fields.Str()
    year = fields.Integer()
    actors = fields.Nested(PersonSchema, many=True)

    @post_load
    def make_movie(self, data, **kwargs):
        return Movie(**data)


movie_schema = MovieSchema()
person_schema = PersonSchema()

json_data = '''
{
    "actors": [
        {"first_name": "John", "last_name": "Cleese", "dob": "1939-10-27", "height": 183},
        {"first_name": "Micheal", "last_name": "Palin", "dob": "1934-05-05", "height": 178}
    ],
    "title": "Parrot Sketch",
    "year": 1989
}
'''

movie = movie_schema.loads(json_data)

print(movie)
print(movie.title)
print(movie.actors)
