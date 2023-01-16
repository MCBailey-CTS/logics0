from puzzles import Puzzle
from Loc import Loc
from colorama import Fore, Style


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

            if  expected.issubset(solved_candidates) and  expected.issuperset(solved_candidates):

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
