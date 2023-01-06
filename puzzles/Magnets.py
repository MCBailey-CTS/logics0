
PLUS = '+'
MINUS = '-'
EMPTY = '.'
from Loc import Loc
# from 

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

