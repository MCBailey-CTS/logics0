from Loc import Loc
from _puzzles import Sudoku


class HiddenUniqueRectangle:
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0
        # return 0
        for corner0 in list(puzzle.unsolved_cells()):
            for corner1 in list(puzzle.unsolved_cells()):

                other_opposite0 = Loc(corner0.row, corner1.col)
                other_opposite1 = Loc(corner1.row, corner0.col)
                corners = [
                    corner0,
                    corner1,
                    other_opposite0,
                    other_opposite1
                ]

                rows = set([loc.row for loc in corners])
                cols = set([loc.col for loc in corners])
                fences = set([puzzle.cell_fence(loc) for loc in corners])

                if len(rows) != 2 or len(cols) != 2 or len(fences) != 2:
                    continue

                corner0_candidates = puzzle.cell_candidates(corner0)

                if len(corner0_candidates) != 2:
                    continue

                # check to see if the other corners are a super set of corner0
                all_temp = all([set(puzzle.cell_candidates(loc)).issuperset(corner0_candidates) for loc in
                                [corner1, other_opposite0, other_opposite1]])

                if not all_temp:
                    continue

                hidden_unique_cells = set(puzzle.house_row(corner1.row) + puzzle.house_col(corner1.col)).difference(
                    corners)

                candidate0, candidate1 = corner0_candidates

                candidate0_any = any([candidate0 in puzzle.cell_candidates(loc) for loc in hidden_unique_cells])
                candidate1_any = any([candidate1 in puzzle.cell_candidates(loc) for loc in hidden_unique_cells])

                if candidate0_any and candidate1_any:
                    continue

                if candidate0_any:
                    edits += puzzle.rem(corner1, [candidate0])

                if candidate1_any:
                    edits += puzzle.rem(corner1, [candidate1])

                # print("mssssade aaaait here")

        return edits

