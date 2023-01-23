from Loc import Loc
from puzzles import Sudoku


class LockedCandidatesPointing:

    @staticmethod
    def solve0(puzzle: Sudoku) -> int:
        edits = 0
        unsolved = puzzle.unsolved_cells()

        if len(unsolved) == 0:
            return edits
        for house in puzzle.houses_rows_cols_fences():
            for candidate in puzzle.expected_candidates():
                locs = [loc for loc in house if candidate in puzzle.cell_candidates(loc)]
                loc_set = set(locs)
                if len(locs) < 2:
                    continue
                if all([locs[0].row == loc.row for loc in locs]):
                    for loc in puzzle.house_row(locs[0].row):
                        if loc not in loc_set:
                            edits += puzzle.rem(loc, [candidate])
                if all([locs[0].col == loc.col for loc in locs]):
                    for loc in puzzle.house_col(locs[0].col):
                        if loc not in loc_set:
                            edits += puzzle.rem(loc, [candidate])
        return edits
