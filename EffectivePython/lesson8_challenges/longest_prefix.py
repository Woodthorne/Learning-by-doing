def longest_common_prefix(strs: list[str]) -> str:
    prefixes = {}
    for word in strs:
        prefix = ''
        for char in word:
            prefix += char
            if prefix not in prefixes:
                prefixes[prefix] = 0
            prefixes[prefix] += 1
    filtered_prefixes = [prefix for prefix in prefixes if prefixes[prefix] == len(strs)]
    if filtered_prefixes:
        return sorted(filtered_prefixes, key = lambda x: len(x), reverse = True)[0]
    else:
        return ''

# Given by instructor
def longest_common_prefix_solved(strs: list[str]) -> str:
    sorted_strs = sorted(strs)
    first = sorted_strs[0]
    last = sorted_strs[-1]
    
    prefix = ''
    for index in range(min(len(first), len(last))):
        if first[index] == last[index]:
            prefix += first[index]
        else:
            break
    return prefix

tests = [
    dict(
        strs = ['flower', 'flow', 'flight'],
        output = 'fl'
    ),
    dict(
        strs = ['dog', 'racecar', 'car'],
        output = ''
    )
]

for func in [longest_common_prefix, longest_common_prefix_solved]:
    print(func.__name__)
    for test in tests:
        result = func(test['strs'])
        print(result == test['output'])
