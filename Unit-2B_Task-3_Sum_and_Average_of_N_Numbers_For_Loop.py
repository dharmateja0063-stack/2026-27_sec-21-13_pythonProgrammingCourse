n = int(input("Enter N: "))
sum = 0

for i in range(n):
    num = int(input("Enter number: "))
    sum += num

avg = sum / n

print("Sum =", sum)
print("Average =", avg)