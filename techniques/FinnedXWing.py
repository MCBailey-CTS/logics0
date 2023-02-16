from colorama import Fore

from techniques.Technique import Technique
from itertools import combinations

class FinnedXWing(Technique):

    def solve0(self, puzzle) -> int:
        edits = 0
        for row0, row1 in combinations(list(range(len(puzzle))), 2):
            for candidate in puzzle.expected_candidates():
                row0_locs = puzzle.house_row(row0, candidate)
                if len(row0_locs) < 2:
                    continue

                row1_locs = puzzle.house_row(row1, candidate)
                if len(row1_locs) < 2:
                    continue

                col_dict = {}

                # if len(row1_locs) == 2 and len():

                # if len()

                # print(f'{row0} {row1} {candidate}')

            # print(f'{row0} {row1}')
        # print(row_indexes)
        return edits
