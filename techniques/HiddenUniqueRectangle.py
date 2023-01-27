from techniques.BaseUniqueRectangle import BaseUniqueRectangle
from puzzles.Sudoku import Sudoku
from Loc import Loc
from colorama import Fore


class HiddenUniqueRectangle(BaseUniqueRectangle):
    def solve_rectangle(self, puzzle: Sudoku, corners: list[Loc]):
        edits: int = 0
        length_2 = [loc for loc in corners if len(puzzle.cell_candidates(loc)) == 2]
        if len(length_2) != 1:
            return edits
        length_2_candidates = puzzle.cell_candidates(length_2[0])
        length_more = [loc for loc in corners if
                       length_2[0] != loc and set(puzzle.cell_candidates(loc)).issuperset(length_2_candidates)]
        if len(length_more) != 3:
            return edits
        for corner in length_more:
            other0, other1 = set(length_more).difference([corner])
            if (corner.in_same_row(other0) and corner.in_same_col(other1)) or (
                    corner.in_same_col(other0) and corner.in_same_row(other1)):
                row_col_house = set(puzzle.house_row(corner.row) + puzzle.house_col(corner.col)).difference(corners)
                candidate0, candidate1 = length_2_candidates
                if not any(candidate0 in puzzle.cell_candidates(loc) for loc in row_col_house):
                    edits += puzzle.rem([corner], [candidate1])
                if not any(candidate1 in puzzle.cell_candidates(loc) for loc in row_col_house):
                    edits += puzzle.rem([corner], [candidate0])
        return edits
