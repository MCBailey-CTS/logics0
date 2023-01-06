
from puzzles import Puzzle
from Loc import Loc
from typing import Union

class Kropki(Puzzle):

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)
        array = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            array.append(temp)
        self.__id = array[0]
        self.__length = int(array[1])
        array.pop(0)
        array.pop(0)
        for r in range(self.__length * 2 - 1):
            split = array[0].strip().replace("  ", " ", -1).split(" ")
            temp = []
            for line in split:
                if len(line) == 0:
                    continue
                temp.append(line)
            self.grid.append(temp)
            array.pop(0)

    def expected_candidates(self) -> list:
        return [candidate for candidate in range(1, self.length + 1)]

    def is_solved(self) -> bool:
        return False

    def iterate_locs(self) -> list[Loc]:
        array = []
        for r in range(self.grid_length):
            for c in range(self.grid_length):
                array.append(Loc(r, c))
        return array

    def iterate_cells(self) -> list[Loc]:
        array = []
        for r in range(self.__length):
            for c in range(self.__length):
                array.append(Loc(r * 2, c * 2))
        return array

    @property
    def grid_length(self):
        return self.__length * 2 - 1

    @property
    def has_fences(self) -> bool:
        return any([s.isalpha() for s in self.grid[0][0]])

    def cell_fence(self, loc: Loc) -> str:
        if not self.has_fences:
            raise Exception(f'Cell {loc} does not have a fence')
        letters = [s for s in self.grid[loc.row][loc.col] if s.isalpha()]
        if len(letters) != 1:
            raise Exception(f'More or less than exactly one fence in cell {loc}')
        return letters[0]

    def house_fence_cell_locs(self, loc_fence: Union[Loc, str]):
        if isinstance(loc_fence, Loc):
            return self.house_fence_cell_locs(self.cell_fence(loc_fence))
        house = []
        for cell in self.iterate_cells():
            if self.cell_fence(cell) == loc_fence:
                house.append(cell)
        return house

    def __str__(self):
        string = f'{self.__id}\n'
        string += f'{self.__length}\n'

        for r in range(self.grid_length):
            for c in range(self.grid_length):
                # if r % 2 == 0:
                string += f'{self.grid[r][c].replace(".", " ", -1)} '
                # elif c % 2 == 0:
                #     string += f'{self.__grid[r][c]} '
                # else:
                #     string += f'{self.__grid[r][c].ljust(self.length)} '

            string += '\n'

        return string

    def is_black(self, loc: Loc) -> bool:
        return "BB" in self.grid[loc.row][loc.col]

    def is_white(self, loc: Loc) -> bool:
        return "WW" in self.grid[loc.row][loc.col]

    def is_empty(self, loc: Loc) -> bool:
        return all([s == "." for s in self.grid[loc.row][loc.col]])

    def all_locs_are_valid(self, locs: list[Loc]) -> bool:
        for loc in locs:
            if not loc.is_valid_kropki(self.grid_length):
                return False
        return True

    def house_row_locs(self, loc: Union[Loc, int]) -> list[Loc]:
        if isinstance(loc, Loc):
            return self.house_row_locs(loc.row)
        locs = []
        for i in range(self.grid_length):
            locs.append(Loc(loc, i))
        return locs

    def house_row_cell_locs(self, loc: Union[Loc, int]) -> list[Loc]:
        if isinstance(loc, Loc):
            return self.house_row_cell_locs(loc.row)

        locs = []
        temp_locs = self.house_row_locs(loc)
        for i in range(0, self.grid_length, 2):
            locs.append(temp_locs[i])
        return locs

    def house_col_locs(self, loc: Union[Loc, int]) -> list[Loc]:
        if isinstance(loc, Loc):
            return self.house_col_locs(loc.col)
        locs = []
        for i in range(self.grid_length):
            locs.append(Loc(i, loc))
        return locs

    def house_col_cell_locs(self, loc: Union[Loc, int]) -> list[Loc]:
        if isinstance(loc, Loc):
            return self.house_col_cell_locs(loc.col)

        locs = []
        temp_locs = self.house_col_locs(loc)
        for i in range(0, self.grid_length, 2):
            locs.append(temp_locs[i])
        return locs

