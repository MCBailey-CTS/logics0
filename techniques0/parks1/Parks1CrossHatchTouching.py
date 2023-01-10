from Loc import Loc
from puzzles import Parks1


class Parks1CrossHatchTouching:

    def solve0(self, puzzle: Parks1) -> int:
        edits = 0
        for r in range(puzzle.length):
            for c in range(puzzle.length):
                loc = Loc(r, c)

                candidates = puzzle.cell_candidates(loc)

                if len(candidates) != 1 or candidates[0] != 1:
                    continue

                directions = [
                    loc.north().west(),
                    loc.north().east(),
                    loc.south().west(),
                    loc.south().east(),
                ]

                for direction in directions:
                    if direction.is_valid_parks(puzzle.grid):
                        edits += puzzle.rem([direction], [1])

        return edits
