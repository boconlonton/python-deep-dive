from copy import deepcopy


class SchemaError(Exception):
    pass


class SchemaKeyMismatch(SchemaError):
    pass


class SchemaTypeMismatch(SchemaError, TypeError):
    pass


# def match_keys(data, valid, path):
#     data_keys = data.keys()
#     valid_keys = valid.keys()
#
#     extra_keys = data_keys - valid_keys
#     missing_keys = valid_keys - data_keys
#
#     if missing_keys or extra_keys:
#         missing_msg = (
#             'missing key' +
#             ','.join(
#                 {path + '.' + str(key) for key in missing_keys}
#             )
#         ) if missing_keys else ''
#         extras_msg = (
#             'missing key' +
#             ','.join(
#                 {path + '.' + str(key) for key in extra_keys}
#             )
#         ) if extra_keys else ''
#         return False, ' '.join((missing_msg, extras_msg))
#     else:
#         return True, None


def match_keys(data, valid, path):
    data_keys = data.keys()
    valid_keys = valid.keys()

    extra_keys = data_keys - valid_keys
    missing_keys = valid_keys - data_keys

    if missing_keys or extra_keys:
        missing_msg = (
            'missing key' +
            ','.join(
                {path + '.' + str(key) for key in missing_keys}
            )
        ) if missing_keys else ''
        extras_msg = (
            'missing key' +
            ','.join(
                {path + '.' + str(key) for key in extra_keys}
            )
        ) if extra_keys else ''
        raise SchemaKeyMismatch(' '.join((missing_msg, extras_msg)))


# def match_types(data, template, path):
#     for key, value in template.items():
#         if isinstance(value, dict):
#             template_type = dict
#         else:
#             template_type = value
#         data_value = data.get(key, object())
#         if not isinstance(data_value, template_type):
#             err_msg = ('incorrect type: ' + path + '.' + key +
#                        ' -> expected ' + template_type.__name__ +
#                        ', found ' + type(data_value).__name__)
#             return False, err_msg
#     return True, None


def match_types(data, template, path):
    for key, value in template.items():
        if isinstance(value, dict):
            template_type = dict
        else:
            template_type = value
        data_value = data.get(key, object())
        if not isinstance(data_value, template_type):
            err_msg = ('incorrect type: ' + path + '.' + key +
                       ' -> expected ' + template_type.__name__ +
                       ', found ' + type(data_value).__name__)
            raise SchemaTypeMismatch(err_msg)


# def recursive_validate(data, template, path):
#     is_ok, err_msg = match_keys(data, template, path)
#     if not is_ok:
#         return False, err_msg
#     is_ok, err_msg = match_types(data, template, path)
#     if not is_ok:
#         return False, err_msg
#
#     dictionary_type_keys = {
#         key for key, value in template.items()
#         if isinstance(value, dict)
#     }
#     for key in dictionary_type_keys:
#         sub_path = path + '.' + str(key)
#         sub_template = template[key]
#         sub_data = data[key]
#         is_ok, err_msg = recursive_validate(sub_data, sub_template, sub_path)
#         if not is_ok:
#             return False, err_msg
#     return True, None


def recursive_validate(data, template, path):
    match_keys(data, template, path)
    match_types(data, template, path)

    dictionary_type_keys = {
        key for key, value in template.items()
        if isinstance(value, dict)
    }
    for key in dictionary_type_keys:
        sub_path = path + '.' + str(key)
        sub_template = template[key]
        sub_data = data[key]
        recursive_validate(sub_data, sub_template, sub_path)

# def validate(data, template):
#     return recursive_validate(data, template, '')


def validate(data, template):
    recursive_validate(data, template, '')


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

# if validate(data_bad_wrong_type, template):
#     print('pass')

try:
    validate(data_bad_missing_key, template)
except SchemaError as ex:
    print(ex)
