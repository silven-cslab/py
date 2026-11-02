# Q10: Check if a substring is present in a given string

text = input("Enter the main string: ")
sub = input("Enter the substring: ")

if sub in text:
    print(f"'{sub}' is present in the string (first index: {text.find(sub)}).")
else:
    print(f"'{sub}' is NOT present in the string.")
