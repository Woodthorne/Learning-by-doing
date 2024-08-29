MY_NAME = 'Daniel'.upper()
MY_AGE = 30
MY_HOBBY = 'spel'
name = input('Skriv in ditt namn: ').upper()
age = int(input('Skriv in din ålder: '))
hobby = input('Skriv in din favorithobby: ').lower()
print(f'Hejsan {name}, mitt namn är {MY_NAME}.')

print(f'Du är {age} år gammal och jag är {MY_AGE}.')
if  age < MY_AGE:
    print(f'Du är {MY_AGE - age} år yngre än mig.')
elif age > MY_AGE:
    print(f'Du är {age - MY_AGE} år äldre än mig.')
else:
    print('Vi är lika gammla!')

if hobby == MY_HOBBY:
    print(f'Vi gillar {hobby} båda två!')
else:
    print(f'Jag gillar {MY_HOBBY} och du gillar {hobby}.')
    
print(f'Trevligt att pratas vid {name}, hoppas vi hörs snart igen!')
