f = open("sample.txt", "r")
data = f.read()

lines = data.splitlines()
words = data.split()
characters = len(data)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)

f.close()