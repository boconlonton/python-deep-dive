"""Generator expressions"""
import math

l = [i**2 for i in range(5)]
print(l)

g = (i**2 for i in range(5))
print(type(g))
for item in g:
    print(item)

# Nested generator expression
start = 1
stop = 10
mult_list = [
    [i*j for j in range(start, stop+1)]
    for i in range(start, stop+1)]
print(mult_list)
mult_gen = (
    (i*j for j in range(start, stop+1))
    for i in range(start, stop+1))
for row in mult_gen:
    # print(', '.join(str(item) for item in row))
    for item in row:
        print(item, end=' ')
    print('')

mult_list = (
    [i*j for j in range(start, stop+1)]
    for i in range(start, stop+1)
)
for item in mult_list:
    print(item)


# Pascal Triangle
size = 5
p_triangle = (
    [math.comb(n, k) for k in range(n+1)]
    for n in range(size+1)
)

for row in p_triangle:
    print(row)
