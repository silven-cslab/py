# Q16: Add a new key-value pair to an existing dictionary

student = {"name": "Ravi", "age": 20}
print("Before:", student)

student["course"] = "B.Sc"          # using assignment
student.update({"city": "Hyderabad"})  # using update()

print("After :", student)
