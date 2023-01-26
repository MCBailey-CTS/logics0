from Loc import Loc
from puzzles import Sudoku
from techniques.BaseUniqueRectangle import BaseUniqueRectangle


class AvoidableRectangleType2(BaseUniqueRectangle):

    def solve_rectangle(self, puzzle: Sudoku, corners: list[Loc]) -> int:
        edits = 0
        return edits

    # def solve_rectangle(self, puzzle: Sudoku, corners: list[Loc]) -> int:
    #     edits = 0
    #     if len(corners) != 4:
    #         return edits
    #     corner_set = set(corners)
    #     base0 = next((loc for loc in corner_set if len(puzzle.cell_candidates(loc)) == 1), None)
    #     if base0 is None:
    #         return edits
    #     corner_set.remove(base0)
    #     base1 = next((loc for loc in corner_set if len(puzzle.cell_candidates(loc)) == 1), None)
    #     if base1 is None:
    #         return edits
    #     corner_set.remove(base1)
    #     same_row = base0.in_same_row(base1)
    #     same_col = base0.in_same_col(base1)
    #     opp_base0 = next((loc for loc in corner_set if len(puzzle.cell_candidates(loc)) == 2 and (
    #             same_row and base0.in_same_col(loc) or same_col and base0.in_same_row(loc))), None)
    #     if opp_base0 is None:
    #         return edits
    #     corner_set.remove(opp_base0)
    #     opp_base1 = next((loc for loc in corner_set if len(puzzle.cell_candidates(loc)) == 2 and (
    #             same_row and base1.in_same_col(loc) or same_col and base1.in_same_row(loc))), None)
    #     if opp_base1 is None:
    #         return edits
    #     corner_set.remove(opp_base1)
    #     base0_candidates = puzzle.cell_candidates(base0)
    #     base1_candidates = puzzle.cell_candidates(base1)
    #     opp_base0_candidates = set(puzzle.cell_candidates(opp_base0))
    #     opp_base1_candidates = set(puzzle.cell_candidates(opp_base1))
    #     if base0_candidates[0] not in opp_base1_candidates or base1_candidates[0] not in opp_base0_candidates:
    #         return edits
    #     opp_base0_candidates.remove(base1_candidates[0])
    #     opp_base1_candidates.remove(base0_candidates[0])
    #     if opp_base0_candidates != opp_base1_candidates:
    #         return edits
    #     __base = (base0, base1)
    #     __opp_base = (opp_base0, opp_base1)
    #     candidate = opp_base0_candidates.pop()
    #     rows = set(loc.row for loc in __opp_base)
    #     cols = set(loc.col for loc in __opp_base)
    #     fences = set(puzzle.cell_fence(loc) for loc in __opp_base)
    #     row_col_house = None
    #     fence_house = None
    #     if len(rows) == 1:
    #         row_col_house = puzzle.house_row(list(rows)[0])
    #     if len(cols) == 1:
    #         row_col_house = puzzle.house_col(list(cols)[0])
    #     if len(fences) == 1:
    #         fence_house = puzzle.house_fence(list(fences)[0])
    #     if row_col_house is not None:
    #         __intersection = row_col_house
    #         if fence_house is not None:
    #             __intersection = __intersection + fence_house
    #         __remove = set(__intersection).difference(__opp_base)
    #         puzzle.override_loc_color(__intersection, Fore.RED)
    #         puzzle.override_loc_color(list(__base), Fore.GREEN)
    #         puzzle.override_loc_color(list(__opp_base), Fore.YELLOW)
    #         edits += puzzle.rem(__remove, [candidate])
    #
    #     return edits
