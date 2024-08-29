lookfor = input('Skriv ett ord att leta efter: ')
with open('sample.txt') as f:
    for line in f:
        if lookfor in line:
            print(line.replace('\n',''))