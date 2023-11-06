word = input('Mata in en sträng bokstaver: ').upper()
if not word.isalpha():
    print('Bara bokstäver tillåtna.')
    quit()
else:
    code_word = ''
    char_index = 0
    check = word[0]
    char_count = 0
    while char_index <= len(word)-1:
        if word[char_index] == check:
            char_index += 1
            char_count += 1
        else:
            code_word += str(char_count) + check
            check = word[char_index]
            char_count = 0
    code_word += str(char_count) + check
    print(code_word)