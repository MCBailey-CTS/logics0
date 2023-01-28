from Loc import Loc
from puzzles import Sudoku
from techniques.Technique import Technique


class AlmostLockedCandidatesPointing(Technique):
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        # need to iterate through row chute

        if len(puzzle) == 4:
            nw = Loc(0, 0)
            ne = Loc(0, 1)
            sw = Loc(1, 0)
            se = Loc(1, 1)




        return edits

