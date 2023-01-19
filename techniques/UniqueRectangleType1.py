from techniques.BaseUniqueRectangle import BaseUniqueRectangle
from puzzles import Sudoku
from Loc import Loc

class UniqueRectangleType1(BaseUniqueRectangle):
    def solve_rectangle(self, puzzle: Sudoku, corners: list[Loc]) -> int:
        edits = 0
        corner_set = set(corners)

        length_2 = [loc for loc in corners if len(puzzle.cell_candidates(loc)) == 2]

        if len(length_2) != 3:
            return edits

        candidate_set = set()

        for loc in length_2:
            cell = puzzle.cell_candidates(loc)

            if len(cell) == 1:
                return edits
            for c in cell:
                candidate_set.add(c)

        if len(candidate_set) != 2:
            return edits

        corner_unique_set = corner_set.difference(length_2)

        if len(corner_unique_set) != 1:
            return edits

        edits += puzzle.rem([corner_unique_set.pop()], candidate_set)

        return edits
