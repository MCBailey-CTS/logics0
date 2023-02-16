

from Loc import Loc
from techniques.Technique import Technique


def solve_two_cell(puzzle, cell0: Loc, cell1: Loc, candidate: int) -> int:
    edits = 0
    if cell0.row == cell1.row:
        for row in set(range(len(puzzle))).difference([cell0.row]):
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
            locs_to_remove_from = set(puzzle.house_col(other0.col) + puzzle.house_col(other1.col)).difference(
                corners)
            edits += puzzle.rem(locs_to_remove_from, [candidate])

    if cell0.col == cell1.col:
        for col in set(range(len(puzzle))).difference([cell0.col]):
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
            locs_to_remove_from = set(puzzle.house_row(other0.row) + puzzle.house_row(other1.row)).difference(
                corners)
            edits += puzzle.rem(locs_to_remove_from, [candidate])

    return edits


class Parks1XWing(Technique):

    def solve_one_cell(self, puzzle, cell0: Loc, candidate: int) -> int:

        edits = 0
        # need to find the next cell to form a base

        row_cells = set(puzzle.house_row(cell0.row, candidate))
        col_cells = set(puzzle.house_col(cell0.col, candidate))

        if len(row_cells) == 2:
            row_cells.remove(cell0)
            edits += solve_two_cell(puzzle, cell0, row_cells.pop(), candidate)

        if len(col_cells) == 2:
            col_cells.remove(cell0)
            edits += solve_two_cell(puzzle, cell0, col_cells.pop(), candidate)

        return edits

    def solve0(self, puzzle) -> int:
        edits = 0
        for r in range(len(puzzle)):
            for c in range(len(puzzle)):
                loc = Loc(r, c)

                if puzzle.is_cell_solved(loc):
                    continue

                for candidate in [1]:
                    edits += self.solve_one_cell(puzzle, loc, candidate)
        return edits
