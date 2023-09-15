inventory = {1:['vindruvor',20,'klase',5,0],
             2:['vitlök',25,'st',5,0],
             3:['vattenmelon',70,'st',5,0],
             4:['mandarin',23,'kg',5,0],
             5:['citron',6,'st',5,0],
             6:['banan',28,'kg',5,0],
             7:['ananas',45,'st',5,0],
             8:['mango',30,'st',5,0],
             9:['äpple',32,'kg',5,0],
             10:['kiwi',7,'st',5,0],
             11:['tomat',26,'kg',5,0],
             12:['kokosnöt',60,'st',5,0],
             13:['avokado',13,'st',5,0],
             14:['äggplanta',20,'st',5,0],
             15:['potatis',13,'kg',5,0],
             16:['chilipeppar',199,'kg',5,0],
             17:['paprika',59,'kg',5,0],
             18:['broccoli',14,'st',5,0]}

specials = {'avokado':[3,30]}

orders_all = {}
order_id = 0

while True:
    print("ANDERSSON'S FRUKT OCH GRÖNT")
    print('Huvudmeny\n 1. Starta ny beställning\n 2. Skriv ut dagens beställningar\n 3. Avsluta dagen')
    opt = input('Menyval: ')
    if opt.isnumeric():
        opt = int(opt)
    if opt == 1:
        order_id += 1
        orders_all[order_id] = []
        while True:
            print("ANDERSSON'S FRUKT OCH GRÖNT")
            print('Ny beställning #',order_id)
            for item in inventory.keys():
                if inventory[item][0] in specials.keys():
                    print(f'{item}: {inventory[item][0]}: {inventory[item][1]} kr/{inventory[item][2]} ({inventory[item][3]} i lager) (rabatt: {specials[inventory[item][0]][0]} för {specials[inventory[item][0]][1]} kr)') 
                else:
                    print(f'{item}: {inventory[item][0]}: {inventory[item][1]} kr/{inventory[item][2]} ({inventory[item][3]} i lager)')
            opt = input("Varans # eller 'avsluta' för att avsluta beställning: ").lower()
            if opt == 'avsluta':
                break
            elif opt.isnumeric() and int(opt) in inventory.keys():
                opt = int(opt)
                if inventory[opt][0] in specials.keys():
                    print(f'RABATT: {specials[inventory[opt][0]][0]} för {specials[inventory[opt][0]][1]}')
                if inventory[opt][2] == 'kg':
                    print(f'Hur många kg {inventory[opt][0]} (max {inventory[opt][3]}) vill du lägga till i beställningen? ',end='')
                else:
                    print(f'Hur många {inventory[opt][0]} (max {inventory[opt][3]}) vill du lägga till i beställningen? ',end='')
                qty = input()
                if qty.isnumeric():
                    while True:
                        qty = int(qty)
                        if qty > inventory[opt][3]:
                            input('Otillräcklig mängd i lager. ENTER för att fortsätta.')
                        elif inventory[opt][0] in specials.keys() and qty > specials[inventory[opt][0]][0]:
                            inventory[opt][3] -= specials[inventory[opt][0]][0]
                            inventory[opt][4] += specials[inventory[opt][0]][0]
                            orders_all[order_id].extend([opt,specials[inventory[opt][0]][0],specials[inventory[opt][0]][1]])
                            qty -= specials[inventory[opt][0]][0]
                        elif qty == 0:
                            break
                        else:
                            inventory[opt][3] -= qty
                            inventory[opt][4] += qty
                            orders_all[order_id].extend([opt,qty,qty*inventory[opt][1]])
                            break
                else:
                    input('Felaktig inmatning. ENTER för att fortsätta.')
            else:
                input('Felaktig inmatning. ENTER för att fortsätta.')

        print(orders_all)

    elif opt == 2:
        for order in orders_all.keys():
            print('==============================')
            print('Beställning #',order)
            item = 0
            total = 0
            while item < len(orders_all[order]):
                print(f'{orders_all[order][item+1]}x {inventory[orders_all[order][item]][0]}: {orders_all[order][item+2]}')
                total += orders_all[order][item+2]
                item += 3
            print('Totalt pris:',total,'kr')
    elif opt == 3:
        print('Dagens sålda varor:')
        for item in inventory.keys():
            if inventory[item][4] != 0:
                print(f'{inventory[item][0]}: {inventory[item][4]} {inventory[item][2]} sålda')
        print('==============================')
        for item in inventory.keys():
            print(f'{inventory[item][0]}: {inventory[item][3]} {inventory[item][2]} i lager')
        quit()
    else:
        print('Felaktig inmatning. Försök igen.')