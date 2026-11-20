class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter student marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")

    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

except ValueError:
    print("Enter valid numbers")

except InvalidMarksError as e:
    print(e)

finally:
    print("Program finished")