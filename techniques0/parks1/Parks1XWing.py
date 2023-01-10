from Loc import Loc
from puzzles import Parks1

class Parks1FenceWing:

    def solve0(self, puzzle: Parks1) ->int:
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

    def solve1(self, puzzle: Parks1, unsolved0: list[Loc], unsolved1: list[Loc])->int:
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

class Parks1XWing:


    def solve_two_cell(self, puzzle: Parks1, cell0: Loc, cell1: Loc, candidate: int) -> int:
        edits = 0
        # edits = Parks1FenceWing().solve0(puzzle)

        if cell0.row == cell1.row:
            for row in set(range(puzzle.length)).difference([cell0.row]):
                other0 = Loc(row, cell0.col)
                other1 = Loc(row, cell1.col)
                corners = [cell0, cell1, other0, other1]
                other_candidates0 = puzzle.cell_candidates(other0)
                other_candidates1 = puzzle.cell_candidates(other1)
                if len(other_candidates0) == 1 or \
                        len(other_candidates1) == 1 or \
                        candidate not in other_candidates0 or \
                        candidate not in other_candidates1:
                    continue
                other_row_house = puzzle.house_row(other0.row, candidate)
                if len(other_row_house) != 2:
                    continue
                if {other0, other1} != set(other_row_house):
                    continue
                locs_to_remove_from = set(puzzle.house_col(other0.col) + puzzle.house_col(other1.col)).difference(corners)
                edits += puzzle.rem(locs_to_remove_from, [candidate])

        if cell0.col == cell1.col:
            for col in set(range(puzzle.length)).difference([cell0.col]):
                other0 = Loc(cell0.row, col)
                other1 = Loc(cell1.row, col)
                corners = [cell0, cell1, other0, other1]
                other_candidates0 = puzzle.cell_candidates(other0)
                other_candidates1 = puzzle.cell_candidates(other1)
                if len(other_candidates0) == 1 or \
                        len(other_candidates1) == 1 or \
                        candidate not in other_candidates0 or \
                        candidate not in other_candidates1:
                    continue
                other_col_house = puzzle.house_col(other0.col, candidate)
                if len(other_col_house) != 2:
                    continue
                if {other0, other1} != set(other_col_house):
                    continue
                locs_to_remove_from = set(puzzle.house_row(other0.row) + puzzle.house_row(other1.row)).difference(corners)
                edits += puzzle.rem(locs_to_remove_from, [candidate])

        return edits

    def solve_one_cell(self, puzzle: Parks1, cell0: Loc, candidate: int)->int:

        edits = 0
        # need to find the next cell to form a base

        row_cells = set(puzzle.house_row(cell0.row, candidate))
        col_cells = set(puzzle.house_col(cell0.col, candidate))

        if len(row_cells) == 2:
            row_cells.remove(cell0)
            edits += self.solve_two_cell(puzzle, cell0, row_cells.pop(), candidate)

        if len(col_cells) == 2:
            col_cells.remove(cell0)
            edits += self.solve_two_cell(puzzle, cell0, col_cells.pop(), candidate)


        return edits

    def solve0(self, puzzle: Parks1) -> int:
        edits = 0
        # print("heresssss")
        for r in range(puzzle.length):
            for c in range(puzzle.length):
                loc = Loc(r, c)

                if puzzle.is_cell_solved(loc):
                    continue

                for candidate in [1]:
                    edits += self.solve_one_cell(puzzle, loc, candidate)
        return edits



