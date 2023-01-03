from abc import abstractmethod
from typing import Optional, Union

from colorama import Fore, Style

from Loc import Loc

PLUS = "+"
MINUS = "-"
EMPTY = "."


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

    def is_cell_solved(self, loc: Loc, solved_with_candidate=None) -> bool:
        candidates = self.cell_candidates(loc)
        if solved_with_candidate is None:
            return len(candidates) == 1
        return candidates[0] == solved_with_candidate

    def expected_candidates(self) -> list:
        return [candidate for candidate in range(1, self.length + 1)]

    def rem(self, locs: Union[list[Loc], set[Loc], Loc], candidates: iter) -> int:
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


class Sumscrapers(Puzzle):
    def __init__(self, puzzle: str, row_length: int = 2, col_length: int = 2):
        super().__init__(puzzle, row_length, col_length)

        for r in range(self.length):
            for c in range(self.length):
                if self.grid[r][c] == '_':
                    string = ""
                    for candidate in self.expected_candidates():
                        string += f'{candidate}'

                    self.grid[r][c] = string
                    # print(string)

    # def is_solved(self) -> bool:
    #     return False

    @property
    def has_fences(self) -> bool:
        return False

    def __scaper_or_none(self, loc: Loc):
        string = self.grid[loc.row][loc.col]
        if string.isnumeric():
            return int(string)
        return None

    def north_scraper(self, col: int) -> Optional[int]:
        return self.__scaper_or_none(Loc(self.length, col))

    def south_scraper(self, col: int) -> Optional[int]:
        return self.__scaper_or_none(Loc(self.length + 1, col))

    def east_scraper(self, row: int) -> Optional[int]:
        return self.__scaper_or_none(Loc(row, self.length + 1))

    def west_scraper(self, row: int) -> Optional[int]:
        return self.__scaper_or_none(Loc(row, self.length))

    def __str__(self):
        string = f'{super().__str__()}\n'

        string += f'{"$$".ljust(self.length)} '

        for index in range(self.length):
            north = self.north_scraper(index)

            if north is None:
                string += f'{"??".ljust(self.length)} '
            else:
                string += f'{f"{north}".ljust(self.length)} '

        string += "$$\n"

        for row in range(self.length):
            west = self.west_scraper(row)
            if west is None:
                string += f'{"??".ljust(self.length)} '
            else:
                string += f'{f"{west}".ljust(self.length)} '

            for col in range(self.length):
                string += f'{self.grid[row][col]} '

            east = self.east_scraper(row)
            if east is None:
                string += f'{"??".ljust(self.length)} '
            else:
                string += f'{f"{east}".ljust(self.length)} '

            string += '\n'

        string += f'{"$$".ljust(self.length)} '

        for index in range(self.length):
            south = self.south_scraper(index)
            if south is None:
                string += f'{"??".ljust(self.length)} '
            else:
                string += f'{f"{south}".ljust(self.length)} '

        string += "$$\n"

        return string

    def _is_scraper_solved(self, sumscraper: Optional[int], house: list[Loc]) -> bool:
        solved_candidates = [self.cell_candidates(loc)[0] for loc in house if len(self.cell_candidates(loc)) == 1]
        if len(solved_candidates) != self.length:
            return False
        if sumscraper is None:
            return True

        current = 0
        max0 = 0

        for candidate in solved_candidates:
            if candidate < max0:
                continue
            current += candidate
            max0 = candidate

        return sumscraper == current

    def is_solved(self) -> bool:
        houses = []
        for index in range(self.length):
            houses.append(self.house_row(index))
            houses.append(self.house_col(index))
        for house in houses:
            solved_candidates = [self.cell_candidates(loc)[0] for loc in house if len(self.cell_candidates(loc)) == 1]

            expected = set(self.expected_candidates())

            if not expected.issuperset(solved_candidates) or not expected.issubset(solved_candidates):
                return False

        for index in range(self.length):
            house = self.house_row(index)

            if not self._is_scraper_solved(self.west_scraper(index), house):
                return False

            house.reverse()

            if not self._is_scraper_solved(self.east_scraper(index), house):
                return False

            house = self.house_col(index)

            if not self._is_scraper_solved(self.north_scraper(index), house):
                return False

            house.reverse()

            if not self._is_scraper_solved(self.south_scraper(index), house):
                return False

        return True


class Skyscrapers(Sumscrapers):
    def __init__(self, puzzle: str):
        super().__init__(puzzle)

    def _is_scraper_solved(self, sumscraper: Optional[int], house: list[Loc]) -> bool:
        solved_candidates = [self.cell_candidates(loc)[0] for loc in house if len(self.cell_candidates(loc)) == 1]
        if len(solved_candidates) != self.length:
            return False
        if sumscraper is None:
            return True

        current = 0
        max0 = 0

        for candidate in solved_candidates:
            if candidate < max0:
                continue
            current += 1
            max0 = candidate

        return sumscraper == current


class Sudoku(Puzzle):

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)

        for r in range(self.length):
            for c in range(self.length):
                loc = Loc(r, c)

                candidates = self.cell_candidates(loc)

                if len(candidates) == 0 or len(candidates) == 1 and candidates[0] == 0:
                    new_string = ""

                    for candidate in self.expected_candidates():
                        new_string += f'{candidate}'

                    if self.has_fences:
                        new_string += f'{self.cell_fence(loc)}'

                    self.grid[r][c] = new_string
                else:
                    new_string = ""

                    for candidate in self.expected_candidates():
                        if candidate in candidates:
                            new_string += f'{candidate}'
                        else:
                            new_string += '_'

                    if self.has_fences:
                        new_string += f'{self.cell_fence(loc)}'

                    self.grid[r][c] = new_string

        # array = []
        # for line in puzzle.split("\n"):
        #     temp = line.strip()
        #     if len(temp) == 0:
        #         continue
        #     print(temp)
        #     array.append(temp)

    # def rem(self, loc: Loc, candidates0) -> int:
    #     edits = 0
    #     for c in candidates0:
    #         cell = self.cell_candidates(loc)
    #         if c not in cell:
    #             continue
    #         cell.remove(c)
    #         # if len(cell) == 1:
    #         #     self.__un_solved_locs.remove(loc)
    #         edits += 1
    #     return edits
    #
    # @staticmethod
    # def default_sudoku_fence_grid():
    #     a = "a"
    #     b = "b"
    #     c = "c"
    #     d = "d"
    #     e = "e"
    #     f = "f"
    #     g = "g"
    #     h = "h"
    #     i = "i"
    #     return [
    #         [a, a, a, b, b, b, c, c, c],
    #         [a, a, a, b, b, b, c, c, c],
    #         [a, a, a, b, b, b, c, c, c],
    #         [d, d, d, e, e, e, f, f, f],
    #         [d, d, d, e, e, e, f, f, f],
    #         [d, d, d, e, e, e, f, f, f],
    #         [g, g, g, h, h, h, i, i, i],
    #         [g, g, g, h, h, h, i, i, i],
    #         [g, g, g, h, h, h, i, i, i],
    #     ]
    #
    # @staticmethod
    # def unpack_sudoku_id_length_grid(grid: str) -> tuple[str, int, list[list[str]]]:
    #     if "|" in grid:
    #
    #         temp_array: list[str] = grid.replace("|", "", -1).replace("\t", " ", -1).replace("\r", " ", -1).replace("+",
    #                                                                                                                 "",
    #                                                                                                                 -1).replace(
    #             "-", "", -1).split('\n')
    #
    #         array: list[str] = []
    #
    #         for i in range(len(temp_array)):
    #             temp = temp_array[i].replace(" ", "", -1)
    #             if len(temp) != 0:
    #                 array.append(temp)
    #
    #         # print(array)
    #
    #         _id: str = array[0]
    #         _length: int = int(array[1])
    #
    #         array.pop(0)
    #         array.pop(0)
    #
    #         _grid = []
    #
    #         index = 0
    #
    #         while index < _length:
    #
    #             string = array[index].replace(" ", "", -1)
    #
    #             if len(string) != _length:
    #                 array.pop(index)
    #                 continue
    #
    #             _grid.append([s for s in string])
    #
    #             index += 1
    #         return _id, _length, _grid
    #
    #     else:
    #
    #         array: list[str] = grid.replace("\n", " ").replace("\t", " ").replace("\r", " ").replace(
    #             "  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ").replace("  ",
    #                                                                                                            " ").lstrip().rstrip().split(
    #             " ")
    #         _id: str = array[0]
    #         _length: int = int(array[1])
    #
    #         _grid = []
    #         index = 0
    #         for row in range(_length):
    #             _grid.append([])
    #             for col in range(_length):
    #                 _grid[row].append([])
    #                 _grid[row][col] = array[index + 2]
    #                 index += 1
    #         return _id, _length, _grid

    # def __str__(self) -> str:
    #     string = f'{self.id()}\n'
    #     string += f'{self.length}\n'
    #     for r in range(self.length):
    #         for c in range(self.length):
    #             loc = Loc(r, c)
    #             candidates = self.cell_candidates(loc)
    #
    #             for candidate in self.expected_candidates():
    #                 if candidate in candidates:
    #                     string += f'{candidate}'
    #                 else:
    #                     string += "_"
    #
    #             if len(self.houses_fences()) > 0:
    #                 fence = self.cell_fence(loc)
    #                 string += fence
    #
    #             string += " "
    #
    #         string += '\n'
    #     return string

    def unsolved_cells(self) -> set[Loc]:
        unsolved = set()
        for r in range(self.length):
            for c in range(self.length):
                loc = Loc(r, c)
                if len(self.cell_candidates(loc)) == 1:
                    continue
                unsolved.add(loc)
        return unsolved

    # def expected_candidates(self) -> list[int]:
    #     return [i + 1 for i in range(self.length)]

    def any_cell_is_solved(self, locs) -> bool:
        return [len(self.cell_candidates(loc)) == 1 for loc in locs] > 0

    def list_all_cell_locs(self) -> list[Loc]:
        locs = []
        for r in range(self.length):
            for c in range(self.length):
                locs.append(Loc(r, c))
        return locs

    def is_solved(self) -> bool:
        for house in self.houses_rows_cols_fences():
            solved_candidates = [list(self.cell_candidates(loc))[0] for loc in house if
                                 len(self.cell_candidates(loc)) == 1]

            if len(solved_candidates) != self.length:
                print("house wasn't completely solved")
                return False

            expected = set(self.expected_candidates())

            if expected.issubset(solved_candidates) and expected.issuperset(solved_candidates):
                continue

            print(solved_candidates)

            return False

        return True

    def row_chute(self, loc: Loc) -> int:
        if self.length != 9:
            raise Exception("Can only ask for row chute of 9x9 sudoku")
        if loc.row < 0:
            raise Exception(f'Invalid loc to ask row chute for {loc}')
        if loc.row < 3:
            return 0
        elif loc.row < 6:
            return 1
        elif loc.row < 9:
            return 2
        raise Exception(f'Invalid loc to ask row chute for {loc}')

    def col_chute(self, loc: Loc) -> int:
        if self.length != 9:
            raise Exception("Can only ask for col chute of 9x9 sudoku")
        if loc.col < 0:
            raise Exception(f'Invalid loc to ask col chute for {loc}')
        if loc.col < 3:
            return 0
        elif loc.col < 6:
            return 1
        elif loc.col < 9:
            return 2
        raise Exception(f'Invalid loc to ask col chute for {loc}')

    def loc_chute(self, loc: Loc) -> Loc:
        return Loc(self.row_chute(loc), self.col_chute(loc))

    def fence_from_chute(self, chute_loc: Loc) -> str:
        r, c = chute_loc

        if r == 0 and c == 0:
            return self.cell_fence(Loc(0, 0))

        if r == 0 and c == 1:
            return self.cell_fence(Loc(0, 3))

        if r == 0 and c == 2:
            return self.cell_fence(Loc(0, 6))

        if r == 1 and c == 0:
            return self.cell_fence(Loc(3, 0))

        if r == 1 and c == 1:
            return self.cell_fence(Loc(3, 3))

        if r == 1 and c == 2:
            return self.cell_fence(Loc(3, 6))

        if r == 2 and c == 0:
            return self.cell_fence(Loc(6, 0))

        if r == 2 and c == 1:
            return self.cell_fence(Loc(6, 3))

        if r == 2 and c == 2:
            return self.cell_fence(Loc(6, 6))

        raise Exception(f'Invalid chute loc: {chute_loc}')


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


class Magnets:
    def __init__(self, puzzle: str) -> None:
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
        self.__grid = []
        for r in range(self.__length + 2):
            line = array[0].strip().replace("  ", " ", -1).split(" ")
            self.__grid.append(line)
            array.pop(0)

    def is_solved(self):
        return False

    def rem(self, locs: list[Loc], candidates: list) -> int:
        edits = 0

        for loc in locs:
            for candidate in candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                self.__grid[loc.row][loc.col] = self.__grid[loc.row][loc.col].replace(candidate, "_")
                edits += 1

        return edits

    def cell_candidates(self, loc: Loc) -> list[str]:
        string = self.__grid[loc.row][loc.col]
        lst: list[str] = []
        if PLUS in string:
            lst.append(PLUS)
        if MINUS in string:
            lst.append(MINUS)
        if EMPTY in string:
            lst.append(EMPTY)
        return lst

    def __str__(self) -> str:
        string = f'{self.__id}\n'
        string += f'{self.__length}\n'
        for r in range(self.__length + 2):
            for c in range(self.__length + 2):
                if r == 0 and c == 0:
                    string += f'{Fore.RED}{self.__grid[r][c]}{Style.RESET_ALL} '
                elif r == self.__length + 2 - 1 and c == self.__length + 2 - 1:
                    string += f'{Fore.BLUE}{self.__grid[r][c]}{Style.RESET_ALL} '
                else:
                    string += f'{self.__grid[r][c]} '
            string += '\n'
        return string

    # def unsolved_cells(self) -> set[Loc]:
    #     return self.__un_solved_locs

    # def solved_cells(self) -> set[Loc]:
    #     return self.__solved_locs

    def expected_candidates(self) -> list[int]:
        return [i + 1 for i in range(self.__length)]

    def id(self) -> str:
        return self.__id

    @property
    def length(self) -> int:
        return self.__length

    def plus_row_value(self, row_index: int) -> int:
        string: str = self.__grid[row_index + 1][0]
        if not string.isnumeric():
            return -1
        return int(string)

    def minus_row_value(self, row_index: int) -> int:
        string: str = self.__grid[row_index + 1][self.__length + 1]
        if not string.isnumeric():
            return -1
        return int(string)

    def house_row(self, row_index: int) -> list[Loc]:
        house = []
        for i in range(0, self.__length):
            house.append(Loc(row_index + 1, i + 1))
        return house

    def plus_col_value(self, col_index: int) -> int:
        string: str = self.__grid[0][col_index + 1].replace(".", "", -1)
        if not string.isnumeric():
            return -1
        return int(string)

    def minus_col_value(self, col_index: int) -> int:
        string: str = self.__grid[self.__length + 1][col_index + 1].replace(".", "", -1)
        if not string.isnumeric():
            return -1
        return int(string)

    def house_col(self, col_index: int) -> list[Loc]:
        house = []
        for i in range(0, self.__length):
            house.append(Loc(i + 1, col_index + 1))
        return house

    def house_fence(self, loc: Loc) -> str:
        fence = self.__grid[loc.row][loc.col] \
            .replace(PLUS, "") \
            .replace(MINUS, "") \
            .replace(EMPTY, "") \
            .replace("_", "")

        if len(fence) != 1:
            raise ValueError(f"could not find fence in magnets cell {loc}")

        return fence

    def house_fences(self) -> list[list[Loc]]:
        dct = {}
        for r in range(self.__length):
            for c in range(self.__length):
                loc = Loc(r + 1, c + 1)
                print(loc)
                fence = self.house_fence(loc)
                if fence not in dct:
                    dct[fence] = []
                dct[fence].append(loc)

        print(dct)

        houses = []
        for fence in dct:
            houses.append(dct[fence])
        return houses


class RobotFences(Sudoku):
    def __init__(self, puzzle: str) -> None:
        Sudoku.__init__(self, puzzle)

    def is_solved(self) -> bool:
        for house in self.houses_rows_cols():
            solved_candidates = [list(self.cell_candidates(loc))[0] for loc in house if
                                 len(self.cell_candidates(loc)) == 1]

            if len(solved_candidates) != self.length:
                print("row or column wasn't completely solved")
                return False

            expected = set(self.expected_candidates())

            if expected.issubset(solved_candidates) and expected.issuperset(solved_candidates):
                continue

            return False

        for house in self.houses_fences():
            solved_candidates = [list(self.cell_candidates(house[index]))[0] for index in range(len(house))]

            solved_candidates.sort()

            if len(solved_candidates) == 1:
                continue
            for index in range(len(house) - 1):
                if solved_candidates[index] + 1 != solved_candidates[index + 1]:
                    print("Fence house not solved")
                    return False

        return True


class Parks1(Puzzle):
    def expected_candidates(self) -> list:
        return [0, 1]

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)
        self.grid = []
        self.__color_fence_dict = {
            'a': Fore.RED,
            'b': Fore.CYAN,
            'c': Fore.GREEN,
            'd': Fore.LIGHTBLUE_EX,
            'e': Fore.LIGHTMAGENTA_EX,
            'f': Fore.LIGHTGREEN_EX,
            'g': Fore.LIGHTWHITE_EX,
            'h': Fore.LIGHTYELLOW_EX,
            'i': Fore.LIGHTRED_EX,
            'j': Fore.YELLOW,
            'k': Fore.RED
        }
        array = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            array.append(temp)
        array.pop(0)
        array.pop(0)
        for line in array:
            self.grid.append(line.split(" "))

    def is_solved(self) -> bool:
        houses = []
        for house in self.houses_rows():
            houses.append(house)
        for house in self.houses_cols():
            houses.append(house)
        fence_dict = {}
        # for house in puzzle.
        for r in range(self.length):
            for c in range(self.length):
                loc = Loc(r, c)
                fence = self.cell_fence(loc)
                if fence not in fence_dict:
                    fence_dict[fence] = []
                fence_dict[fence].append(loc)

        for fence in fence_dict.keys():
            fence_locs = fence_dict[fence]
            houses.append(fence_locs)
        for house in houses:
            solved_empty = [loc for loc in house if
                            len(self.cell_candidates(loc)) == 1 and self.cell_candidates(loc)[0] == 0]
            solved_tree = [loc for loc in house if
                           len(self.cell_candidates(loc)) == 1 and self.cell_candidates(loc)[0] == 1]
            unsolved = list(set(house).difference(solved_tree + solved_empty))
            if len(solved_tree) == 1:
                continue
            if len(unsolved) != 0:
                return False

        for r in range(self.length):
            for c in range(self.length):
                loc = Loc(r, c)
                candidates0 = self.cell_candidates(loc)
                if len(candidates0) != 1 or candidates0[0] != 1:
                    continue
                directions = [
                    loc.north().west(),
                    loc.north().east(),
                    loc.south().west(),
                    loc.south().east(),
                ]

                for direction in directions:
                    if not direction.is_valid_parks(self.grid):
                        continue
                    candidates1 = self.cell_candidates(direction)
                    if len(candidates1) != 1:
                        return False
                    if candidates1[0] == 1 and candidates0[0] == 1:
                        return False

        return True

    def color_fence(self, loc: Loc) -> str:

        return self.__color_fence_dict[self.cell_fence(loc)]

    def __str__(self) -> str:
        string = f'{Fore.LIGHTCYAN_EX}########################\n'
        string += f'{self.id()}\n'
        string += f'{self.length}\n'
        for r in range(self.length):
            for c in range(self.length):
                loc = Loc(r, c)
                grid_string = self.grid[r][c]
                candidates = "".join([char for char in grid_string if not char.isalpha()])
                # fence = [char for char in grid_string if char.isalpha()][0]
                # string += f'{self.color_fence(loc)}{candidates}{fence}{Style.RESET_ALL} '
                # fence = [char for char in grid_string if char.isalpha()][0]
                string += f'{self.color_fence(loc)}{candidates}{Style.RESET_ALL} '
            string += '\n'
        string += f'{Fore.CYAN}########################\n{Style.RESET_ALL}'
        return string

    def houses_rows_cols_fences(self, loc: Optional[Loc] = None) -> list[list[Loc]]:
        if loc is None:
            return self.houses_rows_cols() + self.houses_fences()
        fence = self.__fences[loc.row][loc.col]
        return [self.house_row(loc.row), self.house_col(loc.col), self.house_fence(fence)]

    def cell_fence(self, loc: Loc) -> str:
        return [char for char in self.grid[loc.row][loc.col] if char.isalpha()][0]

        return [self.house_fence(fence) for fence in self.__fence_dict]

    def house_fence(self, fence: str) -> list[Loc]:
        locs = []
        for r in range(self.length):
            for c in range(self.length):
                loc = Loc(r, c)
                if self.cell_fence(loc) == fence:
                    locs.append(loc)
        return locs

    def house_row(self, row: int, candidate=None) -> list[Loc]:
        if candidate is None:
            return [Loc(row, c) for c in range(self.length)]
        return [loc for loc in self.house_row(row) if candidate in self.cell_candidates(loc)]

    def house_col(self, col: int) -> list[Loc]:
        return [Loc(r, col) for r in range(self.length)]


class Tenner(Puzzle):

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)
        self.grid = []
        array = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            array.append(temp)
        array.pop(0)
        array.pop(0)
        for row in range(self.length + 1):
            temp = []
            split = array[row].replace("-1", "0123456789", -1).replace("\r", " ", -1).replace("\t", " ",
                                                                                              -1).replace(
                "  ", " ", -1).strip().split(' ')

            # print(split)
            for t in split:
                if len(t) == 0:
                    continue
                if row != self.length and t == "00":
                    temp.append("0_________")
                elif row != self.length and t == "01":
                    temp.append("_1________")
                elif row != self.length and t == "02":
                    temp.append("__2_______")
                elif row != self.length and t == "03":
                    temp.append("___3______")
                elif row != self.length and t == "04":
                    temp.append("____4_____")
                elif row != self.length and t == "05":
                    temp.append("_____5____")
                elif row != self.length and t == "06":
                    temp.append("______6___")
                elif row != self.length and t == "07":
                    temp.append("_______7__")
                elif row != self.length and t == "08":
                    temp.append("________8_")
                elif row != self.length and t == "09":
                    temp.append("_________9")
                else:
                    temp.append(t)
            self.grid.append(temp)

    def int_to_cell_string(self, candidate: int) -> str:
        string = ""
        for i in self.expected_candidates():
            if i == candidate:
                string += f'{candidate}'
            else:
                string += '_'
        return string

    @property
    def col_length(self) -> int:
        return 10

    def is_row_house_solved(self, row: int) -> bool:
        solved_candidates = set(
            [self.cell_candidates(loc)[0] for loc in self.house_row_cell_locs(row) if self.is_cell_solved(loc)])
        return solved_candidates.issuperset(self.expected_candidates()) and solved_candidates.issubset(
            self.expected_candidates())

    def is_col_house_solved(self, col: int) -> bool:
        solved_candidates = [
            self.cell_candidates(loc)[0]
            for loc in self.house_col_cell_locs(col)
            if self.is_cell_solved(loc)
        ]
        if len(solved_candidates) != self.length:
            return False
        total = self.total(col)
        if total is None:
            return True
        return sum(solved_candidates) == total

    def is_solved(self) -> bool:
        for row in range(self.length):
            if not self.is_row_house_solved(row):
                print(f'print bad row: {row}')

                return False

        for col in range(self.col_length):
            if not self.is_col_house_solved(col):
                print(f'print bad col: {col}')
                return False

        for r in range(self.length):
            for c in range(self.col_length):
                cell = Loc(r, c)
                if not self.is_cell_solved(cell):
                    # print(f'{self.__grid[r][c]}///////////////////////////')
                    return False
                solved_candidate = self.cell_candidates(cell)[0]
                directions = [
                    cell.north(),
                    cell.east(),
                    cell.south(),
                    cell.west(),
                    cell.north().east(),
                    cell.north().west(),
                    cell.south().east(),
                    cell.south().west()
                ]
                for direction in directions:
                    if direction.row < 0 or direction.col < 0:
                        continue
                    if direction.row >= self.length or direction.col >= 10:
                        continue

                    if not self.is_cell_solved(direction):
                        return False

                    other = self.cell_candidates(direction)[0]

                    if other == solved_candidate:
                        print(f'{cell} {direction}')
                        return False

        return True

    def expected_candidates(self) -> list:
        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __str__(self):
        string = f'{Fore.RED}{self.id()}{Style.RESET_ALL}\n'
        string += f'{self.length}\n'
        for r in range(self.length + 1):
            for c in range(self.col_length):

                cell_candidates = self.cell_candidates(Loc(r, c))

                if len(cell_candidates) == 0:
                    string += f'{Fore.GREEN}{self.grid[r][c].ljust(self.col_length)}{Style.RESET_ALL} '
                else:
                    string += f'{self.grid[r][c].ljust(self.col_length)} '
            string += '\n'
        return string

    def house_row_cell_locs(self, loc_row: Union[int, Loc]) -> list[Loc]:
        if isinstance(loc_row, Loc):
            return self.house_row_cell_locs(loc_row.row)
        return [Loc(loc_row, col) for col in range(self.col_length)]

    def house_col_cell_locs(self, loc_col: Union[int, Loc]) -> list[Loc]:
        if isinstance(loc_col, Loc):
            return self.house_col_cell_locs(loc_col.col)
        return [Loc(row, loc_col) for row in range(self.length)]

    def total(self, col: int) -> Union[int, None]:
        string = self.grid[self.length][col]
        if string.isnumeric():
            return int(string)
        return None


class Knightoku:  # (Sudoku):
    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)


class RobotCrosswords(Puzzle):
    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)
        array = []
        self.grid = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            array.append(temp)
        array.pop(0)
        array.pop(0)
        for line in array:
            split = line.split(' ')
            other = []

            for item in split:
                if item == '.' or item == '_':
                    other.append('123456789')
                elif item == 'x':
                    other.append('xxxxxxxxx')
                elif item.isalnum():
                    number = int(item)
                    temp = ''
                    for num in range(1, 10):
                        if number == num:
                            temp += f'{num}'
                        else:
                            temp += '_'
                    other.append(temp)
            # print(split)
            # self.grid.append(line.split(" "))
            self.grid.append(other)

    def __str__(self) -> str:
        string = f'///////////////////////////////////\n'
        string += f'{self.id()}\n'
        string += f'{self.length}\n'
        for r in range(self.length):
            for c in range(self.length):
                string += f'{self.grid[r][c]} '
            string += '\n'
        string += f'///////////////////////////////////'
        return string

    def is_solved(self) -> bool:
        return False


class Minesweeper(Puzzle):
    def is_solved(self) -> bool:
        return False

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)
        # array = []
        # self.grid = []
        # for line in puzzle.split("\n"):
        #     temp = line.strip()
        #     if len(temp) == 0:
        #         continue
        #     array.append(temp)
        # array.pop(0)
        # array.pop(0)
        # for line in array:
        #     self.grid.append(line.split(' '))

    def is_number_cell(self, loc: Loc) -> bool:
        return self.grid[loc.row][loc.col].isalnum()

    def is_mine_cell(self, loc: Loc) -> bool:
        return not self.is_number_cell(loc)

    def __str__(self):
        string = f'{self.id()}\n'
        string += f'{self.length}\n'
        for r in range(self.length):
            for c in range(self.length):
                string += f'{self.grid[r][c]} '
            string += '\n'
        return string

    def rem(self, locs: list[Loc], candidates: list[str]) -> int:
        edits = 0

        for loc in locs:
            for candidate in candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                self.grid[loc.row][loc.col] = self.grid[loc.row][loc.col].replace(str(candidate), "_")
                edits += 1

        return edits


class Snail3:
    pass


class Walls:
    pass


class Parks2:
    pass


class BattleShips:
    pass


class Clouds:
    def is_solved(self):
        return False


class PowerGrid(Puzzle):

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle, 1, 1)

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
        for index in range(self.length):
            if not self.__is_solved0(self.house_row(index), self.east_scraper(index)):
                return False
            if not self.__is_solved0(self.house_col(index), self.south_scraper(index)):
                return False
        return True

    def east_scraper(self, row: int) -> Optional[int]:
        string = self.grid[row][self.length]
        if string.isnumeric():
            return int(string)
        return None

    def south_scraper(self, col: int) -> Optional[int]:
        string = self.grid[self.length][col]
        if string.isnumeric():
            return int(string)
        return None

    def __str__(self):
        return super().__str__() \
            .replace("  ", " ", -1) \
            .replace("  ", " ", -1) \
            .replace("  ", " ", -1) \
            .replace("  ", " ", -1) \
            .replace("10", "__", -1) \
            .replace("1_", "PP", -1) \
            .replace("_0", "..", -1)


class Sentinels:
    pass


class Tents:
    pass


class Futoshiki:
    def __init__(self, puzzle: str) -> None:
        array = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            # print(temp)

            array.append(temp)
        self.Constantsid = array[0]
        self.Constantslength = int(array[1])
        array.pop(0)
        array.pop(0)
        self.Constantsgrid = []
        for r in range(self.Constantslength * 2 - 1):
            line = array[0].strip().replace("  ", " ", -1).split(" ")
            print(line)
            self.Constantsgrid.append(line)
            array.pop(0)

        # print("/////")
        # print(array)

    def id(self) -> str:
        return self.Constantsid

    @property
    def length(self):
        return self.Constantslength

    def cell_string(self, loc: Loc) -> str:
        return self.Constantsgrid[loc.row][loc.col]

    def cell_candidates(self, loc: Loc) -> list[int]:
        return [int(s) for s in self.Constantsgrid[loc.row][loc.col] if s.isnumeric()]

    def rem(self, locs: list[Loc], candidates: list) -> int:
        edits = 0

        for loc in locs:
            for candidate in candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                self.Constantsgrid[loc.row][loc.col] = self.Constantsgrid[loc.row][loc.col].replace(candidate, "_")
                edits += 1

        return edits

    def __str__(self):
        string = f'{self.Constantsid}\n'
        string += f'{self.Constantslength}\n'

        for r in range(self.Constantslength * 2 - 1):
            for c in range(self.Constantslength * 2 - 1):
                string += f'{self.Constantsgrid[r][c]} '
            string += '\n'
        return string


class HiddenStars:

    def is_solved(self):
        return False


class Kakuro:
    pass


class Mathrax:
    def __init__(self, puzzle: str) -> None:
        pass

    def solve0(self):
        pass


class MineShips:
    pass


class Nurikabe:
    pass


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

        return power is None or power == len(solved_abstract_locs)

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


class Lighthouses(Puzzle):
    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)

    def is_solved(self) -> bool:
        return False




class LightenUp(Puzzle):
    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)

    # def __str__(self):
    #     return super().__str__()\
    #         .replace("  ", " ", -1)\
    #         .replace("  ", " ", -1)\
    #         .replace("  ", " ", -1)\
    #         .replace("  ", " ", -1)\
    #         .replace("+-", "__", -1)

    def is_solved(self) -> bool:
        return False
