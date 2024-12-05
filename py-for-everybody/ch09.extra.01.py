# dictionary default values

d = dict()
d_keys = ['aa', 'bb', 'cc', 'aa', 'aa', 'bb', 'dd']

for dk in d_keys:
    # Use dictionary.get(key, default) to set a default value
    d[dk] = d.get(dk, 0) + 1

for k,v in d.items():
    print(f"key: {k}  value: {v}")