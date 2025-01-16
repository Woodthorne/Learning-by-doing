import random

from bot import Bot
from utils import ActionEnum, CellEnum, State

class Environment:
    def __init__(
            self,
            grid: list[list[CellEnum]],
            view_range: int
    ) -> None:
        self.grid = grid
        self.bot = Bot(
            grid_dimensions=(len(grid[0]), len(grid)),
            view_range=view_range
        )
        self.bot_range = view_range

    def simulate(self, bot_start: tuple[int, int]|None = None) -> None:
        if bot_start == None:
            while True:
                row = random.randint(0, len(self.grid))
                col = random.randint(0, len(self.grid[0]))
                if self.grid[row][col] == CellEnum.EMPTY:
                    bot_start = (col, row)
                    break
        
        state = State(bot_start, self._bot_scan(bot_start))
        remaining_victims = sum(1 for row in self.grid for cell in row if cell == CellEnum.VICTIM)
        while remaining_victims:
            c_index, r_index = state.bot_location
            match self.bot.get_action(state):
                case ActionEnum.IDLE:
                    idle_count = state.idle_count + 1
                    if idle_count == 2 \
                    and self.grid[r_index][c_index] == CellEnum.VICTIM:
                        self.grid[r_index][c_index] = CellEnum.EMPTY
                        remaining_victims -= 1
                case ActionEnum.RIGHT:
                    idle_count = 0
                    if c_index + 1 <= len(self.grid[0]):
                        c_index += 1
                case ActionEnum.DOWN:
                    idle_count = 0
                    if r_index + 1 <= len(self.grid):
                        r_index += 1
                case ActionEnum.LEFT:
                    idle_count = 0
                    if 0 <= c_index - 1:
                        c_index -= 1
                case ActionEnum.UP:
                    idle_count = 0
                    if 0 <= r_index + 1:
                        r_index -= 1
            
            new_location = (c_index, r_index)
            state = State(
                bot_location=new_location,
                bot_view=self._bot_scan(new_location),
                idle_count=idle_count
            )
        
    
    def _bot_scan(self, location: tuple[int, int]) -> list[list[CellEnum]]:
        scan_r_0 = location[1] - self.bot_range
        scan_c_0 = location[0] - self.bot_range

        grid_scan: list[list[CellEnum]] = []
        for r_local in range(2 * self.bot_range + 1):
            r_index = scan_r_0 + r_local
            grid_scan.append([])
            for c_local in range(2 * self.bot_range + 1):
                c_index = scan_c_0 + c_local
                if 0 <= r_index < len(self.grid) \
                and 0 <= c_index < len(self.grid[0]):
                    grid_scan[r_local].append(self.grid[r_index][c_index])
                else:
                    grid_scan[r_local].append(None)
        
        return grid_scan
