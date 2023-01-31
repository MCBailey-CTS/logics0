from colorama import Fore

from Loc import Loc
from techniques.Technique import Technique

from puzzles import PowerGrid


def power_grid_techniques() -> list:
    return [
        # tech.PowerGridTech(),
        # tech.PowerGridCrossHatch(),
        # tech.PowerGridHiddenPower(),
        # tech.PowerGridTechExplicit()
        # PowerGridLength9Power5(),
        # PowerGridLength9Power6(),
        PowerGridLength9Power7(),
        PowerGridHiddenPowerPair(),
        PowerGridTouchingPower(),
        PowerGridOnePowerSolvedBadMath(),
        PowerGrid2Solved(),
        PowerGrid1Solved1Unsolved(),
        PowerGridRequirePower(),
        # PowerGridBothPowersSolved()

    ]

class PowerGridLength9Power7(Technique):

    def solve1(self, puzzle: PowerGrid, house: list[Loc], power: int) -> int:
        edits = 0
        solved_cells = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "1_"]

        if len(solved_cells) != 0:
            return edits

        for i, loc in enumerate(house):
            if puzzle.grid[loc.row][loc.col] != "10":
                continue

            minus = i - power - 1
            plus = i + power + 1

            if minus >= 0 and 1 in puzzle.cell_candidates(house[minus]):
                continue

            if plus < len(house) and 1 in puzzle.cell_candidates(house[plus]):
                continue

            edits += puzzle.rem([loc], [1])
        return edits

    def solve0(self, puzzle: PowerGrid) -> int:
        edits = 0

        if len(puzzle) != 9:
            return edits

        for index in range(len(puzzle)):
            col_house = puzzle.house_col(index)
            col_scraper = puzzle.south_scraper(index)

            if col_scraper is not None:
                edits += self.solve1(puzzle, col_house, col_scraper)

            row_house = puzzle.house_row(index)
            row_scraper = puzzle.east_scraper(index)

            if row_scraper is not None:
                edits += self.solve1(puzzle, row_house, row_scraper)

        return edits


class PowerGridOnePowerSolvedBadMath(Technique):

    def solve1(self, puzzle: PowerGrid, house: list[Loc], power: int) -> int:
        edits = 0
        if not all(loc.row == 0 for loc in house):
            return edits
        solved_indexes = [index for index, loc in enumerate(house) if puzzle.grid[loc.row][loc.col] == "1_"]
        if len(solved_indexes) != 1:
            return edits
        solved_index = solved_indexes[0]
        for index, loc in enumerate(house):
            if index == solved_index:
                continue
            if abs(solved_index - index) - 1 == power:
                continue
            edits += puzzle.rem([house[index]], [1])
        return edits

    def solve0(self, puzzle: PowerGrid) -> int:
        edits = 0

        if len(puzzle) != 9:
            return edits

        for index in range(len(puzzle)):
            col_house = puzzle.house_col(index)
            col_scraper = puzzle.south_scraper(index)

            if col_scraper is not None:
                edits += self.solve1(puzzle, col_house, col_scraper)

            row_house = puzzle.house_row(index)
            row_scraper = puzzle.east_scraper(index)

            if row_scraper is not None:
                edits += self.solve1(puzzle, row_house, row_scraper)

        return edits


class PowerGridHiddenPowerPair(Technique):

    def solve0(self, puzzle: PowerGrid) -> int:
        edits = 0

        if len(puzzle) != 9:
            return edits

        for index in range(len(puzzle)):
            col_house = puzzle.house_col(index)

            row_house = puzzle.house_row(index)

            for house in [row_house, col_house]:
                solved_power = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "1_"]
                solved_empty = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "_0"]
                unsolved = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "10"]

                if len(solved_power) > 0:
                    continue

                if len(unsolved) != 2:
                    continue

                edits += puzzle.rem(unsolved, [0])

        return edits



class PowerGrid2Solved(Technique):

    def solve0(self, puzzle: PowerGrid) -> int:
        edits = 0

        if len(puzzle) != 9:
            return edits

        for index in range(len(puzzle)):
            # col_house = puzzle.house_col(index)

            row_house = puzzle.house_row(index)

            # for house in [row_house, col_house]:
            for house in [row_house]:
                solved_power = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "1_"]
                solved_empty = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "_0"]
                unsolved = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "10"]

                if len(solved_power) == 2:
                    # puzzle.override_loc_color(unsolved, Fore.RED)

                    edits += puzzle.rem(unsolved, [1])

        return edits


class PowerGrid1Solved1Unsolved(Technique):

    def solve0(self, puzzle: PowerGrid) -> int:
        edits = 0
        if len(puzzle) != 9:
            return edits
        for index in range(len(puzzle)):
            col_house = puzzle.house_col(index)
            row_house = puzzle.house_row(index)
            for house in [row_house, col_house]:
                solved_power = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "1_"]
                solved_empty = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "_0"]
                unsolved = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "10"]
                if len(solved_power) == 1 and len(unsolved) == 1:
                    edits += puzzle.rem(unsolved, [0])
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

            power_solved = [loc for loc in col_house if 0 not in puzzle.cell_candidates(loc)]

            if len(power_solved) != 2:
                continue

            remove = set(col_house) - set(power_solved)

            # puzzle.override_loc_color(remove, Fore.RED)
            edits += puzzle.rem(list(remove), [1])

        return edits


class PowerGridRequirePower(Technique):

    def solve0(self, puzzle: PowerGrid) -> int:
        edits = 0
        if len(puzzle) != 9:
            return edits
        for index in range(len(puzzle)):
            col_house = puzzle.house_col(index)
            row_house = puzzle.house_row(index)
            for house in [row_house, col_house]:
                unsolved = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "10"]
                if len(unsolved) != 4:
                    continue
                unsolved_set = set(unsolved)
                first = unsolved_set.pop()
                next_gen = next((loc for loc in unsolved_set if loc.is_next_to(first)), None)
                if next_gen is None:
                    continue
                left = [first, next_gen]
                unsolved_set.remove(next_gen)
                second = unsolved_set.pop()
                next_gen_second = next((loc for loc in unsolved_set if loc.is_next_to(second)), None)
                if next_gen_second is None:
                    continue
                right = [second, next_gen_second]

                locs = right + left

                # if all(loc.row == row_house[0].row for loc in row_house):
                #     for loc in locs:
                #         north = loc.north()
                #         if 0 > north.row >= len(puzzle):
                #             continue
                #         edits += puzzle.rem([north], [1])
                #
                #         south = loc.south()
                #         if 0 > south.row >= len(puzzle):
                #             continue
                #         edits += puzzle.rem([south], [1])

        return edits