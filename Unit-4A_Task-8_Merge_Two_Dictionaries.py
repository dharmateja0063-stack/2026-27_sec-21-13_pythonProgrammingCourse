dict1 = {"name": "Krishna", "age": 18}
dict2 = {"course": "CSE", "city": "Guntur"}

merged = dict1.copy()
merged.update(dict2)

print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged)