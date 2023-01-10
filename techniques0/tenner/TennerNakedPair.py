from puzzles import Tenner
from techniques0 import NakedPair


class TennerNakedPair:
    def solve0(self, puzzle: Tenner) -> int:
        edits = 0
        for row in range(puzzle.length):
            house = puzzle.house_row_cell_locs(row)
            edits += NakedPair.static_solve_house(puzzle, house)
        return edits
