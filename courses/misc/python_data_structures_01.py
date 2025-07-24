'''
Source:

https://www.dataquest.io/blog/data-structures-in-python/
'''

# # 01
# list_01 = ['a', 'b', 'c']
# list_01.append('d')
# print(f"list_01 {list_01}")
# list_01.remove('c')            # Any element, not just pop
# print(f"list_01 {list_01}")

# 02
list_02 = []
list_03 = [10, 20, 30, 40]
list_04 = list_03[2:]
list_05 = list_03[:2]

def list_name(some_list):
   # Not reliable if values are the same in two lists
   globals_dict = globals()
   for k,v in globals_dict.items():
      if v == some_list:
         return k


for l in [list_02, list_03, list_04, list_05]:
   print(f"{list_name(l)}: {l} ")