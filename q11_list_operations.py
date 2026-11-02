# Q11: List operations - addition, insertion, slicing

nums = [10, 20, 30, 40, 50]
print("Original list:", nums)

# i. Addition (append / extend / concatenation)
nums.append(60)
print("After append(60):", nums)
nums.extend([70, 80])
print("After extend([70, 80]):", nums)
combined = nums + [90, 100]
print("Concatenation with [90, 100]:", combined)

# ii. Insertion
nums.insert(2, 25)
print("After insert(2, 25):", nums)

# iii. Slicing
print("nums[1:4]  :", nums[1:4])
print("nums[:3]   :", nums[:3])
print("nums[4:]   :", nums[4:])
print("nums[::2]  :", nums[::2])
print("nums[::-1] :", nums[::-1])
print("nums[-3:]  :", nums[-3:])
