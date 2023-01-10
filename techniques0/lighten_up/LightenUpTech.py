from Loc import Loc
from puzzles import LightenUp

class LightenUpTech:
    def solve0(self, puzzle: LightenUp) -> int:
        edits = 0
        for r in range(puzzle.length):
            for c in range(puzzle.length):
                loc = Loc(r, c)
                # print(puzzle.grid[r][c])

                if puzzle.grid[r][c].isnumeric():
                    # print(puzzle.grid[r][c])

                    number = int(puzzle.grid[r][c])



                    # print(number)
                    directions = [
                        loc.north(),
                        loc.east(),
                        loc.south(),
                        loc.west()
                    ]

                    # valid_locs = [loc for loc in directions if loc.is_valid_parks(puzzle.grid)]
                    #
                    # if number == 0:
                    #
                    # if len(valid_locs) == int(puzzle.grid[r][c]):

                    if number == 4:
                        print("here")
                        edits += puzzle.rem(directions, ["-"])



                    # surrounding = Techs.MinesweeperSolver.surrounding(puzzle, loc)

                    # surrounding_numbers = []







        return edits

