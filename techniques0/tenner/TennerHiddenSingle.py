from puzzles import Tenner
from techniques0 import HiddenSingle


class TennerHiddenSingle:
    def solve0(self, puzzle: Tenner) -> int:
        edits = 0
        for row in range(puzzle.length):
            house = puzzle.house_row_cell_locs(row)
            edits += HiddenSingle.solve1(puzzle, house)
        return edits
