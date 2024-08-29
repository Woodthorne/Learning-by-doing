def convert_raw_chipotle(source: str) -> None:
    def get_food_weight(weight: str) -> float:
        pounds = int(weight.split('.')[0])
        ounces = int(weight.split('.')[1])
        grams = int(weight.split('.')[2])
        float_weight = pounds * 453.59 + ounces * 28.35 + grams
        return float_weight  
        

    with open(source, 'r', encoding='utf-8') as f:
        data = f.readlines()

    store_id = -1
    for row in data:
        clean_row = row.replace('\n', '')
        split_row = clean_row.split('\t')
        burrito = split_row[0]
        bowl = split_row[1]
        chips = split_row[2]
        order = split_row[3]
        meat = split_row[4]
        store = split_row[6]
                
        if store != '':
            store_id += 1
        
        if order == 'Person':
            order = 0
        elif order == 'Online':
            order = 1
        
        if meat == 'Chicken':
            meat = 0
        elif meat == 'Carnitas':
            meat = 1
        
        with open('chipotle.csv', 'a', encoding='utf-8') as f:
            if burrito != '':
                food = 0
                weight = get_food_weight(burrito)
            elif bowl != '':
                food = 1
                weight = get_food_weight(bowl)
            f.write(f'{food},{order},{meat},{weight},{store_id}\n')
            if chips != '':
                weight = get_food_weight(chips)
                f.write(f'2,{order},,{weight},{store_id}\n')

convert_raw_chipotle('chipotle_raw.txt')

# Food,Order,Meat,Weight,Store
