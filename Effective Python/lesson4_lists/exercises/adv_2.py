words = 'Python is powerful and fun'.split()
some_initials = {word[0] for word in words if len(word) > 3}
print(some_initials)