from typing import Optional
from Loc import Loc
from puzzles import PowerGrid

class AbstractPainting(PowerGrid):
    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)

    def __is_solved0(self, house: list[Loc], power: Optional[int]) -> bool:
        ABSTRACT = 1
        EMPTY = 0

        candidates_array = [self.cell_candidates(loc) for loc in house]

        all_cells_solved = [len(candidates_array[index]) == 1 for index in range(len(candidates_array))]

        if not all(all_cells_solved):
            return False

        solved_abstract_locs = [loc for loc in house if self.is_cell_solved(loc, ABSTRACT)]

        return power is None or  power == len(solved_abstract_locs)


    def is_solved(self) -> bool:
        for index in range(self.length):
            if not self.__is_solved0(self.house_row(index), self.east_scraper(index)):
                return False
            if not self.__is_solved0(self.house_col(index), self.south_scraper(index)):
                return False
        return True

    def __str__(self):
        string = f'{self.id()}\n'
        string += f'{self.length}\n'
        for r in range(self.row_length):
            for c in range(self.col_length):
                string += f'{self.grid[r][c].ljust(self.length)} '
            string += '\n'
        return string