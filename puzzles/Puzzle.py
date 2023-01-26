from abc import abstractmethod
from typing import Optional, Union
from colorama import Fore, Style
from Loc import Loc
import numpy


class Puzzle:
    def __init__(self,
                 puzzle: Union[str, numpy.ndarray],
                 length: Optional[int] = None,
                 id: Optional[str] = None) -> None:
        self.grid = []
        self.color_override = {}

        array = []

        if isinstance(puzzle, numpy.ndarray) and isinstance(length, int) and isinstance(id, str):
            self.grid = puzzle
            self.__id = id
            self.__length = length
            return

        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            array.append(temp)
        self.__id = array[0]
        self.__length = int(array[1].replace("$","",-1))
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

    def __len__(self):
        return self.__length

    def solve(self, techniques):
        edits = 0
        edit_dict = {}
        while True:
            original_edits = edits
            for tech1 in techniques:
                _edits = tech1.solve0(self)
                if tech1.__class__.__name__ not in edit_dict:
                    edit_dict[tech1.__class__.__name__] = 0
                edit_dict[tech1.__class__.__name__] += _edits
                edits = edits + _edits
            if original_edits == edits:
                break
        for tech1 in edit_dict:
            if edit_dict[tech1] == 0:
                continue
            print(f'{tech1}: {edit_dict[tech1]}')
        print(f'Total edits: {edits}')
        # for
        return edits

    def __repr__(self):
        return f'{self.__class__.__name__}( {self.id()} )'

    def fences(self) -> set[str]:
        house = set()

        for r in range(self.__length):
            for c in range(self.__length):
                loc = Loc(r, c)
                other = self.cell_fence(loc)
                house.add(other)

        return house

    def houses_fences(self) -> list[list[Loc]]:
        return [self.house_fence(fence) for fence in self.fences()]

    def house_fence(self, fence: str) -> list[Loc]:
        house = []

        for r in range(len(self)):
            for c in range(len(self)):
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

    # @property
    # def row_length(self) -> int:
    #     return self.__row_length

    def unsolved_cells(self) -> list[Loc]:
        unsolved = []
        for r in range(len(self)):
            for c in range(len(self)):
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

    # @property
    # def col_length(self) -> int:
    #     return self.__col_length

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
        return [candidate for candidate in range(1, len(self) + 1)]

    def rem(self, locs: Union[Loc, list[Loc], set[Loc]], candidates: iter) -> int:
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
            return [Loc(row, c) for c in range(len(self))]
        return [loc for loc in self.house_row(row) if candidate in self.cell_candidates(loc)]

    def house_col(self, col: int, candidate=None) -> list[Loc]:
        if candidate is None:
            return [Loc(r, col) for r in range(len(self))]
        return [loc for loc in self.house_col(col) if candidate in self.cell_candidates(loc)]

    @property
    def grid_length(self):
        return self.__length

    @property
    def has_fences(self) -> bool:
        return any([s.isalpha() for s in self.grid[0][0]])

    def cell_fence(self, loc: Loc) -> str:
        return "".join([s for s in self.grid[loc.row][loc.col] if s.isalpha()])

    def houses_rows_cols(self) -> list[list[Loc]]:
        return self.houses_rows() + self.houses_cols()

    def houses_rows(self) -> list[list[Loc]]:
        return [self.house_row(i) for i in range(len(self))]

    def houses_cols(self) -> list[list[Loc]]:
        return [self.house_col(i) for i in range(len(self))]

    def override_loc_color(self, locs: list[Loc], color):
        for loc in locs:
            self.color_override[loc] = color

    def to_string(self, include_colors=True) -> str:
        string = f'{self.id()}\n'
        string += f'{len(self)}\n'
        for r in range(len(self)):
            for c in range(len(self)):
                loc = Loc(r, c)
                if include_colors and loc in self.color_override:
                    string += f'{self.color_override[loc]}{self.grid[r][c].ljust(len(self))}{Style.RESET_ALL} '
                    continue
                if len(self.cell_candidates(loc)) == 0:
                    string += f'{Fore.GREEN}{self.grid[r][c].ljust(len(self))}{Style.RESET_ALL} '
                else:
                    string += f'{self.grid[r][c].ljust(len(self))} '
            string += '\n'
        return string

    def __str__(self):
        return self.to_string(False)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Puzzle):
            raise TypeError(f'Cannot == because not a puzzle {type(other)}')

        if isinstance(self.grid, numpy.ndarray) and isinstance(other.grid, numpy.ndarray):
            # print('in here')
            print(self.grid)
            print(other.grid)
            return (self.grid == other.grid).all()

        return False


class Mathrax(Puzzle):

    def __init__(self, puzzle: Union[str, numpy.ndarray],
                 length: Optional[int] = None,
                 id: Optional[str] = None) -> None:
        super().__init__(puzzle)

        if isinstance(puzzle, numpy.ndarray) and isinstance(length, int) and isinstance(id, str):
            return

    def house_row(self, row: int, candidate=None) -> list[Loc]:
        if candidate is None:
            temp = [Loc(row, c) for c in range(0, len(self) * 2 - 1, 2)]
            return temp
        return [loc for loc in self.house_row(row) if candidate in self.cell_candidates(loc)]

    def house_col(self, col: int, candidate=None) -> list[Loc]:
        if candidate is None:
            temp = [Loc(r, col) for r in range(0, len(self) * 2 - 1, 2)]
            return temp
        return [loc for loc in self.house_col(col) if candidate in self.cell_candidates(loc)]

    def houses_rows(self) -> list[list[Loc]]:
        return [self.house_row(i) for i in range(0, len(self) * 2 - 1, 2)]

    def houses_cols(self) -> list[list[Loc]]:
        return [self.house_col(i) for i in range(0, len(self) * 2 - 1, 2)]

    def unsolved_cells(self) -> list[Loc]:
        unsolved = []
        for r in range(0, len(self) * 2 - 1, 2):
            for c in range(0, len(self) * 2 - 1, 2):
                loc = Loc(r, c)
                if len(self.cell_candidates(loc)) == 1:
                    continue
                unsolved.append(loc)
        return unsolved

    @property
    def has_fences(self):
        return False

    def iterate_cell_locs(self) -> list[Loc]:
        locs = []
        for r in range(0, len(self) * 2 - 1, 2):
            for c in range(0, len(self) * 2 - 1, 2):
                locs.append(Loc(r, c))
        return locs

    def is_solved(self) -> bool:
        for house in self.houses_rows() + self.houses_cols():
            solved_candidates = [list(self.cell_candidates(loc))[0] for loc in house if
                                 len(self.cell_candidates(loc)) == 1]

            if len(solved_candidates) != len(self):
                print('/////')
                print(house)
                print(solved_candidates)
                print("house wasn't completely solved")
                print('/////')
                return False

            expected = set(self.expected_candidates())

            if expected.issubset(solved_candidates) and expected.issuperset(solved_candidates):
                continue

            # print("bad subset")
            # print(expected)
            # print(solved_candidates)
            # print('////')

            # print(solved_candidates)

            return False

        for r in range(len(self) * 2 - 1):
            for c in range(len(self) * 2 - 1):
                if r % 2 != 0 and c % 2 != 0:
                    loc = Loc(r, c)
                    mathrax_intersection = self.grid[r][c]
                    if '+' in mathrax_intersection:
                        number = int(mathrax_intersection.replace('+', ''))
                        tl_candidate = self.cell_candidates(loc.top_left())[0]
                        br_candidate = self.cell_candidates(loc.bottom_right())[0]

                        tr_candidate = self.cell_candidates(loc.top_right())[0]
                        bl_candidate = self.cell_candidates(loc.bottom_left())[0]

                        if tl_candidate + br_candidate != number:
                            # print(f'{tl_candidate} {br_candidate} {number}')
                            return False

                        if tr_candidate + bl_candidate != number:
                            # print(f'{tr_candidate} {bl_candidate} {number}')
                            return False

                    # print(self.grid[r][c])

        return True
        # return len(self.unsolved_cells()) == 0 and all(
        #     len(self.cell_candidates(loc)) == 1 for loc in self.iterate_cell_locs())

    def to_string(self, include_colors=True) -> str:
        string = f'{self.id()}\n'
        string += f'{len(self)}\n'
        for r in range(len(self) * 2 - 1):
            for c in range(len(self) * 2 - 1):
                loc = Loc(r, c)
                if include_colors and loc in self.color_override:
                    string += f'{self.color_override[loc]}{self.grid[r][c]}{Style.RESET_ALL} '
                    continue
                if len(self.cell_candidates(loc)) == 0:
                    string += f'{Fore.GREEN}{self.grid[r][c]}{Style.RESET_ALL} '
                else:
                    string += f'{self.grid[r][c]} '
            string += '\n'
        return string

    def __str__(self):
        string = f'{self.id()}\n'
        string += f'{len(self)}\n'
        for r in range(len(self) * 2 - 1):
            for c in range(len(self) * 2 - 1):
                # loc = Loc(r, c)
                # if loc in self.__color_override:
                #     string += f'{self.__color_override[loc]}{self.grid[r][c].ljust(len(self))}{Style.RESET_ALL} '
                #     continue
                # if len(self.cell_candidates(loc)) == 0:
                #     string += f'{Fore.GREEN}{self.grid[r][c].ljust(len(self))}{Style.RESET_ALL} '
                # else:
                string += f'{self.grid[r][c]} '
            string += '\n'
        return string


class Kropki(Mathrax):

    def __init__(self, puzzle: Union[str, numpy.ndarray],
                 length: Optional[int] = None,
                 id: Optional[str] = None) -> None:
        super().__init__(puzzle, length, id)

        if isinstance(puzzle, numpy.ndarray) and isinstance(length, int) and isinstance(id, str):
            return

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
            # noinspection PyUnresolvedReferences
            self.grid.append(temp)
            array.pop(0)

    def expected_candidates(self) -> list:
        return [candidate for candidate in range(1, self.__length + 1)]

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

    # def house_fence_cell_locs(self, loc_fence: Union[Loc, str]):
    #     if isinstance(loc_fence, Loc):
    #         return self.house_fence_cell_locs(self.cell_fence(loc_fence))
    #     house = []
    #     for cell in self.iterate_cells():
    #         if self.cell_fence(cell) == loc_fence:
    #             house.append(cell)
    #     return house

    def __str__(self):
        string = f'{self.__id}\n'
        string += f'{self.__length}\n'

        for r in range(self.grid_length):
            for c in range(self.grid_length):
                if c % 2 != 0:
                    string += f'{self.grid[r][c].center(3, " ")} '
                    continue
                # if r % 2 == 0:

                # if

                # string += f'{self.grid[r][c].replace("123456789$", "__________", -1).replace("123456789", "_________", -1).center(len(self) + 1, " ")} '
                string += f'{self.grid[r][c].center(len(self) + 1, " ")} '
                # elif c % 2 == 0:
                #     string += f'{self.__grid[r][c]} '
                # else:
                #     string += f'{self.__grid[r][c].ljust(self.length)} '

            string += '\n'

        return string

    def is_black(self, loc: Loc) -> bool:
        return "BB" in self.grid[loc.row][loc.col] or "b" in self.grid[loc.row][loc.col]

    def is_white(self, loc: Loc) -> bool:
        return "WW" in self.grid[loc.row][loc.col] or "w" in self.grid[loc.row][loc.col]

    def is_empty(self, loc: Loc) -> bool:
        return all([s == "." for s in self.grid[loc.row][loc.col]])

    def all_locs_are_valid(self, locs: list[Loc]) -> bool:
        for loc in locs:
            if not loc.is_valid_kropki(self.grid_length):
                return False
        return True

    # def house_row_locs(self, loc: Union[Loc, int]) -> list[Loc]:
    #     if isinstance(loc, Loc):
    #         return self.house_row_locs(loc.row)
    #     locs = []
    #     for i in range(self.grid_length):
    #         locs.append(Loc(loc, i))
    #     return locs
    #
    # def house_row_cell_locs(self, loc: Union[Loc, int]) -> list[Loc]:
    #     if isinstance(loc, Loc):
    #         return self.house_row_cell_locs(loc.row)
    #
    #     locs = []
    #     temp_locs = self.house_row_locs(loc)
    #     for i in range(0, self.grid_length, 2):
    #         locs.append(temp_locs[i])
    #     return locs
    #
    # def house_col_locs(self, loc: Union[Loc, int]) -> list[Loc]:
    #     if isinstance(loc, Loc):
    #         return self.house_col_locs(loc.col)
    #     locs = []
    #     for i in range(self.grid_length):
    #         locs.append(Loc(i, loc))
    #     return locs
    #
    # def house_col_cell_locs(self, loc: Union[Loc, int]) -> list[Loc]:
    #     if isinstance(loc, Loc):
    #         return self.house_col_cell_locs(loc.col)
    #
    #     locs = []
    #     temp_locs = self.house_col_locs(loc)
    #     for i in range(0, self.grid_length, 2):
    #         locs.append(temp_locs[i])
    #     return locs

    def is_solved(self) -> bool:
        for house in self.houses_rows() + self.houses_cols():
            solved_candidates = [list(self.cell_candidates(loc))[0] for loc in house if
                                 len(self.cell_candidates(loc)) == 1]

            if len(solved_candidates) != len(self):
                print('/////')
                print(house)
                print(solved_candidates)
                print("house wasn't completely solved")
                print('/////')
                return False

            expected = set(self.expected_candidates())

            if expected.issubset(solved_candidates) and expected.issuperset(solved_candidates):
                continue

            # print("bad subset")
            # print(expected)
            # print(solved_candidates)
            # print('////')

            # print(solved_candidates)

            return False

        # for r in range(len(self) * 2 - 1):
        #     for c in range(len(self) * 2 - 1):
        #         if r % 2 != 0 and c % 2 != 0:
        #             loc = Loc(r, c)
        #             mathrax_intersection = self.grid[r][c]
        #             if '+' in mathrax_intersection:
        #                 number = int(mathrax_intersection.replace('+', ''))
        #                 tl_candidate = self.cell_candidates(loc.top_left())[0]
        #                 br_candidate = self.cell_candidates(loc.bottom_right())[0]
        #
        #                 tr_candidate = self.cell_candidates(loc.top_right())[0]
        #                 bl_candidate = self.cell_candidates(loc.bottom_left())[0]
        #
        #                 if tl_candidate + br_candidate != number:
        #                     # print(f'{tl_candidate} {br_candidate} {number}')
        #                     return False
        #
        #                 if tr_candidate + bl_candidate != number:
        #                     # print(f'{tr_candidate} {bl_candidate} {number}')
        #                     return False

        # print(self.grid[r][c])

        return True
        # return len(self.unsolved_cells()) == 0 and all(
        #     len(self.cell_candidates(loc)) == 1 for loc in self.iterate_cell_locs())
