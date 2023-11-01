# This is a computer game based on a tabletop game I made to be about a year ago.
# The objective of the game is to buy and sell goods, trying to make enough profit
# to be the first to retire wealthy.

# For those familiar with the tabletop game (I don't really know who it would include)
# this version plays with the planet row option to simplify movement, and also comes
# with the option of having a automatic bot-player join as well.

import random


class Good:
    def __init__(self, name: str, base_price: int) -> None:
        self._name = name
        self._base_price = base_price

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def base_price(self) -> int:
        return self._base_price


class Supply:
    def __init__(self) -> None:
        self._all_goods: list[Good] = []
        for _ in range(0, 5):
            self._all_goods.append(Good('foodstuffs', 2))
            self._all_goods.append(Good('materials', 2))
            self._all_goods.append(Good('technologies', 3))
            self._all_goods.append(Good('entertainments', 4))
            self._all_goods.append(Good('luxuries', 6))

    def fetch_market(self) -> list[Good]:
        market: list[Good] = []
        random.shuffle(self._all_goods)
        while len(market) < 5:
            market.append(self._all_goods.pop(0))
        return market

    def return_market(self, market: list[Good]) -> None:
        self._all_goods.extend(market)

    # def grab_random_good(self):
    #    random.shuffle(self._all_goods)
    #    return self._all_goods[0]


class World:
    def __init__(self, name: str,
                       exports: list[str],
                       imports: list[str]) -> None:
        self._name = name
        self._exports = exports
        self._imports = imports

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def exports(self) -> list[str]:
        return self._exports
    
    @property
    def imports(self) -> list[str]:
        return self._imports


class Player:
    def __init__(self, name: str, human: bool) -> None:
        self._name = name
        self._is_human = human
        self._location_index: int = 0
        self._credits: int = 5
        self._cargo: list[Good] = []
    
    @property
    def name(self) -> str:
        return self._name

    @property
    def is_human(self) -> bool:
        return self._is_human
    
    @property
    def location_index(self) -> int:
        return self._location_index
    
    @property
    def credits(self) -> int:
        return self._credits
    

class Game:
    _world_names = ['Ezyria', 'Oclite', 'Stradus VI', 'Noxonov'
                    'Amustea', 'Trikanov', 'Veavis', 'Kalvarth']

    def __init__(self, player_amount: int, bot_amount: int) -> None:
        self._players: list[Player] = []
        self._worlds = [World('Station VBY-219', [], [])]
        self._supply = Supply()
        self._victory_condition: int = 15
        
        while len(self._players) < player_amount:
            player_num = len(self._players) + 1
            name = input(f'Input name of player #{player_num}: ')
            self._players.append(Player(name, True))
        for bot_num in range(0, bot_amount):
            self._players.append(Player(f'Bot #{bot_num}', False))
        
        while len(self._worlds) < 7:
            random.shuffle(self._world_names)
            name = self._world_names.pop(0)
            good_names = list(random.shuffle('foodstuffs',
                                             'materials',
                                             'technologies',
                                             'entertaiments',
                                             'luxuries'))
            exports = [good_names.pop(0), good_names.pop(0)]
            imports = [good_names.pop(0)]
            self._worlds.append(World(name, exports, imports))

        self._active_player = self._players[-1]
    
    def main(self) -> None:
        while self._no_victory():
            self._next_player()
            print(f'====== NEW TURN - Player {self._active_player.name} ======')
            if self._active_player:
                self._player_turn()
            else:
                bot_turn()
        print(f'Congratulations! Player {self._active_player.name} has won!')

    def _next_player(self) -> None:
        next_player_index = self._players.index(self._active_player) + 1
        if next_player_index == len(self._players):
            next_player_index = 0
        self._active_player = self._players[next_player_index]
    
    def _player_turn(self) -> None:
        location = self._player_movement()
        print(f'You arrive at the market in {self._worlds[self._active_player.location_index]}.')
        self._player_buy(location)

    def _player_movement(self) -> None:
        reach = random.randint(1, 3)
        for world in self._worlds:
            print(world, end='')
            if self._active_player.location_index == self._worlds.index(world):
                print(' <-- Current Location')
            else:
                print()
        print(f'You are able to move {reach} steps this turn.')
        while True:
            destination = input('Input name of destination: ').lower()
            for world in self._worlds:
                if (world.name.lower() == destination and not
                    abs(self._worlds.index(world) - self._active_player.location_index) > reach):
                    self._active_player.location_index = self._worlds.index(world)
                    destination = 'DONE'
            if destination == 'DONE':
                break
            else:
                print('Invalid destination.')
        return self._worlds[self._active_player.location_index]
    
    def _player_buy(self, location: World) -> None:
        market_inventory = self._supply.fetch_market()
        market: dict[str, list[int, str]] = {}
        for good in market_inventory:
            if good.name in location.exports:
                market[good.name] = [good.base_price - 2, ' Cheap!']
            elif good.name in location.imports:
                market[good.name] = [good.base_price + 2, ' Expensive!']
            else:
                market[good.name] = [good.base_price, '']
        
        for good in market_inventory:


                    

    def _no_victory(self):
        if self._active_player.credits < self._victory_condition:
            return True
        else:
            return False

def run():
    print('()=====(SPACE TRADERS)=====()')
    print('1. Start Game')
    print('2. Quit Game')
    while True:
        opt = input('>>> ')
        if opt == '1':
            break
        elif opt == '2':
            quit()
        else:
            print('Invalid option.')
    while True:
        player_amount = input('How many people are playing? ')
        if player_amount.isdecimal() and int(player_amount) > 0:
            break
        else:
            print('Invalid amount.')
    while True:
        bot_amount = input('How many bots would you like to add? ')
        if bot_amount.isdecimal():
            break
        else:
            print('Invalid amount.')
    game = Game(player_amount, bot_amount)
    game.main()

if __name__ == '__main__':
    run()
# ============================================================================
def _bot_turn(player, victory_condition):
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

def _player_turn(player, victory_condition):
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
