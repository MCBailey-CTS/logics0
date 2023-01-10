from Loc import Loc
from puzzles import PowerGrid


class PowerGridCrossHatch:
    def solve0(self, puzzle: PowerGrid) -> int:
        edits = 0
        POWER = 1
        EMPTY = 0
        for r in range(puzzle.length):
            for c in range(puzzle.length):
                loc = Loc(r, c)
                candidates = puzzle.cell_candidates(loc)
                if len(candidates) > 1:
                    continue
                if POWER in candidates:
                    directions = [
                        loc.west(),
                        loc.north(),
                        loc.east(),
                        loc.south(),
                        loc.north().east(),
                        loc.north().west(),
                        loc.south().east(),
                        loc.south().west(),
                    ]

                    for direction in directions:
                        if direction.is_valid_sudoku(puzzle.length):
                            edits += puzzle.rem([direction], [POWER])

        return edits
