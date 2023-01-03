from Loc import Loc
from _puzzles import PowerGrid


class PowerGridTech:
    def solve0(self, puzzle: PowerGrid) -> int:
        edits = 0

        for index in range(puzzle.length):
            row_house = puzzle.house_row(index)
            row_scraper = puzzle.east_scraper(index)
            if row_scraper is None:
                continue
            edits += self.solve1(puzzle, row_scraper, row_house)
            col_house = puzzle.house_col(index)
            col_scraper = puzzle.south_scraper(index)
            if col_scraper is None:
                continue
            edits += self.solve1(puzzle, col_scraper, col_house)
        return edits

    def solve1(self, puzzle: PowerGrid, power: int, house: list[Loc]) -> int:
        edits = 0

        POWER = 1
        EMPTY = 0

        for index in range(puzzle.length):
            left_index = index - power - 1
            right_index = index + power + 1

            # valid_left =

            if left_index < 0 and right_index >= puzzle.length:
                edits += puzzle.rem([house[index]], [POWER])

            if left_index < 0 and right_index < puzzle.length and POWER not in puzzle.cell_candidates(
                    house[right_index]):
                edits += puzzle.rem([house[index]], [POWER])

            if left_index >= 0 and right_index >= puzzle.length and POWER not in puzzle.cell_candidates(
                    house[left_index]):
                edits += puzzle.rem([house[index]], [POWER])

            if left_index >= 0 and right_index < puzzle.length and POWER not in puzzle.cell_candidates(
                    house[left_index]) and POWER not in puzzle.cell_candidates(house[right_index]):
                edits += puzzle.rem([house[index]], [POWER])

        return edits
