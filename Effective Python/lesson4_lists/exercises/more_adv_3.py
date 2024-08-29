chars = 'fghfgfhggfhggfhggfhfgghfgghghfgfgfffhg'
bigrams = {f'{chars[index]}{chars[index + 1]}': chars.count(f'{chars[index]}{chars[index + 1]}') for index in range(len(chars) - 1)}
print(bigrams)