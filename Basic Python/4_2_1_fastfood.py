import time

menu = {1:['Vanlig burgare',25,0,1],
        2:['Ostburgare',39,0,1],
        3:['Dubbelburgare',55,0,1],
        4:['Varmkorv',20,0,2],
        5:['Pizza Margherita',100,0,3],
        6:['Pizza Vesuvio',110,0,3],
        7:['Pizza Funghi',110,0,3],
        8:['Kebab pizza',125,0,4],
        9:['Pizza Salami',135,0,3],
        10:['Falafel-talrik',95,1,5],
        11:['Lövbiff',130,2,6],
        12:['Kycklingspett',110,0,0],
        13:['Schnitzel',120,3,0],
        14:['Chicken Nuggets',95,4,0],
        15:['Grillad Kyckling',115,5,0],
        16:['Vego sallad',100],
        17:['Bönburrito',90],
        18:['Bön-bowl',110]}

required = {1:['ris','pommes frites',0],
            2:['bearnaisesås','vitlökssås','vitlökssmör',0],
            3:['remouladsås','majonäs',0],
            4:['sweet and sour dipp','BBQ dipp','taco dipp','vitlök dipp','Szechuan dipp',0],
            5:['pommes frites','potatismos',0]}

custom = {1:['gurka',0,'ketchup/senap',0],
          2:['ketchup',0,'senap',0,'rostad lök',5,'räksallad',15],
          3:['jalapeno',10,'extra ost',10,'bacon',10,'oliver',10,'extra kebab',25,'extra skinka',25],
          4:['vit sås',0,'röd sås',0,'jalapeno',10,'extra ost',10,'bacon',10,'oliver',10,'extra kebab',25,'extra skinka',25],
          5:['röd sås',0,'vit sås',0,'lök',0],
          6:['extra lövbit',50]}

receipt = []

print('====VÄLKOMMEN TILL KODAR-KRUBB====')
while True:
    print('____Meny____')
    for item in menu.keys():
        print(f'{item}: {menu[item][0]}: {menu[item][1]} kronor')
    opt = input('Skriv nummer för önskad matträtt eller betala för att avsluta beställning: ').lower()
    if opt.isnumeric():
        opt = int(opt)
        if opt in menu.keys():
            if 'burgare' in menu[opt][0].lower():
                veggie = input('Önskas vegetariskt alternativ?(j/n) ').lower()
                if veggie == 'j':
                    receipt.extend([f'{menu[opt][0]} (vegetarisk)',menu[opt][1]])
            elif 'pizza' in menu[opt][0].lower() and int(time.strftime("%H", time.localtime())) in [11,12]:
                    if 'kebab' in menu[opt][0].lower():
                        receipt.extend([menu[opt][0],menu[opt][1]-15])
                    else:
                        receipt.extend([menu[opt][0],menu[opt][1]-20])
            else:
                receipt.extend([menu[opt][0],menu[opt][1]])
            if menu[opt][2] != 0:
                category = required[menu[opt][2]]
                selecting = True
                extra_dip = False
                while True:
                    option = 0
                    print('Välj tillbehör bland',end='')
                    while option < len(category)-1:
                        print(f' ({option+1}){category[option]}',end='')
                        if option == len(category)-2:
                            print('.',end='')
                        else:
                            print(',',end='')
                        option += 1
                    selection = input()
                    if selection.isnumeric():
                        option = 0
                        while option < len(category)-1:
                            if int(selection)-1 == option:
                                if extra_dip == 'j':
                                    receipt.extend([f' - m. {category[option]} (extra)',category[-1]+5])
                                else:
                                    receipt.extend([f' - m. {category[option]}',category[-1]])
                                selecting = False
                                break
                            option += 1
                        if 'nugget' in menu[opt][0].lower():
                            extra_dip = input('Önskas extra dipp för 5 kr?(j/n) ').lower()
                    if extra_dip == 'j':
                        continue
                    if not selecting:
                        break
                    print('Felakting inmatning.')
            if menu[opt][3] != 0:
                category = custom[menu[opt][3]]
                option = 0
                while option < len(category):
                    addon = input(f'Önskas {category[option]} för {category[option+1]} kr extra?(j/n) ').lower()
                    if addon == 'j':
                        receipt.extend([f' - m. {category[option]}',category[option+1]])
                    option += 2
    elif opt == 'betala':
        break

item = 0
price = 0
while item < len(receipt):
    print(f'{receipt[item]}: {receipt[item+1]} kr')
    price += receipt[item+1]
    item += 2
print(f'Total kostnad {price} kr')