"""
Sets - Update Operations
"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1, id(s1))

s1 |= s2  # Mutate s1

print(s1, id(s1))
s1.update([3, 4, 5], (6, 7, 8), 'abc')
print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 &= s2
print(s1, id(s1))

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.intersection_update(s2)
print(s1, id(s1))

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}
print(s1 ^ s2)
s1 ^= s2
print(s1)


def combine(string, target):
    target.update(string.split(' '))


def cleanup(combined):
    words = {'the', 'and', 'a', 'or', 'is', 'of'}
    combined -= words


result = set()
combine('lumberjacks sleep all night', result)
combine('the ministry of silly walks', result)
combine('this parrot is a late parrot', result)
cleanup(result)
print(result)


# Usage of sets
def gen_read_data():
    yield ['Paris', 'Beijing', 'New York', 'London', 'Madrid', 'Mumbai']
    yield ['Hyderabad', 'New York', 'Milan', 'Phoenix', 'Berlin', 'Cairo']
    yield ['Stockholm', 'Cairo', 'Paris', 'Barcelona', 'San Francisco']


def filter_incoming(*cities, data_set):
    data_set.difference_update(cities)


result = set()
data = gen_read_data()
for page in data:
    result.update(page)
    filter_incoming('Paris', 'London', data_set=result)
print(result)
