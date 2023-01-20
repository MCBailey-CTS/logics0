from colorama import Fore

from puzzles import Sudoku
from tech import Technique


class FinnedXWing(Technique):

    def solve1(self, puzzle: Sudoku, __col0, __col1, __candidate) -> int:
        edits = 0
        containing_locs0 = [loc for loc in __col0 if __candidate in puzzle.cell_candidates(loc)]
        containing_locs1 = [loc for loc in __col1 if __candidate in puzzle.cell_candidates(loc)]

        containing_locs = containing_locs0 + containing_locs1

        rows = set(loc.row for loc in containing_locs)
        cols = set(loc.col for loc in containing_locs)
        row_chutes = set(puzzle.row_chute(loc) for loc in containing_locs)
        col_chutes = set(puzzle.col_chute(loc) for loc in containing_locs)

        fence_dict = {}
        for loc in containing_locs:
            fence = puzzle.cell_fence(loc)
            if fence not in fence_dict:
                fence_dict[fence] = set()
            fence_dict[fence].add(loc)

        chute_dict = {}
        for loc in containing_locs:
            chute = puzzle.loc_chute(loc)
            if chute not in chute_dict:
                chute_dict[chute] = set()
            chute_dict[chute].add(loc)

        count_length_1 = set(chute_fence for chute_fence in chute_dict.keys() if len(chute_dict[chute_fence]) == 1)
        count_length_more_than_1 = set(
            chute_fence for chute_fence in chute_dict.keys() if len(chute_dict[chute_fence]) > 1)

        if (len(rows) == 2 or len(cols) == 2) and \
                len(fence_dict) == 4 and \
                len(row_chutes) == 2 and \
                len(col_chutes) == 2 and \
                len(chute_dict) == 4 and \
                len(count_length_1) == 3 and \
                len(count_length_more_than_1) == 1:
            chute_with_fin = list(count_length_more_than_1)[0]
            fence = puzzle.fence_from_chute(chute_with_fin)
            puzzle.override_loc_color(puzzle.house_fence(fence), Fore.BLUE)

            puzzle.override_loc_color(containing_locs, Fore.YELLOW)
            next_to_chutes = [chute for chute in count_length_1 if
                              chute_with_fin.in_same_row(chute) or chute_with_fin.in_same_col(chute)]
            locs_in_next_to_chute = []
            for chute in next_to_chutes:
                locs_in_next_to_chute.append(
                    set(containing_locs).intersection(puzzle.house_fence(puzzle.fence_from_chute(chute))))
            locs_in_fin_chute = set(containing_locs).intersection(puzzle.house_fence(fence))
            puzzle.override_loc_color(list(locs_in_fin_chute), Fore.YELLOW)
            for loc_chute in locs_in_next_to_chute:
                temp = list(loc_chute)[0]



                row_intersection = set(puzzle.house_row(temp.row)).intersection(puzzle.house_fence(fence)).difference(
                    containing_locs)
                col_intersection = set(puzzle.house_col(temp.col)).intersection(puzzle.house_fence(fence)).difference(
                    containing_locs)

                remove = list(row_intersection) + list(col_intersection)

                puzzle.override_loc_color(remove, Fore.RED)



                edits += puzzle.rem(remove, [__candidate])

                if edits > 0:
                    return edits

        return edits

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0
        for candidate in puzzle.expected_candidates():
            for i in range(0, len(puzzle) - 1):
                for ii in range(i + 1, len(puzzle)):
                    edits += self.solve1(puzzle, puzzle.house_row(i), puzzle.house_row(ii), candidate)
                    edits += self.solve1(puzzle, puzzle.house_col(i), puzzle.house_col(ii), candidate)

        return edits
