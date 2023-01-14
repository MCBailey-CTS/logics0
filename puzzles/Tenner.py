from puzzles import Puzzle
from typing import Union
from Loc import Loc
from colorama import Fore, Style


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
        for row in range(len(self) + 1):
            temp = []
            split = array[row].replace("-1", "0123456789", -1) \
                .replace("\r", " ", -1) \
                .replace("\t", " ", -1)\
                .replace("  ", " ", -1)\
                .strip().split(' ')

            for t in split:
                if len(t) == 0:
                    continue
                if row != len(self) and t == "00":
                    temp.append("0_________")
                elif row != len(self) and t == "01":
                    temp.append("_1________")
                elif row != len(self) and t == "02":
                    temp.append("__2_______")
                elif row != len(self) and t == "03":
                    temp.append("___3______")
                elif row != len(self) and t == "04":
                    temp.append("____4_____")
                elif row != len(self) and t == "05":
                    temp.append("_____5____")
                elif row != len(self) and t == "06":
                    temp.append("______6___")
                elif row != len(self) and t == "07":
                    temp.append("_______7__")
                elif row != len(self) and t == "08":
                    temp.append("________8_")
                elif row != len(self) and t == "09":
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
        if len(solved_candidates) != len(self):
            return False
        total = self.total(col)
        if total is None:
            return True
        return sum(solved_candidates) == total

    def is_solved(self) -> bool:
        for row in range(len(self)):
            if not self.is_row_house_solved(row):
                print(f'print bad row: {row}')

                return False

        for col in range(self.col_length):
            if not self.is_col_house_solved(col):
                print(f'print bad col: {col}')
                return False

        for r in range(len(self)):
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
                    if direction.row >= len(self) or direction.col >= 10:
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
        string += f'{len(self)}\n'
        for r in range(len(self) + 1):
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
        return [Loc(row, loc_col) for row in range(len(self))]

    def total(self, col: int) -> Union[int, None]:
        string = self.grid[len(self)][col]
        if string.isnumeric():
            return int(string)
        return None
