from collections import abc

def decorator_factory(message: str):
    def decorator(func: abc.Callable):
        def wrapper():
            print(message)
            func()
        return wrapper
    return decorator

@decorator_factory('Function called')
def dummy_func():
    print('Hello World!')

if __name__ == '__main__':
    dummy_func()