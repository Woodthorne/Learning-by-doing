# Code in progress

import math

charDict = {}
wordList = []

def stringPermutator(string):
    num_of_char = stringConverter(string)
    recStringPermutator(num_of_char)
    return wordList

def stringConverter(string):
    step = 1
    for char in string:
        charDict[step] = char
        step += 1
    return len(charDict)

def recStringPermutator(num_of_char,word=''):
    if len(wordList) == math.factorial(num_of_char):
        return
    elif len(word) == num_of_char:
        wordList.append(word)
        recStringPermutator(num_of_char)
    for num in charDict.keys():
        word += charDict[num]
        recStringPermutator(num_of_char,word)


print(stringPermutator('Hej'))