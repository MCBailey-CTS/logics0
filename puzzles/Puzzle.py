
from abc import abstractmethod
from typing import Optional

from Loc import Loc


class Puzzle:
    def __init__(self, puzzle: str, row_offset: int = 0, col_offset: int = 0) -> None:
        self.grid = []
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

        for line in array:
            self.grid.append(
                line.replace("  ", " ", -1)
                .replace("  ", " ", -1)
                .replace("  ", " ", -1)
                .replace("  ", " ", -1)
                .strip()
                .split(" "))

        if row_offset is None:
            self.__row_length = self.__length
        else:
            self.__row_length = row_offset + self.__length

        if col_offset is None:
            self.__col_length = self.__length
        else:
            self.__col_length = col_offset + self.__length

    @property
    def length(self) -> int:
        return self.__length

    def fences(self) -> set[str]:
        house = set()

        for r in range(self.length):
            for c in range(self.length):
                loc = Loc(r, c)
                other = self.cell_fence(loc)
                house.add(other)

        return house

    def houses_fences(self) -> list[list[Loc]]:
        return [self.house_fence(fence) for fence in self.fences()]

    def house_fence(self, fence: str) -> list[Loc]:
        house = []

        for r in range(self.length):
            for c in range(self.length):
                loc = Loc(r, c)
                other = self.cell_fence(loc)
                if other == fence:
                    house.append(loc)

        return house

    def houses_rows_cols_fences(self, loc: Optional[Loc] = None) -> list[list[Loc]]:
        if loc is None:
            return self.houses_rows_cols() + self.houses_fences()
        fence = self.cell_fence(loc)
        return [self.house_row(loc.row), self.house_col(loc.col), self.house_fence(fence)]

    @property
    def row_length(self) -> int:
        return self.__row_length

    def unsolved_cells(self) -> list[Loc]:
        unsolved = []
        for r in range(self.length):
            for c in range(self.length):
                loc = Loc(r, c)
                if len(self.cell_candidates(loc)) == 1:
                    unsolved.append(loc)
        return unsolved

    # @cache
    def surrounding(self, loc: Loc) -> list[Loc]:
        valid = []
        directions = [
            loc.north(),
            loc.east(),
            loc.south(),
            loc.west(),
            loc.north().east(),
            loc.north().west(),
            loc.south().east(),
            loc.south().west(),
        ]

        for temp in directions:
            if temp.is_valid_parks(self.grid):
                valid.append(temp)

        return valid

    @property
    def col_length(self) -> int:
        return self.__col_length

    def id(self) -> str:
        return self.__id

    @abstractmethod
    def is_solved(self) -> bool:
        raise NotImplementedError()

    def cell_candidates(self, loc: Loc) -> list:
        return [int(char) for char in self.grid[loc.row][loc.col] if char.isnumeric()]

    def is_cell_solved(self, loc: Loc, solved_with_candidate = None) -> bool:
        candidates = self.cell_candidates(loc)
        if solved_with_candidate is None:
            return len(candidates) == 1
        return candidates[0] == solved_with_candidate


    def expected_candidates(self) -> list:
        return [candidate for candidate in range(1, self.length + 1)]

    def rem(self, locs: list[Loc], candidates: iter) -> int:
        edits = 0
        if isinstance(locs, Loc):
            locs = [locs]

        for loc in locs:

            for candidate in candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                self.grid[loc.row][loc.col] = self.grid[loc.row][loc.col].replace(str(candidate), "_")
                edits += 1

        return edits

    def house_row(self, row: int, candidate=None) -> list[Loc]:
        if candidate is None:
            return [Loc(row, c) for c in range(self.length)]
        return [loc for loc in self.house_row(row) if candidate in self.cell_candidates(loc)]

    def house_col(self, col: int) -> list[Loc]:
        return [Loc(r, col) for r in range(self.length)]

    @property
    def grid_length(self):
        return self.length

    @property
    def has_fences(self) -> bool:
        return any([s.isalpha() for s in self.grid[0][0]])

    def cell_fence(self, loc: Loc) -> str:
        return "".join([s for s in self.grid[loc.row][loc.col] if s.isalpha()])

    def houses_rows_cols(self) -> list[list[Loc]]:
        return self.houses_rows() + self.houses_cols()

    def houses_rows(self) -> list[list[Loc]]:
        return [self.house_row(i) for i in range(self.length)]

    def houses_cols(self) -> list[list[Loc]]:
        return [self.house_col(i) for i in range(self.length)]

    def __str__(self):
        string = f'{self.id()}\n'
        string += f'{self.length}\n'
        for r in range(self.row_length):
            for c in range(self.col_length):
                string += f'{self.grid[r][c].ljust(self.length)} '
            string += '\n'
        return string

