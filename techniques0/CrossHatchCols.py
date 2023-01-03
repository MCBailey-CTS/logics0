from _puzzles import Sudoku


class CrossHatchCols:
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0
        for house in puzzle.houses_cols():
            print(house)
            for loc0 in house:
                for loc1 in house:
                    if loc0 == loc1:
                        continue

                    candidates = puzzle.cell_candidates(loc0)

                    if len(candidates) != 1:
                        continue

                    candiate = list(candidates)[0]

                    edits += puzzle.rem(loc1, [candiate])

        return edits

