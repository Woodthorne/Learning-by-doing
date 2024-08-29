list_of_lines = []
with open('sample.txt','r') as f:
    for line in f:
        list_of_lines.append(line.lower().strip('.\n').split())

print(list_of_lines)

dict_of_words = {}
wordcount = 0
for line in list_of_lines:
    for word in line:
        wordcount += 1
        if word in dict_of_words.keys():
            dict_of_words[word] += 1
        else:
            dict_of_words[word] = 1

print(f'Antalet ord: {wordcount}')
print(f'Antalet unika ord: {len(dict_of_words.keys())}')
print('Frekvensen av varje ord: ')
for key in dict_of_words.keys():
    print(f'{key}: {dict_of_words[key]}')