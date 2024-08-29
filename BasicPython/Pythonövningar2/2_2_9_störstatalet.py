num1 = input('Ange tal 1: ')
num2 = input('Ange tal 2: ')
num3 = input('Ange tal 3: ')

if num1 >= num2 and num1 >= num3:
    print('Det första talet är störst.')
elif num2 >= num3:
    print('Det andra talet är störst.')
else:
    print('Det tredje talet är störst')