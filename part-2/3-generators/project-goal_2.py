"""
Project goal 1: Fred way
"""
from collections import namedtuple, defaultdict
from datetime import datetime
from functools import partial


def transform_headers(headers):
    """Processing headers from file"""
    column_names = [
        header.replace(' ', '_').lower()
        for header in headers
    ]
    return column_names


def read_data():
    """
    A generator that return each row in data file
    :return:
    """
    global file_name
    with open(file_name) as f:
        next(f)
        yield from f


def column_parsers():
    """
    Create the column parser which instructs how to
    validate each cell on a row
    """
    return (
        parse_int,
        parse_string,
        lambda x: parse_string(x, default=''),
        partial(parse_string, default=''),
        parse_date,
        parse_int,
        lambda x: parse_string(x, default=''),
        parse_string,
        lambda x: parse_string(x, default='')
    )


def parse_row(raw_row, *, default=None):
    """
    This function:
        - Validate each cell on a row based on the definition
        in column_parser
        - Turn each row into a Ticket instance if valid
        - Otherwise, return the default
    :param raw_row:
    :param default:
    :return:
    """

    fields = raw_row.strip('\n').split(',')
    # Use generator here for lazy evaluation
    processed_row = [func(field)
                     for func, field in zip(column_parser, fields)]

    # Evaluate if all cell is not None, also means valid
    if all(item is not None for item in processed_row):
        return Ticket(*processed_row)
    else:
        return default


def parse_data():
    """
    This generator:
        - Read the data row by row
        - Validate each cell on a row
        - Only if valid, yield it as a Ticket instance
    :return:
    """
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed


def violation_count_by_make():
    """
    This function count violation for each make
    :return: an descended order of make by violation count
    """
    makes_counts = defaultdict(int)
    for data in parsed_rows:
        makes_counts[data.vehicle_make] += 1
    return {make: cnt
            for make, cnt in
            sorted(makes_counts.items(),
                   key=lambda t: t[1],
                   reverse=True)
            }


# Utils functions
def parse_int(value, *, default=None):
    """
    Parse the value into integer type
    otherwise, replace it with None
    """
    try:
        return int(value)
    except ValueError:
        return default


def parse_date(value, *, default=None):
    """
    Parse the value into date type
    otherwise, replace it with None
    """
    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default


def parse_string(value, *, default=None):
    """
    Parse the value into string type
    otherwise, replace it with None
    """
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        else:
            return cleaned
    except ValueError:
        return default


file_name = 'nyc_parking_tickets_extract.csv'

with open(file_name) as f:
    sample_headers = next(f).strip('\n').split(',')
    raw_data = next(f)

Ticket = namedtuple(
    'Ticket',
    transform_headers(sample_headers)
)

column_parser = column_parsers()

parsed_rows = parse_data()

# First solution (Mine)
# makes_counts = {}
# for data in parsed_rows:
#     # if makes_counts.get(data.vehicle_make):
#     #     makes_counts[data.vehicle_make] += 1
#     # else:
#     #     makes_counts[data.vehicle_make] = 1
#     if data.vehicle_make in makes_counts:
#         makes_counts[data.vehicle_make] += 1
#     else:
#         makes_counts[data.vehicle_make] = 1
# for make, cnt in sorted(makes_counts.items(),
#                         key=lambda t: t[1],
#                         reverse=True):
#     print(make, cnt)

# d = defaultdict(int)
# d['a'] = 'hello'
# print(d['a'])  # 'hello' since it is existed
# print(d['b'])  # 0 since we set default = int

# Second solution (Fred)
print(violation_count_by_make())
