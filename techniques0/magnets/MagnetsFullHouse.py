from puzzles import Magnets

EMPTY = 0

class MagnetsFullHouse:
    def solve0(self, puzzle: Magnets) -> int:
        edits = 0

        for i in range(puzzle.length):
            plus_row_value = puzzle.plus_row_value(i)
            minus_row_value = puzzle.minus_row_value(i)
            row_house = puzzle.house_row(i)

            if plus_row_value + minus_row_value == puzzle.length:
                edits += puzzle.rem(row_house, [EMPTY])

            plus_col_value = puzzle.plus_col_value(i)
            minus_col_value = puzzle.minus_col_value(i)
            col_house = puzzle.house_col(i)

            if plus_col_value + minus_col_value == puzzle.length:
                edits += puzzle.rem(col_house, [EMPTY])

        return edits
