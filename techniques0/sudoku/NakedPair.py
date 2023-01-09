from turtle import pu
from Loc import Loc
from _puzzles import Sudoku
from techniques0.BaseSudokuHouseTechnique import BaseSudokuHouseTechnique

class NakedPair(BaseSudokuHouseTechnique):
    @staticmethod
    def static_solve_house(puzzle: Sudoku, house: list[Loc]) -> int:
        edits = 0
        for i in range(0, puzzle.length - 1):
            for ii in range(i + 1, puzzle.length):
                if i == ii:
                    continue
                index_set = {i, ii}
                candidate_set = set()
                candidates0 = puzzle.cell_candidates(house[i])
                candidates1 = puzzle.cell_candidates(house[ii])
                if len(candidates0) == 1 or len(candidates1) == 1:
                    continue
                for c in candidates0:
                    candidate_set.add(c)
                for c in candidates1:
                    candidate_set.add(c)
                if len(candidate_set) != 2:
                    continue
                for j in range(puzzle.length):
                    if j not in index_set:
                        edits += puzzle.rem([house[j]], list(candidate_set))
        return edits

    def solve_house(self, puzzle: Sudoku, house: list[Loc]) -> int:
        return NakedPair.static_solve_house(puzzle, house)