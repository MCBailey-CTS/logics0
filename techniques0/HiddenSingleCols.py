from _puzzles import Sudoku
from techniques0 import HiddenSingle


class HiddenSingleCols:
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0
        for house in puzzle.houses_cols():
            edits += HiddenSingle.solve1(puzzle, house)
        return edits
