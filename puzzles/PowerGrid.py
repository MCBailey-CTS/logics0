from puzzles import Puzzle
from typing import Optional
from Loc import Loc


class PowerGrid(Puzzle):

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)

    def __is_solved0(self, house: list[Loc], power: Optional[int]) -> bool:
        POWER = 1
        EMPTY = 0

        candidates_array = [self.cell_candidates(loc) for loc in house]

        all_cells_solved = [len(candidates_array[index]) == 1 for index in range(len(candidates_array))]

        if not all(all_cells_solved):
            return False

        solved_power_indexes = [index for index in range(len(candidates_array)) if POWER in candidates_array[index]]

        if len(solved_power_indexes) > 2:
            raise Exception("Found power grid house with more than 2 solved power cells")

        if len(solved_power_indexes) != 2:
            return False

        # unsolved = []

        # # for index

        # for index in range(len(house)):
        #     candidates = puzzle.cell_candidates(house[index])

        #     if len(candidates) > 1:
        #         unsolved.append(house[index])
        #         continue

        #     if POWER in candidates:
        #         solved_power.append(house[index])

        #     if EMPTY in candidates:
        #         solved_empty.append(house[index])

        # if len(solved_power) == 2:
        #     edits += puzzle.rem(unsolved, [POWER])

        # if len(solved_power) == 0 and len(unsolved) == 2:
        #     edits += puzzle.rem(unsolved, [EMPTY])

        # if len(solved_power) == 1 and len(unsolved) == 1:
        #     edits += puzzle.rem(unsolved, [EMPTY])
        # for index in range(len(house)):

        return True

    def is_solved(self) -> bool:
        for index in range(len(self)):
            if not self.__is_solved0(self.house_row(index), self.east_scraper(index)):
                return False
            if not self.__is_solved0(self.house_col(index), self.south_scraper(index)):
                return False
        return True

    def east_scraper(self, row: int) -> Optional[int]:
        string = self.grid[row][len(self)]
        if string.isnumeric():
            return int(string)
        return None

    def south_scraper(self, col: int) -> Optional[int]:
        string = self.grid[len(self)][col]
        if string.isnumeric():
            return int(string)
        return None

    def __str__(self):
        string = f'{self.id()}\n{len(self)}\n'
        for r in range(len(self) + 1):
            for c in range(len(self) + 1):
                string += f'{self.grid[r][c]} '
            string += '\n'
        return string.replace('10', '__', -1).replace('_0', '..', -1).replace('1_', 'PP', -1)

