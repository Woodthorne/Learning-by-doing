from collections import abc

def arguments(func: abc.Callable):
    def wrapper(*args):
        print(func.__name__)
        for arg in args:
            print(arg)
        func(*args)
    return wrapper

@arguments
def dummy_func(instances: int):
    for _ in range(instances):
        print('Hello World!')

if __name__ == '__main__':
    dummy_func(10)