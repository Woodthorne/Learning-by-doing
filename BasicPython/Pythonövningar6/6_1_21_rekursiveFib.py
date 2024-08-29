fib_seq={1:0,2:1}

def recfib(n,m=1):
    if n < m:
        print('Ett fel har uppstått.')
        quit()
    if n == 1:
        return {1:0}
    elif n == 2:
        return {1:0,2:1}
    if n in fib_seq.keys():
        return fib_seq.values()
    elif m not in fib_seq.keys():
        fib_seq[m] = fib_seq[m-1] + fib_seq[m-2]
    if n != m:
        recfib(n,m+1)
    return fib_seq

if __name__ == '__main__':
    print(recfib(3))