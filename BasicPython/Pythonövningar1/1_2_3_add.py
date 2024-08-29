print('Låt mig addera två heltal åt dig!')
num1 = input('Skriv in det första talet: ')
num2 = input('Skriv in det andra talet: ')
if num1.isnumeric() and num2.isnumeric():
    print(f'Summan av {num1} + {num2} är {int(num1)+int(num2)} !')
else:
    print(f'Du har inte anget två heltal.')