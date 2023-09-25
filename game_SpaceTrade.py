# This is a computer game based on a tabletop game I made to be about a year ago.
# The objective of the game is to buy and sell goods, trying to make enough profit
# to be the first to retire wealthy.

# For those familiar with the tabletop game (I don't really know who it would include)
# this version plays with the planet row option to simplify movement, and also comes
# with the option of having a automatic bot-player join as well.

import random

dict_goods = {'foodstuffs':2,
              'materials':2,
              'technologies':3,
              'entertainments':4,
              'luxuries':6}

dict_planets = {'space station':{},
                'techon'  :{'technologies':-2,
                            'entertainments':-2,
                            'foodstuffs':2},
                'glamille':{'entertainments':-2,
                            'luxuries':-2,
                            'materials':2},
                'automic' :{'luxuries':-2,
                            'foodstuffs':-2,
                            'technologies':2},
                'grunto'  :{'foodstuffs':-2,
                            'materials':-2,
                            'entertainments':2},
                'laboria' :{'materials':-2,
                            'technologies':-2,
                            'luxuries':2},
                'robosol' :{'foodstuffs':-2,
                            'technologies':-2,
                            'materials':2},
                'bultor'  :{'materials':-2,
                            'entertainments':-2,
                            'technologies':2},
                'misera'  :{'technologies':-2,
                            'luxuries':-2,
                            'entertainments':2},
                'beverill':{'entertainments':-2,
                            'foodstuffs':-2,
                            'luxuries':2},
                'monor'   :{'luxuries':-2,
                            'materials':-2,
                            'foodstuffs':2}}

dict_players = {}

unused_planets = []
for planet in dict_planets.keys():
    if planet != 'space station':
        unused_planets.append(planet)
planet_system = ['space station']
while len(planet_system) < 7:
    planet_system.append(unused_planets.pop(random.randint(0,len(unused_planets)-1)))

supply_goods = []
for good in dict_goods.keys():
    count = 0
    while count < 5:
        supply_goods.append(good)
        count += 1

def bot_turn(player, victory_condition):
    location = dict_players[player][0]
    credits = dict_players[player][1]
    cargo = dict_players[player][2]

    print(f'====== NEW TURN - Bot ===========')    

    # Bot moves
    destination = random.randint(1,3)
    if location + destination < len(planet_system):
        destination = location + destination
    else:
        destination = location - destination
    print(f'{player.capitalize()} moves from {planet_system[location]} to {planet_system[destination]}')
    location = destination

    # Bot sells
    market_prices = establish_market(location)
    selling = []
    for item in cargo:
        if market_prices[item] > dict_goods[item]:
            credits += market_prices[item]
            cargo.remove(item)
            supply_goods.append(item)
            selling.append(item)
    print(f'{player.capitalize()} sells',end=' ')
    for item in selling:
        print(item,end=' ')
    print()

    # Bot buys
    market_goods = []
    buying = []
    while len(market_goods) < 5:
        market_goods.append(supply_goods.pop(random.randint(0,len(supply_goods)-1)))
    for item in market_goods:
        if market_prices[item] <= dict_goods[item] and len(cargo) < 5 and not market_prices[item] > credits:
            credits -= market_prices[item]
            cargo.append(item)
            market_goods.remove(item)
            buying.append(item)
    supply_goods.extend(market_goods)
    print(f'{player.capitalize()} buys',end=' ')
    for item in buying:
        print(item,end=' ')
    print()

    # Bot ends
    print(f'{player.capitalize()} has {credits} credits')
    if credits < victory_condition:
        return False
    else:
        return True

def buying(location, credits, cargo):
    market_prices = establish_market(location)
    market_goods = []
    while len(market_goods) < 5:
        market_goods.append(supply_goods.pop(random.randint(0,len(supply_goods)-1)))
    buying = True
    while buying == True and len(market_goods) > 0:
        market_count = 1
        print(f'You have {credits} credits and the following goods are available for sale at the market:')
        for good in market_goods:
            print(f'{market_count}. {good.capitalize()}: {market_prices[good]} credits')
            market_count += 1
        option = input("Choose the number of the item you wish to buy, or 'done' if you are done: ")
        if option == 'done':
            buying = False
        elif option.isnumeric():
            if int(option)-1 < len(market_goods):
                option = int(option)-1
                if market_prices[market_goods[option]] > credits:
                    print('You do not have enough credits. Press ENTER to return to market.')
                else:
                    bought = market_goods.pop(option)
                    credits -= market_prices[bought]
                    cargo.append(bought)
        else:
            input('Invalid option. Press ENTER to try again.')
    supply_goods.extend(market_goods)
    return credits, cargo

def end_turn(cargo, credits, victory_condition):
    print(f'You prepare to leave the planet with your credits ({credits}) and',end=' ')
    if len(cargo) > 0:
        print('the contents of your cargo hold:')
        for good in cargo:
            print(good.capitalize())
    else:
        print('an empty cargo hold.')

    if credits < victory_condition:
        return False
    else:
        return True

def establish_market(location):
    market_prices = dict_goods.copy()
    for good in dict_planets[planet_system[location]].keys():
        market_prices[good] += dict_planets[planet_system[location]][good]
    return market_prices    

def main():
    start_game()
    active_player = 0
    victory = False
    victory_condition = 10
    while not victory:
        if active_player == 'bot':
            active_player = 1
        else:
            active_player += 1
        if active_player not in dict_players.keys():
            active_player = 'bot'
        if active_player == 'bot':
            victory = bot_turn(active_player, victory_condition)
        else:
            victory = player_turn(active_player, victory_condition)
    print(f'Congratulations player {active_player}! You won!')

def movement(origin):
    moved = False
    move_dice = random.randint(1,3)
    for planet in planet_system:
        print(planet.capitalize(),end=' ')
        if origin == planet_system.index(planet):
            print('<--YOU ARE HERE')
        else:
            print()
    while not moved:
        destination = input(f'You are able to move {move_dice} steps this turn. Where would you like to go? ').lower()
        if destination in planet_system:
            if abs(planet_system.index(destination) - origin) > move_dice:
                print('That destination is beyond your reach. Try again.')
            else:
                return planet_system.index(destination)
        else:
            print('That destination does not exist. Try again.')

def player_turn(player, victory_condition):
    location = dict_players[player][0]
    credits = dict_players[player][1]
    cargo = dict_players[player][2]

    print(f'====== NEW TURN - Player {player} ======')
    location = movement(location)
    credits, cargo = selling(location, credits, cargo)
    credits, cargo = buying(location, credits, cargo)
    dict_players[player][0] = location
    dict_players[player][1] = credits
    dict_players[player][2] = cargo
    return end_turn(cargo, credits, victory_condition)

def selling(location, credits, cargo):
    market_prices = establish_market(location)
    print(f'You arrive at the market in {planet_system[location].capitalize()}.')
    if len(cargo) == 0:
        print('Your cargo holds are empty.')
    else:
        selling = True
        while selling == True and len(cargo) > 0:
            inventory_count = 1
            print(f'Your carry {credits} credits and the following cargo:')
            for good in cargo:
                print(f'{inventory_count}. {good}: {market_prices[good]} credits')
                inventory_count += 1
            option = input("Choose the number of the item you wish to sell, or 'done' if you are done: ")
            if option == 'done':
                selling = False
            elif option.isnumeric and int(option)-1 < len(cargo):
                option = int(option)-1
                sold = cargo.pop(option)
                credits += market_prices[sold]
                supply_goods.append(sold)
            else:
                input('Invalid option. Press ENTER to try again.')
    return credits, cargo

def start_game():
    while True:
        player_count = input('How many are playing? ')
        if player_count.isnumeric():
            if int(player_count) > 0:
                player_count = int(player_count)
                bot_playing = input('Do you wish to add a bot?(y/n) ').lower()
                if bot_playing == 'y':
                    dict_players['bot'] = [0,5,[]]
                break
            else:
                print('No players. Closing game.')
                quit()
        else:
            print('Invalid input. Needs to be an integer.')
    for player in range(player_count):
        dict_players[player+1] = [0,5,[]]

if __name__ == '__main__':
    main()