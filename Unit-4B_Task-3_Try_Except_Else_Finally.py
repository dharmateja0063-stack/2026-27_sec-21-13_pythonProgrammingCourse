try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Program finished")