from puzzles import Puzzle
from Loc import Loc


class Sudoku(Puzzle):

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)

        self.__unsolved_locs: set[Loc] = set()

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

                if len(self.cell_candidates(loc)) > 1:
                    self.__unsolved_locs.add(loc)

    def rem(self, locs: list[Loc], candidates: iter) -> int:
        edits = 0
        if isinstance(locs, Loc):
            return self.rem([locs], candidates)
        for loc in locs:
            for candidate in candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                if len(cell_candidates) == 1:
                    raise Exception(f'Cannot remove final candidate {candidate} from Loc {loc}')
                if len(cell_candidates) == 2:
                    self.__unsolved_locs.remove(loc)
                self.grid[loc.row][loc.col] = self.grid[loc.row][loc.col].replace(str(candidate), "_")
                edits += 1
        return edits

    def unsolved_cells(self) -> set[Loc]:
        # unsolved = set()
        # for r in range(self.length):
        #     for c in range(self.length):
        #         loc = Loc(r, c)
        #         if len(self.cell_candidates(loc)) == 1:
        #             continue
        #         unsolved.add(loc)
        # return unsolved
        return self.__unsolved_locs

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
