import json
import re
from decimal import Decimal


j = '''
{
    "a": 100,
    "b": [1, 2, 3],
    "c": "python",
    "d": {
        "e": 4,
        "f": 5.5
    }
}
'''


class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        print("decode: ", type(arg), arg)
        return "a simple string object"


result = json.loads(j, cls=CustomDecoder)
print(result)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x},y={self.y})'


j_points = '''
{
    "points" : [
        [10, 20],
        [-1, -2],
        [0.5, 0.5]
    ]
}
'''

j_other = '''
{
    "a": 1,
    "b": 2
}
'''


class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        if 'points' in arg:
            obj = json.loads(arg)
            return "parsing object for points"
        else:
            return super().decode(arg)


result = json.loads(j_points, cls=CustomDecoder)
print(result)

result = json.loads(j_other, cls=CustomDecoder)
print(result)


class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        if 'points' in obj:
            obj['points'] = [
                Point(x, y)
                for x, y in obj['points']
            ]
        return obj


result = json.loads(j_points, cls=CustomDecoder)
print(result)

result = json.loads(j, cls=CustomDecoder)
print(result)

pattern = r'"_type"\s*:\s*"point"'
regexp = re.compile(pattern)
print(regexp.search('"_type": "point"'))


class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        pattern = r'"_type"\s*:\s*"point"'
        if re.search(pattern, arg):
            obj = self.make_pts(obj)
        return obj

    def make_pts(self, obj):
        if isinstance(obj, dict):
            # if '_type' in obj and obj['_type'] == 'point':
            if obj.get('_type', None) == 'point':
                obj = Point(obj['x'], obj['y'])
            else:
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj


class CustomDecoder1(json.JSONDecoder):
    base_decoder = json.JSONDecoder(parse_float=Decimal)

    def decode(self, arg):
        obj = self.base_decoder.decode(arg)
        pattern = r'"_type"\s*:\s*"point"'
        if re.search(pattern, arg):
            obj = self.make_pts(obj)
        return obj

    def make_pts(self, obj):
        if isinstance(obj, dict):
            # if '_type' in obj and obj['_type'] == 'point':
            if obj.get('_type', None) == 'point':
                obj = Point(obj['x'], obj['y'])
            else:
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj


class CustomDecoder2(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(parse_float=Decimal)

    def decode(self, arg):
        obj = super().decode(arg)
        pattern = r'"_type"\s*:\s*"point"'
        if re.search(pattern, arg):
            obj = self.make_pts(obj)
        return obj

    def make_pts(self, obj):
        if isinstance(obj, dict):
            # if '_type' in obj and obj['_type'] == 'point':
            if obj.get('_type', None) == 'point':
                obj = Point(obj['x'], obj['y'])
            else:
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj


print(json.loads(j, cls=CustomDecoder1))
