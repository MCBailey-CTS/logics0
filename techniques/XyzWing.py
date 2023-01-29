from Loc import Loc
from puzzles import Sudoku
from techniques.Technique import Technique


class XyzWing(Technique):
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        for r in range(len(puzzle)):
            for c in range(len(puzzle)):
                pivot = Loc(r, c)

                pivot_candidates = puzzle.cell_candidates(pivot)

                if len(pivot_candidates) != 3:
                    continue

                # row_col_locs = [loc for loc in puzzle.house_row(pivot.row) + puzzle.house_col(pivot.col) if pivot != loc and ]
                #
                # for pincer in row_col_locs:
                #     pincer_candidates = puzzle.cell_candidates(pincer)
                #
                #     if loc



        return edits