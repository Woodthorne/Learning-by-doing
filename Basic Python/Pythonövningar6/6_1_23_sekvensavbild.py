def odd_and_even(cap):
    odd = ''
    even = ''
    for num in range(1,cap+1):
        if num % 2 == 0:
            even += f'{num} '
        else:
            odd += f'{num} '
    return [even.strip(),odd.strip()]

print(odd_and_even(10))