from _puzzles import Sudoku


class CrossHatchRobotFences:
    @staticmethod
    def solve0(puzzle: Sudoku) -> int:
        edits = 0
        for cell in list(puzzle.unsolved_cells()):
            neighbors = set(puzzle.house_row(cell.row) + puzzle.house_col(cell.col))
            neighbors.remove(cell)
            for neighbor in neighbors:
                if neighbor not in puzzle.unsolved_cells():
                    _candidates = puzzle.cell_candidates(neighbor)
                    if len(_candidates) == 1:
                        edits += puzzle.rem(cell, [list(_candidates)[0]])
        return edits


