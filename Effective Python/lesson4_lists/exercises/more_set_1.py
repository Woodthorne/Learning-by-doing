words = 'apple banana avocado'.split()
unique_chars = {char for word in words for char in word}
print(unique_chars)
