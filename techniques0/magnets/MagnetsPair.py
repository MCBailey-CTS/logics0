from Loc import Loc
from puzzles import Magnets
PLUS = 1
MINUS = 0
EMPTY = MINUS

class MagnetsPair:



    def solve1(self, puzzle: Magnets, loc0: Loc, loc1: Loc) -> int:
        edits = 0
        candidates0 = puzzle.cell_candidates(loc0)
        candidates1 = puzzle.cell_candidates(loc1)

        if EMPTY not in candidates0:
            edits += puzzle.rem([loc1], [EMPTY])

        if EMPTY not in candidates1:
            edits += puzzle.rem([loc0], [EMPTY])

        if PLUS not in candidates0:
            edits += puzzle.rem([loc1], [MINUS])

        if PLUS not in candidates1:
            edits += puzzle.rem([loc0], [MINUS])

        if MINUS not in candidates0:
            edits += puzzle.rem([loc1], [PLUS])

        if MINUS not in candidates1:
            edits += puzzle.rem([loc0], [PLUS])

        return edits

    def solve0(self, puzzle: Magnets) -> int:
        edits = 0

        # loc0 = Loc(1, 1)
        # loc1 = Loc(1, 2)

        for magnets_fence_pair in puzzle.house_fences():
            loc0, loc1 = magnets_fence_pair
            #
            #     if puzzle.house_fence(loc0) != 'a':
            #         continue
            #
            edits += self.solve1(puzzle, loc0, loc1)

        return edits
