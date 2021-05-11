"""
Consuming Iterator manually
"""
from collections import namedtuple


def cast(data_type, value):
    """Cast the value into a correct data type"""
    if data_type == 'DOUBLE':
        return float(value)
    elif data_type == 'STRING':
        return str(value)
    elif data_type == 'INT':
        return int(value)


def cast_row(data_types1, data_row):
    return [
        cast(data_type, value)
        for data_type, value in zip(data_types1, data_row)
    ]


# cars = []

# with open('cars.csv') as file:
#     row_index = 0
#     for line in file:
#         if row_index == 0:
#             # Header row
#             headers = line.strip('\n').split(';')
#             Car = namedtuple('Car', headers)
#         elif row_index == 1:
#             data_types = line.strip('\n').split(';')
#             # print('types', data_types)
#         else:
#             # data row
#             data = line.strip('\n').split(';')
#             data = cast_row(data_types, data)
#             car = Car(*data)
#             cars.append(car)
#             # print(data)
#         row_index += 1

# with open('cars.csv') as file:
#     file_iter = iter(file)
#     headers = next(file_iter).strip('\n').split(';')
#     Car = namedtuple('Car', headers)
#     data_types = next(file_iter).strip('\n').split(';')
#     for line in file_iter:
#         data = line.strip('\n').split(';')
#         data = cast_row(data_types, data)
#         car = Car(*data)
#         cars.append(car)

with open('cars.csv') as file:
    file_iter = iter(file)
    headers = next(file_iter).strip('\n').split(';')
    Car = namedtuple('Car', headers)
    data_types = next(file_iter).strip('\n').split(';')
    cars = [Car(*cast_row(
                data_types,
                line.strip('\n').split(';')
                ))
            for line in file_iter]

print(cars)
