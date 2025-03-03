# tuples


# # CHECK TYPES
# d = {'a': 1, 'b': 2, 'g': 7}
# print(type(d))

# for k,v in d.items():
#     # NOTE: k,v aren't a tuple 
#     print(f"k: {k} v: {v} types: {type(k), type(v)} ")

# for di in d:
#     # NOTE: di is a string
#     print(f"di: {di} type: {type(di)} ")

# for di in d.items():
#     # NOTE: di is a tuple
#     print(f"di: {di} type: {type(di)} ")

# MULTI-VALUE DICT KEY
d = dict()
t1 = (1,2)
t2 = (2,3)
t3 = (3,4)

n1 = 'bob'
n2 = 'ted'
n3 = 'carol'
n4 = 'alice'

d[t1] = n1
d[t2] = n2
d[t3] = n3

print(d)
first = 4
last = 5

d[first, last] = n4
print(d)
print(d[2,3])