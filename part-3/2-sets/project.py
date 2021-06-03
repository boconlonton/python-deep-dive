"""
Goal: validate one dictionary structure against a template dictionary
def validate(data, template):
    implement
    and return True/False
    in the case of False, return a string describing
    the first error encountered
    in the case of True, string can be empty
    return state, error
"""
from copy import deepcopy


def validate(data, template):
    # Step 1: Retrieve all keys of template
    template_keys = template.keys()
    # Step 2: Check data key existed as in template
    data_keys = data.keys()
    difference = template_keys - data_keys
    if difference:
        raise KeyError(f'Missing key {difference}')
    for k, v in data.items():
        if isinstance(v, dict):
            validate(v, template[k])
        elif not isinstance(v, template[k]):
            if isinstance(template[k], str):
                raise ValueError(f'Value of key {k} must be a string')
            else:
                raise ValueError(f'Value of key {k} must be an integer')
    return True, ''


template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}

data_good = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
    },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
        }
    }
}

data_bad_missing_key = deepcopy(data_good)
del data_bad_missing_key['bio']['birthplace']['city']

data_bad_wrong_type = deepcopy(data_good)
data_bad_wrong_type['bio']['dob']['month'] = 'May'

# if validate(data_good, template):
#     print('pass')
#
# if validate(data_bad_missing_key, template):
#     print('pass')

if validate(data_bad_wrong_type, template):
    print('pass')
