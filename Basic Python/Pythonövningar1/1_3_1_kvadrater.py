val = input('Vill du räkna ut en kvadrat(1) eller kvadratrot(2)? ').lower()
tal = int(input('Mata in ett heltal: '))
if val == '1' or val == 'kvadrat':
    print(f'Kvadraten av {tal} är {tal * tal}')
elif val == '2' or val == 'kvadratrot':
    import math
    print(f'Kvadratroten av {tal} är {math.sqrt(tal)}')