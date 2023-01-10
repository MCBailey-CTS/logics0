from Loc import Loc
from puzzles import Sudoku


class UniqueRectangleType2:
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0
        for corner0 in puzzle.unsolved_cells():
            for corner1 in puzzle.unsolved_cells():
                corners = [
                    corner0,
                    corner1,
                    Loc(corner0.row, corner1.col),
                    Loc(corner1.row, corner0.col),
                ]

                rows = set([loc.row for loc in corners])
                cols = set([loc.col for loc in corners])
                fences = set([puzzle.cell_fence(loc) for loc in corners])
                try:
                    if len(rows) != 2 or len(cols) != 2 or len(fences) != 2:
                        continue
                    length_2 = [loc for loc in corners if len(puzzle.cell_candidates(loc)) == 2]
                    length_3 = [loc for loc in corners if len(puzzle.cell_candidates(loc)) == 3]

                    if len(length_2) != 2 or len(length_3) != 2:
                        continue

                    length_2_candidates = [puzzle.cell_candidates(loc) for loc in length_2]
                    length_3_candidates = [puzzle.cell_candidates(loc) for loc in length_3]

                    if not set(length_2_candidates[0]).issubset(length_2_candidates[1]) or \
                            not set(length_2_candidates[0]).issuperset(length_2_candidates[1]):
                        continue

                    if not set(length_3_candidates[0]).issubset(length_3_candidates[1]) or not set(length_3_candidates[0]).issuperset(length_3_candidates[1]):
                        continue

                    if not set(length_3_candidates[0]).issuperset(length_2_candidates[0]):
                        continue

                    # print(length_2_candidates[0])
                    # print(length_3_candidates[0])

                    candidate_to_remove = list(set(length_3_candidates[0]).difference(length_2_candidates[0]))[0]

                    # print(candidate_to_remove)

                    if length_3[0].col == length_3[1].col:
                        locs_to_remove_from = set(puzzle.house_col(length_3[0].col)).difference(length_3)

                        for loc in locs_to_remove_from:
                            edits += puzzle.rem(loc, [candidate_to_remove])

                    if length_3[0].row == length_3[1].row:
                        locs_to_remove_from = set(puzzle.house_row(length_3[0].row)).difference(length_3)

                        for loc in locs_to_remove_from:
                            edits += puzzle.rem(loc, [candidate_to_remove])

                    if puzzle.cell_fence(length_3[0]) == puzzle.cell_fence(length_3[1]):
                        locs_to_remove_from = set(puzzle.house_fence(puzzle.cell_fence(length_3[0]))).difference(
                            length_3)

                        for loc in locs_to_remove_from:
                            edits += puzzle.rem(loc, [candidate_to_remove])
                except Exception as e:
                    print(corners)
                    print(puzzle)
                    raise e


        return edits

    # def solve1(self, puzzle: Sudoku, corners: list[Loc]) -> int:
    #     edits = 0

    #     corner_set = set(corners)

    #     if len(corner_set) != 4:
    #         raise ValueError(f'cannot make unique rectangle from {len(corner_set)} corner(s)')

    #     rows = set([loc.row for loc in corner_set])
    #     if len(rows) != 2:
    #         raise ValueError(f'cannot make unique rectangle from {len(rows)} row(s)')

    #     cols = set([loc.col for loc in corner_set])
    #     if len(cols) != 2:
    #         raise ValueError(f'cannot make unique rectangle from {len(cols)} col(s)')

    #     fences = set([puzzle.cell_fence(loc) for loc in corner_set])
    #     if len(fences) != 2:
    #         raise ValueError(f'cannot make unique rectangle from {len(fences)} fence(s)')

    #     two_candidates = [loc for loc in corner_set if len(puzzle.cell_candidates(loc)) == 2]
    #     three_candidates = [loc for loc in corner_set if len(puzzle.cell_candidates(loc)) == 3]

    #     if len(two_candidates) != 2:
    #         return edits

    #     if len(three_candidates) != 2:
    #         return edits

    #     two_candidates_set0 = set(puzzle.cell_candidates(two_candidates[0]))
    #     two_candidates_set1 = set(puzzle.cell_candidates(two_candidates[1]))

    #     three_candidates_set0 = set(puzzle.cell_candidates(three_candidates[0]))
    #     three_candidates_set1 = set(puzzle.cell_candidates(three_candidates[1]))

    #     if puzzle.cell_fence(two_candidates[0]) != puzzle.cell_fence(two_candidates[1]):
    #         return edits

    #     if puzzle.cell_fence(three_candidates[0]) != puzzle.cell_fence(three_candidates[1]):
    #         return edits

    #     # checks to see if the two_candidates are the same set
    #     if not two_candidates_set0.issubset(two_candidates_set1):
    #         return edits

    #     # checks to see if the three_candidates are the same set
    #     if not three_candidates_set0.issubset(three_candidates_set1):
    #         return edits

    #     # checks to see that three_candidates is a superset of two_candidates
    #     if not three_candidates_set0.issuperset(two_candidates_set0):
    #         return edits

    #     if three_candidates[0].row == three_candidates[1].row:
    #         row = three_candidates[0].row
    #         fence = puzzle.cell_fence(three_candidates[0])
    #         row_house_set = set(puzzle.house_row(row))
    #         fence_house_set = set(puzzle.house_fence(fence))

    #         row_house_set.discard(three_candidates[0])
    #         row_house_set.discard(three_candidates[1])
    #         fence_house_set.discard(three_candidates[0])
    #         fence_house_set.discard(three_candidates[1])

    #         for loc in list(row_house_set) + list(fence_house_set):
    #             edits += puzzle.rem(loc, set(three_candidates_set0).difference(two_candidates_set0))

    #     return edits
