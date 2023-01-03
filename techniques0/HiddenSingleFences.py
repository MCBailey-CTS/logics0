from _puzzles import Sudoku
from techniques0 import HiddenSingle


class HiddenSingleFences:
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0
        for house in puzzle.houses_fences():
            edits += HiddenSingle.solve1(puzzle, house)
        return edits
