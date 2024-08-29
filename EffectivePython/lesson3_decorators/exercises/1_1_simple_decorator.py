from collections import abc

def herald_function(func: abc.Callable):
    def wrapper():
        print('Före funktionen')
        func()
        print('Efter funktionen')
    return wrapper

@herald_function
def dummy_func():
    print('Hello World!')


if __name__ == '__main__':
    dummy_func()