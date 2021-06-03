"""
Suppose you have a API load balacned across multiple nodes
- This API receives various requests for resources and logs each request to some local storage
- Each instance of the API is able to return a dictionary containing the resource that was accessed and the number
of time it was requested
- Your task is to identify resource that have been requested on some, but NOT all the servers so you can determine
if you have an issue wit your load balancer NOT distributing certain resource requests across all nodes.
- Write a function that takes 3 dictionaries as arguments for node1, node2, node3 => Return a dictionary that contains
only keys that are NOT found in all the dictionary.
    + The value should be a list containing the number of times it was requested in each node.
    + 0 if the resource was NOT requested from the corresponding node
"""


# def finding_difference(*dictionaries):
#     keys = {}
#     dict_result = dict()
#     for position, dictionary in enumerate(dictionaries):
#         if position+1 < len(dictionaries):
#             diff = dictionary.keys() - dictionaries[position+1].keys()
#         else:
#             diff = dictionary.keys() - dictionaries[0].keys()
#         for key in diff:
#             dict_result[key] = tuple((dict_temp.get(key, 0) for dict_temp in dictionaries))
#     return dict_result


def finding_difference(n1, n2, n3):
    union = n1.keys() | n2.keys() | n3.keys()
    intersection = n1.keys() & n2.keys() & n3.keys()
    relevant = union - intersection
    return {
        k: (n1.get(k, 0), n2.get(k, 0), n3.get(k, 0))
        for k in relevant
    }


n1 = {'employess': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employess': 250, 'users': 23, 'user': 230}
n3 = {'employess': 150, 'users': 4, 'login': 1000}
d = finding_difference(n1, n2, n3)
print(d)
