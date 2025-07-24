# Duplicate keys - BAD BAD BAD
dup_keys = {"same": 1, "same": 2, "same": 3}

print(f"Dict: {dup_keys}")  # Only prints one
print(f"same: {dup_keys['same']}")
print(f"Length: {len(dup_keys)}")
count = 0
for k,v in dup_keys.items():
    count +=1
print(f"Alt length: {count}")