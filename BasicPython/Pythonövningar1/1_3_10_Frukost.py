mat1 = input('Vad är en sak som du äter till frukost? ').lower()
mat2 = input('Vad är en annan sak som du äter till frukost? ').lower()
mat3 = input('Vad är en tredje sak som du äter till frukost? ').lower()

danmat1 = 'smörgås'
danmat2 = 'yoghurt'
danmat3 = 'fil'

if mat1 == danmat1 or mat1 == danmat2 or mat1 == danmat3:
    print(f'Till frukost åt du {mat1} (samma här!), ', end='')
else:
    print(f'Till frukost åt du {mat1}, ', end='')

if mat2 == danmat1 or mat2 == danmat2 or mat2 == danmat3:
    print(f'{mat2} (jag också!) ', end='')
else:
    print(f'{mat2} ', end='')

if mat3 == danmat1 or mat3 == danmat2 or mat3 == danmat3:
    print(f'och {mat3} (jag också!).')
else:
    print(f'och {mat3}.')