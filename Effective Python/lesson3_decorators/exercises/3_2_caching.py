from collections import abc

def cacher(func: abc.Callable):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print('Using cache: ', end='')
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cacher
def dummy_func(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    print(dummy_func(1,2))
    print(dummy_func(1,2))
    print(dummy_func(2,1))
    print(dummy_func(3,4))
    print(dummy_func(2,1))