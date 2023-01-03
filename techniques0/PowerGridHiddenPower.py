from Loc import Loc
from _puzzles import PowerGrid


class PowerGridHiddenPower:
    def solve0(self, puzzle: PowerGrid) -> int:
        edits = 0

        for index in range(puzzle.length):
            row_house = puzzle.house_row(index)
            row_scraper = puzzle.east_scraper(index)
            # if row_scraper is None:
            #     continue
            edits += self.solve1(puzzle, row_scraper, row_house)
            col_house = puzzle.house_col(index)
            col_scraper = puzzle.south_scraper(index)
            # if col_scraper is None:
            #     continue
            edits += self.solve1(puzzle, col_scraper, col_house)
        return edits

    def solve1(self, puzzle: PowerGrid, power: int, house: list[Loc]) -> int:
        edits = 0

        POWER = 1
        EMPTY = 0

        solved_power = []
        solved_empty = []
        unsolved = []

        # for index

        for index in range(len(house)):
            candidates = puzzle.cell_candidates(house[index])

            if len(candidates) > 1:
                unsolved.append(house[index])
                continue

            if POWER in candidates:
                solved_power.append(house[index])

            if EMPTY in candidates:
                solved_empty.append(house[index])

        if len(solved_power) == 2:
            edits += puzzle.rem(unsolved, [POWER])

        if len(solved_power) == 0 and len(unsolved) == 2:
            edits += puzzle.rem(unsolved, [EMPTY])

        if len(solved_power) == 1 and len(unsolved) == 1:
            edits += puzzle.rem(unsolved, [EMPTY])

        return edits
