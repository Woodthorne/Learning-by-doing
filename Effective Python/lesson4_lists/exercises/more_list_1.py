nums = [3, 6, 9, 12, 15]
mult_nums = [num * 2 if num % 2 == 0 else num * 3 for num in nums]
print(mult_nums)