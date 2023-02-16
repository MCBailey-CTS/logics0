# 
# robot_fences_techniques
# @pytest.mark.skip("skipped")
# 
# 
# assert default_test_puzzle(puzzle_string, RobotFences, robot_fences_techniques())
import pytest

from Loc import Loc
from Puzzle import Puzzle
from _defaults import default_test_puzzle
from solving import Solving


class Minesweeper(Puzzle):
    def is_solved(self) -> bool:
        return False

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)
        array = []
        self.grid = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            array.append(temp)
        array.pop(0)
        array.pop(0)
        for line in array:
            self.grid.append(line.split(' '))

    def is_number_cell(self, loc: Loc) -> bool:
        return self.grid[loc.row][loc.col].isalnum()

    def is_mine_cell(self, loc: Loc) -> bool:
        return not self.is_number_cell(loc)

    def __str__(self):
        string = f'{self.id()}\n'
        string += f'{len(self)}\n'
        for r in range(len(self)):
            for c in range(len(self)):
                string += f'{self.grid[r][c]} '
            string += '\n'
        return string

    def rem(self, locs: list[Loc], candidates: list[str]) -> int:
        edits = 0

        for loc in locs:
            for candidate in candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                self.grid[loc.row][loc.col] = self.grid[loc.row][loc.col].replace(str(candidate), "_")
                edits += 1

        return edits


def minesweeper_techniques():
    return [tech.MinesweeperSolver()]


# @staticmethod
# def minesweeper_explicit_0_actual():
#     return f"""
#     minesweeper_explicit_0_actual.minesweeper
#     5
#     +- +- +- +- +-
#     +- +- +- +- +-
#     +- +- 00 +- +-
#     +- +- +- +- +-
#     +- +- +- +- +-
#     """

# @staticmethod
# def minesweeper_explicit_0_expected():
#     return f"""
#     minesweeper_explicit_0_expected.minesweeper
#     5
#     +- +- +- +- +-
#     +- .- +.- .- +-
#     +- .- 00 .- +-
#     +- .- .- .- +-
#     +- +- +- +- +-
#     """


@pytest.mark.skip("skipped")
def test_minesweeper_001():
    puzzle_string = f"""
    001.minesweeper
    5
    # 01 01 02 01 01
    # +- +- 04 +- 02
    # +- 04 +- +- 03
    # 02 +- +- +- 03
    # 01 01 +- +- 02
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_002():
    puzzle_string = f"""
    002.minesweeper
    5
    01 01 02 01 01
    +- +- 04 +- 02
    +- 04 +- +- 03
    02 +- +- +- 03
    01 01 +- +- 02
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_003():
    puzzle_string = f"""
    003.minesweeper
    5
    01 02 +- 02 +-
    +- +- +- 03 02
    +- +- 03 02 +-
    04 +- 02 +- 01
    +- 02 01 +- +-
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_004():
    puzzle_string = f"""
    004.minesweeper
    5
    02 +- +- +- +-
    +- 03 05 +- 03
    +- +- +- +- 03
    01 02 02 +- +-
    +- +- +- 01 +-
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_005():
    puzzle_string = f"""
    005.minesweeper
    6
    +- 02 04 +- +- +-
    +- +- +- +- 04 +-
    01 +- +- +- 05 +-
    +- 01 02 +- +- 03
    01 01 +- 02 +- +-
    +- +- 00 +- 01 +-
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_006():
    puzzle_string = f"""
    006.minesweeper
    6
    01 +- 01 01 +- +-
    +- 02 +- +- +- 01
    +- 04 04 +- 02 +-
    +- +- +- +- 02 00
    02 03 +- +- 02 00
    +- +- 02 +- 02 +-
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_007():
    puzzle_string = f"""
    007.minesweeper
    6
    +- +- +- 02 01 +-
    02 +- 04 +- 02 +-
    03 +- +- +- 04 +-
    +- +- 03 +- +- +-
    +- 03 +- 03 +- +-
    +- +- +- +- 01 01
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_008():
    puzzle_string = f"""
    008.minesweeper
    7
    +- +- 02 +- +- +- 01
    01 +- 02 02 +- +- 02
    +- 00 01 02 03 04 +-
    +- +- 01 +- +- +- +-
    01 01 02 +- 03 +- 02
    +- +- +- 01 +- +- 01
    01 02 +- +- +- +- 0
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_009():
    puzzle_string = f"""
    009.minesweeper
    7
    01 02 03 +- +- +- +-
    +- +- +- 05 +- +- 03
    02 +- +- +- +- 03 01
    +- 03 +- +- 02 +- +-
    +- 02 +- +- +- +- +-
    +- 01 +- 02 +- 04 +-
    +- +- 01 02 01 +- 01
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_010():
    puzzle_string = f"""
    010.minesweeper
    7
    00 01 +- +- +- +- +-
    +- +- +- 05 05 +- 03
    +- 02 02 +- +- 05 +-
    +- +- +- 04 +- +- +-
    +- 03 +- +- +- +- 03
    03 +- +- 00 01 02 +-
    02 +- +- +- 01 +- +-
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_011():
    puzzle_string = f"""
    011.minesweeper
    8
    01 03 +- +- 03 +- +- +-
    +- +- +- 03 +- +- 03 +-
    02 +- 02 01 +- 03 +- +-
    01 02 +- +- 03 +- +- +-
    +- 02 +- +- +- 03 02 +-
    01 +- +- +- 6 +- +- +-
    +- +- 04 +- +- +- 01 00
    01 01 +- +- 03 01 +- +-
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_012():
    puzzle_string = f"""
    012.minesweeper
    8
    02 +- +- +- +- 02 02 +-
    +- 06 +- 04 +- +- +- +-
    +- +- +- 03 02 03 +- 02
    +- 04 +- +- 02 +- 03 +-
    +- +- 02 +- 04 +- +- 01
    +- 01 +- +- 02 +- +- 02
    +- 02 02 +- +- +- 04 +-
    02 +- +- 00 00 +- +- +-
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_013():
    puzzle_string = f"""
    013.minesweeper
    8
    01 01 +- +- +- +- 03 +-
    +- +- 02 +- 03 +- +- 02
    +- 03 +- 04 +- +- +- 01
    +- 04 +- +- 01 +- 02 +-
    01 +- +- +- 02 +- +- 01
    +- +- +- +- 01 +- +- +-
    +- 02 +- +- 01 00 +- +-
    01 +- 01 01 +- +- 00 +-
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_014():
    puzzle_string = f"""
    014.minesweeper
    8
    +- 02 +- +- +- +- +- +-
    01 +- +- 04 03 04 03 +-
    +- 02 +- +- +- +- +- +-
    03 04 +- +- 03 +- +- 04
    +- +- +- +- 02 +- +- 02
    02 +- 05 +- +- 01 +- +-
    +- 03 +- 04 +- +- 01 00
    +- 03 +- 03 +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_015():
    puzzle_string = f"""
    015.minesweeper
    9
    +- +- +- +- +- +- +- 03 +-
    +- 01 02 01 02 +- 03 04 +-
    +- +- +- +- +- +- 01 +- +-
    02 02 +- +- 00 00 +- +- +-
    +- 01 00 00 01 02 +- 04 +-
    02 +- +- +- +- +- +- 04 +-
    +- +- 02 +- 03 +- +- +- 01
    01 +- +- 01 +- +- 04 02 01
    +- 00 +- +- 01 +- +- +- +-
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_016():
    puzzle_string = f"""
    016.minesweeper
    9
    +- 02 +- +- +- +- +- +- 00
    +- +- 02 03 +- 02 +- +- 00
    +- 03 02 +- +- 01 +- +- +-
    +- 02 +- +- +- 01 +- +- 02
    01 +- 01 01 +- +- 02 +- 02
    +- +- 02 +- +- 02 +- +- +-
    +- +- 02 01 +- +- +- +- 01
    04 04 02 +- 02 03 03 +- 01
    +- +- +- +- +- +- +- +- 01
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_017():
    puzzle_string = f"""
    017.minesweeper
    9
    +- 04 +- +- +- +- 02 +- 00
    +- 05 +- +- 02 02 +- +- 01
    03 +- +- 03 +- +- +- +- +-
    +- +- 05 +- 03 +- 04 +- +-
    +- 05 +- +- +- +- +- 04 +-
    03 +- +- +- +- 03 +- +- 01
    +- 04 +- +- 01 +- +- 05 03
    +- 04 04 +- +- +- 03 +- +-
    +- +- +- 01 +- +- +- 02 +-
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())


@pytest.mark.skip("skipped")
def test_minesweeper_024():
    puzzle_string = f"""
    024.minesweeper
    15
    +- 03 +- +- +- 01 +- +- +- +- 01 +- 02 +- +-
    +- +- 02 +- +- 01 03 +- 02 +- +- 01 +- 03 +-
    +- 03 +- 02 +- +- +- +- 04 +- +- 02 +- 05 +-
    +- 01 +- +- 02 +- 03 +- +- +- +- +- +- +- +-
    +- +- +- +- +- 04 05 +- 05 03 +- +- 03 03 +-
    +- 00 +- +- +- +- +- +- +- 02 01 +- +- +- +-
    +- +- 01 01 03 03 04 +- +- +- +- 04 +- +- +-
    +- 01 +- +- +- +- +- 03 02 04 +- +- +- 02 +-
    03 +- +- 01 +- 02 +- 03 +- +- +- 04 +- 02 01
    +- +- 01 +- 02 +- +- +- +- 04 +- +- 00 +- +-
    +- 03 +- +- +- +- +- +- +- +- 03 +- +- 03 +-
    +- +- 01 +- +- 06 05 +- +- +- 03 02 +- +- +-
    03 +- +- +- 03 +- +- +- 03 +- +- +- 02 +- 02
    +- 03 02 +- +- 04 +- +- +- 04 +- +- 03 +- 03
    +- +- +- 01 01 +- 03 +- 04 +- 03 +- 03 +- +-
    """
    assert default_test_puzzle(puzzle_string, Minesweeper, minesweeper_techniques())
