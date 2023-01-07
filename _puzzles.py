from abc import abstractmethod
from typing import Optional, Union

from colorama import Fore, Style

from Loc import Loc
from puzzles import Sudoku
from puzzles import Sumscrapers
from puzzles import Puzzle

PLUS = "+"
MINUS = "-"
EMPTY = "."




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
            'h':Fore.LIGHTYELLOW_EX,
            'i':Fore.LIGHTRED_EX,
            'j':Fore.YELLOW,
            'k':Fore.RED
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

    # def houses_rows_cols_fences(self, loc: Optional[Loc] = None) -> list[list[Loc]]:
    #     if loc is None:
    #         return self.houses_rows_cols() + self.houses_fences()
    #     fence = self.__fences[loc.row][loc.col]
    #     return [self.house_row(loc.row), self.house_col(loc.col), self.house_fence(fence)]
    #
    # def cell_fence(self, loc: Loc) -> str:
    #     return [char for char in self.grid[loc.row][loc.col] if char.isalpha()][0]
    #
    #     return [self.house_fence(fence) for fence in self.__fence_dict]
    #
    # def house_fence(self, fence: str) -> list[Loc]:
    #     locs = []
    #     for r in range(self.length):
    #         for c in range(self.length):
    #             loc = Loc(r, c)
    #             if self.cell_fence(loc) == fence:
    #                 locs.append(loc)
    #     return locs
    #
    # def house_row(self, row: int, candidate=None) -> list[Loc]:
    #     if candidate is None:
    #         return [Loc(row, c) for c in range(self.length)]
    #     return [loc for loc in self.house_row(row) if candidate in self.cell_candidates(loc)]
    #
    # def house_col(self, col: int) -> list[Loc]:
    #     return [Loc(r, col) for r in range(self.length)]


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


# class Knightoku:  
#     def __init__(self, puzzle: str) -> None:
#         super().__init__(puzzle)


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


class Minesweeper: 
    def is_solved(self) -> bool:
        return False

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
            self.grid.append(line.split(' '))

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


# class Snail3:
#     pass


# class Walls:
#     pass


# class Parks2:
#     pass





# class BattleShips:
#     pass


# class Clouds:
#     def is_solved(self):
#         return False


class PowerGrid(Puzzle):

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle, 1, 1)

    

    def __is_solved0(self,  house: list[Loc], power: Optional[int])->bool:
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
        return super().__str__()\
            .replace("  ", " ", -1)\
            .replace("  ", " ", -1)\
            .replace("  ", " ", -1)\
            .replace("  ", " ", -1)\
            .replace("10", "__", -1)\
            .replace("1_", "PP", -1)\
            .replace("_0", "..", -1)


# class Sentinels:
#     pass



# class Tents:
#     pass


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


# class HiddenStars:

#     def is_solved(self):
#         return False


# class Kakuro:
#     pass





class Mathrax:
    def __init__(self, puzzle: str) -> None:
        pass

    def solve0(self):
        pass



# class MineShips:
#     pass


# class Nurikabe:
#     pass

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


class Lighthouses(Puzzle):
    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)

    def is_solved(self)->bool:
        return False



class LightenUp:  # (Sudoku):
    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)
        
    def is_solved(self)->bool:
        return False

