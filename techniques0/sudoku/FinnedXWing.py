from _puzzles import Sudoku


class FinnedXWing:
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        for index0 in range(puzzle.length):
            for index1 in range(puzzle.length):

                col_house0 = puzzle.house_col(index0)
                col_house1 = puzzle.house_col(index1)

                row_house0 = puzzle.house_row(index0)
                row_house1 = puzzle.house_row(index1)

                for candidate in puzzle.expected_candidates():

                    row_house0_with_candidate = [loc for loc in row_house0 if
                                                 candidate in puzzle.cell_candidates(loc)]
                    row_house1_with_candidate = [loc for loc in row_house1 if
                                                 candidate in puzzle.cell_candidates(loc)]

                    row_locs_set = set(row_house0_with_candidate + row_house1_with_candidate)

                    fence_dict = puzzle.fence_dict(row_locs_set)

                    if len(fence_dict) != 4:
                        continue

                    fence_with_multiples = [fence for fence in fence_dict if len(fence_dict[fence]) > 1]

                    if len(fence_with_multiples) != 1:
                        continue

                    fence_with_fin = fence_with_multiples[0]

                    for loc in fence_dict[fence_with_fin]:
                        row_locs_set.remove(loc)

                    # need to find the two cells that are in the same col right now
                    loc0, loc1, loc2 = row_locs_set

                    col_set = None

                    if loc0.col == loc1.col:
                        col_set = set(puzzle.house_col(loc2.col)).difference([loc2])
                    elif loc0.col == loc2.col:
                        col_set = set(puzzle.house_col(loc1.col)).difference([loc1])
                    elif loc1.col == loc2.col:
                        col_set = set(puzzle.house_col(loc0.col)).difference([loc0])

                    fence_set = set(puzzle.house_fence(fence_with_fin)).difference(fence_dict[fence_with_fin])

                    if col_set is None or fence_set is None:
                        continue

                    intersection = col_set.intersection(fence_set)

                    for loc in intersection:
                        edits += puzzle.rem(loc, [candidate])

                for candidate in puzzle.expected_candidates():

                    col_house0_with_candidate = [loc for loc in col_house0 if
                                                 candidate in puzzle.cell_candidates(loc)]
                    col_house1_with_candidate = [loc for loc in col_house1 if
                                                 candidate in puzzle.cell_candidates(loc)]

                    col_locs_set = set(col_house0_with_candidate + col_house1_with_candidate)

                    fence_dict = puzzle.fence_dict(col_locs_set)

                    if len(fence_dict) != 4:
                        continue

                    fence_with_multiples = [fence for fence in fence_dict if len(fence_dict[fence]) > 1]

                    if len(fence_with_multiples) != 1:
                        continue

                    fence_with_fin = fence_with_multiples[0]

                    for loc in fence_dict[fence_with_fin]:
                        col_locs_set.remove(loc)

                    # need to find the two cells that are in the same row right now
                    loc0, loc1, loc2 = col_locs_set

                    row_set = None

                    if loc0.row == loc1.row:
                        row_set = set(puzzle.house_row(loc2.row)).difference([loc2])
                    elif loc0.row == loc2.row:
                        row_set = set(puzzle.house_row(loc1.row)).difference([loc1])
                    elif loc1.row == loc2.row:
                        row_set = set(puzzle.house_row(loc0.row)).difference([loc0])

                    fence_set = set(puzzle.house_fence(fence_with_fin)).difference(fence_dict[fence_with_fin])

                    if row_set is None or fence_set is None:
                        continue

                    intersection = row_set.intersection(fence_set)

                    # if intersection is not None:

                    for loc in intersection:
                        edits += puzzle.rem(loc, [candidate])

        return edits

