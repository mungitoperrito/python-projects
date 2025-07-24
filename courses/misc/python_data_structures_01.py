'''
Source:

https://www.dataquest.io/blog/data-structures-in-python/
'''

# HELPERS
def list_name(some_list):
   # Not reliable if values are the same in two lists
   globals_dict = globals()
   for k,v in globals_dict.items():
      if v == some_list:
         return k


# # 01
# list_01 = ['a', 'b', 'c']
# list_01.append('d')
# print(f"list_01 {list_01}")
# list_01.remove('c')            # Any element, not just pop
# print(f"list_01 {list_01}")

# # 02
# list_02 = []
# list_03 = [10, 20, 30, 40]
# list_04 = list_03[2:]
# list_05 = list_03[:2]

# for l in [list_02, list_03, list_04, list_05]:
#    print(f"{list_name(l)}: {l} ")

# 03
list_06 = ['a', 'b', 'c']
list_07 = ['d', 'e', 'f']
list_08 = list_06[:] ; list_08.append(list_07)
list_09 = list_06[:] ; list_09.extend(list_07)
list_10 = list_06[:] ; list_10.remove('b')
list_11 = list_06 + list_07            # NOTE list_name gets this wrong
list_12 = list_06[:] ; list_12.pop(1)  # Delete value by index

for l in [list_06, list_07, list_08, list_09, list_10, list_11, list_12]:
   print(f"{list_name(l)}: {l} ")


