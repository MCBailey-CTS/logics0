from Loc import Loc
from _puzzles import Sudoku


class XWing:

    def solve_two_cell(self, puzzle: Sudoku, cell0: Loc, cell1: Loc, candidate: int) -> int:
        edits = 0
        # print(f'{cell0} {cell1} {candidate}')

        if cell0.row == cell1.row:
            cell_xy = cell0
            cell_xz = cell1
            print("rows")
            # need to look up and down
            # pass

        if cell0.col == cell1.col:
            for col in range(puzzle.length):
                if col == cell0.col:
                    continue
                other0 = Loc(cell0.row, col)
                other1 = Loc(cell1.row, col)

                other_candidates0 = puzzle.cell_candidates(other0)
                other_candidates1 = puzzle.cell_candidates(other1)

                if len(other_candidates0) == 1 or \
                        len(other_candidates1) == 1 or \
                        candidate not in other_candidates0 or \
                        candidate not in other_candidates1:
                    continue

                # check if other candidates row only contains the two locations

                other_col_house = puzzle.house_col(other0.col, candidate)

                if len(other_col_house) != 2:
                    continue

                if {other0, other1} != set(other_col_house):
                    continue

                locs_to_remove_from = puzzle.house_col(other0.col) + puzzle.house_col(other1.col)

                print('1111')

                # if

                # print(f'{cell0} {cell1} {other0} {other1}')

            # need to look left and right
            # pass

        return edits

    def solve_one_cell(self, puzzle: Sudoku, cell0: Loc, candidate: int)->int:

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

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0
        for r in range(puzzle.length):
            for c in range(puzzle.length):
                loc = Loc(r, c)

                if puzzle.is_cell_solved(loc):
                    continue

                for candidate in puzzle.cell_candidates(loc):
                    edits += self.solve_one_cell(puzzle, loc, candidate)
        return edits


