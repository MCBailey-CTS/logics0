from puzzles import Sudoku


class XyzWing:
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        for pivot in puzzle.unsolved_cells():
            pivot_candidates = set(puzzle.cell_candidates(pivot))

            if len(pivot_candidates) != 3:
                continue

            pivot_fence = puzzle.cell_fence(pivot)

            pivot_fence_set = set(puzzle.house_fence(pivot_fence)).difference([pivot])

            for loc_in_fence in pivot_fence_set:
                loc_in_fence_candidates = puzzle.cell_candidates(loc_in_fence)

                if len(loc_in_fence_candidates) != 2:
                    continue

                # print(pivot_candidates)

                if not pivot_candidates.issuperset(loc_in_fence_candidates):
                    continue

                pivot_row_set = set(puzzle.house_row(pivot.row)).difference([pivot, loc_in_fence])

                for loc_in_row in pivot_row_set:
                    loc_in_row_candidates = puzzle.cell_candidates(loc_in_row)

                    if len(loc_in_row_candidates) != 2:
                        continue

                    if not pivot_candidates.issuperset(loc_in_row_candidates):
                        continue

                    if loc_in_row_candidates.issuperset(loc_in_fence_candidates):
                        continue

                    if not pivot_candidates.issuperset(list(loc_in_row_candidates) + list(loc_in_fence_candidates)):
                        continue

                    intersection = pivot_candidates.intersection(loc_in_row_candidates).intersection(
                        loc_in_fence_candidates)

                    if len(intersection) != 1:
                        continue

                    candidate_to_remove = list(intersection)[0]

                    intersection_locs = pivot_fence_set.intersection(pivot_row_set)

                    for loc in intersection_locs:
                        edits += puzzle.rem(loc, [candidate_to_remove])

                pivot_col_set = set(puzzle.house_col(pivot.col)).difference([pivot, loc_in_fence])

                for loc_in_col in pivot_col_set:
                    loc_in_col_candidates = puzzle.cell_candidates(loc_in_col)

                    if len(loc_in_col_candidates) != 2:
                        continue

                    if not pivot_candidates.issuperset(loc_in_col_candidates):
                        continue

                    if loc_in_col_candidates.issuperset(loc_in_fence_candidates):
                        continue

                    if not pivot_candidates.issuperset(list(loc_in_col_candidates) + list(loc_in_fence_candidates)):
                        continue

                    intersection = pivot_candidates.intersection(loc_in_col_candidates).intersection(
                        loc_in_fence_candidates)

                    if len(intersection) != 1:
                        continue

                    candidate_to_remove = list(intersection)[0]

                    intersection_locs = pivot_fence_set.intersection(pivot_col_set)

                    for loc in intersection_locs:
                        edits += puzzle.rem(loc, [candidate_to_remove])
        return edits

