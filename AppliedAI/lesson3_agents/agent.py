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

bot = VacuumAgent()
grid = [
    {'name': 'A', 'state': 'Clean'},
    {'name': 'B', 'state': 'Clean'}
]
location = 0
score = 0
random = iter(quasirandom_percentage(70))
for _ in range(1_000):
    for space in grid:
        if next(random):
            space['state'] = 'Dirty'
    
    percept = tuple(grid[location].values())
    match bot.action(percept):
        case ActionEnum.Suck:
            grid[location]['state'] = 'Clean'
        case ActionEnum.Right:
            if location != 1:
                location = 1
        case ActionEnum.Left:
            if location != 0:
                location = 0

    for space in grid:
        score += len([space for space in grid if space['state'] == 'Clean'])

print(f'{score=}')