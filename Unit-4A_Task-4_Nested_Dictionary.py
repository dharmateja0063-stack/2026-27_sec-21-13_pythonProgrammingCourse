students = {
    1: {"name": "Krishna", "marks": 90},
    2: {"name": "Ram", "marks": 85},
    3: {"name": "Ravi", "marks": 95}
}

for key, value in students.items():
    print("Name:", value["name"])
    print("Marks:", value["marks"])