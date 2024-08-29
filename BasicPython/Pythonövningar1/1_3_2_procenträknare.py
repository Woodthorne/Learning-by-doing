num1 = float(input('Ange startvärde: '))
num2 = float(input('Ange nuvarande värde: '))
acc = int(input('Ange önskad precision i antal decimaler: '))

print(f'Värdet har förändrats med {round(100*(num2/num1), acc)} procent')