print('Skriv in tre heltal!')
num1 = int(input('Skriv tal 1: '))
num2 = int(input('Skriv tal 2: '))
num3 = int(input('Skriv tal 3: '))

print('======================================================')
print(f'Att {num1} är större än {num2} är {num1 > num2}')
print(f'Att {num2} är större än {num3} är {num2 > num3}')
print(f'Att {num3} är större än {num1} är {num3 > num1}')

if num1 >= num2:
    if num2 >= num3:
        print(f'Deras storleksordning från störst till minst är {num1}, {num2}, {num3}')
    elif num1 >= num3:
        print(f'Deras storleksordning från störst till minst är {num1}, {num3}, {num2}')
    else:
        print(f'Deras storleksordning från störst till minst är {num3}, {num1}, {num2}')
elif num1 >= num3:
    print(f'Deras storleksordning från störst till minst är {num2}, {num1}, {num3}')
elif num2 >= num3:
    print(f'Deras storleksordning från störst till minst är {num2}, {num3}, {num1}')
else:
    print(f'Deras storleksordning från störst till minst är {num3}, {num2}, {num1}')

if num1 == num2 or num2 == num3 or num2 == num3:
    print('Det ser ut som att några tal är lika.')

print(f'Medelvärdet av {num1}, {num2} och {num3} är {(num1+num2+num3)/3}')

if num1 < 0 or num2 < 0 or num3 < 0:
    print('Du har använt dig av negativa tal!')