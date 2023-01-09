from abc import abstractmethod

from Loc import Loc
from _puzzles import Sudoku
from techniques0 import *
class BaseSudokuHouseTechnique(Technique):

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        unsolved = puzzle.unsolved_cells()

        if len(unsolved) == 0:
            return edits

        for house in puzzle.houses_rows_cols_fences():
            edits += self.solve_house(puzzle, house)

        return edits

    @abstractmethod
    def solve_house(self, puzzle: Sudoku, house: list[Loc])->int:
        pass
