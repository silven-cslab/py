# Q15: Check if a given key exists in a dictionary

student = {"name": "Ravi", "age": 20, "course": "B.Sc"}
print("Dictionary:", student)

key = input("Enter key to search: ")

if key in student:
    print(f"Key '{key}' exists, value = {student[key]}")
else:
    print(f"Key '{key}' does not exist.")
