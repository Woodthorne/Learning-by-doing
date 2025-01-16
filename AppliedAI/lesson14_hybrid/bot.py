from utils import ActionEnum, CellEnum, State


class Bot:
    def __init__(self, grid_dimensions: tuple[int, int], view_range: int):
        cols, rows = grid_dimensions
        self.grid = [[CellEnum.UNKNOWN for _ in range(cols)]
                     for _ in range(rows)]
        self.view_range: int
    
    def get_action(self, state: State) -> ActionEnum:
        self._update_grid(state.bot_location, state.bot_view)
        if any(CellEnum.DANGER in cell
               for row in state.bot_view
               for cell in row):
            pass # Find closest danger and avoid
    
    def _update_grid(
            self,
            location: tuple[int,int],
            view: list[list[CellEnum]]
    ) -> None:
        for r_index, row in view:
            for c_index, cell in row:
                grid_row = r_index - self.view_range + location[1]
                grid_col = c_index - self.view_range + location[0]
                if 0 <= grid_col < 10 and 0 <= grid_row < 10:
                    self.grid[grid_row][grid_col] = cell
    