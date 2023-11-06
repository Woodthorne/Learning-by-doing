def isprime(num):
    if num == 2:
        return True
    all_primes = [2]
    for n in range(2,num // 2):
        prime = True
        for divisor in all_primes:
            if n % divisor == 0:
                prime = False
        if prime:
            all_primes.append(n)
            if num % divisor == 0:
                return False

    for divisor in all_primes:
        if num % divisor == 0:
            prime = False
    return prime

if __name__ == '__main__':
    print(isprime(int(input())))