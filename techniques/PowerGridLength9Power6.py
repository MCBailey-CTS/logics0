from colorama import Fore

from Loc import Loc
from techniques.Technique import Technique
from puzzles import PowerGrid


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

        print(house)

        # print("made it here")


        solved_indexes = [index for index, loc in enumerate(house) if puzzle.grid[loc.row][loc.col] == "1_"]

        if len(solved_indexes) != 1:
            return edits

        solved = solved_indexes[0]





        # for i, loc in enumerate(house):
        #     if puzzle.grid[loc.row][loc.col] != "10":
        #         continue
        #

        for index, loc in enumerate(house):
            if index == solved:
                continue

            print(abs(solved - index))

            # minus = i - power - 1
            # plus = i + power + 1
        #
        #     if minus >= 0 and 1 in puzzle.cell_candidates(house[minus]):
        #         continue
        #
        #     if plus < len(house) and 1 in puzzle.cell_candidates(house[plus]):
        #         continue
        #
        #     edits += puzzle.rem([loc], [1])
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

            # if col_scraper is not None:
            #     edits += self.solve1(puzzle, col_house, col_scraper)

            row_house = puzzle.house_row(index)

            for house in [row_house, col_house]:
                solved_power = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "1_"]
                solved_empty = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "_0"]
                unsolved = [loc for loc in house if puzzle.grid[loc.row][loc.col] == "10"]

                if len(solved_power) > 0:
                    continue

                if len(unsolved) != 2:
                    continue

                # if row_scraper is not None:
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
