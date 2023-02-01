# 
# robot_fences_techniques
# @pytest.mark.skip("skipped")
# 
# 
# assert default_test_puzzle(puzzle_string, RobotFences, Solving.robot_fences_techniques())
import pytest

from _defaults import default_test_puzzle
from puzzles import Minesweeper
from solving import Solving


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())


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
    assert default_test_puzzle(puzzle_string, Minesweeper, Solving.minesweeper_techniques())
