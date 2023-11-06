var = input('Skriv in en mening: ')
if var == '':
    print('Jaha, skit i det då!')
elif var == ' ':
    print('Spacit!!!')
elif var[0:2] == 'He':
    print('He........!')
elif var[-1] == '.':
    print('Korrekt avslut!')
elif len(var) > 24:
    print('Oj, du va en produktiv jäkel!')
elif var[0] == var[-1]:
    print(var[1:-1])
elif var.count('a') == 3 or var.count('b') == 4 or var.count('c'):
    print('aaa eller bbbb eller cc min kära användare!')
elif var.isupper():
    print('BIG LETTERS!')