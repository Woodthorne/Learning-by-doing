from collections import abc
from timeit import default_timer

def timer(func: abc.Callable):
    def wrapper():
        start_time = default_timer()
        func()
        end_time = default_timer()
        print('Time taken (seconds):', end_time - start_time)
    return wrapper

@timer
def dummy_func():
    for num in range(10_000):
        num ** num
    print('Hello World!')

if __name__ == '__main__':
    dummy_func()