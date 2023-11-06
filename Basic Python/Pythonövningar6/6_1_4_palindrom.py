def ispalindrome(word):
    word = ''.join(word.split(' ')).lower()
    drow = ''.join(list(reversed(word)))
    return word == drow

if __name__ == '__main__':
    print(ispalindrome(input('Skriv för att testa om palindrom: ')))