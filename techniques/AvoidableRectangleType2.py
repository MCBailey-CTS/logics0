from Loc import Loc
from techniques.BaseUniqueRectangle import BaseUniqueRectangle
import numpy
from colorama import Fore


class AvoidableRectangleType2(BaseUniqueRectangle):

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

        if len(ne_candidates) == 1 and len(se_candidates) == 1:
            if set(ne_candidates) != set(se_candidates) and len(nw_candidates) == 2 and len(sw_candidates) == 2:
                if len(nw_candidates) == 2 and len(sw_candidates) == 2:
                    if set(nw_candidates) != set(sw_candidates):
                        ne_nw_intersection = set(ne_candidates).intersection(nw_candidates)
                        se_sw_intersection = set(se_candidates).intersection(sw_candidates)
                        nw_sw_intersection = set(nw_candidates).intersection(sw_candidates)
                        if len(ne_nw_intersection) == 0 and len(se_sw_intersection) == 0 and len(
                                nw_sw_intersection) == 1:
                            if set(sw_candidates).issuperset(ne_candidates) and set(nw_candidates).issuperset(
                                    se_candidates):
                                extra_candidate = list(nw_sw_intersection)[0]
                                puzzle.override_loc_color([nw, sw], Fore.YELLOW)
                                puzzle.override_loc_color([ne, se], Fore.GREEN)
                                nw_fence_house = puzzle.house_fence(puzzle.cell_fence(nw))
                                sw_fence_house = puzzle.house_fence(puzzle.cell_fence(sw))
                                remove = set(nw_fence_house).intersection(sw_fence_house)
                                if nw.col == sw.col:
                                    remove = remove.union(puzzle.house_col(nw.col)).difference([nw, sw])
                                if nw.row == sw.row:
                                    remove = remove.union(puzzle.house_row(nw.row)).difference([nw, sw])
                                edits += puzzle.rem(remove, [extra_candidate])
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
