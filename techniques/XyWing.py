from techniques.Technique import Technique
from puzzles import Sudoku
from Loc import Loc
from colorama import Fore


class XyWing(Technique):
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        length2 = []

        for r in range(len(puzzle)):
            for c in range(len(puzzle)):
                loc = Loc(r, c)
                if len(puzzle.cell_candidates(loc)) == 2:
                    length2.append(loc)

        for i in range(len(length2) - 2):
            loc0 = length2[i]
            for ii in range(i + 1, len(length2) - 1):
                loc1 = length2[ii]
                for iii in range(ii + 1, len(length2)):
                    loc2 = length2[iii]

                    locs = [loc0, loc1, loc2]

                    for loc in locs:
                        other0, other1 = set(locs).difference([loc])






                    loc0_candidates = puzzle.cell_candidates(loc0)
                    loc1_candidates = puzzle.cell_candidates(loc1)
                    loc2_candidates = puzzle.cell_candidates(loc2)







        return edits
