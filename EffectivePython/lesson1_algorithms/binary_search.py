items = [1,2,2,4,8,12,13,13,14,17,19,22,23,33,43,44]

def binary_search(target: int, items: list[int]):
    first = 0
    last = len(items) - 1

    while not first > last:
        mid = (first + last) // 2
        if items[mid] == target:
            return True
        elif items[mid] < target:
            first = mid + 1
        elif items[mid] > target:
            last = mid - 1
    return False

if __name__ == '__main__':
    while True:
        target = int(input('Search for integer: '))
        if binary_search(target, items):
            print('Target found!')
        else:
            print('Target not found!')