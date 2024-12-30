# https://testautomationu.applitools.com/python-tutorial/chapter7.html
# Dictionaries - scratch

# # Example 01
# dict_no_default = {}
# try:
#     dict_no_default["some_key"] += 1
# except Exception as e:
#     print(f"FAILED 01: {e}")     # Should fail
# print(f"NO DEF: {dict_no_default}")

# dict_default = {}
# try:
#     for i in range(3):
#         # dict_default.setdefault('a', 0) += 1   # Fails

#         dict_default.setdefault('a', 0)          # Works
#         dict_default['a'] += 1
# except Exception as e:
#     print(f"FAILED 02: {e}")
# print(f"SET DIF: {dict_default}")

# # Example 02
# sample_dict = {'a': 1, 'b': 2, 'c': 3}
# extend_values = {'e': 5, 'f': 6, 'g': 7}
# update_values = {'e': 15, 'f': 16, 'g': 17}

# print(f"DICT: {sample_dict}")

# sample_dict.update(extend_values)
# print(f"EXTEND: {sample_dict}")

# sample_dict.update(update_values)
# print(f"UPDATE: {sample_dict}")

# Example 03
sample_dict = {'a': 1, 'b': 2, 'c': 3}

print(f"KEYS: {list(sample_dict.keys())}")
print(f"VALS: {list(sample_dict.values())}")
print(f"ITEMS: {list(sample_dict.items())}")

sample_dict.pop('b')
print(f"POP: {sample_dict}")