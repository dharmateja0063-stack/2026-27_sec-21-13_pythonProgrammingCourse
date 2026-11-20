students = [
    {"name": "Krishna", "marks": 90},
    {"name": "Ram", "marks": 75},
    {"name": "Ravi", "marks": 85}
]

ascending = sorted(students, key=lambda x: x["marks"])
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("Ascending Order:", ascending)
print("Descending Order:", descending)