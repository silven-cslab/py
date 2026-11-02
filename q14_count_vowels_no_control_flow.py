# Q14: Count vowels in a string (no control flow: no if/for/while)

s = input("Enter a string: ")

# map() applies str.count for each vowel and sum() adds the results,
# so no if/for/while statement is needed
count = sum(map(s.lower().count, "aeiou"))

print("Number of vowels:", count)
