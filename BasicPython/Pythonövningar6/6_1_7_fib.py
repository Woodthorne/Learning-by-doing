def fib(n):
    fib_seq = [0,1]
    if n == 1:
        return [0]
    elif n == 2:
        return fib_seq
    elif n > 2:
        while n > 2:
            fib_seq.append(fib_seq[-2]+fib_seq[-1])
            n -= 1
        return fib_seq
    
def recfib(n,m=0,fib_seq=[0,1]):
    if n < m:
        print('Ett fel har uppstått.')
        quit()
    elif m > len(fib_seq):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])    
    if n == m:
        return fib_seq[:n]
    else:
        return recfib(n,m+1,fib_seq)
    
if __name__ == '__main__':
    n = 7
    print(fib(n))
    print(recfib(n))