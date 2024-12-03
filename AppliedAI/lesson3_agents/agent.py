from enum import Enum
from typing import Sequence

from tools import quasirandom_percentage

class ActionEnum(Enum):
    Passive = 0
    Suck = 1
    Right = 2
    Left = 3


class VacuumAgent:
    def action(self, percept: tuple[str, str]) -> ActionEnum:
        assert isinstance(percept, Sequence), 'percept needs to be a sequence of data'
        assert len(percept) == 2, 'percept needs to have length two'

        match percept:
            case _, 'Dirty':
                return ActionEnum.Suck
            case 'A', 'Clean':
                return ActionEnum.Right
            case 'B', 'Clean':
                return ActionEnum.Left
            case _:
                raise ValueError('Unrecognised percept values.')


class Environment:
    def __init__(self, dirty_chance: int = 50) -> None:
        self.grid = [
            {'name': 'A', 'state': 'Clean'},
            {'name': 'B', 'state': 'Clean'}
        ]
        self.random = iter(quasirandom_percentage(dirty_chance))
    
    def dirtify(self) -> None:
        for space in self.grid:
            if next(self.random):
                space['state'] = 'Dirty'


env = Environment()
bot = VacuumAgent()
agent_location = 0
score = 0
random = iter(quasirandom_percentage(50))
for _ in range(1_000):
    env.dirtify()

    percept = tuple(env.grid[agent_location].values())
    match bot.action(percept):
        case ActionEnum.Suck:
            print('Cleaning')
            env.grid[agent_location]['state'] = 'Clean'
        case ActionEnum.Right:
            if agent_location != 1:
                print('Moving')
                agent_location = 1
        case ActionEnum.Left:
            if agent_location != 0:
                print('Moving')
                agent_location = 0
        case _:
            print('Idling')

    for space in env.grid:
        score += len([space for space in env.grid
                      if space['state'] == 'Clean'])

print(f'{score=}')