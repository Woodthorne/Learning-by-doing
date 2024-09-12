from timeit import default_timer

def two_sum(nums: list[int], target: int) -> list[int]:
    for index1, num1 in enumerate(nums):
        for index2, num2 in enumerate(nums):
            if index1 == index2:
                break
            elif num1 + num2 == target:
                return [index1, index2]

def two_sum_2(nums: list[int], target: int) -> list[int]:
    sorted_nums = sorted(nums)
    index1 = 0
    index2 = len(sorted_nums)
    while index1 < index2:
        sum_ = sorted_nums[index1] + sorted_nums[index2]
        if sum_ == target:
            return [index1, index2]
        if sum_ > target:
            index2 -= 1
        elif sum_ < target:
            index1 += 1

def two_sum_3(nums: list[int], target: int) -> list[int]:
    dict_nums = {num: index for index, num in enumerate(nums)}
    for index, num in enumerate(nums):
        target_buddy = target - num
        if target_buddy in dict_nums \
        and index != dict_nums[target_buddy]:
            return index, dict_nums[target_buddy]

# Solution given from instructor
def two_sum_solved(nums: list[int], target: int) -> list[int]:
    dict_nums = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in dict_nums:
            return [index, dict_nums[complement]]
        dict_nums[num] = index
    return []

tests = [
    dict(
        nums = [2,7,11,15],
        target = 9,
        output = [0,1]
    ),
    dict(
        nums = [3,2,4],
        target = 6,
        output = [1,2]
    ),
    dict(
        nums = [3,3],
        target = 6,
        output = [0,1]
    )
]

for func in [two_sum, two_sum_2, two_sum_3, two_sum_solved]:
    print(func.__name__)
    start = default_timer()
    for test in tests:
        result = two_sum(nums = test['nums'], target = test['target'])
        print(set(result) == set(test['output']))
    print('Time taken:', default_timer() - start)
