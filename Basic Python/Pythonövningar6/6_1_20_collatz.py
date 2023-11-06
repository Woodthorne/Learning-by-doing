def collatz(n):
    steps = 0
    if n < 1:
        return 'Något har gått fel.'
    elif n == 1:
        return steps
    elif n % 2 == 0:
        n /= 2
        steps += 1
    else:
        n = n * 3 + 1
        steps += 1
    steps += collatz(n)
    return steps

if __name__ == '__main__':
    print(collatz(3))