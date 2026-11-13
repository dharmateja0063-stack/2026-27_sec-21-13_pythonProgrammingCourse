def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(name="Krishna", Maths=90, Physics=85, Python=95)