# P8-Q6
student = {
    "Name":"Rahul",
    "Age":20,
    "Marks":85
}

print("Keys:")
for key in student:
    print(key)

print("Values:")
for value in student.values():
    print(value)

print("Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)
