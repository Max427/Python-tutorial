student = ("Max", "23", "male")

print(student.count("Max"))
print(student.index("male"))

for x in student:
    print(x)

if "Max" in student:
    print("Max is here!")