from Loc import Loc
from puzzles import Sudoku
from techniques0.BaseSudokuHouseTechnique import BaseSudokuHouseTechnique


class HiddenPair(BaseSudokuHouseTechnique):

    def solve_house(self, puzzle: Sudoku, house: list[Loc]) -> int:
        edits = 0
        expected = puzzle.expected_candidates()
        for i in range(len(expected) - 1):
            for ii in range(i, len(expected)):
                if expected[i] == expected[ii]:
                    continue
                locs0 = [loc for loc in house if expected[i] in puzzle.cell_candidates(loc)]
                locs1 = [loc for loc in house if expected[ii] in puzzle.cell_candidates(loc)]
                if len(locs0) != 2 or len(locs1) != 2:
                    continue
                loc_set = set(locs0 + locs1)
                if len(loc_set) != 2:
                    continue
                temp_locs = list(loc_set)
                for k in set(expected).difference([expected[i], expected[ii]]):
                    edits += puzzle.rem([temp_locs[0]], [k])
                    edits += puzzle.rem([temp_locs[1]], [k])

        return edits
