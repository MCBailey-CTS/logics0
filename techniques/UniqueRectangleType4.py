from Loc import Loc
from puzzles import Sudoku

from techniques.BaseUniqueRectangle import BaseUniqueRectangle
import numpy
from colorama import Fore


class UniqueRectangleType4(BaseUniqueRectangle):

    def solve_temp(self, puzzle: Sudoku, narray: numpy.ndarray) -> int:
        edits = 0
        nw = narray[0][0]
        ne = narray[0][1]

        sw = narray[1][0]
        se = narray[1][1]

        ne_candidates = puzzle.cell_candidates(ne)
        se_candidates = puzzle.cell_candidates(se)

        nw_candidates = puzzle.cell_candidates(nw)
        sw_candidates = puzzle.cell_candidates(sw)

        # puzzle.override_loc_color([Loc(1, 1), Loc(2, 2), Loc(2, 1), Loc(1, 2)], Fore.RED)

        # if {nw, ne, sw, se} == {Loc(1, 1), Loc(2, 2), Loc(2, 1), Loc(2, 1)}:
        #     print('herre')

        if len(sw_candidates) != 2 or len(se_candidates) != 2:
            return edits

        if set(sw_candidates) != set(se_candidates):
            return edits

        if not set(ne_candidates).issuperset(sw_candidates) or not set(nw_candidates).issuperset(sw_candidates):
            return edits

        if {Loc(1, 1), Loc(2, 1)} == {ne, nw} and {Loc(2, 2), Loc(1, 2)} == {se, sw}:
            puzzle.override_loc_color([ne, nw], Fore.YELLOW)
            puzzle.override_loc_color([se, sw], Fore.GREEN)

        candidate0, candidate1 = sw_candidates

        if ne.row == nw.row:
            candidate0_locs = puzzle.house_row(ne.row, candidate0)
            candidate1_locs = puzzle.house_row(ne.row, candidate1)
        elif ne.col == nw.col:
            candidate0_locs = puzzle.house_col(ne.col, candidate0)
            candidate1_locs = puzzle.house_col(ne.col, candidate1)
        else:
            return edits


        if len(candidate0_locs) == 2 and set(candidate0_locs) == {ne, nw}:
            remove_candidate = candidate1

        elif len(candidate1_locs) == 2 and set(candidate1_locs) == {ne, nw}:
            remove_candidate = candidate0
        else:
            return edits

        puzzle.override_loc_color([sw, se], Fore.GREEN)

        edits += puzzle.rem([ne, nw], [remove_candidate])

        return edits

    def solve_rectangle(self, puzzle: Sudoku, corners: list[Loc]):
        edits = 0
        # if puzzle.
        rows = set([loc.row for loc in corners])
        cols = set([loc.col for loc in corners])
        fences = set([puzzle.cell_fence(loc) for loc in corners])
        if len(rows) != 2 or len(cols) != 2 or len(fences) != 2:
            return edits
        min_row = min(corner.row for corner in corners)
        max_row = max(corner.row for corner in corners)
        min_col = min(corner.col for corner in corners)
        max_col = max(corner.col for corner in corners)
        narray = numpy.empty((2, 2), dtype=object)
        nw = Loc(min_row, min_col)
        ne = Loc(min_row, max_col)
        sw = Loc(max_row, min_col)
        se = Loc(max_row, max_col)
        narray[0][0] = nw
        narray[0][1] = ne
        narray[1][0] = sw
        narray[1][1] = se
        for _ in range(4):
            narray = numpy.rot90(narray, 1)
            edits += self.solve_temp(puzzle, narray)
            # if temp_edits > 0:
            #     return temp_edits
            # edits +=
        return edits
