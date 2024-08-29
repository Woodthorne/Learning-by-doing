from collections import abc

def handle_function(func: abc.Callable):
    def wrapper():
        try:
            func()
        except:
            print('Something went wrong.')
    return wrapper

@handle_function
def dummy_func():
    print('Hello World!')
    1 / 0

if __name__ == '__main__':
    dummy_func()