def marks(a, b, c):
    total = a + b + c
    average = total / 3
    return total, average

a = int(input("Enter mark 1: "))
b = int(input("Enter mark 2: "))
c = int(input("Enter mark 3: "))

t, avg = marks(a, b, c)

print("Total =", t)
print("Average =", avg)