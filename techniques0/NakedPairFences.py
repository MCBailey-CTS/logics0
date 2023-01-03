
    class NakedPairFences():
        def solve0(self, puzzle: Sudoku) -> int:
            edits = 0
            for house in puzzle.houses_fences():
                edits += NakedPair.solve1(puzzle, house)
            return edits
