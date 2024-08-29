from collections import abc

def call_count(func: abc.Callable):
    counter = 0
    def wrapper():
        nonlocal counter
        counter += 1
        print('Function called', counter, 'times.')
        func()
    return wrapper

@call_count
def dummy_func():
    print('Hello World!')

if __name__ == '__main__':
    for _ in range(10):
        dummy_func()
    