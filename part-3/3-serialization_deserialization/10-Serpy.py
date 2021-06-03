import serpy
import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


class Movie:
    def __init__(self, title, year, actors):
        self.title = title
        self.year = year
        self.actors = actors


class PersonSerializer(serpy.Serializer):
    name = serpy.StrField()
    age = serpy.IntField()


class MovieSerializer(serpy.Serializer):
    title = serpy.StrField()
    year = serpy.IntField()
    actors = PersonSerializer(many=True)


p1 = Person('Micheal Palin', 75)
p2 = Person('John Cleese', 79)
movie = Movie('Parrot Sketch', 1989, [p1, p2])
print(PersonSerializer(p1).data)
data = MovieSerializer(movie).data
print(json.dumps(data))
