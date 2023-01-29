from techniques.Technique import Technique
from puzzles import Sudoku
from Loc import Loc
from colorama import Fore


class XyWing(Technique):

    def solve1(self, puzzle: Sudoku, pincer0: Loc)->int:
        edits = 0

        # for r in range(len(puzzle)):
        #     for c in range(len(puzzle)):
        #         pivot = Loc(r, c)
        #         if pivot == pincer0:
        #             continue
        #         if len(puzzle.cell_candidates(pincer0)) != 2:
        #             continue
        #
        #         if pincer0.row != pivot.row and pincer0.col != pivot.col:




        return edits

    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0
        for r in range(len(puzzle)):
            for c in range(len(puzzle)):
                pincer0 = Loc(r, c)
                if len(puzzle.cell_candidates(pincer0)) == 2:
                    edits += self.solve1(puzzle, pincer0)
        return edits
