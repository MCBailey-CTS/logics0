from Loc import Loc
from _puzzles import Sudoku


class XyWing:
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0
        unsolved = puzzle.unsolved_cells()

        if len(unsolved) == 0:
            return edits
        for pivot in puzzle.unsolved_cells():
            pivot_candidates = puzzle.cell_candidates(pivot)

            pivot_fence = puzzle.cell_fence(pivot)

            if len(pivot_candidates) != 2:
                continue

            row_locs = [loc for loc in puzzle.house_row(pivot.row) if
                        loc != pivot and len(puzzle.cell_candidates(loc)) == 2]
            col_locs = [loc for loc in puzzle.house_col(pivot.col) if
                        loc != pivot and len(puzzle.cell_candidates(loc)) == 2]
            fence_locs = [loc for loc in puzzle.house_fence(puzzle.cell_fence(pivot)) if
                          loc != pivot and len(puzzle.cell_candidates(loc)) == 2]

            for row_loc in row_locs:
                row_difference = set(puzzle.cell_candidates(row_loc)).difference(pivot_candidates)
                row_fence = puzzle.cell_fence(row_loc)
                if len(row_difference) != 1:
                    continue
                for col_loc in col_locs:
                    col_difference = set(puzzle.cell_candidates(col_loc)).difference(pivot_candidates)
                    col_fence = puzzle.cell_fence(col_loc)
                    if col_fence == row_fence:
                        continue
                    if len(col_difference) != 1:
                        continue
                    if not row_difference.issubset(col_difference):
                        continue
                    # check if three fences
                    if row_fence != pivot_fence and col_fence != pivot_fence:
                        other_loc = Loc(col_loc.row, row_loc.col)
                        edits += puzzle.rem(other_loc, row_difference)

        return edits

    # @staticmethod
    # def solve1(puzzle: Sudoku, locs: list[Loc]) -> int:
    #     edits = 0
    #     if len(locs) != 3:
    #         return edits
    #
    #     candidate_set = set()
    #
    #     for loc in locs:
    #         for candidate in puzzle.cell_candidates(loc):
    #             candidate_set.add(candidate)
    #
    #     if len(candidate_set) != 3:
    #         return edits
    #
    #     # need to find a pivot
    #     for pivot in locs:
    #         pincers = set(locs)
    #         pincers.remove(pivot)
    #         pincer0, pincer1 = pincers
    #
    #         pincer_fence0 = puzzle.cell_fence(pincer0)
    #         pincer_fence1 = puzzle.cell_fence(pincer1)
    #
    #         if pincer_fence0 == pincer_fence1:
    #             continue
    #
    #         temp_pivot0 = Loc(pincer0.row, pincer1.col)
    #         temp_pivot1 = Loc(pincer1.row, pincer0.col)
    #
    #         pivot_candidates = puzzle.cell_candidates(pivot)
    #         pincer0_candidates = set(puzzle.cell_candidates(pincer0))
    #         pincer1_candidates = set(puzzle.cell_candidates(pincer1))
    #
    #         if len(pivot_candidates) != 2 or len(pincer0_candidates) != 2 or len(pincer1_candidates) != 2:
    #             continue
    #
    #         if pincer0_candidates.issubset(pincer1_candidates):
    #             continue
    #
    #         # print(f'{pivot} {pincer0} {pincer1}')
    #
    #         for candidate in pivot_candidates:
    #             if candidate in pincer0_candidates:
    #                 pincer0_candidates.remove(candidate)
    #             if candidate in pincer1_candidates:
    #                 pincer1_candidates.remove(candidate)
    #
    #         if len(pincer0_candidates) != 1 or len(pincer1_candidates) != 1 or not pincer1_candidates.issubset(
    #                 pincer0_candidates):
    #             continue
    #
    #         shared_candidate = list(pincer0_candidates)[0]
    #
    #         other_pivot = None
    #
    #         if pivot == temp_pivot0:
    #             other_pivot = temp_pivot1
    #
    #         if pivot == temp_pivot1:
    #             other_pivot = temp_pivot0
    #
    #         if other_pivot is None:
    #             continue
    #
    #         if len(puzzle.cell_candidates(other_pivot)) == 1:
    #             continue
    #
    #             #
    #         # print(f'{pivot} {pincer0} {pincer1} {other_pivot}')
    #         # print(f'{puzzle.cell_candidates(pivot)} {puzzle.cell_candidates(pincer0)} {self.cell_candidates(pincer1)} {self.cell_candidates(other_pivot)}')
    #         edits += puzzle.rem(other_pivot, [shared_candidate])
    #
    #     return edits

