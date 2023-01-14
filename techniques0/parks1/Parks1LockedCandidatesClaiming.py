from puzzles import Parks1
from Loc import Loc


class Parks1LockedCandidatesClaiming:

    def solve1(self, puzzle: Parks1, row_col_house: list[Loc])->int:
        edits = 0

        solved_empty = [loc for loc in row_col_house if
                            len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
        solved_tree = [loc for loc in row_col_house if
                       len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
        unsolved = list(set(row_col_house).difference(solved_tree + solved_empty))

        if len(solved_tree) == 1:
            return edits

        fence = puzzle.cell_fence(unsolved[0])

        if not all(fence == puzzle.cell_fence(loc) for loc in unsolved):
            return edits

        fence_locs = set(puzzle.house_fence(fence))

        locs_to_remove = list(fence_locs.difference(unsolved))


        return puzzle.rem(locs_to_remove, [1])

    def solve0(self, puzzle: Parks1) -> int:
        edits = 0

        for index in range(len(puzzle)):
            edits += self.solve1(puzzle, puzzle.house_row(index)) + self.solve1(puzzle, puzzle.house_col(index))

        return edits
