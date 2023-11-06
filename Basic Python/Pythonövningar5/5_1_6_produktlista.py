all_products = {}

while True:
    print('___Meny___\n 1. Skapa ny produkt\n 2. Lista alla produkter\n 3. Avsluta')
    opt = input('Menyval: ')
    if opt == '1':
        new_id = input('Mata in önskat produkt-id (5 siffror): ')
        if new_id in all_products.keys():
            print('Produkt-id finns redan.')
            continue
        elif len(new_id) == 5 and new_id.isnumeric():
            all_products[new_id] = []
            all_products[new_id].append(input('Mata in produktens namn: '))
            all_products[new_id].append(input('Mata in produktens pris: '))
        else:
            print('Ogiltigt produkt-id.')
    elif opt == '2':
        print('Produkter:')
        for item in all_products.keys():
            print(f'{item}:{all_products[item][1]}:{all_products[item][0]}')
    elif opt == '3':
        quit()
    else:
        input('Felaktigt val. Tryck ENTER för att försöka igen.')