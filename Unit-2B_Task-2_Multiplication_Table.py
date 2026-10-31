n = int(input("Enter a number: "))

print("Using for loop:")
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

print("Using while loop:")
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1