# See a sample of what is in each file
import itertools
from functools import partial

import constants
import parse_utils
import datetime


# for fname, class_name, parser in zip(constants.fnames, constants.class_names, constants.parsers):
#     file_iter = parse_utils.iter_file(fname, class_name, parser)
#     print(fname)
#     for _ in range(3):
#         print(next(file_iter))
#     print()


# def group_key(item):
#     return item.vehicle_make
#
#
# cutoff_date = datetime.datetime(2017, 3, 1)
#
# print('group_m')
# for row in groups_m:
#     print(row)
#
# data_f = (row for row in data2 if row.gender == 'Female')
# sorted_data_m = sorted(data_m, key=group_key)
# groups_m = itertools.groupby(sorted_data_m, key=group_key)


def filter_key(cutoff_date, gender, row):
    return row.last_updated >= cutoff_date and row.gender == gender


cutoff_date = datetime.datetime(2017, 3, 1)

result_f = parse_utils.group_data(constants.fnames, constants.class_names, constants.parsers,
                                  constants.compress_fields,
                                  filter_key=partial(filter_key, cutoff_date, 'Female'),
                                  group_key=lambda row: row.vehicle_make)

result_m = parse_utils.group_data(constants.fnames, constants.class_names, constants.parsers,
                                  constants.compress_fields,
                                  filter_key=partial(filter_key, cutoff_date, 'Male'),
                                  group_key=lambda row: row.vehicle_make)

for row in result_f:
    print(row)

for row in result_m:
    print(row)
