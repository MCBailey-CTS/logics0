
from puzzles import Puzzle
from Loc import Loc
from typing import Optional

class Sumscrapers(Puzzle):
    def __init__(self, puzzle: str, row_length: int = 2, col_length: int = 2):
        super().__init__(puzzle, row_length, col_length)

        for r in range(self.length):
            for c in range(self.length):
                if self.grid[r][c] == '_':
                    string = ""
                    for candidate in self.expected_candidates():
                        string += f'{candidate}'
                    self.grid[r][c] = string

    @property
    def has_fences(self) -> bool:
        return False

    def __scaper_or_none(self, loc: Loc):
        string = self.grid[loc.row][loc.col]
        if string.isnumeric():
            return int(string)
        return None

    def north_scraper(self, col: int) -> Optional[int]:
        return self.__scaper_or_none(Loc(self.length, col))

    def south_scraper(self, col: int) -> Optional[int]:
        return self.__scaper_or_none(Loc(self.length + 1, col))

    def east_scraper(self, row: int) -> Optional[int]:
        return self.__scaper_or_none(Loc(row, self.length + 1))

    def west_scraper(self, row: int) -> Optional[int]:
        return self.__scaper_or_none(Loc(row, self.length))

    def __str__(self):
        string = f'{super().__str__()}\n'

        string += f'{"$$".ljust(self.length)} '

        for index in range(self.length):
            north = self.north_scraper(index)

            if north is None:
                string += f'{"??".ljust(self.length)} '
            else:
                string += f'{f"{north}".ljust(self.length)} '

        string += "$$\n"

        for row in range(self.length):
            west = self.west_scraper(row)
            if west is None:
                string += f'{"??".ljust(self.length)} '
            else:
                string += f'{f"{west}".ljust(self.length)} '

            for col in range(self.length):
                string += f'{self.grid[row][col]} '

            east = self.east_scraper(row)
            if east is None:
                string += f'{"??".ljust(self.length)} '
            else:
                string += f'{f"{east}".ljust(self.length)} '

            string += '\n'

        string += f'{"$$".ljust(self.length)} '

        for index in range(self.length):
            south = self.south_scraper(index)
            if south is None:
                string += f'{"??".ljust(self.length)} '
            else:
                string += f'{f"{south}".ljust(self.length)} '

        string += "$$\n"

        return string

    def _is_scraper_solved(self, sumscraper: Optional[int], house: list[Loc]) -> bool:
        solved_candidates = [self.cell_candidates(loc)[0] for loc in house if len(self.cell_candidates(loc)) == 1]
        if len(solved_candidates) != self.length:
            return False
        if sumscraper is None:
            return True

        current = 0
        max0 = 0

        for candidate in solved_candidates:
            if candidate < max0:
                continue
            current += candidate
            max0 = candidate

        return sumscraper == current

    def is_solved(self) -> bool:
        houses = []
        for index in range(self.length):
            houses.append(self.house_row(index))
            houses.append(self.house_col(index))
        for house in houses:
            solved_candidates = [self.cell_candidates(loc)[0] for loc in house if len(self.cell_candidates(loc)) == 1]

            expected = set(self.expected_candidates())

            if not expected.issuperset(solved_candidates) or not expected.issubset(solved_candidates):
                return False

        for index in range(self.length):
            house = self.house_row(index)

            if not self._is_scraper_solved(self.west_scraper(index), house):
                return False

            house.reverse()

            if not self._is_scraper_solved(self.east_scraper(index), house):
                return False

            house = self.house_col(index)

            if not self._is_scraper_solved(self.north_scraper(index), house):
                return False

            house.reverse()

            if not self._is_scraper_solved(self.south_scraper(index), house):
                return False

        return True

