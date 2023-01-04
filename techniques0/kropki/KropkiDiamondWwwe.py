from Loc import Loc
from _puzzles import Kropki


class KropkiDiamondWwwe:
    def solve0(self, puzzle: Kropki) -> int:
        edits = 0
        for r in range(puzzle.grid_length):
            for c in range(puzzle.grid_length):
                if r % 2 == 0 or c % 2 == 0:
                    continue

                loc = Loc(r, c)

                kropki_directions = [
                    loc.north(),
                    loc.east(),
                    loc.south(),
                    loc.west()
                ]

                all_our_valid = all([loc.is_valid_kropki(puzzle.grid_length) for loc in kropki_directions])

                if not all_our_valid:
                    continue

                empty_kropki = [loc for loc in kropki_directions if puzzle.is_empty(loc)]

                white_kropki = [loc for loc in kropki_directions if puzzle.is_white(loc)]

                if len(empty_kropki) != 1 or len(white_kropki) != 3:
                    continue

                empty = empty_kropki[0]

                if empty == loc.south():
                    edits += puzzle.rem([empty.west(), empty.east()], [3])
                    edits += puzzle.rem([empty.west().north(2), empty.east().north(2)], [1, 9])

                if empty == loc.north():
                    edits += puzzle.rem([empty.west(), empty.east()], [3])
                    edits += puzzle.rem([empty.west().south(2), empty.east().south(2)], [1, 9])

                if empty == loc.west():
                    edits += puzzle.rem([empty.north(), empty.south()], [3])
                    edits += puzzle.rem([empty.north().east(2), empty.south().east(2)], [1, 9])

                if empty == loc.east():
                    edits += puzzle.rem([empty.north(), empty.south()], [3])
                    edits += puzzle.rem([empty.north().west(2), empty.south().west(2)], [1, 9])

        return edits
