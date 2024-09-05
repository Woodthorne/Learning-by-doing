from collections import abc
from dataclasses import dataclass

@dataclass
class Player:
    name: str
    goals: int
    assists: int

def bubble_sort_players(iterable: list, key: abc.Callable) -> None:
    for loop in range(len(iterable)):
        for index in range(1, len(iterable) - loop):
            if key(iterable[index]) < key(iterable[index - 1]):
                iterable[index], iterable[index - 1] = iterable[index - 1], iterable[index]

team = [
    Player('Adam', 11, 32),
    Player('Berit', 13, 16),
    Player('Carl', 23, 1)
]

bubble_sort_players(team, lambda x: x.goals + x.assists)
print(team)