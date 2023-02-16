import pytest
from colorama import Style

from Loc import Loc
from Puzzle import Puzzle
from _defaults import default_test_puzzle
from techniques.PowerGridTechniques import power_grid_techniques

EXPLICITLY = "EXPLICITLY"



class PowerGrid(Puzzle):

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)

    def __is_solved0(self, house: list[Loc], power: int|None) -> bool:
        POWER = 1
        EMPTY = 0

        candidates_array = [self.cell_candidates(loc) for loc in house]

        all_cells_solved = [len(candidates_array[index]) == 1 for index in range(len(candidates_array))]

        if not all(all_cells_solved):
            return False

        solved_power_indexes = [index for index in range(len(candidates_array)) if POWER in candidates_array[index]]

        if len(solved_power_indexes) > 2:
            raise Exception("Found power grid house with more than 2 solved power cells")

        if len(solved_power_indexes) != 2:
            return False

        # unsolved = []

        # # for index

        # for index in range(len(house)):
        #     candidates = puzzle.cell_candidates(house[index])

        #     if len(candidates) > 1:
        #         unsolved.append(house[index])
        #         continue

        #     if POWER in candidates:
        #         solved_power.append(house[index])

        #     if EMPTY in candidates:
        #         solved_empty.append(house[index])

        # if len(solved_power) == 2:
        #     edits += puzzle.rem(unsolved, [POWER])

        # if len(solved_power) == 0 and len(unsolved) == 2:
        #     edits += puzzle.rem(unsolved, [EMPTY])

        # if len(solved_power) == 1 and len(unsolved) == 1:
        #     edits += puzzle.rem(unsolved, [EMPTY])
        # for index in range(len(house)):

        return True

    def is_solved(self) -> bool:
        for index in range(len(self)):
            if not self.__is_solved0(self.house_row(index), self.east_scraper(index)):
                return False
            if not self.__is_solved0(self.house_col(index), self.south_scraper(index)):
                return False
        return True

    def east_scraper(self, row: int) -> int|None:
        string = self.grid[row][len(self)]
        if string.isnumeric():
            return int(string)
        return None

    def south_scraper(self, col: int) -> int|None:
        string = self.grid[len(self)][col]
        if string.isnumeric():
            return int(string)
        return None

    def __str__(self):
        string = f'{self.id()}\n{len(self)}\n'
        for r in range(len(self) + 1):
            for c in range(len(self) + 1):
                string += f'{self.grid[r][c]} '
            string += '\n'
        return string.replace('10', '__', -1).replace('_0', '..', -1).replace('1_', 'PP', -1)

    def surrounding(self, loc: Loc) -> list[Loc]:
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
            if temp.row < 0 or temp.row >= len(self):
                continue
            if temp.col < 0 or temp.col >= len(self):
                continue

            # if temp.is_valid_parks(self.grid):
            valid.append(temp)

        return valid

    def to_string(self, include_colors=True) -> str:
        string = f'{self.id()}\n{len(self)}\n'
        for r in range(len(self) + 1):
            for c in range(len(self) + 1):
                loc = Loc(r, c)
                # string += f'{self.grid[r][c]} '
                if include_colors and loc in self.color_override:
                    string += f'{self.color_override[loc]}{self.grid[r][c]}{Style.RESET_ALL} '
                    continue
                # if len(self.cell_candidates(loc)) == 0:
                #     string += f'{Fore.GREEN}{self.grid[r][c]}{Style.RESET_ALL} '
                # else:
                string += f'{self.grid[r][c]} '
            string += '\n'
        return string.replace('10', '__', -1).replace('_0', '..', -1).replace('1_', 'PP', -1)
        # string = f'{self.id()}\n'
        # string += f'{len(self)}\n'
        # for r in range(len(self)):
        #     for c in range(len(self)):
        #         loc = Loc(r, c)
        #         if include_colors and loc in self.color_override:
        #             string += f'{self.color_override[loc]}{self.grid[r][c].ljust(len(self))}{Style.RESET_ALL} '
        #             continue
        #         if len(self.cell_candidates(loc)) == 0:
        #             string += f'{Fore.GREEN}{self.grid[r][c].ljust(len(self))}{Style.RESET_ALL} '
        #         else:
        #             string += f'{self.grid[r][c].ljust(len(self))} '
        #     string += '\n'
        # return string



# from tests_explicit.test_small_explicit import solve
# from techniques.CrossHatch import CrossHatch

# def test_explicit_power_grid_():
#     actual = \
#         f"""
        
#         """
#     expected = \
#         f"""
        
#         """
#     if solve(4, actual, expected, None):
#         return
#     assert False

from techniques.PowerGridTechniques import  PowerGridTouchingPower, PowerGridBothPowersSolved, \
    PowerGridLength9Power7, PowerGridHiddenPowerPair, PowerGridOnePowerSolvedBadMath, PowerGrid2Solved, PowerGrid1Solved1Unsolved, PowerGridRequirePower


# def test_row_():
#     actual = \
#         f"""
#         ______a ______a ______a   ______b ______b ______b
#         ______a ______a ______a   ______b ______b ______b
#
#         ______c ______c ______c   ______d ______d ______d
#         ______c ______c ______c   ______d ______d ______d
#
#         ______e ______e ______e   ______f ______f ______f
#         ______e ______e ______e   ______f ______f ______f
#         """
#
#     expected = \
#         f"""
#         ______a ______a ______a   ______b ______b ______b
#         ______a ______a ______a   ______b ______b ______b
#
#         ______c ______c ______c   ______d ______d ______d
#         ______c ______c ______c   ______d ______d ______d
#
#         ______e ______e ______e   ______f ______f ______f
#         ______e ______e ______e   ______f ______f ______f
#         """
#     if solve(actual, expected, None):
#         return
#     assert False


def test_power_grid_001():
    puzzle_string = f"""
    001.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    05 01 06 01 05 05 01 06 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_002():
    puzzle_string = f"""
    002.power_grid
    9
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    04 03 03 07 01 05 01 06 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_003():
    puzzle_string = f"""
    003.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 04
    04 03 03 03 04 04 04 03 03 $$
    diagonal        
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_004():
    puzzle_string = f"""
    004.power_grid
    9
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    01 01 02 01 01 01 01 03 04 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_005():
    puzzle_string = f"""
    005.power_grid
    9
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    02 06 01 01 01 01 01 01 03 $$
    diagonal     
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_006():
    puzzle_string = f"""
    006.power_grid
    9
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    03 03 01 01 06 01 05 01 06 $$      
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("explicitly")
def test_power_grid_007():
    puzzle_string = f"""
    007.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    01 01 01 01 01 01 03 04 04 $$     
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_008():
    puzzle_string = f"""
    008.power_grid
    9
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    01 01 01 01 01 01 03 03 03 $$     
    diagonal
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_009():
    puzzle_string = f"""
    009.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 01
    02 01 01 01 01 01 02 01 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_010():
    puzzle_string = f"""
    010.power_grid
    9
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    01 01 01 01 01 01 03 05 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_011():
    puzzle_string = f"""
    011.power_grid
    9
    10 10 10 10 10 10 10 10 10 ??
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 ??
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 05
    06 01 06 01 05 01 01 01 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_012():
    puzzle_string = f"""
    012.power_grid
    9
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    03 ?? 01 05 01 ?? 01 01 02 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_013():
    puzzle_string = f"""
    013.power_grid
    9
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    03 03 ?? 01 06 ?? 05 01 06 $$
    diagonal
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("help")
def test_power_grid_014():
    puzzle_string = f"""
    014.power_grid
    9
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 ??
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    05 01 01 ?? 01 01 02 01 02 $$
    diagonal
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_015():
    puzzle_string = f"""
    015.power_grid
    9
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ??
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    ?? 01 01 01 03 03 03 01 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_016():
    puzzle_string = f"""
    016.power_grid
    9
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 01
    01 01 02 01 02 01 ?? ?? 02 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_017():
    puzzle_string = f"""
    017.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ??
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ??
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 07
    10 10 10 10 10 10 10 10 10 01
    01 01 02 01 01 01 05 01 06 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_018():
    puzzle_string = f"""
    018.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01 
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    01 01 ?? 01 01 ?? 01 01 01 $$
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_019():
    puzzle_string = f"""
    019.power_grid
    9
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    03 03 03 01 01 .. 01 01 01 ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_020():
    puzzle_string = f"""
    020.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    01 01 01 01 03 05 01 01 01 ..
    diagonal
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_021():
    puzzle_string = f"""
    021.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 04
    02 01 01 01 01 .. .. 04 03 ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_022():
    puzzle_string = f"""
    022.power_grid
    9
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    01 05 05 01 06 .. 05 01 06 ..
    diagonal
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_023():
    puzzle_string = f"""
    023.power_grid
    9
    10 10 10 10 10 10 10 10 10 06
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    .. 01 01 .. 01 01 01 06 .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


def test_power_grid_024():
    puzzle_string = f"""
    024.power_grid
    9
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 02
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 01
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 01
    .. 05 05 .. 07 01 .. 01 05 ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_025():
    puzzle_string = f"""
    025.power_grid
    9
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 03
    10 10 10 10 10 10 10 10 10 05
    10 10 10 10 10 10 10 10 10 04
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 03
    .. 01 01 01 01 01 01 .. 01 ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_026():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_027():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_028():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_29():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_030():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_031():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_032():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_033():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_034():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_035():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_036():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_037():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_038():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_039():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_040():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_041():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_042():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_043():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_044():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_045():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_046():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_047():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_048():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_049():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_050():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_051():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_052():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_053():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_054():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_055():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_056():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_057():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_058():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_059():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_power_grid_060():
    puzzle_string = f"""
    0.power_grid
    9
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    10 10 10 10 10 10 10 10 10 ..
    .. .. .. .. .. .. .. .. .. ..
    """
    assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())

# def test_power_grid_094():
#     puzzle_string = f"""
#     018.power_grid
#     10
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     10 10 10 10 10 10 10 10 10 10 ..
#     .. .. .. .. .. .. .. .. .. .. ..
#     """
#     assert default_test_puzzle(puzzle_string, PowerGrid, power_grid_techniques())
