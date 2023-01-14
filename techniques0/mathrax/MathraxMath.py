from Loc import Loc
from puzzles import Mathrax

PLUS = 1
MINUS = 0
EMPTY = MINUS

class MathraxMath:

    def solve0(self, puzzle: Mathrax) -> int:
        edits = 0
        for r in range(1, len(puzzle) * 2 - 1, 2):
            for c in range(1, len(puzzle) * 2 - 1, 2):
                loc = Loc(r, c)
                string = puzzle.grid[r][c]
                if '+' in string:
                    number = int(string.replace('+',''))
                    edits += self.solve_addition(puzzle, number, loc.top_left(), loc.bottom_right())
                    edits += self.solve_addition(puzzle, number, loc.top_right(), loc.bottom_left())
        return edits

    @staticmethod
    def __solve_addition(puzzle:Mathrax, number:int, cell0: Loc, cell1: Loc)->int:
        edits = 0
        candidates1 = set(puzzle.cell_candidates(cell1))
        for candidate0 in puzzle.cell_candidates(cell0):
            if any(candidate0 + candidate1 == number for candidate1 in candidates1 ):
                continue
            edits += puzzle.rem([cell0], [candidate0])
        return edits

    def solve_addition(self, puzzle:Mathrax, number:int, cell0: Loc, cell1: Loc)->int:
        edits = self.__solve_addition(puzzle, number, cell0, cell1)
        edits = self.__solve_addition(puzzle, number, cell1, cell0)
        return edits
