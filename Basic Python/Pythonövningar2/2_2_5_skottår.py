year = int(input('Ange ett årtal: '))
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print('Det är skottår, det bör vi fira!')
    else:
        print('Tusan också att det inte är skottår då!')
else:
    print('Tusan också att det inte är skottår då!')