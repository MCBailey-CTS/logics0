from Loc import Loc
from puzzles import Parks1


class Parks1HiddenSingle:
    def solve0(self, puzzle: Parks1) -> int:
        edits = 0
        fence_dict = {}
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
            if len(unsolved) == 1:
                edits += puzzle.rem(unsolved, [0])
        return edits
