N = int(input('Mata in ett högsta värde (minimum 3): '))
all_primes = [2]
for num in range(2,N):
    prime = True
    for divisor in all_primes:
        if num % divisor == 0:
            prime = False
    if prime:
        all_primes.append(num)
print(all_primes)