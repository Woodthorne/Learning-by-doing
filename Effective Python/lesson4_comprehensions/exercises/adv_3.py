sentence = 'Python comprehensions are powerful'
word_dict = {word: word[::-1] for word in sentence.split()}
print(word_dict)