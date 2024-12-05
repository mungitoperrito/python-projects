# split

s = 'a string with         spaces'

print(f"string: '{s}'")
print(f"default: {len(s.split())}")
print(f"specify space: {len(s.split(' '))}")
