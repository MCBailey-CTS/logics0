import numpy
from colorama import Fore

from Loc import Loc
from techniques.BaseUniqueRectangle import BaseUniqueRectangle


class UniqueRectangleType2(BaseUniqueRectangle):

    def solve_temp(self, puzzle, narray: numpy.ndarray) -> int:
        edits = 0
        nw = narray[0][0]
        ne = narray[0][1]

        sw = narray[1][0]
        se = narray[1][1]

        ne_candidates = puzzle.cell_candidates(ne)
        se_candidates = puzzle.cell_candidates(se)

        nw_candidates = puzzle.cell_candidates(nw)
        sw_candidates = puzzle.cell_candidates(sw)

        if len(ne_candidates) == 3 and len(se_candidates) == 3:
            if set(ne_candidates) == set(se_candidates):
                if len(nw_candidates) == 2 and len(sw_candidates) == 2:
                    if set(nw_candidates) == set(sw_candidates) and set(ne_candidates).issuperset(set(sw_candidates)):
                        puzzle.override_loc_color([nw, sw], Fore.GREEN)
                        puzzle.override_loc_color([ne, se], Fore.YELLOW)
                        candidate = set(ne_candidates).difference(set(sw_candidates)).pop()

                        ne_fence_house = puzzle.house_fence(puzzle.cell_fence(ne))
                        se_fence_house = puzzle.house_fence(puzzle.cell_fence(se))

                        remove = set(ne_fence_house).intersection(se_fence_house)

                        if ne.col == se.col:
                            remove = remove.union(puzzle.house_col(ne.col)).difference([ne, se])

                        if ne.row == se.row:
                            remove = remove.union(puzzle.house_row(ne.row)).difference([ne, se])

                        edits += puzzle.rem(remove, [candidate])
        return edits

    def solve_rectangle(self, puzzle, corners: list[Loc]):
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
