from typing import Optional

from puzzles import Puzzle

PLUS = '+'
MINUS = '-'
EMPTY = '.'
from Loc import Loc
from colorama import Fore, Style, Back
import numpy


class Magnets:
    def __init__(self, __puzzle: str) -> None:
        __array = []
        for line in __puzzle.replace('\n', ' ', -1).split(' '):
            if len(line) > 0:
                __array.append(line)
        self.__id = __array[0]
        self.__length = int(__array[1])
        __array.pop(0)
        __array.pop(0)

        # __temp = []
        #
        # for item in __array:

        self.__grid = numpy.reshape(__array, (self.__length + 2, self.__length + 2))

        # for r in range(len(self)):
        #     for c in range(len(self)):
        #         string: str = self.__grid[r][c]
        #
        #         if len(string) == 4:
        #             continue
        #
        #         if '#' in string:
        #             self.__grid[r][c] = '####'
        #
        #         if len(string) == 1 and string.isalpha():
        #             self.__grid[r][c] = f'+-.{string}'

    def to_string_with_grid(self) -> str:
        #  ┼────┼────┼────┼────┼

        g = self.__grid

        # ┴
        # │
        # ┼
        # ┬
        # └
        # ├
        # ┐
        # ┤
        # ┘
        # ┌
        # ─

        # string = ''
        # string += f'┌────┬────┬────┬────┐\n'
        # string += f'│{g[0][0]}│{g[0][1]}│{g[0][2]}│{g[0][3]}│ {g[0][4]} {g[0][5]}\n'
        # string += f'├────┼────┼────┼────┤\n'
        # string += f'│{g[1][0]}│{g[1][1]}│{g[1][2]}│{g[1][3]}│ {g[1][4]} {g[1][5]}\n'
        # string += f'├────┼────┼────┼────┤\n'
        # string += f'│{g[2][0]}│{g[2][1]}│{g[2][2]}│{g[2][3]}│ {g[2][4]} {g[2][5]}\n'
        # string += f'├────┼────┼────┼────┤\n'
        # string += f'│{g[3][0]}│{g[3][1]}│{g[3][2]}│{g[3][3]}│ {g[3][4]} {g[3][5]}\n'
        # string += f'└────┴────┴────┴────┘\n'
        # string += f'  {g[4][0]}   {g[4][1]}   {g[4][2]}   {g[4][3]}   {g[4][4]}  {g[4][5]}\n'
        # string += f'  {g[5][0]}   {g[5][1]}   {g[5][2]}   {g[5][3]}   {g[5][4]}  {g[5][5]}\n'

        def to_row_cell_string(puzzle: Magnets, __r: int) -> str:
            __string0 = '│'
            __row = puzzle.house_row(__r)
            for i in range(len(puzzle) - 1):
                l0 = __row[i]
                l1 = __row[i + 1]
                __string0 += f'{puzzle.__grid[l0.row][l0.col]}'
                __string0 += ' ' if self.cell_fence(l0) == self.cell_fence(l1) else '│'
            __string0 += f'{puzzle.__grid[__row[-1].row][__row[-1].col]}'
            return f'{__string0}│ {puzzle.__grid[__r][len(self)]} {puzzle.__grid[__r][len(self) + 1]}\n'

        def get_top_row_border(puzzle: Magnets) -> str:
            __string0 = '┌'
            for i in range(len(puzzle) - 1):
                __string0 += '────┬'
            return f'{__string0}────┐\n'

        def get_bottom_row_border(puzzle: Magnets) -> str:
            __string0 = '└'
            for i in range(len(puzzle) - 1):
                __string0 += '────┴'
            return f'{__string0}────┘\n'

        def get_inner_row_border(puzzle: Magnets, __r: int) -> str:
            __string = '├'

            __row0 = puzzle.house_row(__r)
            __row1 = puzzle.house_row(__r + 1)

            for l0, l1 in zip(__row0, __row1):
                f0 = puzzle.cell_fence(l0)
                f1 = puzzle.cell_fence(l1)

                # __string += '    ' if f0 == f1 else '┼────'
                __string += '    ' if f0 == f1 else '────'

            return __string + '\n'

            # return f'├────┼────┼────┼────┤\n'

        def get_southern_magnet_numbers(puzzle: Magnets, __r: int) -> str:
            __string = "  "
            __string += "".join(f'{puzzle.__grid[__r][i]}   ' for i in range(len(puzzle)))
            __string = __string.strip()
            return f'  {__string}   {puzzle.__grid[__r][len(puzzle)]}  {puzzle.__grid[__r][len(puzzle) + 1]}\n'

        string = get_top_row_border(self)

        for __r in range(len(self) - 1):
            string += to_row_cell_string(self, __r)
            string += get_inner_row_border(self, __r)

        string += to_row_cell_string(self, len(self) - 1)
        string += get_bottom_row_border(self)
        string += get_southern_magnet_numbers(self, len(self))
        string += get_southern_magnet_numbers(self, len(self) + 1)

        return string

    def to_string(self, color=True) -> str:

        if self.__id == "001.magnets":
            return self.to_string_with_grid()

        __string = f'{self.__id}\n'
        __string += f'{self.__length}\n'

        for r in range(len(self)):
            for c in range(len(self) + 2):
                loc = Loc(r, c)
                __temp: str = self.__grid[loc.row][loc.col]

                # if color and __temp.startswith('+__'):
                #     __string += f'{Back.GREEN}{Fore.RED}{__temp}{Fore.RESET}{Back.RESET} '
                # elif color and __temp.startswith('_-_'):
                #     __string += f'{Fore.CYAN}{__temp}{Fore.RESET} '
                # else:
                #     __string += f'{__temp} '
                if color and __temp.startswith('+__'):
                    __string += f'{Back.GREEN}{Fore.RED}{__temp}{Fore.RESET}{Back.RESET} '
                elif color and __temp.startswith('_-_'):
                    __string += f'{Fore.CYAN}{__temp}{Fore.RESET} '
                else:
                    __string += f'{__temp} '
            __string += '\n'

        for c in range(len(self)):
            __string += f'{self.__grid[len(self)][c].strip().ljust(4)} '
        __string += f'{self.__grid[len(self)][len(self)]} '
        __string += f'{self.__grid[len(self)][len(self) + 1]} '
        __string += '\n'

        for c in range(len(self)):
            __string += f'{self.__grid[len(self) + 1][c].ljust(4)} '
        __string += f'{self.__grid[len(self) + 1][len(self)]} '
        __string += f'{self.__grid[len(self) + 1][len(self) + 1]} '
        __string += '\n'

        return __string

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self):
        return self.__length

    def is_solved(self):
        for fence_house in self.house_fences():
            loc0_candidates = self.cell_candidates(fence_house[0])
            loc1_candidates = self.cell_candidates(fence_house[1])

            if len(loc0_candidates) > 1 or len(loc1_candidates) > 1:
                return False

        return True

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

    def plus_row_value(self, row_index: int) -> Optional[int]:
        string: str = self.__grid[row_index][len(self)]
        if not string.isnumeric():
            return None
        return int(string)

    def minus_row_value(self, row_index: int) -> Optional[int]:
        string: str = self.__grid[row_index][len(self) + 1]
        if not string.isnumeric():
            return None
        return int(string)

    def house_row(self, row_index: int) -> list[Loc]:
        house = []
        for i in range(0, self.__length):
            house.append(Loc(row_index, i))
        return house

    def plus_col_value(self, col_index: int) -> Optional[int]:
        string: str = self.__grid[len(self)][col_index].replace(".", "", -1)
        if not string.isnumeric():
            return None
        return int(string)

    def minus_col_value(self, col_index: int) -> Optional[int]:
        string: str = self.__grid[len(self) + 1][col_index].replace(".", "", -1)
        if not string.isnumeric():
            return None
        return int(string)

    def house_col(self, col_index: int) -> list[Loc]:
        house = []
        for i in range(0, self.__length):
            house.append(Loc(i, col_index))
        return house

    def is_magnet_cell(self, loc: Loc) -> bool:
        return '#' not in self.__grid[loc.row][loc.col]

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
                loc = Loc(r, c)
                if not self.is_magnet_cell(loc):
                    continue
                fence = self.house_fence(loc)
                if fence not in dct:
                    dct[fence] = []
                dct[fence].append(loc)

        # print(dct)

        houses = []
        for fence in dct:
            houses.append(dct[fence])
        return houses

    def cell_fence(self, loc: Loc) -> str:
        return "".join([s for s in self.__grid[loc.row][loc.col] if s.isalpha()])
