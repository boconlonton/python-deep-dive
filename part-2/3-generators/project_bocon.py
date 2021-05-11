"""
Project: Car Violations
Data: nyc_parking_tickets_extract.csv
"""
from collections import namedtuple
from datetime import datetime


def produce_named_tuple_from_headers(headers_row):
    """This function creates a named tuple"""
    headers_lower = headers_row.lower()
    headers_list = headers_lower.strip('\n').split(',')
    final_headers = [
        '_'.join(word for word in item.split(' '))
        for item in headers_list]
    print(final_headers)
    return namedtuple('ViolationRecord',
                      final_headers), final_headers


def transform_row_into_list(row):
    """This function transform a row into a named tuple"""
    result = row.strip('\n').split(',')
    return result


def cast_data(data, index, headers):
    """This function transform data into appropriate type"""
    field_name = headers[index]
    if field_name == 'summons_number' \
            or field_name == 'violation_code':
        return int(data)
    elif field_name == 'issue_date':
        return datetime.strptime(data, '%m/%d/%Y')
    else:
        return str(data)


def row_generator(file_name):
    """Create a generator from file"""
    with open(file_name) as f:
        ticket, headers = produce_named_tuple_from_headers(next(f))
        for row in f:
            row_list = transform_row_into_list(row)
            row_list_validated = [
                cast_data(row_list[i], i, headers)
                for i in range(len(row_list))]
            yield ticket(*row_list_validated)


# Usage
vio_iter = row_generator('nyc_parking_tickets_extract.csv')

for case in vio_iter:
    print(case)


