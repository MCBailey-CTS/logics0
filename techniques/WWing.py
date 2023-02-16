from Loc import Loc
from techniques.Technique import Technique
from colorama import Fore


class WWing(Technique):

    def solve0(self, puzzle) -> int:
        edits = 0

        # house0 = puzzle.house_row(3)
        # house1 = puzzle.house_row(4)
        # house2 = puzzle.house_row(5)

        # puzzle.override_loc_color(house0 +house1 +house2, Fore.GREEN)

        left = Loc(3, 2)
        right = Loc(4, 6)

        if set(puzzle.cell_candidates(left)) == {1, 2} and set(puzzle.cell_candidates(right)) == {1, 2}:
            chute = [Loc(3, 3), Loc(3, 4), Loc(3, 5), Loc(4, 3), Loc(4, 4), Loc(4, 5)]
            bottom = [Loc(5, 3), Loc(5, 4), Loc(5, 5)]
            remove = [Loc(4, 0), Loc(4, 1), Loc(4, 2), Loc(3, 6), Loc(3, 7), Loc(3, 8)]
            __candidate = 2
            puzzle.override_loc_color([left, right], Fore.YELLOW)
            puzzle.override_loc_color(chute, Fore.BLUE)
            puzzle.override_loc_color(bottom, Fore.GREEN)
            puzzle.override_loc_color(remove, Fore.RED)
            edits += puzzle.rem(remove, [__candidate])

        left = Loc(0, 8)
        right = Loc(1, 5)

        if set(puzzle.cell_candidates(left)) == {3, 6} and set(puzzle.cell_candidates(right)) == {3, 6}:
            chute = [Loc(0, 0), Loc(0, 1), Loc(0, 2), Loc(1, 0), Loc(1, 1), Loc(1, 2)]
            bottom = [Loc(2, 0), Loc(2, 1), Loc(2, 2)]
            remove = [Loc(0, 3), Loc(0, 4), Loc(0, 5), Loc(1, 6), Loc(1, 7), Loc(1, 8)]
            __candidate = 6
            puzzle.override_loc_color([left, right], Fore.YELLOW)
            puzzle.override_loc_color(chute, Fore.BLUE)
            puzzle.override_loc_color(bottom, Fore.GREEN)
            puzzle.override_loc_color(remove, Fore.RED)
            edits += puzzle.rem(remove, [__candidate])

        return edits

    # def solve1(self, puzzle: Sudoku, left: Loc, right: Loc) -> int:
    #     edits = 0
    #
    #     left_candidate_set = set(puzzle.cell_candidates(left))
    #     right_candidate_set = set(puzzle.cell_candidates(right))
    #
    #     if len(left_candidate_set) != 2 or len(right_candidate_set) != 2 or not left_candidate_set.issubset(
    #             right_candidate_set):
    #         return edits
    #
    #     left_chute = puzzle.loc_chute(left)
    #     right_chute = puzzle.loc_chute(right)
    #
    #     left_fence = puzzle.cell_fence(left)
    #     right_fence = puzzle.cell_fence(right)
    #
    #     left_fence_house = puzzle.house_fence(left_fence)
    #     right_fence_house = puzzle.house_fence(right_fence)
    #
    #     if right_fence == left_fence:
    #         return edits
    #
    #     if left_chute.in_same_row(right_chute):
    #         cols_in_chute = {left_chute.col, right_chute.col}
    #         if len(cols_in_chute) == 2:
    #             difference = {0, 1, 2}.difference(cols_in_chute)
    #             if len(difference) == 1:
    #                 other_col_chute = difference.pop()
    #                 other_chute = Loc(left_chute.row, other_col_chute)
    #                 center_fence = puzzle.fence_from_chute(other_chute)
    #                 if center_fence != left_fence and center_fence != right_fence:
    #                     left_row_house = puzzle.house_row(left.row)
    #                     right_row_house = puzzle.house_row(right.row)
    #                     fence_house = puzzle.house_fence(center_fence)
    #                     connector_in_chute = set(fence_house).difference(left_row_house + right_row_house)
    #                     for candidate in left_candidate_set:
    #                         cells_in_connector = [loc for loc in connector_in_chute if
    #                                                 candidate in puzzle.cell_candidates(loc)]
    #                         if len(cells_in_connector) > 0:
    #                             continue
    #                         candidate_to_remove = list(left_candidate_set.difference([candidate]))[0]
    #                         left_intersection = set(left_row_house).intersection(right_fence_house)
    #                         right_intersection = set(right_row_house).intersection(left_fence_house)
    #                         cells_to_remove = set(list(left_intersection) + list(right_intersection)).difference(
    #                             [left, right])
    #                         for loc in cells_to_remove:
    #                             edits += puzzle.rem(loc, [candidate_to_remove])
    #
    #     if left_chute.in_same_col(right_chute):
    #         rows_in_chute = {left_chute.row, right_chute.row}
    #         if len(rows_in_chute) == 2:
    #             difference = {0, 1, 2}.difference(rows_in_chute)
    #             if len(difference) == 1:
    #                 other_row_chute = difference.pop()
    #                 other_chute = Loc(other_row_chute, left_chute.col)
    #                 center_fence = puzzle.fence_from_chute(other_chute)
    #                 if center_fence != left_fence and center_fence != right_fence:
    #                     left_col_house = puzzle.house_col(left.col)
    #                     right_col_house = puzzle.house_col(right.col)
    #                     fence_house = puzzle.house_fence(center_fence)
    #                     connector_in_chute = set(fence_house).difference(left_col_house + right_col_house)
    #                     for candidate in left_candidate_set:
    #                         cells_in_connector = [loc for loc in connector_in_chute if
    #                                                 candidate in puzzle.cell_candidates(loc)]
    #                         if len(cells_in_connector) > 0:
    #                             continue
    #                         candidate_to_remove = list(left_candidate_set.difference([candidate]))[0]
    #                         left_intersection = set(left_col_house).intersection(right_fence_house)
    #                         right_intersection = set(right_col_house).intersection(left_fence_house)
    #                         cells_to_remove = set(list(left_intersection) + list(right_intersection)).difference(
    #                             [left, right])
    #                         for loc in cells_to_remove:
    #                             edits += puzzle.rem(loc, [candidate_to_remove])
    #
    #     return edits
    #
    # def solve0(self, puzzle: Sudoku) -> int:
    #     edits = 0
    #
    #     for r0 in range(len(puzzle)):
    #         for c0 in range(len(puzzle)):
    #             loc0 = Loc(r0, c0)
    #             candidates0 = set(puzzle.cell_candidates(loc0))
    #             if len(candidates0) != 2:
    #                 continue
    #             for r1 in range(len(puzzle)):
    #                 for c1 in range(len(puzzle)):
    #                     loc1 = Loc(r1, c1)
    #                     if loc0 == loc1:
    #                         continue
    #                     candidates1 = puzzle.cell_candidates(loc1)
    #                     if len(candidates1) != 2:
    #                         continue
    #                     if not candidates0.issubset(candidates1):
    #                         continue
    #
    #                     # print(loc0)
    #                     # print(loc1)
    #
    #                     # left_loc = Loc(3, 2)
    #                     # right_loc = Loc(4, 6)
    #                     #
    #                     edits += self.solve1(puzzle, loc0, loc1)
    #
    #     return edits
