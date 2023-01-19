from puzzles import Tenner
from techniques.HiddenSingle import HiddenSingle
class TennerHiddenSingle:
    def solve0(self, puzzle: Tenner) -> int:
        edits = 0
        for row in range(len(puzzle)):
            house = puzzle.house_row_cell_locs(row)
            edits += HiddenSingle.solve1(puzzle, house)
        return edits
