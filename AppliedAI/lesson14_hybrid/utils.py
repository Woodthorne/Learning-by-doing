import random
from dataclasses import dataclass
from enum import Enum


class ActionEnum(Enum):
    IDLE = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4


class CellEnum(Enum):
    UNKNOWN = 0
    EMPTY = 1
    OBSTACLE = 2
    VICTIM = 3
    DANGER = 4


@dataclass
class State:
    bot_location: tuple[int,int]
    bot_view: list[list[CellEnum]]
    idle_count: int


def generate_grid(
        dimensions: tuple[int, int],
        dangers: int,
        obstacles: int,
        victims: int
) -> list[list[CellEnum]]:
    grid = [[CellEnum.EMPTY for _ in range(dimensions[0])]
                    for _ in range(dimensions[1])]
    
    cells = [
        (dangers, CellEnum.DANGER),
        (obstacles, CellEnum.OBSTACLE),
        (victims, CellEnum.VICTIM)
    ]
    for count, cell in cells:
        for _ in range(count):
            while True:
                c_index = random.randint(0, dimensions[0] - 1)
                r_index = random.randint(0, dimensions[1] - 1)
                if grid[r_index][c_index] == CellEnum.EMPTY:
                    grid[r_index][c_index] = cell
                    break
    
    return grid


