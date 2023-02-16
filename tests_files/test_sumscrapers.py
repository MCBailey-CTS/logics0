# from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# from techniques.LockedCandidatesPointing import LockedCandidatesPointing
from Loc import Loc
from Puzzle import Puzzle

EXPLICITLY = "EXPLICITLY"


class Sumscrapers(Puzzle):
    def __init__(self, puzzle: str, row_length: int = 2, col_length: int = 2):
        super().__init__(puzzle)

        for r in range(len(self)):
            for c in range(len(self)):
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

    def north_scraper(self, col: int) -> int | None:
        return self.__scaper_or_none(Loc(len(self), col))

    def south_scraper(self, col: int) -> int | None:
        return self.__scaper_or_none(Loc(len(self) + 1, col))

    def east_scraper(self, row: int) -> int | None:
        return self.__scaper_or_none(Loc(row, len(self) + 1))

    def west_scraper(self, row: int) -> int | None:
        return self.__scaper_or_none(Loc(row, len(self)))

    def __str__(self):
        string = f'{super().__str__()}\n'

        string += f'{"$$".ljust(len(self))} '

        for index in range(len(self)):
            north = self.north_scraper(index)

            if north is None:
                string += f'{"??".ljust(len(self))} '
            else:
                string += f'{f"{north}".ljust(len(self))} '

        string += "$$\n"

        for row in range(len(self)):
            west = self.west_scraper(row)
            if west is None:
                string += f'{"??".ljust(len(self))} '
            else:
                string += f'{f"{west}".ljust(len(self))} '

            for col in range(len(self)):
                string += f'{self.grid[row][col]} '

            east = self.east_scraper(row)
            if east is None:
                string += f'{"??".ljust(len(self))} '
            else:
                string += f'{f"{east}".ljust(len(self))} '

            string += '\n'

        string += f'{"$$".ljust(len(self))} '

        for index in range(len(self)):
            south = self.south_scraper(index)
            if south is None:
                string += f'{"??".ljust(len(self))} '
            else:
                string += f'{f"{south}".ljust(len(self))} '

        string += "$$\n"

        return string

    def _is_scraper_solved(self, sumscraper: int | None, house: list[Loc]) -> bool:
        solved_candidates = [self.cell_candidates(loc)[0] for loc in house if len(self.cell_candidates(loc)) == 1]
        if len(solved_candidates) != len(self):
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
        for index in range(len(self)):
            houses.append(self.house_row(index))
            houses.append(self.house_col(index))
        for house in houses:
            solved_candidates = [self.cell_candidates(loc)[0] for loc in house if len(self.cell_candidates(loc)) == 1]

            expected = set(self.expected_candidates())

            if not expected.issuperset(solved_candidates) or not expected.issubset(solved_candidates):
                return False

        for index in range(len(self)):
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

# @pytest.mark.parametrize("puzzle_string, constructor, techniques", [
#
#     ("sumscrapers_008", Sumscrapers, Solving.sumscrapers_techniques()),
#     ("sumscrapers_001", Sumscrapers, Solving.sumscrapers_techniques()),
#     ("sumscrapers_002", Sumscrapers, Solving.sumscrapers_techniques()),
#     ("sumscrapers_003", Sumscrapers, Solving.sumscrapers_techniques()),
#     ("sumscrapers_004", Sumscrapers, Solving.sumscrapers_techniques()),
#     ("sumscrapers_005", Sumscrapers, Solving.sumscrapers_techniques()),
#
# ])
# def test_default_puzzle(puzzle_string, constructor, techniques):
#     if "\n" in puzzle_string:
#         pytest.skip(puzzle_string)
#     result = getattr(Constants, puzzle_string)
#     assert default_test_puzzle(result(), constructor, techniques)


# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_001():
#     return f"""
#     001.sumscrapers
#     4
#     1234 1234 1234 1234 04 10
#     1234 1234 1234 1234 07 04
#     1234 1234 1234 1234 06 07
#     1234 1234 1234 1234 05 09
#     04   07   06   05   $$ $$
#     10   04   07   09   $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_002():
#     return f"""
#     002.sumscrapers
#     4
#     1234 1234 1234 1234 07 06
#     1234 1234 1234 1234 05 07
#     1234 1234 1234 1234 04 08
#     1234 1234 1234 1234 09 04
#     07 05 04 09 $$ $$
#     06 07 08 04 $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_003():
#     return f"""
#     003.sumscrapers
#     4
#     1234 1234 1234 1234 07 05
#     1234 1234 1234 1234 05 07
#     1234 1234 1234 1234 09 04
#     1234 1234 1234 1234 04 09
#     07 06 ?? 08  $$ $$
#     ?? 08 07 06 $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_004():
#     return f"""
#     004.sumscrapers
#     4
#     1234 1234 1234 1234 06 ??
#     1234 1234 1234 1234 04 08
#     1234 1234 1234 1234 07 04
#     1234 1234 1234 1234 08 06
#     06 04 08 07 $$ $$
#     08 07 04 ?? $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_005():
#     return f"""
#     005.sumscrapers
#     4
#     1234 1234 1234 1234 04 07
#     1234 1234 1234 1234 ?? ??
#     1234 1234 1234 1234 07 04
#     1234 1234 1234 1234 09 05
#     04 06 08 ?? $$ $$
#     09 ?? 04 05 $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_006():
#     return f"""
#     006.sumscrapers
#     4
#      1234 1234 1234 1234 04 08
#      1234 1234 1234 1234 ?? 04
#      1234 1234 1234 1234 05 07
#      1234 1234 1234 1234 ?? 06
#      04 09 07 ?? $$ $$
#      ?? ?? ?? ?? $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_007():
#     return f"""
#     007.sumscrapers
#     4
#       1234 1234
#      1234 1234 1234 1234 04 ??
#      1234 1234 1234 1234 ?? ??
#      1234 1234 1234 1234 07 ??
#      1234 1234 1234 1234 09 04
#      ?? 09 05 ?? $$ $$
#      ?? 05 ?? ?? $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_008():
#     return f"""
#     008.sumscrapers
#     4
#      1234 1234 1234 1234 ?? 06
#      1234 1234 1234 1234 ?? 07
#      1234 1234 1234 1234 ?? ??
#      1234 1234 1234 1234 ?? ??
#      07 ?? ?? ?? $$ $$
#      ?? 04 ?? 05 $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_010():
#     return f"""
#     010.sumscrapers
#     5
#     .. 09 ?? 08 05 ?? ..
#     09 .. 01 .. .. .. ??
#     08 .. .. .. .. .. ??
#     07 .. .. .. .. .. 12
#     ?? .. .. .. .. .. ??
#     13 .. .. .. .. .. ??
#     .. ?? 12 ?? 14 05 ..
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_011():
#     return f"""
#     011.sumscrapers
#     5
#     .. 09 ?? 14 ?? 12 ..
#     ?? .. .. .. .. .. ??
#     ?? .. .. .. .. .. 09
#     ?? .. .. .. .. .. ??
#     ?? .. .. .. .. .. 11
#     ?? .. .. .. .. .. ??
#     .. 10 ?? ?? 09 ?? ..
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_012():
#     return f"""
#     012.sumscrapers
#     5
#     .. ?? ?? 05 ?? 07 ..
#     ?? .. .. .. .. .. 11
#     ?? .. .. .. .. .. ??
#     09 .. .. .. .. .. ??
#     ?? .. .. .. .. .. ??
#     ?? .. .. .. .. .. 12
#     .. ?? ?? 10 ?? ?? ..
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_017():
#     return f"""
#     017.sumscrapers
#     6
#     .. ?? ?? ?? 06 17 ?? ..
#     11 .. .. .. .. .. .. ??
#     10 .. .. .. .. .. .. ??
#     ?? .. .. .. .. .. .. ??
#     18 .. .. .. .. .. .. ??
#     13 .. .. .. .. .. .. ??
#     ?? .. .. .. .. .. .. ??
#     .. 11 14 ?? 15 ?? 12 ..
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_018():
#     return f"""
#     018.sumscrapers
#     7
#     .. 13 13 20 11 ?? 18 09 ..
#     ?? 01 .. .. .. .. .. .. 14
#     ?? .. .. .. .. .. .. .. 07
#     07 .. .. .. .. .. .. .. 13
#     ?? 03 .. .. .. .. .. .. 12
#     13 .. .. .. .. .. .. .. 17
#     ?? .. .. .. .. 02 .. .. 10
#     12 .. .. .. .. .. .. .. 17
#     .. ?? 10 07 18 13 ?? 22 ..
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_019():
#     return f"""
#     019.sumscrapers
#     7
#     .. 13 ?? 10 20 ?? 12 ?? ..
#     13 .. .. 03 .. .. .. .. 16
#     14 .. .. .. .. .. .. .. 19
#     20 .. .. .. .. .. .. .. 09
#     07 .. .. 05 .. .. .. .. ??
#     22 .. .. .. .. .. 06 .. 07
#     13 .. .. .. .. .. .. .. 18
#     ?? .. .. .. .. .. .. .. 13
#     .. 12 21 24 ?? 07 17 13 ..
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_020():
#     return f"""
#     020.sumscrapers
#     7
#     .. ?? 13 19 07 ?? 18 ?? ..
#     15 .. .. .. .. .. .. .. 15
#     07 .. .. 02 .. .. .. .. 18
#     12 .. .. .. .. 03 .. 02 15
#     13 .. .. .. 03 .. .. .. ??
#     ?? .. 04 .. .. .. .. .. 13
#     16 .. .. .. .. .. .. .. ??
#     16 .. .. .. .. 05 .. .. ??
#     .. ?? ?? ?? ?? ?? 07 17 ..
#     """


# @staticmethod
# def sumscrapers_009():
#     return f"""
#     009.sumscrapers
#     5
#     .. 08 ?? ?? 05 14 ..
#     12 .. .. .. .. .. ??
#     05 .. .. .. .. .. 10
#     11 .. .. .. .. .. 08
#     ?? .. .. .. .. .. 09
#     09 .. .. .. .. .. 05
#     .. 09 07 ?? 12 05 ..
#     """
