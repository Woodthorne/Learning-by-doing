def longest_common_prefix(strs: list[str]) -> str:
    prefixes = {}
    for word in strs:
        prefix = ''
        for char in word:
            prefix += char
            if prefix not in prefixes:
                prefixes[prefix] = 0
            prefixes[prefix] += 1
    sorted_prefixes = [sorted(prefix, key = lambda x: len(x), reverse = True) for prefix in prefixes if prefixes[prefix] > 1]
    if sorted_prefixes:
        return sorted_prefixes[0]
    else:
        return ''

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

for func in [longest_common_prefix]:
    print(func.__name__)
    for test in tests:
        result = func(test['strs'])
        print(result == test['output'])
