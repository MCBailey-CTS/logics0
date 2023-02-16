from abc import abstractmethod

from techniques.Technique import Technique
from Loc import Loc


class BaseSudokuHouseTechnique(Technique):

    def solve0(self, puzzle) -> int:
        edits = 0
        unsolved = puzzle.unsolved_cells()
        if len(unsolved) == 0:
            return edits
        houses = puzzle.houses_rows() + puzzle.houses_cols()
        if puzzle.has_fences:
            houses = houses + puzzle.houses_fences()
        edits += sum(self.solve_house(puzzle, house) for house in houses)
        return edits

    @abstractmethod
    def solve_house(self, puzzle, house: list[Loc]) -> int:
        raise NotImplementedError()