"""
Goal 1: Create each file a lazy iterator which
- Return named tuples
- Transform into data type
"""
import csv
import os
from collections import namedtuple
from datetime import datetime


def read_file(file_name):
    """
    Read csv file, skip the header row
    """
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        # Skip the header
        next(reader)
        yield from reader


def read_headers(file_name):
    """
    Generate headers list from file
    """
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        # Skip the header
        headers = next(reader)
    return headers


def emp_generator():
    Employer = namedtuple("Employer", emp_heads)
    for row in emp_data:
        row = (parse_string(item) for item in row)
        yield Employer(*row)


def pi_generator():
    PersonalInfo = namedtuple("PersonalInfo", personal_info_heads)
    for row in personal_info_data:
        row = (parse_string(data) for data in row)
        yield PersonalInfo(*row)


def up_sta_generator():
    UpdateStatus = namedtuple("UpdateStatus", update_status_heads)
    column_parser = (
        parse_string,
        parse_datetime,
        parse_datetime
    )
    for row in update_status_data:
        row = parse_row(column_parser, row)
        yield UpdateStatus(*row)


def vehicles_generator():
    Vehicles = namedtuple("Vehicles", vehicles_heads)
    column_parser = (
        parse_string,
        parse_string,
        parse_string,
        parse_int
    )
    for row in vehicles_data:
        row = parse_row(column_parser, row)
        yield Vehicles(*row)


# Utils
def parse_string(data, *, default=None):
    """
    Parse data into string type
    :param data: the data to be parsed
    :param default: value if data is None or empty
    :return: converted data
    """
    if data:
        return str(data)
    else:
        return default


def parse_datetime(data, *, default=None):
    """
    Parse data into Python datetime object
    :param data: The data to be parsed
    :param default: Value if data is None or empty
    :return: Python datetime object or default
    """
    if data:
        try:
            return datetime.strptime(data, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            return default
    else:
        return default


def parse_int(data, *, default=None):
    """
    Parse data into Python integer object
    :param data: Data to be parsed
    :param default: If data is blank or invalid
    :return:
    """
    if data:
        try:
            return int(data)
        except (ValueError, TypeError):
            return default
    else:
        return default


def parse_row(column_parser, raw_row):
    """
    Parse row into pre-defined data type
    :param column_parser: a tuple that contains parser related to row
    :param raw_row: row data
    :return: process row
    """
    return (
        func(field)
        for func, field in zip(column_parser, raw_row)
    )


current_dir = os.path.abspath(os.getcwd())
emp_file = os.path.join(current_dir, 'materials/employment.csv')
per_info_file = os.path.join(current_dir, 'materials/personal_info.csv')
update_stat_file = os.path.join(current_dir, 'materials/update_status.csv')
vehicles_file = os.path.join(current_dir, 'materials/vehicles.csv')

# employment.csv
emp_heads = read_headers(emp_file)
emp_data = read_file(emp_file)
emp_iter = emp_generator()
# personal_info.csv
personal_info_heads = read_headers(per_info_file)
personal_info_data = read_file(per_info_file)
personal_info_iter = pi_generator()
# update_status.csv
update_status_heads = read_headers(update_stat_file)
update_status_data = read_file(update_stat_file)
update_status_iter = up_sta_generator()
# vehicles.csv
vehicles_heads = read_headers(vehicles_file)
vehicles_data = read_file(vehicles_file)
vehicles_iter = vehicles_generator()
