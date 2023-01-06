from Loc import Loc
from puzzles import Magnets

PLUS = 1
MINUS = 0
EMPTY = MINUS


class MagnetsZero:
    def solve0(self, puzzle: Magnets) -> int:
        edits = 0
        for i in range(puzzle.length):
            plus_row_value = puzzle.plus_row_value(i)
            row_house = puzzle.house_row(i)
            if plus_row_value == 0:
                for loc in row_house:
                    edits += puzzle.rem([loc], [PLUS])
            plus_col_value = puzzle.plus_col_value(i)
            col_house = puzzle.house_col(i)
            if plus_col_value == 0:
                for loc in col_house:
                    edits += puzzle.rem([loc], [PLUS])
            minus_row_value = puzzle.minus_row_value(i)
            row_house = puzzle.house_row(i)
            if minus_row_value == 0:
                for loc in row_house:
                    edits += puzzle.rem([loc], [MINUS])
            minus_col_value = puzzle.minus_col_value(i)
            col_house = puzzle.house_col(i)
            print(minus_col_value)
            if minus_col_value == 0:
                for loc in col_house:
                    edits += puzzle.rem([loc], [MINUS])
        return edits
