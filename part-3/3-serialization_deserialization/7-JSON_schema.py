"""JSON Schemas"""
from jsonschema import validate, Draft4Validator
from jsonschema.exceptions import ValidationError
from json import loads, dumps, JSONDecodeError


person_schema = {
    "type": "object",
    "properties": {
        "first_name": {
            "type": "string",
            "minLength": 1
        },
        "middle_initial": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1
        },
        "last_name": {
            "type": "string",
            "minLength": 1
        },
        "age": {
            "type": "integer",
            "minimum": 0
        },
        "eye_color": {
            "type": "string",
            "enum": ["amber", "blue", "brown", "gray",
                     "green", "hazel", "red", "violet"]
        },
    },
    "required": [
        "first_name",
        "last_name"
    ]
}

p1 = '''
{
    "first_name": "John",
    "middle_initial": "M",
    "last_name": "Cleese",
    "age": 79
}
'''

p2 = '''
{
    "first_name": "John",
    "middle_initial": 100,
    "last_name": "Cleese",
    "age": "Unknown"
}
'''

p3 = '''
{
    "first_name": "John",
    "age": -10.5
}
'''

p4 = '''
{
    "first_name": "John",
    "last_name": "Cleese",
    "eye_color": "blue"
}
'''

json_doc = p4
try:
    validate(loads(json_doc), person_schema)
except JSONDecodeError as ex:
    print(f'Invalid JSON: {ex}')
except ValidationError as ex:
    print(f'Validation error: {ex}')
else:
    print('JSON is valid and conforms to schema')

validator = Draft4Validator(person_schema)
for error in validator.iter_errors(loads(json_doc)):
    print(error, end='\n-------\n')
