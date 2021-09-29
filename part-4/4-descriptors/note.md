# Descriptors

## 1.Introduction

### 4 main methods that make up the `Descriptor` protocol

- `__get__`: used to get an attribute value (`p.x`)
- `__set__`: used to set an attribute value (`p.x = 100`)
- `__delete__`: used to delete an attribute (`del p.x`)
- `__set_name__`: new in Python 3.6

### 2 categories of descriptors

- **non-data descriptors**: Those that implement `__get__` only
- **data descriptor**: Those that implement `__set__` and/or `__delete__`

## 2.Getter and Setter

### The `__get__` method

- We can return different values from `__get__` depending on:

  - called from class
  - called from instance

- Often, we choose to:

  - Return the descriptor **instance** when called from class itself
  - Return the attribute **value** when called from an **instance** of the class

```
class TimeUTC:
    def __get__(self, instance, owner_class):
        if not instance:
            return self
        return datetime.utcnow().isoformat()
```

### The `__set__` method

- The `__set__` signature is as follows: self, instance, value

  - `self`: just like for the `__get__`, references the descriptor instance
  - `instance`: the instance of the `__set__` method
  - `value`: the value we want to assign to the attribute

### Warning

- We have to be mindful of which instance we are "storing" the data for
- This is one of the reasons both `__get__` and `__set__` need to know the instance

## 3.Strong & Weak References

### Weak references

- In other words, it is as a reference to an object that does NOT affect the
reference count as far as the memory manager is concerned.
- So for the data descriptor, instead of storing the object as key => store a
weak reference to the object.
- Usage: use `weakref` module

```python
import weakref

class Person:
  pass

p1 = Person() # strong reference to the object
p2 = weakref.ref(p1) # p2 is an object that contains a weak reference to the object
# p2 is callable
# p2 returns the original object or None if the object has been garbage collected
```

### Dictionaries of Weak References

- So, we want to create a dictionary of weak references (for our key) for our
data descriptor => use `weakref.WeakKeyDictionary`.
- Only deal with custom class

```python
import weakref

class Person:
  pass

p1 = Person()
d = weakref.WeakKeyDictionary()
d[p1] = 'some value'

del p1 # garbage collected
```

## 4.`__set_name__` method

```python
class ValidString:

    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner, property_name):
        self.property_name = property_name
```

## 5.Property lookup resolution

- For `Data descriptor`, when we call `x.a`, Python always call `__get__`
- For `Non-Data descriptor`, when we call `x.a`, Python always looks in the 
**instance dictionary first**.

## 6.Property vs Descriptor

- `property` objects are data descriptors
  - They have `__get__`, `__set__`, `__delete__` methods

## Use case 1

- Use for reusable class (often type validation class)

## Use case 2
