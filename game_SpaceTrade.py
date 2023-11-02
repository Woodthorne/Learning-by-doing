'''
This is a computer game based on a tabletop game I made around 2020.
The objective of the game is to buy and sell goods, trying to make
enough profit to be the first to retire wealthy.

For those familiar with the tabletop game (I don't really know who it
would include) this version plays with the planet row option to simplify
movement, and also comes with the option of having a automatic bot-player
join as well.
'''

import random
import os


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

    @classmethod
    def create(cls) -> None:
        cls._all_goods: list[Good] = []
        for _ in range(0, 5):
            cls._all_goods.append(Good('foodstuffs', 2))
            cls._all_goods.append(Good('materials', 2))
            cls._all_goods.append(Good('technologies', 3))
            cls._all_goods.append(Good('entertainments', 4))
            cls._all_goods.append(Good('luxuries', 6))

    @classmethod
    def fetch_market(cls) -> list[Good]:
        market: list[Good] = []
        random.shuffle(cls._all_goods)
        while len(market) < 5:
            market.append(cls._all_goods.pop(0))
        market.sort(key = lambda x: x.name)
        return market

    @classmethod
    def return_market(cls, market: list[Good]) -> None:
        cls._all_goods.extend(market)
    
    @classmethod
    def return_good(cls, good: Good) -> None:
        cls._all_goods.append(good)


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


class WorldHandler:
    _worlds: list[World] = []
    _world_names = ['Ezyria', 'Oclite', 'Stradus VI', 'Noxonov',
                    'Amustea', 'Trikanov', 'Veavis', 'Kalvarth']

    @classmethod
    def create(cls) -> None:
        cls._worlds.append(World('Station VBY-219', [], []))
        while len(cls._worlds) < 7:
            random.shuffle(cls._world_names)
            name = cls._world_names.pop(0)
            goods = ['foodstuffs', 'materials', 'technologies',
                     'entertaiments', 'luxuries']
            random.shuffle(goods)
            exports = [goods.pop(0), goods.pop(0)]
            imports = [goods.pop(0)]
            cls._worlds.append(World(name, exports, imports))
    
    @property
    def worlds(cls) -> list[World]:
        return cls._worlds
        

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
    
    @location_index.setter
    def location_index(self, new_index) -> None:
        self._location_index = new_index

    @property
    def credits(self) -> int:
        return self._credits
    
    @property
    def cargo(self) -> list[Good]:
        return self._cargo
    
    def won(self, victory_condition: int) -> bool:
        if self._credits < victory_condition:
            return False
        else:
            return True
    
    def buy(self, good: Good, cost: int) -> None:
        self._credits -= cost
        self._cargo.append(good)
        self._cargo.sort(key = lambda x: x.name)
    
    def sell(self, index: int, cost: int) -> None:
        Supply().return_good(self._cargo.pop(index))
        self._credits += cost


class PlayerHandler:
    def __init__(self, player_amount: int, bot_amount: int) -> None:
        self._players: list[Player] = []
        
        while len(self._players) < player_amount:
            player_num = len(self._players) + 1
            name = input(f'Input name of player #{player_num}: ')
            self._players.append(Player(name, True))
        for bot_num in range(1, bot_amount + 1):
            self._players.append(Player(f'Bot #{bot_num}', False))
        
        self._active_player_index: int = -1

    def next_player(self) -> Player:
        self._active_player_index += 1
        if self._active_player_index == len(self._players):
            self._active_player_index = 0
        return self._players[self._active_player_index]
    
    def active_player(self) -> Player:
        return self._players[self._active_player_index]


def run():
    new_screen()
    print('()=====(SPACE TRADERS)=====()')
    print('1. Start Game')
    print('2. Quit Game')
    while True:
        opt = input('>>> ')
        if opt == '1':
            new_screen()
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
    new_screen()
    main(int(player_amount), int(bot_amount))

def main(player_amount: int, bot_amount: int) -> None:
    players = PlayerHandler(player_amount, bot_amount)
    WorldHandler().create()
    Supply().create()
    VICTORY_CONDITION: int = 15
    player = players.active_player()
    while not player.won(VICTORY_CONDITION):
        new_screen()
        player = players.next_player()
        print(f'====== NEW TURN - Player {player.name} ======')
        if player.is_human:
            player_turn(player)
        else:
            bot_turn(player)
        input('Press [ENTER] to end the turn...')
    print(f'Congratulations! Player {player.name} has won!')

def player_turn(player: Player) -> None:
    location = player_movement(player)
    new_screen()
    print(f'You arrive at the market in {location.name}.')
    player_sell(player, location)
    new_screen()
    player_buy(player, location)
    new_screen()
    print(f'You prepare to leave the planet with your credits ({player.credits}) and',end=' ')
    if player.cargo:
        print('the contents of your cargo hold:')
        for good in player.cargo:
            print(f'- {good.name.capitalize()}')
    else:
        print('an empty cargo hold.')

def player_movement(player: Player) -> World:
    reach = random.randint(1, 3)
    system = WorldHandler().worlds
    for world in system:
        print(world.name, end='')
        if player.location_index == system.index(world):
            print(' <-- Current Location')
        else:
            print()
    print(f'You are able to move {reach} steps this turn.')
    while True:
        destination = input('Input name of destination: ').lower()
        for world in system:
            if (world.name.lower() == destination
                and not abs(system.index(world) - player.location_index) > reach):
                    player.location_index = system.index(world)
                    destination = 'DONE'
        if destination == 'DONE':
            break
        else:
            print('Invalid destination.')
    return system[player.location_index]

def player_sell(player: Player, location: World) -> None:
    if player.cargo:
        prices = determine_prices(player.cargo, location)
        while player.cargo:
            print('You have the following goods in your hold:')
            for index, good in enumerate(player.cargo):
                print(f'{index + 1}. {good.name.capitalize()}: '
                      f'{prices[good.name][0]}  ({prices[good.name][1]})')
            print(f'You have {player.credits} credits.')
            opt = input('Choose good to sell, or [done] to leave: ').lower()
            if opt == 'done':
                return
            elif opt.isdecimal() and 0 < int(opt) <= len(player.cargo):
                index = int(opt) - 1
                good = player.cargo[index]
                player.sell(index, prices[player.cargo[index].name][0])
                new_screen()
            else:
                input('Invalid option.')
    else:
        print('You have nothing to sell.')

def player_buy(player: Player, location: World) -> None:
    market_inventory = Supply().fetch_market()
    prices = determine_prices(market_inventory, location)
    while True:
        print('The following goods are available at market:')
        for index, good in enumerate(market_inventory):
            print(f'{index + 1}. {good.name.capitalize()}: '
                  f'{prices[good.name][0]}  ({prices[good.name][1]})')
        if len(player.cargo) == 5:
            print('Your cargo hold is already full.')
            Supply().return_market(market_inventory)
            return
        print(f'You have {player.credits} credits')
        opt = input('Choose good to buy, or [done] to leave: ').lower()
        if opt == 'done':
            Supply().return_market(market_inventory)
            return
        elif opt.isdecimal() and 0 < int(opt) <= len(market_inventory):
            index = int(opt) - 1
            good = market_inventory[index]
            if not prices[good.name][0] > player.credits:
                player.buy(market_inventory.pop(index), prices[good.name][0])
                new_screen()
            else:
                print('You do not have enough credits.')
        else:
            print('Invalid option.')

def bot_turn(player: Player) -> None:
    # Bot moves
    destination = random.randint(1,3)
    system = WorldHandler().worlds
    if player.location_index + destination < len(system):
        destination_index = player.location_index + destination
    else:
        destination_index = player.location_index - destination
    print(f'{player.name.capitalize()} moves from '
          f'{system[player.location_index].name} to '
          f'{system[destination_index].name}')
    player.location_index = destination_index
    location = system[player.location_index]

    # Bot sells
    prices = determine_prices(player.cargo, location)
    selling: list[str] = []
    for good in player.cargo:
        if prices[good.name][1] == 'High':
            player.sell(player.cargo.index(good), prices[good.name][0])
            selling.append(good.name)
    if selling:
        print(f'{player.name} sells',end=' ')
        for good in selling:
            print(good,end=' ')
        print()

    # Bot buys
    market_inventory = Supply().fetch_market()
    prices = determine_prices(market_inventory, location)
    buying = []
    for good in market_inventory:
        if (prices[good.name][1] in ['Low', 'Average'] 
            and len(player.cargo) < 5 
            and not prices[good.name][0] > player.credits):
                index = market_inventory.index(good)
                player.buy(market_inventory.pop(index), prices[good.name][0])
                buying.append(good.name)
    Supply().return_market(market_inventory)
    if buying:
        print(f'{player.name} buys',end=' ')
        for item in buying:
            print(item,end=' ')
        print()

    # Bot ends
    print(f'{player.name} has {player.credits} credits and', end=' ')
    if player.cargo:
        print('the following in their cargo hold:')
        for good in player.cargo:
            print(f'- {good.name.capitalize()}')
    else:
        print('an empty cargo hold.')

def determine_prices(inventory: list[Good], location: World) -> dict[str, list[int, str]]:
    prices: dict[str, list[int, str]] = {}
    for good in inventory:
        if good.name in prices.keys():
            continue
        elif good.name in location.exports:
            prices[good.name] = [good.base_price - 2, 'Low']
        elif good.name in location.imports:
            prices[good.name] = [good.base_price + 2, 'High']
        else:
            prices[good.name] = [good.base_price, 'Average']
    return prices

def new_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    run()