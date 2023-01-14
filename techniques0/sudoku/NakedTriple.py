from Loc import Loc
from puzzles import Sudoku
from techniques0 import *


class NakedTriple(BaseSudokuHouseTechnique):

    def solve_house(self, puzzle: Sudoku, house: list[Loc]) -> int:
        edits = 0

        naked_count = 3

        for i in range(len(puzzle)):
            for ii in range(len(puzzle)):
                for iii in range(len(puzzle)):
                    indexes = {i, ii, iii}

                    if len(indexes) != naked_count:
                        continue

                    candidate_set = set()
                    for index in indexes:
                        for candidate in puzzle.cell_candidates(house[index]):
                            candidate_set.add(candidate)

                    _candidates0 = puzzle.cell_candidates(house[i])
                    _candidates1 = puzzle.cell_candidates(house[ii])
                    _candidates2 = puzzle.cell_candidates(house[iii])

                    if len(_candidates0) < 2 or len(_candidates0) > naked_count or \
                            len(_candidates1) < 2 or len(_candidates1) > naked_count or \
                            len(_candidates2) < 2 or len(_candidates2) > naked_count:
                        continue

                    if not candidate_set.issuperset(_candidates0) or \
                            not candidate_set.issuperset(_candidates1) or \
                            not candidate_set.issuperset(_candidates2):
                        continue

                    if len(candidate_set) != naked_count:
                        continue

                    for j in range(len(puzzle)):
                        if j not in indexes:
                            edits += puzzle.rem([house[j]], list(candidate_set))
        return edits
