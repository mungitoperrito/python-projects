# dictionary default values

d = dict()
d_keys = ['aa', 'bb', 'cc', 'aa', 'aa', 'bb', 'dd']

# Use dictionary.get(key, default) to set a default value
for dk in d_keys:
    d[dk] = d.get(dk, 0) + 1

# use dictionary.items() and multiple-assignment
for k,v in d.items():
    print(f"key: {k}  value: {v}")