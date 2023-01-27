from puzzles import Sudoku
from techniques.Technique import Technique
from techniques.BaseUniqueRectangle import BaseUniqueRectangle
from Loc import Loc
from colorama import Fore


class AvoidableRectangleType1(BaseUniqueRectangle):

    def solve_rectangle(self, puzzle: Sudoku, corners: list[Loc]) -> int:
        edits = 0

        rows = set([loc.row for loc in corners])
        cols = set([loc.col for loc in corners])
        fences = set([puzzle.cell_fence(loc) for loc in corners])

        if len(rows) != 2 or len(cols) != 2 or len(fences) != 2:
            return edits

        length_1 = [loc for loc in corners if len(puzzle.cell_candidates(loc)) == 1]

        if len(length_1) != 3:
            return edits

        solved_candidates = set(puzzle.cell_candidates(loc)[0] for loc in length_1)

        if len(solved_candidates) != 2:
            return edits

        solved0, solved1 = solved_candidates

        locs0 = [loc for loc in length_1 if solved0 == puzzle.cell_candidates(loc)[0]]
        locs1 = [loc for loc in length_1 if solved1 == puzzle.cell_candidates(loc)[0]]

        if len(locs0) == 2 and len(locs1) == 1:
            two_solved_candidate = solved0
            single_solved_candidate = solved1
        elif len(locs1) == 2 and len(locs0) == 1:
            two_solved_candidate = solved1
            single_solved_candidate = solved0
        else:
            return edits

        min_row = min(corner.row for corner in corners)
        max_row = max(corner.row for corner in corners)
        min_col = min(corner.col for corner in corners)
        max_col = max(corner.col for corner in corners)
        # narray = numpy.empty((2, 2), dtype=object)
        nw = Loc(min_row, min_col)
        ne = Loc(min_row, max_col)
        sw = Loc(max_row, min_col)
        se = Loc(max_row, max_col)

        # north-west -- south-east
        if set(puzzle.cell_candidates(nw)) == {two_solved_candidate} and\
                set(puzzle.cell_candidates(se)) == {two_solved_candidate}:
            # south-west solved
            if set(puzzle.cell_candidates(sw)) == {single_solved_candidate}:
                edits += puzzle.rem([ne], [single_solved_candidate])
            # north-east solved
            if set(puzzle.cell_candidates(ne)) == {single_solved_candidate}:
                edits += puzzle.rem([sw], [single_solved_candidate])

        # north-east -- south-west
        if set(puzzle.cell_candidates(ne)) == {two_solved_candidate} and\
                set(puzzle.cell_candidates(sw)) == {two_solved_candidate}:
            # south-east solved
            if set(puzzle.cell_candidates(se)) == {single_solved_candidate}:
                edits += puzzle.rem([nw], [single_solved_candidate])
            # north-west solved
            if set(puzzle.cell_candidates(nw)) == {single_solved_candidate}:
                edits += puzzle.rem([se], [single_solved_candidate])
        return edits
