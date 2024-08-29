nums = {1: 1, 4: 16, 9: 81}
roots = {key: value ** (1/2) for key, value in nums.items()}
print(roots)