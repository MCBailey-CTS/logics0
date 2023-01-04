from Loc import Loc
from _puzzles import Minesweeper


class MinesweeperSolver:  # :

    @staticmethod
    def surrounding(puzzle, loc: Loc) -> list[Loc]:
        valid = []
        directions = [
            loc.north(),
            loc.east(),
            loc.south(),
            loc.west(),
            loc.north().east(),
            loc.north().west(),
            loc.south().east(),
            loc.south().west(),
        ]

        for temp in directions:
            if temp.is_valid_parks(puzzle.grid):
                valid.append(temp)

        return valid

    def solve0(self, puzzle: Minesweeper) -> int:
        edits = 0
        for r in range(puzzle.length):
            for c in range(puzzle.length):
                loc = Loc(r, c)
                if puzzle.is_number_cell(loc):
                    number = int(puzzle.grid[loc.row][loc.col])

                    if number == 0:
                        edits += puzzle.rem()

        return edits
