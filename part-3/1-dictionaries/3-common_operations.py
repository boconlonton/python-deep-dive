"""Common Operations"""

d = dict(zip('abc', range(1, 4)))

result = d.get('z', 'N/A')

# Usage of d.get(key, default): counter
text = 'asfewfadcdsavfsefwadfavfsfvrewSCDAACacdacdsawerwqa'
counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1
print(counts)

# Examples of removing key

d = dict.fromkeys('abcd', 0)

# del d['a']
result = d.pop('b')  # Return the value of d[b]
result = d.pop('z', 100)  # If key not existed, return default

# Usage of d.popitem()
d = dict({i: i**2 for i in range(1, 5)})
print(d)
result = d.popitem()  # Remove last item and return tuple key, value
print(result)

# Usage of setdefault()
# insert if not exist
