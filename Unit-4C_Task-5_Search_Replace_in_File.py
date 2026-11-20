f = open("sample.txt", "r")
data = f.read()
f.close()

data = data.replace("Python", "Java")

f = open("sample.txt", "w")
f.write(data)
f.close()

print("Word replaced successfully")