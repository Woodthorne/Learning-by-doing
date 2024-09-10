import string

def hash_1(source: str) -> int:
    return sum([ord(char) for char in source])

def hash_1b(source: str, size: int) -> int:
    return hash_1(source) % size

def hash_2(source: str) -> int:
    return sum([ord(char) ** (index + 1) for index, char in enumerate(source)])

def hash_2b(source: str, size: int) -> int:
    return hash_2(source) % size

def char_tumblers(count: int):
    if count != 0:
        for chars in char_tumblers(count - 1):
            for char in string.ascii_lowercase:
                yield char + chars
    yield ''

for func in [hash_1b, hash_2b]:
    print('===', func.__name__, '===')
    for length in range(6):
        source = string.ascii_lowercase[:length]
        hashed = func(source, 208)
        total_count = 0
        similar_count = 0
        for chars in char_tumblers(length):
            total_count += 1
            if func(chars, 208) == hashed:
                # print(chars, hashed)
                similar_count += 1
        print(length, ':', similar_count, '/', total_count, '=', '{:.2f}'.format(100 * similar_count / total_count) + '%')
