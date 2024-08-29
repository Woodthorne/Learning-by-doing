big_nums = [123, 456, 789]
big_nums_sums = [sum([int(num) for num in str(nums)]) for nums in big_nums]

print(big_nums_sums)