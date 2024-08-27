from collections import abc

from faker import Faker

class Player:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f'Player {self.name} is age {self.age}'

faker = Faker()

all_players: list[Player] = []
for _ in range(1_000):
    all_players.append(Player(faker.name(),
                                  faker.random_int(18, 99)
                                  )
                           )

def show_results(func: abc.Callable):
    def wrapper(*args):
        print(func.__name__, 'gives:')
        result = func(*args)
        if type(result) == tuple:
            for player in result:
                print(player)
        else:
            print(result)
        return result
    return wrapper

@show_results
def get_oldest(players: list[Player]) -> Player|None:
    if not players:
        return None
    
    oldest = players[0]

    for player in players:
        if oldest.age < player.age:
            oldest = player
    
    return oldest

@show_results
def get_youngest(players: list[Player]) -> Player|None:
    if not players:
        return None
    
    youngest = players[0]

    for player in players:
        if youngest.age > player.age:
            youngest = player
    
    return youngest

@show_results
def get_oldest_and_youngest(players: list[Player]) -> Player|None:
    if not players:
        return None, None
    
    oldest = players[0]
    youngest = players[0]

    for player in players:
        if oldest.age < player.age:
            oldest = player
        if youngest.age > player.age:
            youngest = player
    
    return oldest, youngest

if __name__ == '__main__':
    for func in [get_oldest, get_youngest, get_oldest_and_youngest]:
        func(all_players)
