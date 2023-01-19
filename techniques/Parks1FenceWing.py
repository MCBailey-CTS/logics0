from puzzles import Parks1
from Loc import Loc
class Parks1FenceWing:

    def solve0(self, puzzle: Parks1) -> int:
        edits = 0
        fences = list(puzzle.fences())
        for fence0 in range(0, len(fences) - 1):
            if fences[fence0] != 'a':
                continue

            fence_locs0 = puzzle.house_fence(fences[fence0])
            solved_empty0 = [loc for loc in fence_locs0 if
                                len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
            solved_tree0 = [loc for loc in fence_locs0 if
                            len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
            unsolved0 = list(set(fence_locs0).difference(solved_tree0 + solved_empty0))
            if len(solved_tree0) == 1:
                continue
            for fence1 in range(1, len(fences)):
                if fences[fence1] != 'c':
                    continue
                fence_locs1 = puzzle.house_fence(fences[fence1])
                solved_empty1 = [loc for loc in fence_locs1 if
                                    len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 0]
                solved_tree1 = [loc for loc in fence_locs1 if
                                len(puzzle.cell_candidates(loc)) == 1 and puzzle.cell_candidates(loc)[0] == 1]
                unsolved1 = list(set(fence_locs1).difference(solved_tree1 + solved_empty1))
                if len(solved_tree1) == 1:
                    continue
                edits += self.solve1(puzzle, unsolved0, unsolved1)
        return edits

    def solve1(self, puzzle: Parks1, unsolved0: list[Loc], unsolved1: list[Loc]) -> int:
        edits = 0
        row_set0 = set([loc.row for loc in unsolved0])
        col_set0 = set([loc.col for loc in unsolved0])
        row_set1 = set([loc.row for loc in unsolved1])
        col_set1 = set([loc.col for loc in unsolved1])

        if col_set0 == col_set1:
            print("fence set cols")

        if row_set0 == row_set1:
            row_locs = []
            for row in row_set0:
                row_locs = row_locs + puzzle.house_row(row)
            locs_to_remove = set(row_locs).difference(unsolved0 + unsolved1)
            edits += puzzle.rem(locs_to_remove, [1])
        return edits
