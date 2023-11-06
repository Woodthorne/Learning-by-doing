var = input('Skriv en mening: ')
if var != '':
    varList = var.split()
    print(f'Du har skrivit {len(varList)} ord.')
    if varList[0][0].isupper() and varList[-1][-1] == '.':
        print('Din mening började korrekt med stor bokstav och slutade med punkt.')