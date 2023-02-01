from _defaults import default_test_puzzle
from puzzles import RobotCrosswords
from solving import Solving
import pytest


# def test_robot_fences_020():
#     puzzle_string = f"""
#     020.robot_fences
#     5
#     0a 4a 5g 0h 0h
#     0a 0e 0f 0f 0h
#     0a 2f 0f 0f 0i
#     1a 0c 4c 0c 5i
#     4b 0c 0d 0d 3d
#     """assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())
#     assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


#
#
@pytest.mark.skip("skipped")
def test_robot_crosswords_002():
    puzzle_string = f"""
    002.robot_crosswords
    5
    x 6 7 x 6
    . . x 4 .
    6 x 4 3 x
    . . . x 9
    x 7 . 9 8
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_003():
    puzzle_string = f"""
    003.robot_crosswords
    5
    9 8 . 7 x
    . x 7 . 6
    . 4 . x .
    7 . x 3 .
    x 5 2 . .
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_004():
    puzzle_string = f"""
    004.robot_crosswords
    5
    . 4 x 9 x
    4 x . . 7
    . 5 . x 6
    2 . . 4 x
    x 4 x 5 4
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_005():
    puzzle_string = f"""
    005.robot_crosswords
    5
    . x 1 . 2
    1 . . . x
    x . . x 9
    4 3 x 7 .
    3 . . 6 x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_006():
    puzzle_string = f"""
    006.robot_crosswords
    6
    . 5 x . 3 1
    7 x 4 . x 2
    . . 3 x 2 x
    x 1 x . . .
    3 . 5 . x 1
    x . . . 4 x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_007():
    puzzle_string = f"""
    007.robot_crosswords
    6
    2 . 5 . x 2
    x 6 x . 4 .
    . . . 2 x 4
    4 x . . 3 x
    . 2 . x . .
    2 x . 4 x 6
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_008():
    puzzle_string = f"""
    008.robot_crosswords
    6
    5 . 3 x 2 x
    x 5 x 1 . .
    1 . . . x 1
    x 2 1 . . x
    2 x 3 x 5 4
    1 . . 3 x 5
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_009():
    puzzle_string = f"""
    009.robot_crosswords
    6
    7 . x 2 3 x
    x . . x 2 .
    7 5 . . x 6
    4 x 2 . 4 .
    . 5 x . x .
    . x 6 . 7 x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_010():
    puzzle_string = f"""
    010.robot_crosswords
    6
    9 x . . 8 x
    . 7 . 6 x 1
    x 6 x . 6 .
    4 . 6 x . 2
    5 x 5 . . .
    x . . 7 . x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_011():
    puzzle_string = f"""
    011.robot_crosswords
    6
    x 9 . 6 . x
    . x 6 x 6 7
    . . . . x 6
    9 x 5 6 4 x
    6 7 x . . .
    x . 5 x 2 3
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_012():
    puzzle_string = f"""
    012.robot_crosswords
    6
    x 2 . . x 8
    4 x 5 . . .
    . . x . . 7
    . . 7 x 8 x
    x 9 x 4 . 6
    8 . . . x 7
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_013():
    puzzle_string = f"""
    013.robot_crosswords
    6
    x . . 4 3 x
    . . 4 x . 4
    6 x . . . x
    x . . 4 x 2
    2 1 x 3 . 4
    3 x 4 . 1 .
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_014():
    puzzle_string = f"""
    014.robot_crosswords
    6
    5 x 9 . . .
    . 3 x 7 x 5
    4 x 4 5 . .
    3 . 5 x 1 x
    x 2 x . . .
    2 . 4 x 2 3
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_015():
    puzzle_string = f"""
    015.robot_crosswords
    6
    2 _ x _ 5 x
    x _ _ 2 x 9
    6 5 x _ _ _
    9 x _ 3 x _
    _ _ _ x 4 x
    7 x _ 6 _ 4
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_031():
    puzzle_string = f"""
    031.robot_crosswords
    7
    . 4 x 2 . 3 x
    4 x . . 5 x 2
    . . 5 . x 4 .
    . 4 . x 2 3 x
    x . 2 . . x 2
    8 . x 6 x 2 3
    9 x 2 . . 3 x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_034():
    puzzle_string = f"""
    034.robot_crosswords
    7
    1 . . . x 1 x
    2 . 4 x . . 4
    x 4 x 2 . x 5
    6 . 4 x 2 . x
    5 x 5 4 x 1 .
    4 5 x . 3 . x
    x . 7 x . . .
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_035():
    puzzle_string = f"""
    035.robot_crosswords
    7
    x 2 x . 8 . 6
    5 . . . x 3 .
    . 4 . x 4 . 5
    . x . . . . x
    . 2 x 3 . x 3
    x . 5 x . . 2
    . . . 1 x 4 x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_036():
    puzzle_string = f"""
    036.robot_crosswords
    7
    1 . x . 3 x 2
    x . 4 . x 4 .
    5 . x 4 5 6 x
    4 x . . x . 6
    x 4 . x . . .
    . x 2 . 4 x 5
    1 . . x 2 4 3
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_071():
    puzzle_string = f"""
    071.robot_crosswords
    8
    7 5 . . . x 6 .
    . . . x 1 . 4 .
    x 4 x 4 . . . .
    9 x 5 . x 5 x 4
    . 5 x . . . 3 .
    . . 4 . . x 2 x
    7 x . x . . . 3
    x 2 . 5 4 3 x 4
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_101():
    puzzle_string = f"""
    101.robot_crosswords
    9
    4 1 . . . x 1 . 2
    3 . 2 x . . . . .
    . . x 5 6 . . x .
    x . 7 . . . x 2 x
    1 . . 4 x 1 . . .
    2 x . . 1 . x 4 .
    x 4 . x 2 x 1 x 1
    3 . . . x . . 6 .
    2 . x 5 3 . . x 5
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_141():
    puzzle_string = f"""
    141.robot_crosswords
    10
    1 . 3 . . x . 5 . 3
    x 5 x 5 x 4 . x . x
    5 . . . . x 1 . . .
    x 4 . . . . x 2 x 5
    9 x 9 . x . . . 7 x
    . 6 . x 2 . x 5 . 7
    . . 8 . x . . 4 x .
    5 . x 6 . x 6 x . 5
    . . . x . 7 x 2 . x
    x . 7 . 8 x . . . 3
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_171():
    puzzle_string = f"""
    171.robot_crosswords
    11
    1 x 8 . . x 6 7 x 2 x
    . 3 x 7 . 9 x . . . 7
    . . 4 x 6 . . x . . x
    x . . 4 . x . . . x 9
    . . . x . . x 2 . . .
    5 6 . . x . 4 . x . 6
    . x . . 3 . x . 5 x .
    . 2 x 7 . . . 6 x 6 7
    3 . 4 x 6 x 6 x 9 . x
    x . x 2 . . . 1 x . 8
    4 . . . x 5 4 x 8 7 x
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())


@pytest.mark.skip("skipped")
def test_robot_crosswords_186():
    puzzle_string = f"""
    186.robot_crosswords
    12
    9 x 2 . 5 . x 4 2 . . .
    . 8 . . x . 4 . x 6 . .
    . x . . . . x . 3 . . x
    x 2 . . 3 x 8 x 2 x . .
    4 . x . x . . . x . 1 .
    x . . x 4 . x . . 3 x 1
    . 3 . . x . . 3 . x . .
    1 x 6 . . x 4 x 4 . . x
    x . . . 5 . x 2 x 7 . .
    1 . x 6 x 1 . . . x . .
    . x 3 . . . x 3 . . 7 .
    x 1 . x 2 . . 1 x 6 x 7
    """
    assert default_test_puzzle(puzzle_string, RobotCrosswords, Solving.robot_crosswords_techniques())
