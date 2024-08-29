tal = int(input('Skriv ett heltal: '))

if (tal % 2) == 0:
    print('Talet är jämnt.')
    if (tal % 3 == 0) and (tal % 5 == 0):
        print('Talet är en multipel av 2*3*5')
else:
    print('Talet är udda.')

