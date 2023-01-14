from puzzles import Puzzle
from Loc import Loc


class Mathrax(Puzzle):

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)

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

    def iterate_cell_locs(self)->list[Loc]:
        locs = []
        for r in range(0, len(self) * 2 - 1, 2):
            for c in range(0, len(self) * 2 - 1, 2):
                locs.append(Loc(r,c))
        return locs

    def is_solved(self) -> bool:
        # for house in self.houses_rows() + self.houses_cols()    :
        #     solved_candidates = [list(self.cell_candidates(loc))[0] for loc in house if
        #                          len(self.cell_candidates(loc)) == 1]
        #
        #     if len(solved_candidates) != len(self):
        #         print(house)
        #         print(solved_candidates)
        #         print("house wasn't completely solved")
        #         return False
        #
        #     expected = set(self.expected_candidates())
        #
        #     if expected.issubset(solved_candidates) and expected.issuperset(solved_candidates):
        #         continue
        #
        #     print(solved_candidates)
        #
        #     return False
        #
        # return True
        return len(self.unsolved_cells()) == 0 and all(len(self.cell_candidates(loc)) == 1 for loc in self.iterate_cell_locs() )

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
