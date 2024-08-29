N = int(input('Mata in hur många fibonaccis tal du vill se: '))
fib_seq = [0,1]
if N == 1:
    print([0])
elif N == 2:
    print(fib_seq)
elif N > 2:
    while N > 2:
        fib_seq.append(fib_seq[-2]+fib_seq[-1])
        N -= 1
    print(fib_seq)