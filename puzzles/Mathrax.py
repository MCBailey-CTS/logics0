from puzzles import Puzzle
from Loc import Loc


class Mathrax(Puzzle):

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)

    def house_row(self, row: int, candidate=None) -> list[Loc]:
        if candidate is None:

            # return
            temp = [Loc(row, c) for c in range(0, len(self) * 2 - 1, 2)]
            print(temp)
            return temp
        return [loc for loc in self.house_row(row) if candidate in self.cell_candidates(loc)]

    def house_col(self, col: int, candidate=None) -> list[Loc]:
        return []
        # if candidate is None:
        #     return [Loc(r, col) for r in range(len(self))]
        # return [loc for loc in self.house_col(col) if candidate in self.cell_candidates(loc)]

    @property
    def has_fences(self):
        return False

    def is_solved(self) -> bool:
        return False

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
                string += f'{self.grid[r][c].ljust(len(self))} '
            string += '\n'
        return string
