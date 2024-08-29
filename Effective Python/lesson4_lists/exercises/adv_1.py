filtered_squares = [num ** 2 for num in range(1, 101) if num % 2 == 0 and num % 4 == 0 and num % 8 != 0]
print(filtered_squares)