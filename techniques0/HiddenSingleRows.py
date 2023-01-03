
    class HiddenSingleRows():
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for house in puzzle.houses_rows():
                edits += HiddenSingle.solve1(puzzle, house)
            return edits
