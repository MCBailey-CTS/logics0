from _puzzles import Sudoku


class LockedCandidatesClaiming:

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0
        unsolved = puzzle.unsolved_cells()

        if len(unsolved) == 0:
            return edits
        for house in puzzle.houses_rows_cols():
            for candidate in puzzle.expected_candidates():
                locs = [
                    loc
                    for loc in house
                    if candidate in puzzle.cell_candidates(loc)
                ]
                fences = set([puzzle.cell_fence(l) for l in locs])
                if len(fences) != 1:
                    continue
                fence = list(fences)[0]
                loc_set = set(locs)
                for loc in puzzle.house_fence(fence):
                    if loc not in loc_set:
                        edits += puzzle.rem(loc, [candidate])
        return edits
