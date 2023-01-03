from Loc import Loc
from _puzzles import Kropki


class KropkiDiamondEbww:
    edits = 0

    def solve0(self, puzzle: Kropki) -> int:
        black_empty = [5, 7, 9]
        black_white = [1, 5, 7, 9]
        white_empty = [3, 5, 7, 9]
        white_white = [1, 4, 6, 8, 9]

        edits = 0
        for r in range(puzzle.grid_length):
            for c in range(puzzle.grid_length):
                if r % 2 == 0 or c % 2 == 0:
                    continue

                loc = Loc(r, c)

                if puzzle.is_empty(loc.north()) and puzzle.is_white(loc.east()) and puzzle.is_white(
                        loc.south()) and puzzle.is_black(loc.west()):
                    edits += puzzle.rem([loc.north().west()], black_empty)
                    edits += puzzle.rem([loc.south().west()], black_white)
                    edits += puzzle.rem([loc.north().east()], white_empty)
                    edits += puzzle.rem([loc.south().east()], white_white)

                if puzzle.is_empty(loc.east()) and puzzle.is_white(loc.south()) and puzzle.is_white(
                        loc.west()) and puzzle.is_black(loc.north()):
                    edits += puzzle.rem([loc.north().west()], black_white)
                    edits += puzzle.rem([loc.south().west()], white_white)
                    edits += puzzle.rem([loc.north().east()], black_empty)
                    edits += puzzle.rem([loc.south().east()], white_empty)

        return edits
