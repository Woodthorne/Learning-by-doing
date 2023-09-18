import time

#        All items on the menu. Key is its number on the menu. Index 0 in the list is its name, 1 is price
#        in sek, 2 is a reference to the dictionary 'required', 3 is a reference to the dictionary 'custom'.
menu = {1:['Hamburger',25,0,1],
        2:['Cheeseburger',39,0,1],
        3:['Doubleburger',55,0,1],
        4:['Hotdog',20,0,2],
        5:['Pizza Margherita',100,0,3],
        6:['Pizza Vesuvio',110,0,3],
        7:['Pizza Funghi',110,0,3],
        8:['Pizza Kebab',125,0,4],
        9:['Pizza Salami',135,0,3],
        10:['Falafel',95,1,5],
        11:['Cube Steak',130,2,6],
        12:['Chicken Skewer',110,0,0],
        13:['Schnitzel',120,3,0],
        14:['Chicken Nuggets',95,4,0],
        15:['Grilled Chicken',115,5,0],
        16:['Vegetarian Salad',100],
        17:['Bean Burrito',90],
        18:['Bean Bowl',110]}

#        A dictionary containing all the required choices for certain menu items. Key is a reference number
#        for the dictionary 'menu' to reference. Index -1 adds nothing by default to all options. All prior
#        indeces are the individual options.
required = {1:['rice','french fries',0],
            2:['bearnaise sauce','garlic sauce','garlic butter',0],
            3:['remoulade','mayonnaise',0],
            4:['sweet and sour dip','BBQ dip','taco dip','garlic dip','szechuan dip',0],
            5:['french fries','mashed potatoes',0]}

#        A dictionary containing all the optional addons for certain menu items. Key is a reference number
#        for the dictionary 'menu' to reference. All even indeces are the names of the addons themselves,
#        whereas the following odd indeces are their price in sek.
custom = {1:['pickles',0,'ketchup/mustard',0],
          2:['ketchup',0,'mustard',0,'fried onions',5,'shrimp salad',15],
          3:['jalapeno',10,'extra cheese',10,'bacon',10,'olives',10,'extra kebab',25,'extra ham',25],
          4:['vhite sauce',0,'red sauce',0,'jalapeno',10,'extra cheese',10,'bacon',10,'olives',10,'extra kebab',25,'extra ham',25],
          5:['red sauce',0,'white sauce',0,'onions',0],
          6:['extra steak',50]}

#        Initialises an empty receipt.
receipt = []

print('====WELCOME TO BIT-BITES====')
while True:

    #        First loops through the keys of dictionary 'menu' and prints out the menu row by row.
    print('____Menu____')
    for item in menu.keys():
        print(f'{item}: {menu[item][0]}: {menu[item][1]} sek')

    #        Takes input and stores it as the relevant dictionary key.
    opt = input("Input desired item # or 'pay' to finish order: ").lower()
    if opt.isnumeric():
        opt = int(opt)
        if opt in menu.keys():

            #        Checks if a burger is ordered, and applies vegetarian option if relevant.
            if 'burger' in menu[Opt][0].lower():
                veggie = input('Vegetarian option?(y/n) ').lower()
                if veggie == 'y':
                    receipt.extend([f'{menu[Opt][0]} (vegetarisk)',menu[Opt][1]])

            #        Checks if a pizza is ordered, and applies lunch hour rates if relevant. (between 11am and 12am)
            elif 'pizza' in menu[Opt][0].lower() and int(time.strftime("%H", time.localtime())) in [11,12]:
                    #        Kebab pizza has a separate lunch hour difference.
                    if 'kebab' in menu[Opt][0].lower():
                        receipt.extend([menu[Opt][0],menu[Opt][1]-15])
                    else:
                        receipt.extend([menu[Opt][0],menu[Opt][1]-20])
            else:
                receipt.extend([menu[Opt][0],menu[Opt][1]])

            #        Checks if the ordered item has required choices to make.
            if menu[Opt][2] != 0:
                category = required[menu[Opt][2]]
                selecting = True
                extra_dip = False        # Nuggets has a special case where additional dips can be ordered
                while True:
                    option = 0
                    print('Choose a side among',end='')
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
                                if extra_dip == 'y':        # Checks if we are adding an additional dip
                                    receipt.extend([f' - w. {category[option]} (extra)',category[-1]+5])
                                else:
                                    receipt.extend([f' - w. {category[option]}',category[-1]])
                                selecting = False
                                break
                            option += 1
                        if 'nugget' in menu[opt][0].lower():
                            extra_dip = input('Would you like an extra dip for 5 sek?(y/n) ').lower()
                    if extra_dip == 'y':
                        continue
                    if not selecting:
                        break
                    print('Unexpected input.')

            #        Checks if optional addons are available for the ordered item.
            if menu[opt][3] != 0:
                category = custom[menu[opt][3]]
                option = 0
                while option < len(category):
                    addon = input(f'Would you like to add {category[option]} for {category[option+1]} sek extra?(y/n) ').lower()
                    if addon == 'y':
                        receipt.extend([f' - w. {category[option]}',category[option+1]])
                    option += 2

    #        Checks if user has decided to end the loop and pay for their order.
    elif opt == 'pay':
        break

item = 0
price = 0
while item < len(receipt):
    print(f'{receipt[item]}: {receipt[item+1]} sek')
    price += receipt[item+1]        # Calculates final price.
    item += 2
print(f'Total price {price} sek')
