## Project

We have a project where we need to define classes that have fields that we want
to validate before we can set their value

This might be because these objects will later be serialized into a database
, and we need to ensure that the data is valid before we write to the db

## Part 1

Write 2 `Data descriptors`:

- `IntegerField`: only allows integral numbers, between minimum & maximum value
- `CharField`: only allows strings with a minimum and maximum length

So we want to be able to use the descriptors like this:
```python
class Person:
    name = CharField(1, 50)
    age = IntegerField(0, 200)
```

## Part 2

- You probably wrote 2 unrelated classes to do this. But you will notice there is
quite a bit of code duplication, with only the actual validation being different

- Refactor your code and create a `BaseValidator` class that will handle the
common functionality. Then change your `IntegerField` and `CharField` descriptors
to inherit from `BaseValidator`.
