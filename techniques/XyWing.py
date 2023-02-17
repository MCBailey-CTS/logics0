from techniques.Technique import Technique
from Loc import Loc
from colorama import Fore


class XyWing(Technique):

    # def solve1(self, puzzle, pincer0: Loc)->int:
    #     edits = 0
    #
    #     for r in range(len(puzzle)):
    #         for c in range(len(puzzle)):
    #             pivot = Loc(r, c)
    #             if pivot == pincer0:
    #                 continue
    #             if len(puzzle.cell_candidates(pincer0)) != 2:
    #                 continue
    #
    #             if pincer0.row != pivot.row and pincer0.col != pivot.col:
    #
    #
    #
    #
    #     return edits

    def solve0(self, puzzle) -> int:
        edits = 0

        unsolved = puzzle.unsolved_cells()

        if len(puzzle.unsolved_cells()) == 0:
            return edits

        for r in range(len(puzzle)):
            for c in range(len(puzzle)):
                pivot = Loc(r, c)
                pivot_candidates = set(puzzle.cell_candidates(pivot))
                if len(pivot_candidates) != 2:
                    continue

                length2_in_row = [loc
                                  for loc in puzzle.house_row(pivot.row)
                                  if pivot != loc and
                                  len(puzzle.cell_candidates(loc)) == 2
                                  and len(
                        set(puzzle.cell_candidates(loc)).intersection(puzzle.cell_candidates(pivot))) == 1]


                for row_loc in length2_in_row:
                    pincer0_candidate = set(puzzle.cell_candidates(row_loc)).difference(pivot_candidates).pop()
                    pincer1_expected = set(pivot_candidates).difference(puzzle.cell_candidates(row_loc)).pop()
                    expected_wing = {pincer0_candidate, pincer1_expected}
                    for col_loc in set(puzzle.house_col(pivot.col)).difference([pivot]):
                        if expected_wing == set(puzzle.cell_candidates(col_loc)):
                            puzzle.override_loc_color([col_loc, row_loc], Fore.YELLOW)
                            puzzle.override_loc_color([pivot], Fore.GREEN)
                            intersection = set(puzzle.cell_candidates(row_loc)).intersection(
                                puzzle.cell_candidates(col_loc))
                            pincer_intersections = [Loc(row_loc.row, col_loc.col), Loc(col_loc.row, row_loc.col)]
                            remove = [loc for loc in pincer_intersections if loc != pivot]
                            intersect_candidate = intersection.pop()
                            puzzle.override_loc_color(remove, Fore.RED)
                            puzzle.rem(remove, [intersect_candidate])

        return edits