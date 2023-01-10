from puzzles import Sudoku
from Loc import Loc

class Bug:

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        unsolved = puzzle.unsolved_cells()

        if len(unsolved) == 0:
            return edits

        length_1: list[Loc] = list()
        length_2: list[Loc] = list()
        length_3: list[Loc] = list()

        for loc in puzzle.list_all_cell_locs():
            _candidates = puzzle.cell_candidates(loc)

            if len(_candidates) == 1:
                length_1.append(loc)
                continue
            if len(_candidates) == 2:
                length_2.append(loc)
                continue

            if len(_candidates) == 3:
                length_3.append(loc)
                continue

            return edits

        total = puzzle.length * puzzle.length

        if len(length_3) != 1 or total != len(length_3) + len(length_2) + len(length_1):
            return edits

        row_house, col_house, fence_house = puzzle.houses_rows_cols_fences(length_3[0])

        for candidate in list(puzzle.cell_candidates(length_3[0])):
            row_count = [l for l in row_house if candidate in puzzle.cell_candidates(l)]
            col_count = [l for l in col_house if candidate in puzzle.cell_candidates(l)]
            fence_count = [l for l in fence_house if candidate in puzzle.cell_candidates(l)]

            if len(row_count) == 3 and len(col_count) == 3 and len(fence_count) == 3:
                for c in list(puzzle.cell_candidates(length_3[0])):
                    if c == candidate:
                        continue
                    edits += puzzle.rem(length_3[0], [c])

        return edits