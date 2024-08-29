def is_prime(num: int):
    if num == 1:
        return False
    for divider in range(2, num - 1):
        if num % divider == 0:
            return False
    return True

prime_squares = [num ** 2 for num in range(1, 51) if is_prime(num)]
print(prime_squares)
