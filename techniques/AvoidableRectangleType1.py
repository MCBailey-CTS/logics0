from puzzles import Sudoku
from Loc import Loc
from techniques.Technique import Technique


class AvoidableRectangleType1(Technique):

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        solved_cells = []
        for r in range(len(puzzle)):
            for c in range(len(puzzle)):
                loc = Loc(r, c)
                if len(puzzle.cell_candidates(loc)) == 1:
                    solved_cells.append(loc)

        for upper_corner in solved_cells:
            for lower_corner in solved_cells:
                other_upper = Loc(upper_corner.row, lower_corner.col)
                other_lower = Loc(lower_corner.row, upper_corner.col)
                corner_set = {upper_corner, lower_corner, other_upper, other_lower}

                if len(corner_set) != 4:
                    continue

                # if not corner_set.issuperset([Loc(0, 0), Loc(0, 1), Loc(8, 0), Loc(8, 1)]):
                #     continue

                row_set = set([loc.row for loc in corner_set])
                col_set = set([loc.col for loc in corner_set])
                fence_set = set([puzzle.cell_fence(loc) for loc in corner_set])

                if len(row_set) != 2 or len(col_set) != 2 or len(fence_set) != 2:
                    continue

                solved_cells = set([loc for loc in corner_set if len(puzzle.cell_candidates(loc)) == 1])

                if len(solved_cells) != 3:
                    continue

                unsolved_cells = set([loc for loc in corner_set if len(puzzle.cell_candidates(loc)) > 1])

                if len(unsolved_cells) != 1:
                    continue

                opposite_corners = set(corner_set)

                opposite_corners.remove(other_upper)
                opposite_corners.remove(other_lower)

                temp_opposite = list(opposite_corners)

                opposite_candidates0 = set(puzzle.cell_candidates(temp_opposite[0]))
                opposite_candidates1 = puzzle.cell_candidates(temp_opposite[1])

                if len(opposite_candidates0) != 1 or len(opposite_candidates1) != 1:
                    continue

                if not opposite_candidates0.issubset(opposite_candidates1):
                    continue

                # opposite_candidate = opposite_candidates0.pop()

                other_solved_cell = list(solved_cells.difference(opposite_corners))[0]

                solved_candidate = list(puzzle.cell_candidates(other_solved_cell))[0]

                edits += puzzle.rem(unsolved_cells.pop(), [solved_candidate])


        return edits