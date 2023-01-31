from Loc import Loc
from techniques.Technique import Technique
from puzzles import PowerGrid

class PowerGridLength9Power6(Technique):
    def solve0(self, puzzle: PowerGrid) -> int:
        edits = 0

        if len(puzzle) != 9:
            return edits

        for index in range(len(puzzle)):
            col_house = puzzle.house_col(index)
            col_scraper = puzzle.south_scraper(index)

            if col_scraper != 7:
                continue

            edits += puzzle.rem([col_house[0], col_house[8]], [0])

        return edits

class PowerGridTouchingPower(Technique):
    def solve0(self, puzzle: PowerGrid) -> int:
        edits = 0

        for r in range(len(puzzle)):
            for c in range(len(puzzle)):
                loc = Loc(r, c)

                candidates = puzzle.cell_candidates(loc)

                if len(candidates) == 1 and 1 in candidates:
                    edits += puzzle.rem(puzzle.surrounding(loc), [1])



        return edits


class PowerGridBothPowersSolved(Technique):
    def solve0(self, puzzle: PowerGrid) -> int:
        edits = 0

        for index in range(len(puzzle)):
            col_house = puzzle.house_col(index)
            col_scraper = puzzle.south_scraper(index)

            # power_solved = [loc for loc in col_house if 0 not in puzzle.cell_fence(loc)]
            #
            # if len(power_solved) != 2:
            #     continue
            #
            # remove = set(power_solved) - set(col_house)
            #
            # edits += puzzle.rem(remove, [1])

        return edits