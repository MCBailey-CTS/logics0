from Loc import Loc
from puzzles import Parks1


class Parks1LockedCandidatesPointing:

    def solve0(self, puzzle: Parks1) -> int:
        edits = 0
        fence_dict = {}

        # for house in puzzle.
        for r in range(len(puzzle)):
            for c in range(len(puzzle)):
                loc = Loc(r, c)
                fence = puzzle.cell_fence(loc)
                if fence not in fence_dict:
                    fence_dict[fence] = []
                fence_dict[fence].append(loc)

        for fence in fence_dict.keys():
            fence_locs = fence_dict[fence]
            solved_empty = [loc for loc in fence_locs if
                            len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
            solved_tree = [loc for loc in fence_locs if
                           len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
            unsolved = list(set(fence_locs).difference(solved_tree + solved_empty))
            if len(solved_tree) == 1:
                continue
            if len(unsolved) >= 2:
                rows = set([loc.row for loc in unsolved])
                cols = set([loc.col for loc in unsolved])
                if len(rows) == 1:
                    temp = set(puzzle.house_row(rows.pop())).difference(unsolved)
                    edits += puzzle.rem(list(temp), [1])
                if len(cols) == 1:
                    temp = set(puzzle.house_col(cols.pop())).difference(unsolved)
                    edits += puzzle.rem(list(temp), [1])
        return edits



