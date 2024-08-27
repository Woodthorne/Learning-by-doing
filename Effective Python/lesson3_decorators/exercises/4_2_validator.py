from collections import abc

def validator(req: type):
    def inner(func: abc.Callable):
        def wrapper(*args):
            for arg in args:
                if type(arg) != req:
                    raise Exception
            func(*args)
        return wrapper
    return inner

@validator(int)
def dummy_func(iter: int):
    for _ in range(iter):
        print('Hello World!')


if __name__ == '__main__':
    dummy_func(2)
    dummy_func('Hej')