age = int(input('Ange ålder: '))
if age < 13:
    print('Personen är ett barn.')
elif 13 <= age < 20:
    print('Personen är en tonåring.')
elif 20 <= age < 67:
    print('Personen är vuxen.')
elif 67 <= age:
    print('Personen är pensionär.')