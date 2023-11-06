nums = []
nums.append(int((input('Ange tal 1: '))))
nums.append(int((input('Ange tal 2: '))))
nums.append(int((input('Ange tal 3: '))))

print(min(nums))
nums.remove(min(nums))
print(max(nums))
nums.remove(max(nums))
print(nums[0])