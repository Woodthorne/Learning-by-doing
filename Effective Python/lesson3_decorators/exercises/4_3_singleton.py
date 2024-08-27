from collections import abc

class Thing:
    def __init__(self) -> None:
        pass

def singleton(func: abc.Callable):
    def wrapper():
        result = func()
        global_content = list(globals().values())
        for item in global_content:
            if type(item) == type(result):
                return None
        return result
    return wrapper

@singleton
def dummy_func():
    return Thing()


if __name__ == '__main__':
    thing1 = dummy_func()
    thing2 = dummy_func()
    print(thing1)
    print(thing2)