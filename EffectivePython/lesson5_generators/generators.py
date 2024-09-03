def example_gen(end: int):
    for num in range(end):
        yield(num)

for num in example_gen(10):
    print(num)

def fib_gen():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b

fibs = iter(fib_gen())
for _ in range(10):
    print(next(fibs))
