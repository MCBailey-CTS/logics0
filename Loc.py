from numpy import ndarray
from typing import Union, Optional

from puzzles import Puzzle


class Loc:
    def __init__(self, r: int, c: int, fence: Optional[str] = None):
        self.__row = r
        self.__col = c
        self.__fence = fence

    def __eq__(self, other) -> bool:
        return self.__row == other.__row and self.__col == other.__col

    def __hash__(self) -> int:
        hash1 = 23
        hash1 = hash1 * 31 + self.__row
        return hash1 * 31 + self.__col

    def __str__(self):
        return f'Loc[{self.__row}, {self.__col}]'

    def __iter__(self):
        return iter((self.__row, self.__col))

    @property
    def row(self) -> int:
        return self.__row

    @property
    def col(self) -> int:
        return self.__col

    @property
    def fence(self) -> str:
        if self.__fence is None:
            raise Exception(f'Loc({self.__row}, {self.__col}) doe snot have a fence')
        return self.__fence

    def row_house_locs(self, length: int):
        for col in range(0, length):
            yield Loc(self.__row, col)

    def col_house_locs(self, length: int):
        for row in range(0, length):
            yield Loc(row, self.__col)

    def is_valid_kropki(self, grid_length) -> bool:
        return -1 < self.__row < grid_length and -1 < self.__col < grid_length

    def is_valid_sudoku(self, length: int):
        return -1 < self.__row < length and -1 < self.__col < length

    def is_valid_parks(self, grid: Union[list[list[str]], ndarray]) -> bool:
        return -1 < self.__row < len(grid) and -1 < self.__col < len(grid)

    def is_valid_tenner(self, grid: list[list[str]]) -> bool:
        return -1 < self.__row < len(grid) - 1 and -1 < self.__col < len(grid) - 1

    def fence_house_locs(self, length: int, fence_grid: list):
        for row in range(0, length):
            for col in range(0, length):
                if fence_grid[row][col] == fence_grid[self.__row][self.__col]:
                    yield Loc(row, col)

    def __repr__(self) -> str:
        return str(self)

    def cell_between(self, other):
        chain: list[Loc] = [self, other]

        if chain[0].north(2) == (chain[1]):
            return chain[0].north()
        if chain[0].east(2) == (chain[1]):
            return chain[0].east()
        if chain[0].south(2) == (chain[1]):
            return chain[0].south()
        if chain[0].west(2) == (chain[1]):
            return chain[0].west()

        raise ValueError()

    # throw Error(`Cannot find intersection between ${loc0} and ${loc1}`);

    def north(self, offset: int = 1) -> 'Loc':
        return Loc(self.__row - offset, self.__col)

    def south(self, offset: int = 1) -> 'Loc':
        return Loc(self.__row + offset, self.__col)

    def west(self, offset: int = 1) -> 'Loc':
        return Loc(self.__row, self.__col - offset)

    def east(self, offset: int = 1) -> 'Loc':
        return Loc(self.__row, self.__col + offset)

    def add(self, x_row: int, y_col: int) -> 'Loc':
        return Loc(self.__row + x_row, self.__col + y_col)

    def add(self, vector):
        if isinstance(vector, Loc):
            return self.add(vector.row, vector.col)
        elif isinstance(vector, list):
            return self.add(vector[0], vector[1])
        else:
            raise TypeError()

    def top_left(self, offset: int = 1):
        return self.north(offset).west(offset)

    def top_right(self, offset: int = 1):
        return self.north(offset).east(offset)

    def bottom_left(self, offset: int = 1):
        return self.south(offset).west(offset)

    def bottom_right(self, offset: int = 1):
        return self.south(offset).east(offset)

    def in_same_row(self, other) -> bool:
        return self.__row == other.row

    def in_same_col(self, other) -> bool:
        return self.__col == other.col

    def is_next_to(self, other) -> bool:
        if self.in_same_row(other) and abs(self.__col - other.col) == 1:
            return True

        if self.in_same_col(other) and abs(self.__row - other.row) == 1:
            return True

        return False

    # @staticmethod
    # def row_chute(loc) -> int:
    #     if self.length != 9:
    #         raise Exception("Can only ask for row chute of 9x9 sudoku")
    #     if loc.row < 0:
    #         raise Exception(f'Invalid loc to ask row chute for {loc}')
    #     if loc.row < 3:
    #         return 0
    #     elif loc.row < 6:
    #         return 1
    #     elif loc.row < 9:
    #         return 2
    #     raise Exception(f'Invalid loc to ask row chute for {loc}')
    #
    # @staticmethod
    # def col_chute(loc) -> int:
    #     if self.length != 9:
    #         raise Exception("Can only ask for col chute of 9x9 sudoku")
    #     if loc.col < 0:
    #         raise Exception(f'Invalid loc to ask col chute for {loc}')
    #     if loc.col < 3:
    #         return 0
    #     elif loc.col < 6:
    #         return 1
    #     elif loc.col < 9:
    #         return 2
    #     raise Exception(f'Invalid loc to ask col chute for {loc}')

    @staticmethod
    def kropki_row_locs(length: int):
        pass

    @staticmethod
    def kropki_row_cell_locs(length: int):
        pass

    @staticmethod
    def kropki_row_intersection_locs(length: int):
        pass

    @staticmethod
    def kropki_col_locs(length: int):
        pass

    @staticmethod
    def kropki_col_cell_locs(length: int):
        pass

    @staticmethod
    def kropki_col_intersection_locs(length: int):
        pass

    @staticmethod
    def sudoku_cell_locs_rows_cols_fences(grid: list[list[str]]) -> list[list]:
        houses = []

        for house in sudoku_cell_locs_rows(grid):
            houses.append(house)

        for house in sudoku_cell_locs_cols(grid):
            houses.append(house)

        for house in sudoku_cell_locs_fences(grid):
            houses.append(house)

        return houses

    # @staticmethod
    # def shape()


# loc0 = Loc(1, 6)

# loc1 = Loc(1, 6)

# loc2 = Loc(1, 7)

# loc3 = Loc(1, 6)

# loc4 = Loc(12, 6)


# s = set()

# s.add(loc0)
# s.add(loc1)
# s.add(loc2)
# s.add(loc3)
# s.add(loc4)


# # print(loc0 == loc1)

# # print(Loc(100, 23))

# print(len(s))

# li = list(Loc(1, 10).col_house_locs(10))

# for x in li:
#     print(x)


def kropki_cell_locs_row(sudoku_length, row) -> list[Loc]:
    return [Loc(row * 2, col * 2) for col in range(sudoku_length)]


def kropki_locs_row(length, row) -> list[Loc]:
    return [Loc(row, col) for col in range(length)]


def kropki_locs_col(length, col) -> list[Loc]:
    return [Loc(row, col) for row in range(length)]


def kropki_cell_locs_col(length, col) -> list[Loc]:
    return [Loc(row * 2, col * 2) for row in range(length)]


def kropki_cell_locs_rows(length) -> list[list[Loc]]:
    return [kropki_cell_locs_row(length, row) for row in range(length)]


def kropki_locs_rows(length) -> list[list[Loc]]:
    return [kropki_locs_row(length, row) for row in range(length)]


def kropki_cell_locs_cols(length) -> list[list[Loc]]:
    return [kropki_cell_locs_col(length, col) for col in range(length)]


def kropki_locs_cols(length) -> list[list[Loc]]:
    return [kropki_locs_col(length, col) for col in range(length)]


def kropki_cell_locs_rows_cols(length) -> list[list[Loc]]:
    houses: list[list[Loc]] = []
    for house in kropki_cell_locs_rows(length):
        houses.append(house)
    for house in kropki_cell_locs_cols(length):
        houses.append(house)
    return houses


def kropki_cell_locs_fences(grid, sudoku_length):
    houses: list[list[Loc]] = []

    fences = dict()

    for r in range(sudoku_length):
        for c in range(sudoku_length):
            loc = Loc(r * 2, c * 2)

            cell: str = grid[loc.row][loc.col]

            array = [x for x in cell if not x.isnumeric() and x != "_"]

            if len(array) != 1:
                continue

            fence = array[0]

            if fence not in fences.keys():
                fences[fence] = list()

            fences[fence].append(loc)

    for fence in fences.keys():
        house = fences[fence]

        if len(house) != sudoku_length:
            raise ValueError(f"""Invalid fence length: '{fence}'""")

        houses.append(house)

    return houses


def kropki_cell_locs_rows_cols_fences(grid, length) -> list[list[Loc]]:
    houses: list[list[Loc]] = []
    for house in kropki_cell_locs_rows(length):
        houses.append(house)
    for house in kropki_cell_locs_cols(length):
        houses.append(house)
    for house in kropki_cell_locs_fences(grid, length):
        houses.append(house)
    return houses


def kropki_locs_rows_cols(length) -> list[list[Loc]]:
    houses: list[list[Loc]] = []
    for house in kropki_locs_rows(length):
        houses.append(house)
    for house in kropki_locs_cols(length):
        houses.append(house)
    return houses


def sudoku_cell_locs_fences(grid):
    houses: list[list[Loc]] = []

    sudoku_length = len(grid)

    fences = dict()

    for r in range(sudoku_length):
        for c in range(sudoku_length):
            loc = Loc(r, c)

            cell: str = grid[loc.row][loc.col]

            array = [x for x in cell if x.isalpha()]

            if len(array) != 1:
                continue

            fence = array[0]

            if fence not in fences.keys():
                fences[fence] = list()

            fences[fence].append(loc)

    for fence in fences.keys():
        house = fences[fence]

        houses.append(house)

    return houses


def parks1_cell_locs_row(grid, row) -> list[Loc]:
    return [Loc(row, col) for col in range(len(grid))]


def parks1_locs_row(grid, row) -> list[Loc]:
    return [Loc(row, col) for col in range(len(grid))]


def parks1_locs_col(grid, col) -> list[Loc]:
    return [Loc(row, col) for row in range(len(grid))]


def parks1_cell_locs_col(grid, col) -> list[Loc]:
    return [Loc(row, col) for row in range(len(grid))]


def sudoku_cell_locs_rows(grid) -> list[list[Loc]]:
    return [parks1_cell_locs_row(grid, row) for row in range(len(grid))]


def parks1_locs_rows(grid) -> list[list[Loc]]:
    return [parks1_locs_row(grid, row) for row in range(len(grid))]


def sudoku_cell_locs_cols(grid) -> list[list[Loc]]:
    return [parks1_cell_locs_col(grid, col) for col in range(len(grid))]


def parks1_locs_cols(grid) -> list[list[Loc]]:
    return [parks1_locs_col(grid, col) for col in range(len(grid))]


def parks1_cell_locs_rows_cols(grid) -> list[list[Loc]]:
    houses: list[list[Loc]] = []
    for house in sudoku_cell_locs_rows(grid):
        houses.append(house)
    for house in sudoku_cell_locs_cols(grid):
        houses.append(house)
    return houses


def get_parks_east_south_locs(loc: Loc) -> list[Loc]:
    return [
        loc,
        loc.east(),
        loc.east().east(),
        loc.east().east().south()
    ]
