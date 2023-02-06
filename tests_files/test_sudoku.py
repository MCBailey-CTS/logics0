# from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# from techniques.LockedCandidatesPointing import LockedCandidatesPointing
import pytest

from _defaults import default_test_puzzle
from puzzles import Sudoku
from solving import Solving
from tech import tech
from techniques.AvoidableRectangleType1 import AvoidableRectangleType1
from techniques.Bug import Bug
from techniques.CrossHatch import CrossHatch
from techniques.HiddenSingle import HiddenSingle
from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
from techniques.LockedCandidatesPointing import LockedCandidatesPointing
from techniques.NakedPair import NakedPair
from techniques.ShashimiXWing import ShashimiXWing
from techniques.UniqueRectangleType1 import UniqueRectangleType1
from techniques.UniqueRectangleType4 import UniqueRectangleType4

EXPLICITLY = "EXPLICITLY"


@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_0():
    puzzle_string = f"""
    almost_locked_candidates_0.sudoku
    9
    .7.|...|198
    829|713|564
    614|985|237
    ---+---+---
    15.|.9.|.7.
    .96|357|..1
    ..7|..1|.59
    ---+---+---
    762|138|945
    ...|629|713
    931|574|...
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_1():
    puzzle_string = f"""
    almost_locked_candidates_1.sudoku
    9
    4 0 0 0 6 0 0 2 0
    8 6 7 4 2 5 3 9 1
    0 0 0 8 0 7 6 4 5
    7 0 0 2 0 0 0 8 6
    3 2 0 0 0 6 0 1 9
    6 9 0 0 0 4 2 0 0
    9 7 0 3 0 2 0 0 0
    5 0 3 0 0 8 9 0 2
    0 8 0 0 5 0 0 0 0
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_2():
    puzzle_string = f"""
    almost_locked_candidates_2.sudoku
    9
    .7.|..6|3..
    .5.|2..|.89
    ..1|...|2..
    ---+---+---
    4.8|..2|...
    ...|1.5|...
    ...|6..|8.1
    ---+---+---
    ..4|...|1..
    18.|..4|.5.
    ..3|8..|.7.
    shashimi xwing
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_3():
    puzzle_string = f"""
    almost_locked_candidates_3.sudoku
    9
    987|..2|.4.
    132|4..|.9.
    .4.|7.9|28.
    ---+---+---
    .98|...|175
    .1.|975|86.
    75.|..1|93.
    ---+---+---
    .69|12.|.5.
    .71|..3|629
    .2.|697|418
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_4():
    puzzle_string = f"""
    almost_locked_candidates_4.sudoku
    9
    ..9|..5|.43
    ...|...|...
    .5.|..3|.28
    ---+---+---
    .8.|.2.|.5.
    ..6|...|9..
    .9.|.4.|.3.
    ---+---+---
    32.|9..|.1.
    ...|...|...
    41.|5..|6..
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_5():
    puzzle_string = f"""
    almost_locked_candidates_5.sudoku
    9
    0 0 0 1 0 0 0 0 4
    2 0 7 0 0 0 0 0 5
    0 1 0 5 0 0 3 6 0
    0 0 5 9 1 0 0 0 6
    0 0 0 0 0 0 0 0 0
    8 0 0 0 2 6 9 0 0
    0 8 3 0 0 5 0 1 0
    5 0 0 0 0 0 7 0 2
    1 0 0 0 0 8 0 0 0
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_almost_locked_candidates_6():
    puzzle_string = f"""
    almost_locked_candidates_6.sudoku
    9
    2 6 1 0 0 8 9 0 5
    3 9 8 6 0 5 4 0 2
    4 5 7 0 9 0 8 0 6
    9 1 4 0 6 0 5 8 3
    8 2 5 0 0 0 6 9 7
    7 3 6 8 5 9 1 2 4
    6 7 2 5 8 1 3 4 9
    1 4 3 9 2 6 7 5 8
    5 8 9 3 0 0 2 6 1
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_00():
    puzzle_string = f"""
    avoidable_rectangle_type1_00.sudoku
    9
    _a _a 8a 0b 3b 0b 0c 4c 0c
    _a _a _a 1b 7b 6b 0c 0c 0c
    6a _a _a 0b 8b 0b 0c 0c 0c
    7d 9d 0d 0e 0e 0e 8f 0f 3f
    0d 0d 4d 0e 0e 0e 9f 0f 0f
    1d 0d 2d 0e 0e 0e 0f 5f 7f
    0g 0g 0g 0h 6h 0h 0i 0i 2i
    0g 0g 0g 5h 2h 9h 0i 0i 0i
    0g 8g 0g 0h 4h 0h 3i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_01():
    puzzle_string = f"""
    avoidable_rectangle_type1_01.sudoku
    9
    _a 9a 3a   2b _b _b   5c _c _c
    _a _a _a   _b _b 4b   9c _c _c
    4a _a _a   _b _b _b   _c 8c _c
    
    _d 4d 9d   3e _e _e   _f _f _f
    _d 7d _d   9e _e 1e   _f 5f _f
    _d _d _d   _e _e 7e   2f 3f _f
    
    _g 8g _g   _h _h _h   _i _i 6i
    _g _g 1g   8h _h _h   _i _i _i
    _g _g 2g   _h _h 5h   3i 1i _i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), NakedPair(),
                                UniqueRectangleType1(), ShashimiXWing(), AvoidableRectangleType1(),
                                LockedCandidatesClaiming()])


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_02():
    puzzle_string = f"""
    avoidable_rectangle_type1_02.sudoku
    9
    _a _a _a 8b 0b 0b 0c 0c 2c
    _a _a _a 0b 0b 6b 4c 0c 5c
    1a _a _a 2b 9b 4b 0c 0c 7c
    0d 0d 0d 0e 0e 0e 2f 0f 9f
    0d 5d 3d 0e 0e 0e 7f 8f 0f
    8d 0d 4d 0e 0e 0e 0f 0f 0f
    4g 0g 0g 3h 5h 7h 0i 0i 6i
    5g 0g 6g 9h 0h 0h 0i 0i 0i
    2g 0g 0g 0h 0h 8h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_03():
    puzzle_string = f"""
    avoidable_rectangle_type1_03.sudoku
    9
    _a _a _a 0b 7b 3b 0c 5c 0c
    2a _a _a 8b 0b 0b 0c 0c 3c
    _a _a _a 0b 2b 0b 0c 8c 0c
    0d 1d 5d 7e 0e 0e 0f 0f 6f
    3d 2d 0d 0e 0e 0e 0f 1f 8f
    8d 0d 0d 0e 0e 2e 9f 3f 0f
    0g 9g 0g 0h 1h 0h 0i 0i 0i
    1g 0g 0g 0h 0h 6h 0i 0i 9i
    0g 6g 0g 5h 4h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_04():
    puzzle_string = f"""
    avoidable_rectangle_type1_04.sudoku
    9
    6a _a _a 9b 0b 0b 5c 1c 4c
    5a 9a 1a 6b 4b 3b 8c 2c 7c
    7a 2a 4a 8b 5b 1b 9c 3c 6c
    8d 5d 2d 7e 6e 4e 1f 9f 3f
    4d 0d 9d 1e 0e 0e 7f 0f 5f
    1d 7d 0d 5e 0e 0e 4f 0f 2f
    2g 0g 0g 4h 0h 0h 3i 5i 8i
    3g 0g 0g 2h 0h 0h 6i 4i 9i
    9g 4g 0g 3h 8h 0h 2i 7i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_05():
    puzzle_string = f"""
    avoidable_rectangle_type1_05.sudoku
    9
    _a _a 6a 0b 2b 8b 0c 5c 0c
    _a 8a _a 0b 0b 0b 0c 0c 0c
    _a _a 1a 0b 0b 6b 7c 0c 9c
    8d 0d 0d 2e 9e 0e 4f 0f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 0d 7d 0e 6e 1e 0f 0f 5f
    6g 0g 4g 7h 0h 0h 1i 0i 0i
    0g 0g 0g 0h 0h 0h 0i 3i 0i
    0g 5g 0g 1h 4h 0h 9i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_07():
    puzzle_string = f"""
    avoidable_rectangle_type1_07.sudoku
    9
    4a _a _a 0b 0b 6b 0c 7c 0c
    1a 8a _a 0b 0b 0b 0c 0c 0c
    3a _a _a 0b 1b 0b 0c 8c 6c
    0d 0d 7d 6e 0e 0e 0f 0f 8f
    0d 6d 0d 0e 5e 0e 0f 9f 0f
    8d 0d 0d 0e 0e 9e 2f 0f 0f
    6g 1g 0g 0h 3h 0h 0i 0i 9i
    0g 0g 0g 0h 0h 0h 0i 2i 4i
    0g 4g 0g 7h 0h 0h 0i 0i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_08():
    puzzle_string = f"""
    avoidable_rectangle_type1_08.sudoku
    9
    _a _a 8a 2b 0b 4b 0c 0c 0c
    _a 2a _a 0b 1b 5b 0c 0c 0c
    _a 4a _a 0b 0b 0b 6c 5c 0c
    0d 0d 4d 7e 0e 0e 0f 0f 8f
    9d 0d 0d 0e 8e 0e 0f 0f 6f
    7d 0d 0d 0e 0e 2e 9f 0f 0f
    0g 1g 3g 0h 0h 0h 0i 7i 0i
    0g 0g 0g 1h 9h 0h 0i 4i 0i
    0g 0g 0g 8h 0h 7h 3i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_09():
    puzzle_string = f"""
    avoidable_rectangle_type1_09.sudoku
    9
    _a _a _a 0b 0b 4b 0c 0c 0c
    4a 7a 1a 0b 0b 0b 2c 9c 0c
    _a _a 9a 7b 0b 0b 1c 0c 8c
    0d 0d 0d 2e 0e 8e 0f 0f 9f
    0d 0d 0d 0e 6e 0e 0f 0f 0f
    3d 0d 0d 5e 0e 7e 0f 0f 0f
    7g 0g 5g 0h 0h 2h 4i 0i 0i
    0g 3g 6g 0h 0h 0h 8i 2i 7i
    0g 0g 0g 3h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_10():
    puzzle_string = f"""
    avoidable_rectangle_type1_10.sudoku
    9
    9a 7a 4a 0b 0b 5b 0c 0c 0c
    _a _a 8a 0b 0b 1b 2c 0c 0c
    _a _a _a 0b 0b 7b 4c 0c 0c
    0d 2d 0d 1e 0e 0e 0f 8f 0f
    0d 0d 0d 0e 8e 0e 0f 0f 0f
    0d 1d 0d 0e 0e 9e 0f 2f 0f
    0g 0g 7g 9h 0h 0h 0i 0i 0i
    0g 0g 6g 5h 0h 0h 3i 0i 0i
    0g 0g 0g 4h 0h 0h 7i 6i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_11():
    puzzle_string = f"""
    avoidable_rectangle_type1_11.sudoku
    9
    1a 4a 9a 0b 3b 0b 0c 0c 0c
    _a 2a _a 0b 0b 0b 1c 0c 0c
    _a 6a 7a 1b 0b 2b 0c 3c 0c
    0d 0d 0d 2e 0e 4e 0f 0f 0f
    0d 8d 0d 0e 0e 0e 0f 7f 0f
    0d 0d 0d 6e 0e 8e 0f 0f 0f
    0g 5g 0g 4h 0h 3h 8i 1i 0i
    0g 0g 4g 0h 0h 0h 0i 6i 0i
    0g 0g 0g 0h 1h 0h 4i 2i 7i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_12():
    puzzle_string = f"""
    avoidable_rectangle_type1_12.sudoku
    9
    _a _a 3a 0b 0b 4b 0c 7c 0c
    _a 4a 2a 0b 0b 0b 0c 0c 8c
    1a 6a _a 0b 8b 0b 0c 0c 0c
    2d 0d 6d 3e 0e 0e 0f 8f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 7d 0d 0e 0e 1e 2f 0f 9f
    0g 0g 0g 0h 1h 0h 0i 2i 3i
    9g 0g 0g 0h 0h 0h 4i 5i 0i
    0g 1g 0g 2h 0h 0h 7i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type1_13():
    puzzle_string = f"""
    avoidable_rectangle_type1_13.sudoku
    9
    _a 2a 5a 0b 7b 6b 0c 4c 0c
    7a 1a 9a 0b 0b 0b 8c 6c 0c
    _a 6a 4a 1b 0b 0b 2c 0c 7c
    0d 3d 8d 7e 0e 2e 0f 0f 6f
    0d 9d 6d 0e 8e 0e 7f 0f 0f
    5d 7d 2d 9e 6e 1e 4f 0f 0f
    9g 4g 3g 6h 1h 7h 5i 0i 0i
    6g 5g 1g 0h 0h 0h 3i 7i 4i
    2g 8g 7g 4h 3h 5h 6i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_avoidable_rectangle_type2_0():
    puzzle_string = f"""
    avoidable_rectangle_type2_0.sudoku
    9
    _a _a 5a 0b 0b 0b 6c 8c 3c
    _a 6a 4a 5b 3b 8b 9c 0c 2c
    8a 2a 3a 9b 6b 0b 0c 5c 0c
    2d 0d 0d 0e 0e 6e 5f 0f 0f
    3d 0d 0d 0e 0e 0e 0f 2f 6f
    6d 0d 1d 2e 0e 0e 0f 0f 9f
    4g 3g 2g 6h 5h 1h 7i 9i 8i
    0g 0g 7g 8h 0h 0h 3i 6i 5i
    5g 8g 6g 0h 0h 0h 2i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_finned_x_wing_02():
    puzzle_string = f"""
    finned_x_wing_02.sudoku
    9
    4a 2a 1a 8b 0b 9b 0c 7c 0c
    6a 5a _a 1b 2b 0b 9c 0c 0c
    3a 9a _a 0b 5b 0b 0c 0c 1c
    0d 8d 0d 0e 0e 1e 7f 0f 0f
    7d 4d 3d 0e 9e 0e 8f 1f 6f
    0d 1d 6d 7e 8e 0e 0f 5f 0f
    8g 3g 0g 9h 4h 0h 1i 6i 7i
    1g 6g 9g 0h 7h 8h 0i 4i 0i
    0g 7g 4g 3h 1h 6h 0i 9i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_finned_x_wing_03():
    puzzle_string = f"""
    finned_x_wing_03.sudoku
    9
    _a 7a 6a 0b 8b 9b 0c 0c 0c
    _a _a _a 0b 0b 3b 0c 8c 6c
    5a 8a 3a 0b 0b 4b 0c 0c 0c
    3d 0d 7d 8e 4e 0e 1f 0f 0f
    0d 2d 0d 0e 9e 0e 0f 4f 0f
    0d 0d 4d 0e 3e 0e 8f 0f 5f
    0g 0g 0g 9h 0h 0h 2i 3i 8i
    6g 0g 2g 3h 0h 8h 0i 0i 0i
    0g 3g 0g 4h 2h 0h 6i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_0():
    puzzle_string = f"""
    hidden_quad_0.sudoku
    9
    8a _a _a 1b 0b 9b 0c 4c 0c
    _a _a _a 0b 5b 0b 0c 6c 8c
    _a _a _a 7b 0b 0b 1c 9c 3c
    1d 0d 2d 0e 0e 0e 0f 5f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 7d 0d 0e 0e 0e 3f 0f 4f
    9g 1g 5g 0h 0h 3h 0i 0i 0i
    7g 2g 0g 0h 6h 0h 0i 0i 0i
    0g 8g 0g 5h 0h 1h 0i 0i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_1():
    puzzle_string = f"""
    hidden_quad_1.sudoku
    9
    3a 6a 4a 0b 0b 9b 0c 0c 0c
    5a _a _a 3b 0b 6b 1c 0c 0c
    8a _a 1a 0b 7b 0b 0c 0c 0c
    7d 0d 0d 0e 0e 0e 6f 2f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 4d 5d 0e 0e 0e 0f 0f 9f
    0g 0g 0g 0h 8h 0h 9i 0i 2i
    0g 0g 2g 6h 0h 7h 0i 0i 1i
    0g 0g 0g 4h 0h 0h 3i 7i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_2():
    puzzle_string = f"""
    hidden_quad_2.sudoku
    9
    _a _a _a 0b 0b 7b 0c 5c 0c
    _a _a _a 0b 0b 3b 0c 4c 0c
    _a _a _a 6b 4b 0b 0c 0c 8c
    0d 4d 1d 0e 0e 0e 2f 9f 0f
    6d 0d 3d 0e 9e 0e 1f 0f 5f
    0d 9d 2d 0e 0e 0e 6f 8f 0f
    3g 0g 0g 0h 1h 9h 0i 0i 0i
    0g 6g 0g 7h 0h 0h 0i 0i 0i
    0g 1g 0g 3h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_3():
    puzzle_string = f"""
    hidden_quad_3.sudoku
    9
    _a _a _a 6b 0b 0b 8c 0c 0c
    _a _a _a 0b 9b 1b 0c 4c 0c
    _a _a _a 3b 0b 0b 9c 0c 0c
    5d 0d 2d 0e 0e 0e 4f 0f 1f
    3d 1d 0d 0e 2e 0e 0f 8f 7f
    7d 0d 9d 0e 0e 0e 2f 0f 5f
    0g 0g 1g 0h 0h 6h 0i 0i 0i
    0g 3g 0g 2h 7h 0h 0i 0i 0i
    0g 0g 7g 0h 0h 3h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_4():
    puzzle_string = f"""
    hidden_quad_4.sudoku
    9
    3a 1a _a 4b 0b 9b 0c 0c 0c
    _a _a _a 1b 7b 5b 0c 0c 0c
    _a _a 7a 0b 3b 0b 0c 0c 0c
    0d 0d 9d 0e 0e 0e 0f 8f 7f
    0d 0d 1d 0e 9e 0e 4f 0f 0f
    8d 7d 0d 0e 0e 0e 3f 0f 0f
    0g 0g 0g 0h 6h 0h 2i 0i 0i
    0g 0g 0g 5h 1h 3h 0i 0i 0i
    0g 0g 0g 9h 0h 2h 0i 6i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_8():
    puzzle_string = f"""
    hidden_quad_8.sudoku
    9
    _a _a _a 5b 4b 1b 0c 9c 0c
    _a _a _a 7b 9b 3b 5c 0c 0c
    _a _a _a 2b 8b 6b 3c 0c 4c
    0d 4d 0d 1e 0e 8e 9f 0f 5f
    0d 6d 0d 9e 2e 5e 4f 3f 0f
    9d 0d 5d 3e 0e 4e 0f 2f 0f
    6g 3g 1g 8h 5h 2h 7i 4i 9i
    0g 0g 0g 4h 3h 7h 0i 0i 0i
    0g 8g 0g 6h 1h 9h 2i 5i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_9():
    puzzle_string = f"""
    hidden_quad_9.sudoku
    9
    2a 4a 7a 6b 3b 1b 9c 8c 5c
    8a 3a 6a 5b 4b 9b 1c 2c 7c
    5a 9a 1a 8b 2b 7b 4c 3c 6c
    6d 0d 0d 0e 0e 0e 3f 7f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 1d 9d 0e 0e 0e 0f 0f 8f
    9g 2g 3g 1h 8h 5h 7i 6i 4i
    1g 7g 5g 4h 6h 2h 8i 9i 3i
    4g 6g 8g 7h 9h 3h 5i 1i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_0():
    puzzle_string = f"""
    hidden_triple_0.sudoku
    9
    _a _a _a 5b 0b 0b 0c 7c 9c
    _a 1a _a 0b 0b 0b 0c 5c 4c
    _a _a 4a 0b 8b 0b 0c 0c 0c
    2d 0d 0d 9e 0e 3e 0f 0f 8f
    0d 0d 7d 0e 0e 0e 9f 0f 0f
    6d 0d 0d 2e 0e 7e 0f 0f 3f
    0g 0g 0g 0h 7h 0h 1i 0i 0i
    1g 6g 0g 0h 0h 0h 0i 8i 0i
    4g 7g 0g 0h 0h 5h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_2():
    puzzle_string = f"""
    hidden_triple_2.sudoku
    9
    _a 3a _a 0b 8b 0b 0c 1c 0c
    _a _a _a 0b 3b 0b 8c 0c 0c
    _a _a _a 6b 7b 0b 0c 3c 5c
    7d 9d 2d 1e 6e 3e 5f 8f 4f
    5d 4d 8d 2e 9e 7e 3f 6f 1f
    3d 0d 0d 5e 4e 8e 7f 0f 0f
    6g 0g 0g 0h 1h 4h 0i 0i 0i
    4g 0g 9g 0h 2h 6h 1i 0i 0i
    0g 7g 0g 0h 5h 9h 0i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_3():
    puzzle_string = f"""
    hidden_triple_3.sudoku
    9
    _a 9a _a 2b 3b 6b 0c 1c 0c
    5a _a _a 1b 7b 0b 3c 0c 9c
    _a _a _a 5b 9b 0b 2c 0c 0c
    0d 0d 0d 9e 4e 2e 7f 0f 0f
    2d 4d 9d 7e 8e 5e 6f 3f 1f
    8d 7d 5d 3e 6e 1e 0f 0f 0f
    0g 5g 7g 6h 2h 3h 0i 0i 0i
    6g 0g 0g 8h 5h 0h 0i 0i 3i
    0g 8g 0g 4h 1h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_4():
    puzzle_string = f"""
    hidden_triple_4.sudoku
    9
    _a _a _a 9b 0b 0b 7c 0c 0c
    _a 5a _a 6b 0b 3b 0c 4c 2c
    _a _a _a 0b 0b 0b 0c 0c 1c
    8d 3d 0d 0e 5e 0e 9f 2f 0f
    7d 0d 0d 0e 0e 0e 0f 0f 3f
    0d 2d 5d 0e 4e 0e 0f 8f 7f
    5g 0g 0g 0h 0h 0h 0i 0i 0i
    3g 6g 0g 8h 0h 7h 0i 1i 0i
    0g 0g 1g 0h 0h 4h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_5():
    puzzle_string = f"""
    hidden_triple_5.sudoku
    9
_a _a _a 0b 7b 0b 0c 0c 0c
9a _a _a 4b 2b 5b 1c 0c 0c
4a _a _a 0b 0b 3b 0c 2c 5c
0d 5d 0d 0e 0e 0e 7f 0f 8f
0d 6d 0d 0e 0e 0e 0f 3f 0f
8d 0d 3d 0e 0e 0e 0f 6f 0f
6g 1g 0g 7h 0h 0h 0i 0i 9i
0g 0g 5g 1h 8h 6h 0i 0i 7i
0g 0g 0g 0h 3h 0h 0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_6():
    puzzle_string = f"""
    hidden_triple_6.sudoku
    9
_a 9a _a 0b 0b 0b 0c 5c 4c
_a _a _a 0b 0b 5b 0c 6c 7c
_a _a 4a 0b 2b 0b 0c 0c 0c
3d 0d 0d 6e 0e 1e 0f 0f 8f
0d 0d 6d 0e 0e 0e 7f 0f 0f
1d 0d 9d 8e 0e 7e 6f 0f 2f
0g 0g 0g 0h 6h 0h 9i 0i 0i
4g 6g 0g 5h 0h 0h 0i 0i 0i
9g 3g 0g 0h 0h 0h 0i 2i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_naked_quad_0():
    puzzle_string = f"""
    naked_quad_0.sudoku
    9
    _a 7a 3a 6b 0b 4b 0c 0c 0c
    _a 4a 2a 0b 0b 1b 0c 0c 0c
    5a _a 9a 3b 0b 0b 0c 4c 0c
    3d 0d 7d 0e 0e 0e 8f 0f 0f
    0d 9d 0d 8e 0e 0e 0f 7f 0f
    0d 0d 6d 0e 0e 0e 3f 0f 4f
    0g 2g 0g 0h 0h 8h 1i 0i 6i
    0g 0g 0g 2h 0h 0h 4i 5i 0i
    0g 0g 0g 1h 0h 9h 7i 2i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_naked_quad_1():
    puzzle_string = f"""
    naked_quad_1.sudoku
    9
    5a _a _a 7b 0b 4b 2c 0c 0c
    _a 7a _a 1b 0b 0b 9c 0c 4c
    _a _a _a 8b 0b 0b 0c 0c 0c
    7d 0d 0d 0e 0e 0e 3f 0f 0f
    2d 0d 1d 0e 0e 0e 7f 0f 5f
    0d 0d 4d 0e 0e 0e 0f 0f 6f
    0g 0g 0g 0h 0h 6h 0i 0i 0i
    4g 0g 6g 0h 0h 8h 0i 1i 0i
    0g 0g 5g 9h 0h 1h 0i 0i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_naked_quad_2():
    puzzle_string = f"""
    naked_quad_2.sudoku
    9
    5a _a _a 1b 4b 0b 0c 7c 2c
    _a 7a _a 0b 0b 6b 0c 0c 5c
    _a _a _a 0b 5b 0b 0c 1c 6c
    0d 0d 0d 5e 0e 0e 0f 0f 0f
    8d 3d 0d 0e 0e 0e 0f 4f 7f
    0d 0d 0d 0e 0e 2e 0f 0f 0f
    6g 8g 0g 0h 0h 0h 0i 0i 0i
    7g 0g 0g 3h 0h 0h 0i 9i 0i
    7g 0g 0g 3h 0h 0h 0i 9i 0i
    9g 4g 0g 0h 8h 5h 0i 0i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_naked_quad_3():
    puzzle_string = f"""
    naked_quad_3.sudoku
    9
    9a _a _a 0b 3b 0b 6c 0c 0c
    _a _a _a 6b 0b 5b 0c 9c 3c
    _a 3a _a 9b 0b 7b 0c 0c 0c
    7d 6d 3d 0e 9e 8e 0f 0f 4f
    5d 4d 8d 7e 6e 0e 3f 0f 9f
    1d 9d 2d 0e 5e 0e 8f 7f 6f
    0g 0g 0g 8h 0h 0h 0i 0i 0i
    8g 2g 0g 5h 0h 0h 0i 0i 0i
    0g 0g 9g 0h 4h 0h 0i 0i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_wxyz_wing_1():
    puzzle_string = f"""
    wxyz_wing_1.sudoku
    9
_a 4a 1a 0b 0b 0b 0c 0c 0c
8a 7a _a 2b 4b 0b 0c 0c 0c
2a _a 6a 0b 0b 9b 0c 0c 0c
4d 0d 0d 7e 9e 5e 3f 0f 0f
0d 0d 0d 3e 0e 0e 0f 0f 0f
0d 0d 5d 6e 8e 4e 0f 0f 9f
0g 0g 4g 9h 0h 0h 1i 0i 2i
0g 0g 0g 1h 6h 3h 4i 5i 8i
0g 0g 0g 4h 0h 0h 9i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_wxyz_wing_2():
    puzzle_string = f"""
    wxyz_wing_2.sudoku
    9
_a 4a 1a 0b 0b 0b 0c 0c 0c
8a 7a _a 2b 4b 0b 0c 0c 0c
2a _a 6a 0b 0b 9b 0c 0c 0c
4d 0d 0d 7e 9e 5e 3f 0f 0f
0d 0d 0d 3e 0e 0e 0f 0f 0f
0d 0d 5d 6e 8e 4e 0f 0f 9f
0g 0g 4g 9h 0h 0h 1i 0i 2i
0g 0g 0g 1h 6h 3h 4i 5i 8i
0g 0g 0g 4h 0h 0h 9i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_wxyz_wing_3():
    puzzle_string = f"""
    wxyz_wing_3.sudoku
    9
_a 4a 1a 0b 0b 0b 0c 0c 0c
8a 7a _a 2b 4b 0b 0c 0c 0c
2a _a 6a 0b 0b 9b 0c 0c 0c
4d 0d 0d 7e 9e 5e 3f 0f 0f
0d 0d 0d 3e 0e 0e 0f 0f 0f
0d 0d 5d 6e 8e 4e 0f 0f 9f
0g 0g 4g 9h 0h 0h 1i 0i 2i
0g 0g 0g 1h 6h 3h 4i 5i 8i
0g 0g 0g 4h 0h 0h 9i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_wxyz_wing_7():
    puzzle_string = f"""
    wxyz_wing_7.sudoku
    9
3a 6a 7a 5b 9b 2b 1c 4c 8c
2a 5a 4a 8b 1b 0b 9c 0c 7c
9a 1a 8a 0b 0b 4b 0c 0c 0c
1d 9d 0d 0e 0e 0e 8f 0f 0f
4d 7d 0d 9e 0e 0e 0f 0f 1f
8d 3d 6d 0e 0e 0e 0f 7f 9f
5g 0g 9g 3h 0h 7h 6i 1i 0i
7g 0g 3g 0h 6h 0h 0i 9i 5i
6g 2g 1g 4h 5h 9h 7i 8i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_wxyz_wing_8():
    puzzle_string = f"""
    wxyz_wing_8.sudoku
    9
4a _a 7a 0b 0b 0b 0c 9c 8c
_a 6a 3a 8b 0b 4b 5c 7c 2c
5a _a 8a 0b 0b 0b 0c 1c 4c
8d 7d 1d 5e 3e 9e 2f 4f 6f
0d 0d 4d 2e 0e 1e 9f 0f 7f
2d 0d 0d 4e 7e 0e 1f 0f 3f
0g 8g 0g 0h 0h 0h 4i 0i 5i
0g 4g 0g 3h 0h 0h 7i 2i 1i
7g 0g 0g 0h 4h 0h 8i 0i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_wxyz_wing_9():
    puzzle_string = f"""
    wxyz_wing_9.sudoku
    9
_a _a _a 0b 0b 7b 5c 2c 0c
_a _a _a 0b 0b 0b 0c 9c 4c
_a _a _a 8b 0b 0b 1c 6c 7c
0d 0d 7d 9e 0e 6e 0f 8f 0f
0d 6d 0d 7e 0e 2e 0f 3f 0f
0d 5d 0d 4e 8e 3e 7f 1f 6f
1g 0g 3g 0h 0h 9h 6i 0i 0i
6g 4g 0g 0h 0h 0h 0i 0i 0i
0g 2g 5g 6h 0h 0h 0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_type_d_1():
    puzzle_string = f"""
    w_wing_type_d_1.sudoku
    9
7a _a _a 9b 0b 5b 2c 0c 0c
2a 5a 4a 0b 8b 7b 0c 9c 6c
9a _a _a 2b 0b 0b 0c 5c 7c
5d 7d 9d 0e 0e 3e 6f 0f 2f
8d 2d 0d 5e 9e 6e 0f 7f 0f
6d 4d 0d 7e 2e 0e 5f 0f 9f
0g 8g 7g 0h 0h 2h 9i 6i 5i
3g 9g 2g 6h 5h 0h 7i 0i 0i
0g 6g 5g 0h 7h 9h 0i 2i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_type_d_2():
    puzzle_string = f"""
    w_wing_type_d_2.sudoku
    9
4a _a 8a 1b 6b 0b 3c 2c 0c
_a _a 1a 0b 0b 0b 8c 4c 0c
_a _a 2a 8b 7b 4b 5c 1c 0c
6d 1d 4d 2e 9e 8e 7f 5f 3f
8d 0d 5d 0e 4e 1e 6f 9f 2f
0d 2d 9d 6e 5e 0e 4f 8f 1f
2g 8g 7g 5h 1h 0h 9i 0i 4i
5g 4g 6g 0h 0h 0h 1i 0i 8i
1g 9g 3g 4h 8h 0h 2i 0i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_type_d_3():
    puzzle_string = f"""
    w_wing_type_d_3.sudoku
    9
_a _a 8a 0b 2b 0b 0c 6c 0c
_a _a 6a 4b 1b 0b 0c 0c 2c
_a 5a _a 8b 0b 0b 0c 9c 0c
5d 0d 0d 0e 0e 0e 0f 0f 0f
9d 0d 7d 0e 0e 0e 3f 0f 6f
0d 0d 0d 0e 0e 0e 0f 0f 7f
0g 3g 0g 0h 0h 9h 0i 2i 0i
1g 0g 0g 0h 8h 2h 6i 0i 0i
0g 7g 0g 0h 6h 0h 1i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_type_d_4():
    puzzle_string = f"""
    w_wing_type_d_4.sudoku
    9
_a 5a _a 0b 0b 0b 9c 3c 0c
9a _a 1a 0b 8b 0b 0c 0c 0c
6a _a 3a 0b 9b 4b 8c 1c 5c
0d 1d 6d 0e 5e 0e 3f 7f 2f
7d 0d 9d 0e 0e 0e 5f 0f 1f
5d 3d 0d 0e 0e 0e 0f 9f 0f
1g 9g 7g 6h 3h 0h 0i 5i 0i
3g 6g 5g 0h 4h 0h 7i 0i 9i
2g 8g 4g 0h 7h 0h 1i 6i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_type_d_5():
    puzzle_string = f"""
    w_wing_type_d_5.sudoku
    9
7a 5a 2a 3b 0b 0b 4c 1c 0c
8a _a _a 0b 0b 9b 0c 0c 0c
_a _a _a 0b 4b 0b 0c 0c 0c
0d 6d 0d 0e 0e 0e 0f 0f 0f
0d 9d 0d 6e 8e 3e 0f 5f 0f
0d 0d 0d 0e 0e 0e 0f 8f 0f
0g 0g 0g 0h 1h 0h 0i 0i 0i
0g 0g 0g 4h 0h 0h 0i 0i 8i
0g 3g 1g 0h 0h 5h 2i 6i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_0():
    puzzle_string = f"""
    xyz_wing_0.sudoku
    9
_a _a _a 0b 0b 3b 4c 0c 5c
_a 9a 6a 0b 0b 0b 7c 8c 0c
_a _a _a 0b 0b 0b 0c 2c 0c
0d 1d 0d 0e 8e 9e 6f 0f 0f
0d 0d 0d 4e 0e 5e 0f 0f 0f
0d 0d 5d 1e 2e 0e 0f 4f 0f
0g 3g 0g 0h 0h 0h 0i 0i 0i
0g 4g 9g 0h 0h 0h 3i 1i 0i
2g 0g 7g 6h 0h 0h 0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_1():
    puzzle_string = f"""
    xyz_wing_1.sudoku
    9
9a 3a _a 0b 0b 8b 0c 0c 0c
_a _a _a 3b 0b 0b 0c 8c 5c
6a _a _a 0b 1b 0b 0c 9c 4c
0d 5d 0d 0e 0e 0e 0f 1f 9f
0d 0d 6d 0e 0e 0e 4f 0f 0f
1d 7d 0d 0e 0e 0e 0f 2f 0f
7g 6g 0g 0h 9h 0h 0i 0i 1i
5g 8g 0g 0h 0h 3h 0i 0i 0i
0g 0g 0g 1h 0h 0h 0i 3i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_2():
    puzzle_string = f"""
    xyz_wing_2.sudoku
    9
9a 3a _a 0b 0b 8b 0c 0c 0c
_a _a _a 3b 0b 0b 0c 8c 5c
6a _a _a 0b 1b 0b 0c 9c 4c
0d 5d 0d 0e 0e 0e 0f 1f 9f
0d 0d 6d 0e 0e 0e 4f 0f 0f
1d 7d 0d 0e 0e 0e 0f 2f 0f
7g 6g 0g 0h 9h 0h 0i 0i 1i
5g 8g 0g 0h 0h 3h 0i 0i 0i
0g 0g 0g 1h 0h 0h 0i 3i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_3():
    puzzle_string = f"""
    xyz_wing_3.sudoku
    9
9a 3a _a 0b 0b 8b 0c 0c 0c
_a _a _a 3b 0b 0b 0c 8c 5c
6a _a _a 0b 1b 0b 0c 9c 4c
0d 5d 0d 0e 0e 0e 0f 1f 9f
0d 0d 6d 0e 0e 0e 4f 0f 0f
1d 7d 0d 0e 0e 0e 0f 2f 0f
7g 6g 0g 0h 9h 0h 0i 0i 1i
5g 8g 0g 0h 0h 3h 0i 0i 0i
0g 0g 0g 1h 0h 0h 0i 3i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_4():
    puzzle_string = f"""
    xyz_wing_4.sudoku
    9
8a _a 3a 7b 6b 0b 0c 2c 1c
1a 7a 2a 0b 0b 0b 0c 9c 6c
4a _a 6a 2b 1b 0b 0c 7c 8c
7d 3d 4d 8e 2e 5e 6f 1f 9f
6d 1d 5d 0e 0e 0e 8f 4f 2f
2d 8d 9d 6e 4e 1e 7f 5f 3f
5g 4g 0g 0h 0h 6h 2i 3i 7i
3g 2g 0g 0h 0h 0h 9i 6i 4i
9g 6g 7g 4h 3h 2h 1i 8i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_5():
    puzzle_string = f"""
    xyz_wing_5.sudoku
    9
    9
9a 7a _a 4b 0b 0b 0c 5c 0c
1a _a _a 0b 0b 0b 0c 0c 0c
_a 3a 8a 0b 0b 2b 0c 7c 0c
5d 0d 0d 2e 3e 0e 0f 0f 0f
0d 0d 0d 1e 0e 6e 0f 0f 0f
0d 0d 0d 0e 4e 7e 0f 0f 8f
0g 2g 0g 3h 0h 0h 1i 6i 0i
0g 0g 0g 0h 0h 0h 0i 0i 4i
0g 8g 0g 0h 0h 5h 0i 9i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_6():
    puzzle_string = f"""
    xyz_wing_6.sudoku
    9
7a 1a 3a 8b 9b 4b 5c 6c 2c
6a 9a 2a 3b 1b 5b 8c 4c 7c
_a _a 5a 7b 6b 2b 3c 1c 9c
0d 0d 8d 1e 5e 9e 0f 0f 0f
0d 0d 1d 4e 8e 7e 0f 0f 0f
0d 0d 9d 2e 3e 6e 1f 0f 8f
0g 0g 7g 6h 2h 1h 0i 0i 0i
1g 5g 4g 9h 7h 8h 6i 2i 3i
9g 2g 6g 5h 4h 3h 7i 8i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_7():
    puzzle_string = f"""
    xyz_wing_7.sudoku
    9
    9
_a 2a 9a 3b 5b 0b 1c 8c 6c
6a 5a 8a 0b 0b 0b 3c 0c 2c
_a _a 3a 2b 6b 8b 0c 9c 0c
8d 6d 5d 1e 4e 3e 0f 0f 0f
9d 7d 1d 8e 2e 5e 0f 0f 3f
0d 0d 2d 9e 7e 6e 8f 5f 1f
0g 8g 6g 0h 0h 0h 0i 0i 0i
2g 0g 7g 5h 8h 0h 0i 0i 4i
5g 9g 4g 6h 3h 2h 7i 1i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_8():
    puzzle_string = f"""
    xyz_wing_8.sudoku
    9
_a _a 6a 3b 5b 8b 0c 4c 0c
5a _a 8a 4b 2b 1b 0c 0c 3c
3a 4a 2a 9b 6b 7b 1c 5c 8c
8d 0d 9d 7e 0e 5e 0f 2f 0f
4d 5d 7d 2e 9e 6e 8f 3f 1f
2d 6d 0d 8e 0e 4e 0f 0f 5f
0g 2g 0g 6h 0h 3h 5i 0i 0i
6g 0g 5g 1h 0h 2h 0i 0i 7i
0g 8g 0g 5h 0h 9h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_9():
    puzzle_string = f"""
    xyz_wing_9.sudoku
    9
5a 4a 3a 8b 6b 1b 7c 9c 2c
7a 9a 2a 5b 3b 4b 0c 8c 0c
8a 1a 6a 9b 7b 2b 0c 0c 4c
9d 2d 1d 0e 0e 0e 8f 7f 3f
4d 5d 8d 7e 2e 3e 0f 6f 0f
6d 3d 7d 1e 9e 8e 4f 2f 5f
1g 0g 9g 3h 0h 0h 2i 0i 7i
3g 0g 4g 2h 0h 7h 0i 1i 0i
2g 7g 5g 0h 1h 9h 0i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_01():
    puzzle_string = f"""
    9
6a 9a _a 0b 7b 8b 5c 3c 2c
_a 7a 3a 9b 2b 0b 6c 8c 4c
2a 8a _a 0b 0b 0b 7c 1c 9c
8d 0d 0d 0e 3e 0e 9f 0f 7f
4d 3d 0d 7e 6e 9e 0f 5f 8f
9d 0d 7d 0e 8e 0e 0f 0f 3f
0g 4g 9g 8h 0h 0h 3i 2i 6i
0g 0g 0g 0h 0h 0h 8i 9i 5i
0g 0g 8g 2h 9h 0h 4i 7i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_02():
    puzzle_string = f"""
    xy_wing_02.sudoku
    9
3a 1a 4a 9b 2b 5b 8c 7c 6c
_a 9a 7a 1b 8b 6b 0c 0c 0c
6a 8a _a 4b 7b 3b 0c 0c 1c
8d 5d 6d 7e 3e 2e 0f 0f 9f
0d 3d 9d 5e 4e 0e 7f 6f 0f
4d 7d 0d 6e 9e 0e 5f 0f 3f
7g 6g 0g 2h 1h 4h 0i 0i 0i
0g 4g 0g 8h 6h 9h 0i 0i 7i
9g 2g 0g 3h 5h 7h 6i 0i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_03():
    puzzle_string = f"""
    xy_wing_03.sudoku
    9
3a 1a 4a 9b 2b 5b 8c 7c 6c
_a 9a 7a 1b 8b 6b 0c 0c 0c
6a 8a _a 4b 7b 3b 0c 0c 1c
8d 5d 6d 7e 3e 2e 0f 0f 9f
0d 3d 9d 5e 4e 0e 7f 6f 0f
4d 7d 0d 6e 9e 0e 5f 0f 3f
7g 6g 0g 2h 1h 4h 0i 0i 0i
0g 4g 0g 8h 6h 9h 0i 0i 7i
9g 2g 0g 3h 5h 7h 6i 0i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_04():
    puzzle_string = f"""
    xy_wing_04.sudoku
    9
_a 6a 3a 0b 4b 5b 2c 8c 0c
_a _a _a 0b 0b 3b 6c 7c 4c
4a _a _a 0b 0b 6b 0c 5c 3c
8d 4d 0d 0e 0e 0e 7f 0f 6f
0d 3d 1d 4e 6e 7e 8f 0f 0f
9d 7d 6d 0e 0e 0e 0f 0f 0f
6g 5g 0g 0h 0h 0h 0i 0i 2i
0g 1g 0g 6h 0h 0h 5i 0i 8i
3g 9g 8g 5h 2h 0h 0i 6i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_05():
    puzzle_string = f"""
    xy_wing_05.sudoku
    9
_a _a 6a 0b 8b 0b 1c 0c 7c
_a _a 8a 0b 0b 0b 9c 0c 5c
7a _a 5a 3b 0b 2b 6c 8c 4c
3d 7d 9d 0e 0e 4e 2f 5f 8f
5d 6d 1d 8e 2e 3e 4f 7f 9f
8d 4d 2d 9e 0e 0e 3f 6f 1f
0g 2g 3g 0h 0h 8h 7i 4i 6i
6g 8g 4g 0h 3h 0h 5i 0i 2i
0g 5g 7g 2h 4h 6h 8i 0i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_06():
    puzzle_string = f"""
    xy_wing_06.sudoku
    9
3a _a 1a 8b 0b 0b 7c 5c 2c
_a _a _a 0b 0b 1b 6c 8c 9c
_a 8a _a 7b 0b 0b 3c 1c 4c
0d 0d 0d 0e 0e 8e 5f 0f 1f
1d 0d 0d 5e 2e 0e 8f 0f 3f
8d 5d 3d 9e 1e 7e 4f 2f 6f
7g 4g 8g 1h 9h 3h 2i 6i 5i
2g 3g 9g 6h 8h 5h 1i 4i 7i
6g 1g 5g 0h 7h 0h 9i 3i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_07():
    puzzle_string = f"""
    xy_wing_07.sudoku
    9
6a 2a 1a 3b 7b 9b 5c 4c 8c
9a 4a 5a 1b 8b 2b 6c 3c 7c
7a 3a 8a 0b 5b 0b 2c 9c 1c
1d 0d 9d 8e 0e 0e 0f 0f 0f
8d 0d 3d 0e 6e 1e 9f 0f 0f
4d 6d 2d 5e 9e 7e 8f 1f 3f
5g 1g 6g 0h 0h 8h 3i 0i 9i
2g 8g 7g 9h 0h 0h 0i 0i 0i
3g 9g 4g 0h 0h 5h 0i 8i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_08():
    puzzle_string = f"""
    xy_wing_08.sudoku
    9
6a 8a 9a 7b 2b 1b 4c 5c 3c
1a 5a 2a 4b 8b 3b 9c 6c 7c
_a 7a _a 9b 6b 5b 0c 8c 0c
0d 4d 0d 8e 3e 0e 0f 7f 5f
7d 0d 0d 0e 4e 0e 3f 0f 8f
0d 3d 0d 0e 7e 2e 0f 0f 4f
0g 0g 0g 6h 5h 8h 7i 4i 9i
5g 9g 7g 2h 1h 4h 8i 3i 6i
0g 6g 0g 3h 9h 7h 5i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_09():
    puzzle_string = f"""
    xy_wing_09.sudoku
    9
    1a 9a 3a 6b 0b 0b 7c 0c 8c
    4a 2a 8a 1b 7b 0b 6c 0c 0c
    7a 5a 6a 0b 0b 0b 0c 0c 0c
    0d 4d 7d 0e 3e 0e 0f 6f 0f
    5d 6d 0d 4e 9e 7e 0f 8f 3f
    0d 3d 0d 0e 6e 0e 4f 7f 0f
    6g 8g 9g 7h 1h 0h 3i 0i 4i
    3g 1g 5g 0h 4h 6h 0i 9i 7i
    2g 7g 4g 0h 0h 0h 0i 1i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_10():
    puzzle_string = f"""
    xy_wing_10.sudoku
    9
_a 6a _a 4b 0b 1b 0c 8c 0c
9a 8a 4a 5b 7b 6b 2c 3c 1c
1a _a _a 0b 0b 9b 6c 7c 4c
6d 0d 2d 0e 0e 3e 4f 0f 7f
3d 4d 1d 7e 9e 0e 8f 6f 0f
8d 7d 0d 6e 4e 0e 1f 0f 3f
4g 0g 8g 0h 0h 7h 0i 0i 6i
5g 3g 0g 2h 6h 4h 0i 1i 8i
0g 1g 6g 0h 0h 8h 0i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xy_wing_11():
    puzzle_string = f"""
    xy_wing_11.sudoku
    9
9a 3a 2a 0b 1b 0b 6c 7c 5c
6a 5a 4a 3b 2b 7b 9c 8c 1c
1a 8a 7a 6b 9b 5b 2c 3c 4c
7d 0d 6d 9e 0e 0e 0f 0f 0f
3d 0d 9d 0e 4e 6e 0f 0f 7f
5d 4d 8d 1e 7e 2e 3f 6f 9f
2g 9g 5g 7h 0h 0h 0i 0i 0i
8g 7g 3g 0h 0h 1h 0i 9i 0i
4g 6g 1g 0h 0h 9h 7i 0i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_x_wing_0():
    puzzle_string = f"""
    x_wing_0.sudoku
    9
    _a _a _a 0b 0b 0b 7c 0c 4c
    3a _a _a 0b 7b 0b 0c 0c 5c
    _a _a _a 0b 1b 8b 0c 0c 2c
    1d 5d 0d 9e 2e 0e 8f 0f 3f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    6d 0d 8d 0e 3e 1e 0f 4f 7f
    2g 0g 0g 8h 4h 0h 0i 0i 0i
    5g 0g 0g 0h 9h 0h 0i 0i 1i
    4g 0g 7g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_x_wing_1():
    puzzle_string = f"""
    x_wing_1.sudoku
    9
    8a 7a 9a _________b 5b _________b 4c _________c _________c
    2a 5a _________a 7b _________b 4b _________c 9c 8c
    _________a 1a 4a 9b 8b 2b 7c 5c _________c
    9d 4d 7d 5e _________e _________e _________f _________f _________f
    1d 8d 5d 6e 2e 7e 3f 4f 9f
    _________d _________d 2d 4e 9e 8e 5f 1f 7f
    4g 2g 1g 8h 7h _________h _________i _________i 5i
    7g 9g _________g 2h _________h 5h _________i _________i 4i
    5g _________g _________g _________h 4h _________h _________i 7i _________i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_x_wing_2():
    puzzle_string = f"""
    x_wing_2.sudoku
    9
9a 8a 7a 2b 5b 6b 1c 4c 3c
4a 3a 6a 8b 1b 7b 9c 2c 5c
5a 2a 1a 9b 3b 4b 0c 7c 0c
7d 5d 0d 6e 2e 1e 0f 9f 0f
0d 4d 9d 5e 7e 8e 0f 1f 0f
1d 6d 0d 4e 9e 3e 0f 5f 7f
0g 1g 0g 7h 8h 9h 5i 6i 0i
6g 9g 5g 3h 4h 2h 7i 8i 1i
8g 7g 0g 1h 6h 5h 0i 3i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_x_wing_3():
    puzzle_string = f"""
    x_wing_3.sudoku
    9
    5a _a 7a 9b 0b 0b 1c 0c 6c
    6a 3a 4a 1b 7b 5b 8c 9c 2c
    _a 1a 9a 0b 0b 0b 5c 0c 7c
    7d 9d 6d 2e 1e 3e 4f 5f 8f
    3d 4d 2d 5e 9e 8e 7f 6f 1f
    1d 5d 8d 6e 4e 7e 9f 2f 3f
    0g 0g 1g 0h 5h 0h 3i 7i 9i
    9g 7g 5g 3h 2h 1h 6i 8i 4i
    4g 0g 3g 7h 0h 9h 2i 1i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type1_south_east_in_rows():
    puzzle_string = f"""
        unique_rectangle_type1_south_east_in_rows.sudoku
        9
        6a 7a 2a 5b 9b 3b 1c 4c 8c
1a 3a 8a 0b 0b 4b 5c 7c 9c
4a 9a 5a 1b 7b 8b 3c 2c 6c
9d 2d 0d 0e 5e 1e 8f 3f 0f
3d 1d 0d 8e 0e 9e 0f 5f 0f
5d 8d 4d 7e 3e 2e 9f 6f 1f
0g 4g 1g 3h 0h 6h 7i 9i 5i
0g 5g 3g 9h 0h 7h 6i 1i 0i
7g 6g 9g 0h 1h 5h 0i 8i 3i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type1_south_west_in_cols():
    puzzle_string = f"""
        unique_rectangle_type1_south_west_in_cols.sudoku
        9
2a 6a _a 9b 3b 0b 0c 0c 0c
_a 8a 3a 6b 4b 0b 0c 0c 2c
4a 9a 7a 5b 2b 8b 6c 3c 1c
7d 4d 6d 2e 8e 9e 3f 1f 5f
8d 5d 9d 3e 1e 6e 2f 4f 7f
0d 0d 2d 7e 5e 4e 8f 6f 9f
6g 2g 8g 4h 9h 5h 1i 7i 3i
9g 7g 0g 0h 6h 3h 5i 2i 0i
0g 0g 0g 0h 7h 2h 0i 0i 6i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type1_north_east_in_cols():
    puzzle_string = f"""
        unique_rectangle_type1_north_east_in_cols.sudoku
        9
9a 1a 2a 5b 4b 8b 7c 3c 6c
5a 4a _a 1b 7b 0b 8c 9c 2c
8a 7a _a 0b 9b 2b 1c 5c 4c
0d 6d 4d 0e 1e 0e 5f 8f 0f
0d 5d 9d 4e 8e 0e 6f 2f 0f
0d 3d 8d 0e 0e 0e 4f 7f 0f
6g 9g 7g 8h 2h 4h 3i 1i 5i
4g 8g 5g 9h 3h 1h 2i 6i 7i
3g 2g 1g 7h 0h 0h 9i 4i 8i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type1_south_east_in_cols():
    puzzle_string = f"""
        unique_rectangle_type1_south_east_in_cols.sudoku
        9
8a 3a 7a 4b 0b 0b 5c 6c 1c
_a _a 9a 5b 3b 6b 2c 7c 8c
5a 2a 6a 1b 7b 8b 9c 0c 0c
2d 0d 8d 9e 4e 3e 0f 1f 5f
3d 0d 5d 8e 6e 1e 0f 2f 9f
0d 9d 1d 2e 5e 7e 8f 0f 0f
0g 0g 4g 7h 0h 5h 3i 8i 0i
7g 5g 3g 6h 8h 0h 1i 9i 0i
0g 8g 2g 3h 0h 0h 0i 5i 7i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type1_north_west_in_rows():
    puzzle_string = f"""
        unique_rectangle_type1_north_west_in_rows.sudoku
        9
9a 1a 2a 0b 0b 0b 6c 0c 8c
8a 4a 6a 9b 0b 2b 0c 0c 5c
3a 7a 5a 8b 6b 1b 9c 4c 2c
6d 5d 9d 7e 8e 4e 3f 2f 1f
1d 8d 3d 5e 2e 9e 4f 6f 7f
4d 2d 7d 6e 1e 3e 5f 8f 9f
2g 6g 8g 0h 0h 0h 0i 0i 3i
5g 0g 4g 0h 0h 8h 2i 0i 6i
7g 0g 1g 2h 0h 6h 8i 5i 4i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type1_north_east_in_rows():
    puzzle_string = f"""
        unique_rectangle_type1_north_east_in_rows.sudoku
        9
2a 3a 7a 6b 5b 9b 8c 4c 1c
8a 9a 6a 3b 0b 0b 7c 2c 5c
5a 4a 1a 8b 2b 7b 9c 6c 3c
6d 7d 3d 1e 8e 5e 2f 9f 4f
9d 8d 0d 2e 0e 6e 0f 0f 7f
1d 2d 0d 9e 7e 0e 6f 0f 8f
4g 5g 2g 7h 9h 0h 0i 8i 6i
7g 0g 8g 5h 0h 2h 4i 0i 9i
3g 0g 9g 4h 0h 8h 5i 7i 2i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type1_north_west_in_cols():
    puzzle_string = f"""
        unique_rectangle_type1_north_west_in_cols.sudoku
        9
_a 9a 7a 2b 0b 0b 0c 3c 0c
_a 3a 4a 0b 0b 7b 0c 2c 0c
2a 5a 8a 0b 6b 0b 0c 1c 7c
7d 2d 5d 0e 0e 0e 3f 6f 9f
4d 1d 6d 0e 7e 0e 2f 5f 8f
3d 8d 9d 5e 2e 6e 7f 4f 1f
9g 4g 1g 7h 3h 5h 6i 8i 2i
5g 6g 3g 8h 9h 2h 1i 7i 4i
8g 7g 2g 6h 1h 4h 5i 9i 3i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type1_south_west_in_rows():
    puzzle_string = f"""   
        unique_rectangle_type1_south_west_in_rows.sudoku
        9
4a _a 3a 7b 0b 0b 0c 0c 5c
8a _a 2a 5b 0b 0b 0c 0c 3c
9a 5a 7a 0b 3b 6b 0c 4c 1c
1d 4d 5d 3e 2e 0e 6f 8f 0f
3d 2d 6d 0e 0e 0e 4f 5f 0f
7d 9d 8d 4e 6e 5e 3f 1f 2f
6g 3g 0g 0h 5h 0h 1i 0i 8i
5g 8g 0g 0h 0h 3h 0i 0i 6i
2g 7g 0g 6h 0h 8h 5i 3i 4i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type2_east():
    puzzle_string = f"""
        unique_rectangle_type2_east.sudoku
        9
7a 2a 3a 0b 5b 4b 9c 8c 0c
_a 8a 4a 0b 9b 2b 0c 0c 3c
_a 9a 1a 8b 0b 3b 0c 2c 4c
3d 4d 5d 0e 1e 8e 0f 9f 2f
8d 0d 6d 3e 2e 9e 4f 0f 5f
9d 0d 2d 4e 0e 5e 8f 3f 0f
2g 3g 7g 9h 4h 6h 1i 5i 8i
4g 5g 9g 2h 8h 1h 3i 6i 7i
1g 6g 8g 5h 3h 7h 2i 4i 9i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type2_south():
    puzzle_string = f"""
        unique_rectangle_type2_south.sudoku
        9
_a 8a _a 0b 3b 0b 2c 7c 4c
_a 4a 2a 0b 0b 7b 0c 5c 3c
3a 7a _a 0b 2b 0b 9c 1c 0c
4d 1d 3d 7e 9e 8e 5f 6f 2f
6d 5d 7d 0e 4e 0e 3f 8f 9f
2d 9d 8d 6e 5e 3e 7f 4f 1f
8g 6g 9g 0h 7h 0h 0i 3i 5i
7g 2g 4g 3h 0h 5h 0i 9i 0i
5g 3g 1g 0h 8h 0h 0i 2i 7i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type2_west():
    puzzle_string = f"""
        unique_rectangle_type2_west.sudoku
        9
2a _a _a 6b 0b 1b 3c 5c 7c
1a 5a 6a 7b 2b 3b 9c 8c 4c
_a 7a 3a 9b 5b 0b 2c 6c 1c
9d 3d 2d 4e 6e 5e 7f 1f 8f
5d 4d 8d 1e 7e 9e 6f 3f 2f
7d 6d 1d 8e 3e 2e 4f 9f 5f
3g 0g 5g 2h 0h 0h 0i 0i 6i
0g 0g 7g 3h 0h 6h 5i 2i 9i
6g 2g 0g 5h 0h 0h 0i 0i 3i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type4_south_rows():
    puzzle_string = f"""
        unique_rectangle_type4_south_rows.sudoku
        9
        3a _a 5a 8b 2b _b 1c 7c 9c
        _a _a _a _b 1b _b 4c _c 6c
        _a _a 1a _b 9b _b 2c _c _c
        5d 1d 6d 4e 8e 9e 7f 2f 3f
        7d 8d 4d _e 3e _e 6f 9f 1f
        2d 9d 3d 6e 7e 1e 8f _f _f
        _g 5g _g _h 6h _h 3i _i 7i
        1g _g 7g _h 5h _h 9i 6i _i
        6g 3g _g _h 4h _h 5i _i 2i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type4_south_cols():
    puzzle_string = f"""
        unique_rectangle_type4_south_cols.sudoku
        9
_a 6a _a 8b 2b 5b 7c 1c 9c
7a _a _a 4b 1b 6b 3c 5c 0c
_a 5a _a 3b 7b 9b 6c 0c 4c
5d 1d 7d 6e 0e 0e 0f 3f 0f
0d 0d 0d 7e 0e 0e 1f 0f 5f
0d 8d 0d 1e 5e 3e 0f 7f 6f
8g 3g 5g 0h 6h 1h 0i 4i 7i
0g 7g 0g 0h 4h 8h 5i 0i 3i
9g 4g 2g 5h 3h 7h 8i 6i 1i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_unique_rectangle_type4_east_rows():
    puzzle_string = f"""
        unique_rectangle_type4_east_rows.sudoku
        9
9a 4a 2a 0b 0b 3b 7c 1c 0c
8a 1a _a 2b 4b 0b 9c 5c 0c
5a 6a _a 0b 0b 1b 4c 2c 0c
2d 8d 6d 3e 0e 0e 0f 9f 4f
0d 7d 9d 0e 8e 2e 3f 6f 0f
0d 3d 5d 0e 0e 0e 8f 7f 2f
6g 5g 1g 7h 3h 4h 2i 8i 9i
7g 9g 4g 0h 2h 8h 6i 3i 0i
3g 2g 8g 6h 0h 0h 0i 4i 7i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_unique_rectangle_type4_west_rows():
    puzzle_string = f"""
        unique_rectangle_type4_west_rows.sudoku
        9        
        6a 9a 1a 0b 4b 8b 2c 7c 0c
_a _a 7a 0b 0b 0b 0c 9c 0c
_a _a _a 0b 9b 7b 0c 4c 0c
7d 8d 6d 9e 1e 2e 3f 5f 4f
9d 0d 0d 0e 3e 0e 7f 8f 1f
5d 1d 3d 7e 8e 4e 9f 2f 6f
1g 3g 0g 0h 0h 0h 8i 6i 7i
0g 7g 0g 0h 6h 0h 5i 1i 2i
2g 6g 5g 8h 7h 1h 4i 3i 9i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_unique_rectangle_type4_west_cols():
    puzzle_string = f"""
        unique_rectangle_type4_west_cols.sudoku
        9
6a 1a _a 5b 7b 4b 0c 0c 2c
2a _a 5a 1b 9b 8b 0c 0c 0c
_a 7a _a 6b 3b 2b 1c 0c 5c
0d 0d 0d 3e 0e 6e 0f 0f 9f
3d 5d 6d 9e 2e 7e 8f 1f 4f
0d 0d 0d 8e 0e 1e 0f 0f 0f
5g 8g 2g 7h 6h 9h 4i 3i 1i
0g 6g 0g 4h 8h 0h 0i 0i 7i
4g 0g 7g 2h 1h 0h 0i 6i 8i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_unique_rectangle_type4_east_cols():
    puzzle_string = f"""
        unique_rectangle_type4_east_cols.sudoku
        9
2a _a _a 0b 0b 0b 7c 9c 5c
_a 5a 7a 9b 0b 0b 6c 1c 4c
9a 1a 6a 7b 4b 5b 3c 8c 2c
7d 6d 1d 2e 8e 4e 5f 3f 9f
0d 0d 0d 5e 9e 1e 8f 6f 7f
5d 9d 8d 3e 7e 6e 2f 4f 1f
1g 3g 0g 8h 5h 7h 0i 2i 6i
0g 0g 5g 0h 0h 9h 0i 7i 3i
6g 7g 0g 4h 0h 0h 0i 5i 8i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_bug():
    puzzle_string = f"""
        bug.sudoku
        9
        4a 6a 5a 1b 3b 2b 9c 7c 8c
        _a _a _a 8b 6b 4b 3c 1c 5c
        1a 3a 8a 5b 9b 7b 4c 2c 6c
        6d 8d 0d 3e 4e 0e 0f 5f 0f
        5d 0d 3d 2e 7e 0e 6f 8f 4f
        0d 0d 4d 6e 5e 8e 0f 3f 0f
        8g 7g 1g 9h 2h 6h 5i 4i 3i
        2g 5g 9g 4h 1h 3h 8i 6i 7i
        3g 4g 6g 7h 8h 5h 2i 9i 1i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_row():
    puzzle_string = f"""
        hidden_triple_row.sudoku
        9
_a 3a 5a 7b 2b 1b 8c 4c 0c
7a _a _a 3b 4b 6b 2c 0c 5c
_a 4a 2a 8b 5b 9b 0c 3c 0c
0d 5d 6d 9e 0e 2e 3f 0f 4f
0d 0d 0d 0e 3e 0e 5f 0f 0f
3d 0d 4d 6e 0e 5e 1f 0f 0f
0g 9g 0g 0h 0h 0h 0i 5i 0i
5g 0g 1g 2h 9h 3h 4i 0i 8i
4g 0g 0g 5h 0h 8h 9i 0i 0i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_fence():
    puzzle_string = f"""
        hidden_quad_fence.sudoku
        9
6a 1a 7a 0b 8b 0b 5c 0c 0c
9a 8a 4a 5b 0b 6b 0c 0c 0c
5a 2a 3a 1b 9b 7b 6c 8c 4c
0d 0d 0d 0e 0e 0e 4f 5f 0f
1d 0d 6d 0e 0e 0e 2f 0f 8f
0d 4d 0d 0e 0e 0e 0f 0f 0f
2g 7g 0g 3h 0h 1h 8i 4i 0i
4g 0g 0g 9h 0h 8h 0i 2i 3i
0g 0g 0g 0h 4h 2h 0i 0i 5i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_col():
    puzzle_string = f"""
        hidden_triple_col.sudoku
        9
3a _a 5a 0b 0b 0b 0c 0c 0c
6a 1a 2a 8b 0b 4b 9c 3c 0c
_a 7a 8a 0b 3b 1b 6c 0c 0c
8d 2d 0d 0e 0e 9e 0f 0f 6f
1d 6d 0d 0e 0e 0e 0f 7f 0f
7d 5d 0d 4e 0e 0e 0f 0f 2f
0g 3g 7g 6h 0h 8h 0i 5i 0i
0g 8g 1g 3h 0h 2h 7i 6i 0i
0g 0g 6g 0h 0h 0h 8i 0i 3i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_triple_fence():
    puzzle_string = f"""
        hidden_triple_fence.sudoku
        9
_a _a 1a 0b 7b 6b 0c 0c 0c
_a 9a _a 0b 3b 1b 0c 4c 0c
8a _a 3a 4b 5b 9b 0c 0c 0c
3d 1d 8d 7e 9e 4e 0f 0f 0f
2d 5d 6d 3e 1e 8e 4f 7f 9f
0d 0d 0d 5e 6e 2e 0f 0f 8f
0g 0g 0g 0h 2h 3h 0i 0i 5i
0g 3g 0g 0h 8h 7h 0i 2i 4i
0g 0g 2g 9h 4h 5h 7i 0i 0i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_row():
    puzzle_string = f"""
        hidden_quad_row.sudoku
        9
_a _a _a 0b 0b 0b 0c 0c 0c
1a 6a _a 0b 9b 2b 0c 8c 3c
5a 9a _a 0b 6b 0b 0c 0c 7c
0d 3d 0d 0e 2e 1e 0f 0f 0f
0d 0d 0d 0e 0e 0e 0f 0f 0f
0d 0d 0d 4e 5e 0e 0f 2f 0f
7g 0g 0g 0h 3h 0h 0i 6i 4i
8g 4g 0g 6h 1h 5h 0i 7i 9i
0g 0g 0g 0h 0h 0h 0i 0i 0i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_hidden_quad_col():
    puzzle_string = f"""
        hidden_quad_col.sudoku
        9
7a 9a 6a 0b 0b 2b 8c 4c 3c
8a 1a 3a 0b 0b 9b 5c 2c 6c
5a 4a 2a 6b 0b 0b 9c 1c 7c
9d 8d 4d 0e 0e 0e 7f 6f 1f
3d 6d 1d 0e 0e 0e 4f 5f 2f
2d 7d 5d 0e 0e 0e 3f 9f 8f
4g 3g 8g 0h 0h 1h 6i 7i 5i
1g 5g 9g 8h 0h 0h 2i 3i 4i
6g 2g 7g 3h 0h 0h 1i 8i 9i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_x_wing_row():
    puzzle_string = f"""
        x_wing_row.sudoku
        9
_a 7a 9a 1b 0b 8b 2c 4c 0c
4a 5a _a 9b 2b 0b 0c 8c 0c
8a _a 2a 4b 0b 0b 0c 0c 0c
2d 4d 5d 3e 7e 1e 9f 6f 8f
7d 3d 6d 8e 4e 9e 1f 5f 2f
1d 9d 8d 5e 6e 2e 4f 3f 7f
9g 2g 4g 0h 8h 5h 0i 1i 3i
5g 0g 0g 0h 9h 3h 8i 2i 4i
0g 8g 0g 2h 1h 4h 5i 0i 0i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), tech.XWing()])


@pytest.mark.skip("skipped")
def test_sudoku_x_wing_col():
    puzzle_string = f"""
        x_wing_col.sudoku
        9
_a 9a 6a 0b 0b 5b 4c 2c 7c
7a _a 4a 2b 0b 6b 5c 1c 9c
2a 1a 5a 7b 4b 9b 6c 8c 3c
9d 4d 7d 5e 6e 1e 8f 3f 2f
5d 0d 0d 4e 0e 3e 0f 7f 6f
0d 6d 3d 0e 7e 2e 0f 5f 4f
0g 0g 0g 0h 5h 4h 7i 6i 8i
4g 5g 8g 6h 2h 7h 3i 9i 1i
6g 7g 0g 3h 0h 8h 2i 4i 5i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair(), Bug(), tech.XWing()])


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_row():
    puzzle_string = f"""
        w_wing_row.sudoku
        9
3a 1a 5a 4b 9b 8b 2c 6c 7c
8a _a _a 0b 0b 0b 4c 3c 1c
_a 7a _a 3b 1b 2b 9c 8c 5c
0d 8d 7d 2e 0e 3e 0f 1f 9f
9d 3d 0d 0e 8e 0e 0f 2f 0f
5d 0d 0d 0e 0e 9e 8f 0f 3f
7g 6g 0g 9h 2h 1h 3i 5i 0i
1g 5g 3g 8h 0h 0h 0i 9i 2i
2g 0g 0g 0h 3h 5h 1i 0i 0i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_col():
    puzzle_string = f"""
        w_wing_col.sudoku
        9
_a 4a 5a 0b 6b 9b 7c 3c 2c
_a 3a _a 0b 5b 0b 4c 8c 9c
_a _a 2a 3b 4b 0b 5c 1c 6c
4d 0d 0d 0e 7e 1e 3f 0f 5f
5d 2d 0d 6e 3e 4e 9f 7f 0f
0d 0d 3d 5e 9e 0e 0f 0f 4f
3g 6g 0g 0h 8h 5h 2i 4i 0i
0g 0g 4g 0h 2h 6h 0i 5i 3i
2g 5g 0g 4h 1h 3h 6i 9i 0i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_rows():
    puzzle_string = f"""
        xyz_wing_rows.sudoku
        9
9a 6a 1a 3b 5b 8b 2c 4c 7c
3a 7a 2a 0b 4b 1b 5c 0c 0c
4a 8a 5a 0b 7b 2b 0c 0c 0c
1d 3d 7d 2e 8e 5e 0f 0f 4f
2d 9d 8d 7e 6e 4e 1f 5f 3f
5d 4d 6d 1e 0e 0e 8f 7f 2f
0g 5g 9g 4h 0h 6h 0i 2i 0i
0g 1g 4g 5h 2h 0h 0i 0i 6i
6g 2g 3g 8h 0h 7h 4i 0i 5i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_xyz_wing_cols():
    puzzle_string = f"""
        xyz_wing_cols.sudoku
        9
1a 8a 2a 0b 0b 0b 9c 0c 7c
5a 9a _a 7b 8b 0b 2c 1c 3c
7a _a _a 9b 2b 1b 0c 5c 0c
8d 2d 1d 3e 4e 7e 0f 0f 0f
3d 6d 5d 1e 9e 8e 7f 0f 0f
9d 0d 0d 5e 6e 2e 3f 8f 1f
2g 1g 0g 0h 0h 0h 0i 0i 0i
4g 5g 8g 2h 7h 9h 1i 3i 6i
6g 0g 9g 8h 1h 0h 4i 0i 0i
        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_center_col():
    puzzle_string = f"""   
        w_wing_center_col.sudoku
        9
9a 8a 1a 0b 0b 5b 2c 3c 7c
5a 7a 3a 8b 1b 2b 4c 9c 6c
2a 4a 6a 0b 0b 9b 1c 8c 5c
6d 5d 7d 9e 2e 8e 3f 1f 4f
8d 3d 4d 1e 0e 0e 5f 2f 9f
1d 2d 9d 0e 5e 0e 7f 6f 8f
0g 6g 5g 2h 9h 0h 8i 4i 1i
0g 1g 2g 0h 8h 0h 9i 5i 3i
0g 9g 8g 5h 0h 1h 6i 7i 2i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_w_wing_left_col():
    puzzle_string = f"""   
        w_wing_left_col.sudoku
        9
2a _a 6a 3b 1b 0b 5c 7c 4c
_a _a 7a 0b 2b 4b 6c 1c 9c
4a _a _a 0b 6b 0b 2c 3c 8c
0d 2d 0d 9e 5e 0e 4f 6f 0f
7d 6d 0d 2e 4e 1e 3f 0f 5f
0d 0d 4d 0e 3e 6e 0f 2f 0f
0g 0g 2g 1h 7h 0h 0i 4i 6i
1g 4g 0g 6h 8h 0h 7i 0i 2i
6g 7g 0g 4h 9h 2h 1i 0i 3i

        """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_001_4x4():
    puzzle_string = f"""
    001_4x4.sudoku
    4
    1234a 1234a 1234c __3_c
    1234a 1___a 1234c ___4c
    ___4b _2__b __3_d 1___d
    1___b __3_b ___4d _2__d
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_bug_0():
    puzzle_string = f"""
    bug_0.sudoku
    9
    _a _a _a 9b 0b 8b 2c 0c 0c
    _a _a _a 0b 1b 0b 0c 7c 0c
    6a _a 2a 0b 0b 0b 4c 0c 0c
    0d 2d 0d 0e 0e 9e 8f 0f 0f
    0d 0d 1d 4e 0e 5e 3f 0f 0f
    0d 0d 6d 8e 0e 0e 0f 1f 0f
    0g 0g 9g 0h 0h 0h 1i 0i 8i
    0g 4g 0g 0h 8h 0h 0i 0i 0i
    0g 0g 3g 5h 0h 7h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_hidden_pair_0():
    puzzle_string = f"""
    hidden_pair_0.sudoku
    9
    6a 5a 1a 8b 9b 7b 4c 3c 2c
    9a _a 2a 0b 1b 3b 7c 0c 0c
    3a 7a _a 0b 2b 6b 1c 0c 9c
    7d 0d 5d 3e 4e 2e 9f 0f 1f
    1d 3d 0d 7e 6e 9e 0f 0f 0f
    2d 0d 9d 1e 8e 5e 3f 7f 0f
    5g 9g 3g 6h 7h 1h 0i 0i 0i
    4g 2g 7g 9h 5h 8h 6i 1i 3i
    8g 1g 6g 2h 3h 4h 5i 9i 7i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_hidden_single_0():
    puzzle_string = f"""
    hidden_single_0.sudoku
    9
    7a 4a 1a 0b 2b 0b 5c 3c 8c
    3a 6a 8a 0b 0b 1b 4c 9c 2c
    5a 9a 2a 4b 3b 8b 1c 6c 7c
    8d 7d 5d 0e 0e 3e 6f 2f 4f
    2d 1d 9d 0e 0e 4e 8f 5f 3f
    6d 3d 4d 2e 8e 5e 9f 7f 1f
    9g 8g 6g 3h 4h 2h 7i 1i 5i
    1g 5g 3g 8h 0h 0h 2i 4i 9i
    4g 2g 7g 0h 0h 0h 3i 8i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_hidden_single_1():
    puzzle_string = f"""
    hidden_single_1.sudoku
    9
    _a 4a _a 0b 0b 3b 0c 2c 6c
    1a _a _a 0b 0b 0b 0c 0c 0c
    _a 2a _a 0b 6b 7b 5c 0c 4c
    0d 0d 6d 0e 0e 1e 0f 0f 5f
    4d 1d 0d 0e 0e 0e 0f 7f 9f
    5d 0d 0d 7e 0e 0e 8f 0f 0f
    2g 0g 1g 3h 7h 0h 0i 5i 0i
    0g 0g 0g 0h 0h 0h 0i 0i 7i
    8g 7g 0g 4h 0h 0h 0i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_hidden_single_2():
    puzzle_string = f"""
    hidden_single_2.sudoku
    9
    2a _a 7a 0b 0b 0b 8c 9c 0c
    _a 9a _a 7b 4b 5b 3c 6c 2c
    _a _a 3a 9b 2b 8b 7c 0c 0c
    9d 0d 0d 3e 0e 4e 5f 0f 0f
    4d 0d 0d 5e 0e 2e 9f 0f 3f
    7d 3d 5d 0e 0e 9e 4f 2f 0f
    0g 0g 0g 4h 0h 0h 6i 0i 9i
    3g 7g 9g 2h 0h 6h 1i 4i 0i
    6g 1g 4g 0h 9h 0h 2i 0i 7i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_locked_candidates_claiming_0():
    puzzle_string = f"""
    locked_candidates_claiming_0.sudoku
    9
    _a _a _a 9b 0b 0b 0c 0c 4c
    4a _a 6a 0b 0b 8b 7c 0c 3c
    _a _a _a 0b 0b 0b 0c 2c 0c
    0d 8d 9d 1e 0e 0e 0f 0f 0f
    6d 0d 7d 0e 0e 0e 9f 0f 5f
    0d 0d 0d 0e 0e 9e 8f 3f 0f
    0g 6g 0g 0h 0h 0h 0i 0i 0i
    3g 0g 2g 5h 0h 0h 1i 0i 7i
    1g 0g 0g 0h 0h 3h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()])


def test_sudoku_locked_candidates_claiming_1():
    puzzle_string = f"""
    locked_candidates_claiming_1.sudoku
    9
    _a _a _a 0b 0b 0b 3c 0c 4c
    8a 5a _a 6b 0b 0b 0c 0c 0c
    _a _a _a 1b 2b 0b 0c 6c 9c
    0d 0d 8d 0e 0e 0e 2f 7f 0f
    9d 0d 0d 0e 0e 0e 0f 0f 6f
    0d 6d 2d 0e 0e 0e 4f 0f 0f
    1g 9g 0g 0h 7h 3h 0i 0i 0i
    0g 0g 0g 0h 0h 2h 0i 1i 3i
    3g 0g 5g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()])


def test_sudoku_locked_candidates_claiming_2():
    puzzle_string = f"""
    locked_candidates_claiming_2.sudoku
    9
    _a 8a _a 0b 0b 2b 0c 0c 0c
    2a _a _a 0b 6b 0b 8c 3c 0c
    _a _a _a 7b 0b 3b 0c 0c 0c
    4d 0d 0d 0e 0e 7e 6f 1f 0f
    0d 0d 8d 0e 0e 0e 9f 0f 0f
    0d 1d 6d 4e 0e 0e 0f 0f 2f
    0g 0g 0g 6h 0h 4h 0i 0i 0i
    0g 4g 7g 0h 9h 0h 0i 0i 1i
    0g 0g 0g 5h 0h 0h 0i 2i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()])


def test_sudoku_locked_candidates_pointing_0():
    puzzle_string = f"""
    locked_candidates_pointing_0.sudoku
    9
    _a 3a _a 0b 0b 0b 0c 6c 0c
    _a _a _a 0b 0b 3b 9c 0c 0c
    _a 4a 2a 6b 0b 0b 0c 8c 0c
    0d 0d 0d 0e 3e 2e 8f 0f 0f
    0d 7d 0d 4e 0e 6e 0f 5f 0f
    0d 0d 5d 1e 7e 0e 0f 0f 0f
    0g 9g 0g 0h 0h 8h 2i 4i 0i
    0g 0g 6g 2h 0h 0h 0i 0i 0i
    0g 8g 0g 0h 0h 0h 0i 9i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesPointing()])


def test_sudoku_naked_pair_0():
    puzzle_string = f"""
    naked_pair_0.sudoku
    9
    _a 1a 9a 3b 0b 8b 0c 0c 0c
    _a 2a 6a 9b 0b 7b 3c 8c 0c
    8a 3a 7a 0b 0b 5b 0c 0c 0c
    6d 7d 2d 5e 0e 9e 8f 4f 0f
    0d 5d 8d 0e 0e 6e 0f 0f 0f
    0d 4d 1d 8e 0e 2e 5f 0f 6f
    1g 8g 3g 6h 9h 4h 7i 5i 2i
    7g 9g 4g 2h 5h 3h 1i 6i 8i
    2g 6g 5g 7h 8h 1h 4i 3i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair()])


def test_sudoku_naked_pair_1():
    puzzle_string = f"""
    naked_pair_1.sudoku
    9
    6a 1a _a 8b 5b 3b 0c 0c 9c
    9a _a 8a 0b 4b 0b 6c 3c 5c
    5a _a _a 9b 0b 6b 0c 1c 8c
    3d 8d 9d 0e 0e 4e 1f 0f 6f
    2d 6d 1d 0e 3e 8e 0f 9f 4f
    7d 4d 5d 6e 0e 0e 3f 8f 2f
    8g 5g 0g 4h 0h 2h 9i 6i 0i
    4g 0g 0g 0h 0h 0h 0i 0i 0i
    1g 0g 0g 3h 0h 5h 0i 0i 7i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair()])


def test_sudoku_naked_pair_2():
    puzzle_string = f"""
    naked_pair_2.sudoku
    9
    _a _a 1a 2b 0b 9b 0c 7c 0c
    6a _a _a 4b 5b 7b 8c 3c 1c
    _a _a 7a 8b 1b 0b 9c 2c 0c
    2d 0d 5d 7e 0e 0e 1f 0f 8f
    0d 0d 0d 0e 2e 0e 0f 5f 3f
    3d 0d 4d 0e 8e 5e 7f 0f 2f
    0g 0g 3g 5h 7h 8h 0i 0i 9i
    9g 5g 8g 6h 4h 2h 3i 1i 7i
    0g 0g 0g 3h 9h 1h 0i 8i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_0():
    puzzle_string = f"""
    naked_triple_0.sudoku
    9
    _a 4a _a 0b 0b 0b 3c 0c 0c
    2a _a _a 7b 0b 0b 0c 6c 0c
    _a _a 9a 8b 0b 0b 0c 0c 0c
    0d 0d 8d 0e 0e 0e 0f 9f 6f
    9d 0d 0d 2e 0e 4e 0f 0f 1f
    7d 2d 0d 0e 0e 0e 5f 0f 0f
    0g 0g 0g 0h 0h 5h 8i 0i 0i
    0g 1g 0g 0h 0h 7h 0i 0i 2i
    0g 0g 3g 0h 0h 0h 0i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_1():
    puzzle_string = f"""
    naked_triple_1.sudoku
    9
    _a _a _a 9b 0b 0b 0c 0c 0c
    _a _a _a 0b 3b 6b 0c 4c 9c
    3a 5a _a 0b 0b 1b 0c 0c 0c
    0d 0d 0d 2e 0e 0e 8f 0f 6f
    5d 6d 0d 0e 0e 0e 0f 7f 4f
    9d 0d 3d 0e 0e 4e 0f 0f 0f
    0g 0g 0g 4h 0h 0h 0i 8i 1i
    2g 9g 0g 6h 1h 0h 0i 0i 0i
    0g 0g 0g 0h 0h 7h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_2():
    puzzle_string = f"""
    naked_triple_2.sudoku
    9
    _a _a _a 0b 2b 0b 0c 0c 0c
    _a 3a 5a 6b 0b 0b 2c 0c 0c
    4a _a _a 5b 0b 0b 0c 0c 8c
    0d 0d 8d 0e 9e 7e 0f 0f 0f
    0d 0d 2d 8e 0e 6e 1f 0f 0f
    0d 0d 0d 4e 1e 0e 5f 0f 0f
    3g 0g 0g 0h 0h 5h 0i 0i 7i
    0g 0g 4g 0h 0h 8h 9i 6i 0i
    0g 0g 0g 0h 4h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_3():
    puzzle_string = f"""
    naked_triple_3.sudoku
    9
    6a _a _a 0b 0b 0b 0c 0c 7c
    _a _a 5a 0b 6b 0b 0c 9c 0c
    8a _a _a 4b 0b 0b 2c 0c 0c
    0d 3d 0d 0e 0e 0e 7f 0f 0f
    0d 1d 0d 9e 0e 7e 0f 3f 0f
    0d 0d 8d 0e 0e 0e 0f 1f 0f
    0g 0g 7g 0h 0h 5h 0i 0i 8i
    0g 2g 0g 0h 8h 0h 1i 0i 0i
    4g 0g 0g 0h 0h 0h 0i 0i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_4():
    puzzle_string = f"""
    naked_triple_4.sudoku
    9
    _a _a _a 0b 0b 0b 6c 9c 8c
    _a _a _a 0b 2b 6b 0c 0c 0c
    1a _a _a 9b 0b 0b 0c 0c 5c
    0d 0d 7d 0e 4e 0e 0f 3f 2f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    3d 6d 0d 0e 5e 0e 8f 0f 0f
    5g 0g 0g 0h 0h 4h 0i 0i 1i
    0g 0g 0g 5h 7h 0h 0i 0i 0i
    9g 2g 8g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_5():
    puzzle_string = f"""
    naked_triple_5.sudoku
    9
    4a 7a 8a 0b 1b 0b 6c 5c 0c
    _a 3a _a 0b 0b 7b 8c 1c 0c
    _a 1a _a 0b 0b 8b 0c 0c 0c
    0d 0d 7d 5e 8e 0e 0f 3f 6f
    6d 5d 4d 7e 3e 2e 1f 9f 8f
    3d 8d 0d 0e 9e 6e 5f 0f 0f
    8g 0g 0g 0h 0h 0h 0i 6i 0i
    0g 6g 0g 8h 0h 0h 0i 4i 0i
    7g 0g 3g 0h 6h 5h 9i 8i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_6():
    puzzle_string = f"""
    naked_triple_6.sudoku
    9
    5a 8a _a 7b 3b 9b 2c 1c 0c
    9a 3a _a 1b 2b 6b 0c 0c 8c
    1a 2a _a 5b 8b 4b 0c 9c 3c
    0d 9d 5d 8e 4e 2e 0f 0f 0f
    6d 4d 8d 9e 1e 0e 0f 2f 5f
    0d 1d 2d 6e 0e 0e 4f 8f 9f
    8g 7g 9g 4h 0h 1h 0i 3i 2i
    4g 6g 3g 2h 0h 0h 0i 0i 0i
    2g 5g 1g 3h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_7():
    puzzle_string = f"""
    naked_triple_7.sudoku
    9
    1a 6a _a 0b 7b 5b 4c 0c 0c
    _a 5a 4a 2b 1b 0b 0c 0c 7c
    2a 3a 7a 9b 4b 6b 8c 1c 5c
    5d 9d 3d 7e 8e 2e 1f 4f 6f
    7d 8d 2d 1e 6e 4e 5f 3f 9f
    4d 1d 6d 0e 0e 0e 2f 7f 8f
    0g 2g 5g 4h 3h 7h 0i 0i 1i
    0g 4g 0g 0h 0h 1h 7i 0i 0i
    0g 7g 1g 6h 2h 0h 0i 5i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_8():
    puzzle_string = f"""
    naked_triple_8.sudoku
    9
    _a 4a _a 0b 0b 0b 9c 3c 0c
    3a 7a _a 2b 0b 8b 6c 4c 1c
    _a 6a _a 0b 4b 0b 5c 0c 7c
    5d 0d 4d 0e 1e 7e 3f 9f 0f
    6d 0d 1d 0e 0e 0e 0f 7f 5f
    9d 0d 7d 5e 0e 0e 1f 0f 4f
    4g 1g 6g 0h 2h 9h 0i 5i 3i
    7g 5g 2g 1h 0h 0h 0i 0i 9i
    8g 9g 3g 0h 0h 0h 0i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_9():
    puzzle_string = f"""
    naked_triple_9.sudoku
    9
    _a 4a 2a 7b 0b 0b 0c 0c 0c
    _a _a 3a 9b 0b 0b 7c 0c 4c
    5a 7a _a 0b 4b 0b 0c 0c 0c
    7d 0d 5d 0e 6e 2e 4f 0f 0f
    0d 0d 0d 0e 9e 0e 0f 0f 0f
    0d 0d 0d 4e 7e 0e 2f 0f 3f
    0g 0g 0g 0h 0h 7h 0i 8i 6i
    6g 0g 1g 0h 0h 4h 5i 0i 0i
    0g 0g 7g 6h 0h 9h 3i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_naked_triple_row():
    puzzle_string = f"""
    naked_triple_row.sudoku
    9
    7a 8a 2a 3b 5b 4b 1c 9c 6c
    _a _a _a 2b 6b 7b 4c 5c 8c
    4a 5a 6a 8b 9b 1b 3c 2c 7c
    0d 0d 1d 5e 0e 0e 6f 0f 0f
    5d 7d 0d 6e 0e 9e 2f 0f 1f
    0d 6d 0d 0e 0e 8e 5f 0f 0f
    6g 3g 7g 4h 8h 5h 9i 1i 2i
    0g 4g 0g 0h 0h 6h 0i 3i 5i
    0g 0g 5g 9h 0h 0h 0i 6i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), tech.NakedTriple()])


def test_sudoku_unique_rectangle_type1_00():
    puzzle_string = f"""
    unique_rectangle_type1_00.sudoku
    9
    _a 6a 4a 0b 3b 7b 0c 0c 0c
    1a _a _a 0b 0b 0b 0c 0c 0c
    5a _a _a 4b 0b 0b 3c 0c 9c
    0d 0d 0d 9e 5e 0e 2f 0f 0f
    0d 9d 0d 0e 0e 0e 0f 8f 0f
    0d 0d 8d 0e 4e 1e 0f 0f 0f
    7g 0g 1g 0h 0h 2h 0i 0i 8i
    0g 0g 0g 0h 0h 0h 0i 0i 4i
    0g 0g 0g 7h 9h 0h 6i 3i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()])


def test_sudoku_unique_rectangle_type1_01():
    puzzle_string = f"""
    unique_rectangle_type1_01.sudoku
    9
    3a _a 2a 4b 0b 0b 0c 0c 7c
    _a 6a 4a 0b 7b 0b 3c 5c 0c
    _a 7a _a 0b 0b 0b 0c 2c 0c
    0d 5d 7d 0e 0e 0e 0f 6f 1f
    0d 0d 0d 6e 0e 8e 0f 0f 0f
    6d 4d 0d 0e 0e 0e 8f 9f 0f
    0g 3g 0g 0h 0h 0h 0i 4i 0i
    0g 1g 6g 0h 8h 0h 5i 3i 0i
    4g 0g 0g 0h 0h 6h 1i 0i 2i
"""
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()])


def test_sudoku_unique_rectangle_type1_02():
    puzzle_string = f"""
    unique_rectangle_type1_02.sudoku
    9
    _a 3a _a 8b 0b 5b 4c 6c 0c
    _a _a _a 0b 0b 0b 0c 3c 0c
    _a _a _a 6b 4b 0b 1c 0c 2c
    6d 0d 9d 0e 0e 0e 0f 2f 0f
    0d 1d 4d 0e 0e 0e 9f 8f 0f
    0d 2d 0d 0e 0e 0e 6f 0f 1f
    1g 0g 2g 0h 5h 7h 0i 0i 0i
    0g 9g 0g 0h 0h 0h 0i 0i 0i
    0g 4g 7g 1h 0h 6h 0i 5i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair(), UniqueRectangleType1()])


def test_sudoku_unique_rectangle_type1_03():
    puzzle_string = f"""
    unique_rectangle_type1_03.sudoku
    9
    _a _a _a 8b 0b 0b 7c 2c 0c
    _a _a 8a 0b 4b 0b 0c 0c 0c
    _a _a 3a 1b 7b 2b 9c 0c 0c
    0d 3d 0d 0e 0e 0e 0f 0f 8f
    0d 0d 4d 0e 0e 0e 1f 0f 0f
    2d 0d 0d 0e 0e 0e 0f 7f 0f
    0g 0g 2g 6h 8h 9h 3i 0i 0i
    0g 0g 0g 0h 3h 0h 4i 0i 0i
    0g 1g 6g 0h 0h 4h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()])


def test_sudoku_unique_rectangle_type1_04():
    puzzle_string = f"""
    unique_rectangle_type1_04.sudoku
    9
    6a 2a _a _b _b 4b 5c _c _c
    8a _a _a _b _b _b _c 4c _c
    _a _a 4a 3b _b _b _c _c 8c
    2d 9d _d 1e _e _e 3f _f _f
    _d _d _d _e 8e _e _f _f _f
    _d _d 8d _e _e 9e _f 2f 6f
    4g _g _g _h _h 2h 6i _i _i
    _g 6g _g _h _h _h _i _i 1i
    _g _g 1g 5h _h _h _i 3i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_almost_locked_candidates_col():
    puzzle_string = f"""
    almost_locked_candidates_col.sudoku
    9
    _a 5a _a   2b 0b 0b   8c 7c 4c
    2a 8a 7a   5b 0b 0b   3c 1c 9c
    1a 3a 4a   8b 7b 9b   5c 2c 6c

    0d 2d 8d   0e 5e 0e   0f 6f 1f
    0d 0d 0d   7e 8e 2e   4f 0f 0f
    0d 4d 3d   0e 9e 0e   0f 8f 0f

    8g 6g 2g   9h 0h 5h   1i 0i 7i
    3g 0g 5g   0h 2h 7h   6i 0i 8i
    4g 7g 0g   0h 0h 8h   0i 5i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_almost_locked_candidates_row():
    puzzle_string = f"""
    almost_locked_candidates_row.sudoku
    9
_a 2a 9a   7b 0b 0b   0c 4c 0c
_a 7a 8a   0b 9b 0b   0c 0c 6c
_a 5a 1a   3b 0b 0b   7c 0c 9c

1d 6d 2d   5e 8e 9e   4f 7f 3f
8d 9d 7d   0e 3e 0e   0f 0f 0f
5d 3d 4d   6e 1e 7e   2f 9f 8f

2g 8g 5g   1h 7h 6h   9i 3i 4i
9g 4g 6g   8h 2h 3h   5i 1i 7i
7g 1g 3g   9h 0h 0h   0i 0i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_almost_locked_candidates_rows_center():
    puzzle_string = f"""
    almost_locked_candidates_rows_center.sudoku
    9
6a 2a _a   0b 0b 4b   9c 3c 1c
_a _a 5a   6b 0b 3b   2c 8c 4c
3a 4a _a   0b 9b 0b   6c 5c 7c

0d 1d 0d   0e 2e 0e   8f 6f 5f
8d 0d 0d   1e 6e 5e   0f 2f 0f
2d 5d 6d   0e 8e 0e   0f 1f 0f

5g 8g 0g   7h 0h 6h   0i 9i 2i
0g 3g 2g   9h 0h 8h   5i 7i 6i
7g 6g 9g   0h 0h 0h   0i 4i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_als_xz():
    puzzle_string = f"""
    als_xz.sudoku
    9
4a _a _a   0b 0b 0b   5c 0c 0c
6a _a _a   4b 5b 2b   8c 0c 0c
3a 5a _a   0b 0b 7b   4c 1c 0c

9d 0d 0d   0e 0e 6e   0f 5f 0f
0d 2d 0d   5e 3e 4e   0f 7f 0f
5d 3d 0d   7e 0e 0e   0f 8f 4f

0g 6g 3g   9h 0h 5h   0i 4i 0i
0g 0g 5g   2h 4h 0h   0i 0i 8i
0g 0g 0g   0h 0h 0h   0i 0i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_alternating_inference_chain():
    puzzle_string = f"""
    alternating_inference_chain.sudoku
    9
_a 5a _a   0b 0b 0b   0c 3c 0c
_a 3a 2a   4b 1b 0b   5c 9c 7c
_a 1a 9a   0b 3b 5b   0c 8c 0c

0d 2d 0d   8e 0e 1e   9f 6f 0f
9d 6d 0d   0e 0e 0e   8f 1f 0f
1d 4d 8d   3e 0e 0e   7f 2f 5f

0g 9g 0g   5h 8h 7h   3i 4i 0i
5g 8g 4g   1h 2h 3h   6i 7i 9i
0g 7g 0g   0h 0h 0h   0i 5i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type1_0():
    puzzle_string = f"""
    avoidable_rectangle_type1_0.sudoku
    9
_a 6a _a   0b 0b 0b   0c 3c 9c
_a 8a _a   3b 2b 0b   0c 0c 0c
9a _a _a   5b 0b 6b   0c 0c 0c

2d 0d 0d   0e 0e 4e   6f 0f 0f
0d 0d 7d   0e 5e 0e   2f 0f 0f
0d 0d 5d   6e 0e 0e   0f 0f 8f

0g 0g 0g   4h 0h 8h   0i 0i 5i
0g 0g 0g   0h 3h 1h   0i 4i 0i
7g 1g 0g   0h 0h 0h   0i 8i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_1():
    puzzle_string = f"""
    avoidable_rectangle_type2_1.sudoku
    9
_a _a 2a   0b 0b 0b   0c 3c 0c
_a _a 6a   0b 3b 1b   0c 4c 0c
3a _a _a   0b 0b 9b   2c 7c 0c

0d 0d 7d   0e 0e 2e   0f 0f 0f
2d 0d 0d   0e 0e 0e   0f 0f 6f
0d 0d 0d   1e 0e 0e   9f 0f 0f

0g 4g 9g   5h 0h 0h   0i 0i 2i
0g 2g 0g   6h 9h 0h   7i 0i 0i
0g 1g 0g   0h 0h 0h   4i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_2():
    puzzle_string = f"""
    avoidable_rectangle_type2_2.sudoku
    9
_a _a _a   0b 0b 0b   0c 0c 1c
_a 6a _a   3b 0b 8b   0c 0c 7c
5a _a 3a   4b 0b 0b   0c 0c 2c

0d 0d 0d   0e 8e 0e   6f 7f 0f
4d 0d 0d   6e 0e 3e   0f 0f 5f
0d 5d 6d   0e 4e 0e   0f 0f 0f

9g 0g 0g   0h 0h 7h   5i 0i 8i
7g 0g 0g   2h 0h 4h   0i 3i 0i
6g 0g 0g   0h 0h 0h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_3():
    puzzle_string = f"""
    avoidable_rectangle_type2_3.sudoku
    9
_a _a _a   0b 0b 0b   0c 0c 1c
_a 6a _a   3b 0b 8b   0c 0c 7c
5a _a 3a   4b 0b 0b   0c 0c 2c

0d 0d 0d   0e 8e 0e   6f 7f 0f
4d 0d 0d   6e 0e 3e   0f 0f 5f
0d 5d 6d   0e 4e 0e   0f 0f 0f

9g 0g 0g   0h 0h 7h   5i 0i 8i
7g 0g 0g   2h 0h 4h   0i 3i 0i
6g 0g 0g   0h 0h 0h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_4():
    puzzle_string = f"""
    avoidable_rectangle_type2_4.sudoku
    9
_a _a 3a   0b 0b 0b   0c 7c 0c
_a _a _a   3b 0b 0b   0c 0c 4c
_a _a 5a   2b 4b 9b   6c 0c 0c

3d 0d 0d   1e 0e 0e   0f 0f 0f
6d 0d 7d   0e 0e 0e   4f 0f 3f
0d 0d 0d   0e 0e 5e   0f 0f 6f

0g 0g 8g   7h 6h 3h   2i 0i 0i
5g 0g 0g   0h 0h 4h   0i 0i 0i
0g 3g 0g   0h 0h 0h   9i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_5():
    puzzle_string = f"""
    avoidable_rectangle_type2_5.sudoku
    9
_a _a _a   9b 0b 0b   2c 0c 0c
9a _a _a   0b 0b 4b   0c 1c 7c
_a 7a _a   0b 6b 8b   5c 0c 0c

0d 4d 0d   0e 0e 0e   0f 6f 8f
0d 0d 8d   0e 0e 0e   4f 0f 0f
1d 9d 0d   0e 0e 0e   0f 3f 0f

0g 0g 1g   4h 7h 0h   0i 5i 0i
3g 6g 0g   5h 0h 0h   0i 0i 4i
0g 0g 7g   0h 0h 9h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_6():
    puzzle_string = f"""
    avoidable_rectangle_type2_6.sudoku
    9
_a _a _a   0b 0b 0b   0c 0c 7c
_a 6a _a   2b 0b 3b   0c 0c 4c
9a _a 1a   0b 0b 4b   0c 0c 8c

0d 4d 7d   0e 9e 0e   0f 0f 0f
1d 0d 0d   7e 0e 6e   0f 0f 3f
0d 0d 0d   0e 3e 0e   7f 1f 0f

2g 0g 0g   3h 0h 0h   6i 0i 1i
4g 0g 0g   6h 0h 9h   0i 7i 0i
5g 0g 0g   0h 0h 0h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_north():
    puzzle_string = f"""
    avoidable_rectangle_type2_north.sudoku
    9
_a 7a 5a   4b 0b 0b   0c 2c 0c
_a 1a _a   0b 0b 0b   0c 0c 6c
4a _a 9a   0b 6b 8b   7c 0c 0c

9d 0d 0d   1e 0e 0e   0f 8f 0f
0d 0d 0d   0e 0e 0e   0f 0f 0f
0d 6d 0d   0e 0e 5e   0f 0f 1f

0g 0g 6g   9h 5h 0h   1i 0i 4i
7g 0g 0g   0h 0h 0h   0i 6i 0i
0g 9g 0g   0h 0h 4h   5i 3i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_south():
    puzzle_string = f"""
    avoidable_rectangle_type2_south.sudoku
    9
_a _a 5a   0b 0b 0b   0c 0c 4c
_a _a 7a   3b 9b 6b   2c 0c 0c
_a _a _a   0b 0b 5b   0c 9c 0c

0d 5d 0d   0e 0e 1e   0f 0f 0f
0d 2d 4d   0e 0e 0e   9f 5f 0f
0d 0d 0d   7e 0e 0e   0f 2f 0f

0g 7g 0g   9h 0h 0h   0i 0i 0i
0g 0g 8g   5h 2h 4h   6i 0i 0i
5g 0g 0g   0h 0h 0h   3i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_avoidable_rectangle_type2_west():
    puzzle_string = f"""
    avoidable_rectangle_type2_west.sudoku
    9
_a 9a 4a   1b 0b 0b   0c 0c 3c
5a _a _a   0b 4b 0b   0c 0c 0c
_a _a _a   0b 0b 0b   7c 4c 2c

3d 7d 0d   4e 0e 0e   0f 0f 0f
0d 5d 0d   0e 0e 0e   0f 3f 0f
0d 0d 0d   0e 0e 7e   0f 9f 8f

1g 2g 5g   0h 0h 0h   0i 0i 0i
0g 0g 0g   0h 9h 0h   0i 0i 4i
4g 0g 0g   0h 0h 3h   2i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_jellyfish_0():
    puzzle_string = f"""
    finned_jellyfish_0.sudoku
    9

4a _a _a   2b 0b 9b   0c 7c 8c
_a 9a _a   8b 0b 0b   4c 0c 0c
8a _a _a   4b 6b 0b   1c 9c 0c

0d 0d 0d   3e 0e 4e   0f 8f 0f
0d 0d 9d   0e 8e 0e   2f 0f 0f
0d 4d 8d   9e 0e 5e   0f 0f 0f

0g 7g 4g   0h 9h 0h   0i 0i 5i
5g 8g 1g   0h 0h 2h   0i 0i 0i
9g 3g 0g   5h 4h 0h   0i 0i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_jellyfish_1():
    puzzle_string = f"""
    finned_jellyfish_1.sudoku
    9

_a _a _a   1b 0b 0b   9c 0c 0c
_a 9a _a   0b 0b 8b   0c 0c 7c
_a 1a _a   0b 4b 0b   5c 0c 8c

9d 0d 0d   8e 0e 6e   0f 0f 0f
0d 0d 8d   0e 1e 0e   2f 0f 0f
0d 0d 0d   3e 0e 9e   0f 0f 1f

7g 0g 9g   0h 8h 0h   0i 6i 0i
3g 0g 0g   6h 0h 0h   0i 7i 0i
0g 0g 5g   0h 0h 2h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_jellyfish_2():
    puzzle_string = f"""
    finned_jellyfish_2.sudoku
    9

_a _a _a   4b 0b 3b   8c 0c 5c
8a 5a _a   0b 0b 0b   6c 3c 4c
_a 4a 3a   6b 5b 8b   7c 0c 9c

3d 0d 7d   8e 0e 4e   2f 5f 0f
5d 0d 0d   0e 3e 0e   0f 0f 0f
0d 0d 4d   5e 0e 6e   3f 0f 8f

4g 0g 5g   3h 0h 0h   0i 0i 2i
0g 3g 2g   0h 0h 5h   0i 8i 0i
6g 0g 0g   7h 0h 2h   5i 0i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_jellyfish_3():
    puzzle_string = f"""
    finned_jellyfish_3.sudoku
    9

_a 6a 5a   3b 2b 0b   9c 7c 8c
9a 2a _a   7b 0b 8b   0c 0c 0c
8a 3a 7a   0b 5b 0b   0c 0c 0c

0d 9d 2d   0e 0e 5e   0f 7f 8f
5d 0d 8d   2e 0e 7e   0f 9f 6f
0d 7d 6d   8e 0e 0e   1f 5f 2f

6g 0g 9g   0h 8h 3h   0i 0i 7i
2g 0g 0g   0h 7h 6h   8i 3i 9i
7g 8g 3g   0h 0h 2h   6i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_swordfish_0():
    puzzle_string = f"""
    finned_swordfish_0.sudoku
    9

_a _a _a   0b 4b 0b   5c 9c 0c
_a 5a 9a   0b 0b 0b   1c 4c 2c
_a 1a _a   5b 9b 0b   0c 8c 0c

6d 2d 5d   7e 1e 8e   9f 3f 4f
0d 0d 8d   6e 5e 3e   2f 7f 1f
3d 7d 1d   4e 2e 9e   8f 6f 5f

5g 8g 0g   2h 0h 4h   0i 1i 9i
1g 0g 0g   9h 0h 5h   3i 2i 8i
0g 0g 2g   0h 8h 0h   4i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_swordfish_1():
    puzzle_string = f"""
    finned_swordfish_1.sudoku
    9

2a _a _a   0b 6b 1b   9c 0c 0c
_a _a _a   3b 0b 0b   0c 0c 5c
_a 5a _a   0b 0b 9b   0c 6c 0c

0d 1d 0d   0e 7e 8e   0f 0f 0f
0d 0d 4d   0e 0e 0e   6f 0f 0f
0d 0d 0d   2e 3e 0e   0f 4f 0f

0g 6g 0g   7h 0h 0h   0i 5i 0i
9g 0g 0g   0h 0h 4h   0i 0i 0i
0g 0g 1g   6h 9h 0h   0i 0i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_swordfish_2():
    puzzle_string = f"""
    finned_swordfish_2.sudoku
    9

8a _a 5a   9b 0b 0b   0c 0c 0c
7a 4a 1a   0b 0b 8b   9c 0c 0c
_a 9a _a   0b 1b 5b   0c 7c 8c

0d 0d 0d   8e 0e 0e   6f 9f 0f
0d 8d 0d   1e 9e 2e   0f 4f 0f
0d 0d 9d   0e 0e 0e   0f 0f 0f

1g 3g 0g   5h 0h 9h   0i 2i 0i
9g 5g 8g   7h 2h 4h   1i 6i 3i
0g 0g 0g   0h 0h 1h   0i 0i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_swordfish_3():
    puzzle_string = f"""
    finned_swordfish_3.sudoku
    9

2a _a 8a   0b 0b 0b   0c 0c 3c
1a 4a _a   0b 0b 2b   0c 0c 9c
7a _a 6a   0b 5b 0b   0c 4c 2c

0d 0d 0d   3e 0e 0e   0f 0f 0f
5d 0d 2d   4e 8e 1e   9f 0f 6f
0d 0d 0d   2e 0e 5e   0f 0f 0f

3g 0g 0g   0h 2h 0h   4i 9i 5i
6g 0g 0g   9h 0h 0h   0i 8i 7i
4g 0g 9g   5h 0h 0h   6i 0i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_00():
    puzzle_string = f"""
    finned_x_wing_00.sudoku
    9

4a 5a 6a   9b 8b 7b   3c 1c 2c
_a 9a _a   4b 3b 2b   6c 7c 5c
2a 3a 7a   0b 1b 0b   0c 9c 0c

0d 4d 0d   8e 0e 0e   0f 2f 0f
0d 6d 0d   3e 0e 4e   0f 5f 0f
0d 0d 0d   0e 0e 1e   0f 6f 0f

0g 8g 0g   0h 4h 9h   0i 3i 1i
9g 0g 4g   1h 5h 3h   0i 8i 6i
0g 1g 3g   7h 0h 8h   0i 4i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_04():
    puzzle_string = f"""
    finned_x_wing_04.sudoku
    9

_a _a 8a   0b 0b 9b   3c 5c 2c
5a _a 3a   0b 2b 8b   0c 1c 0c
_a 4a _a   3b 5b 0b   8c 7c 0c

0d 2d 0d   0e 0e 5e   0f 3f 8f
6d 8d 0d   2e 9e 3e   0f 4f 0f
3d 0d 0d   8e 0e 0e   2f 6f 0f

8g 5g 6g   0h 3h 2h   0i 9i 0i
0g 1g 0g   9h 0h 0h   5i 8i 3i
4g 3g 9g   5h 8h 0h   6i 2i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_05():
    puzzle_string = f"""
    finned_x_wing_05.sudoku
    9

_a _a _a   5b 9b 1b   3c 4c 8c
_a _a _a   7b 4b 2b   0c 0c 6c
4a _a 5a   8b 6b 3b   7c 2c 0c

1d 0d 0d   9e 0e 8e   6f 0f 5f
0d 0d 0d   1e 0e 5e   4f 8f 0f
5d 0d 8d   6e 0e 4e   0f 0f 2f

0g 0g 2g   4h 0h 6h   0i 0i 0i
6g 0g 0g   3h 0h 9h   2i 0i 7i
9g 5g 3g   2h 1h 7h   8i 6i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_06():
    puzzle_string = f"""
    finned_x_wing_06.sudoku
    9

_a 1a _a   3b 0b 7b   0c 4c 9c
_a _a _a   0b 0b 0b   0c 0c 0c
_a _a 8a   5b 0b 0b   3c 6c 0c

0d 0d 7d   0e 0e 3e   0f 0f 4f
4d 0d 6d   0e 0e 0e   1f 0f 3f
1d 0d 0d   2e 0e 0e   7f 0f 0f

0g 5g 1g   0h 0h 2h   4i 0i 0i
0g 0g 0g   0h 0h 0h   0i 0i 0i
6g 2g 0g   9h 0h 1h   0i 3i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_07():
    puzzle_string = f"""
    finned_x_wing_07.sudoku
    9

1a 4a _a   0b 0b 0b   9c 0c 8c
_a 2a _a   0b 9b 4b   1c 0c 6c
_a _a 6a   5b 1b 0b   2c 3c 4c

0d 0d 4d   0e 0e 0e   0f 8f 2f
0d 5d 2d   0e 0e 0e   4f 0f 1f
8d 1d 0d   0e 0e 0e   5f 0f 0f

2g 3g 7g   0h 0h 0h   8i 1i 5i
5g 0g 0g   0h 0h 0h   0i 4i 0i
4g 0g 1g   0h 0h 0h   0i 2i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_08():
    puzzle_string = f"""
    finned_x_wing_08.sudoku
    9

_a _a _a   9b 0b 7b   0c 3c 0c
_a _a _a   0b 2b 0b   0c 8c 7c
_a _a 1a   0b 0b 3b   0c 6c 0c

0d 0d 0d   0e 0e 0e   3f 9f 4f
2d 0d 0d   0e 0e 0e   0f 0f 8f
9d 4d 3d   0e 0e 0e   0f 0f 0f

0g 8g 0g   6h 0h 0h   1i 0i 0i
5g 3g 0g   0h 9h 0h   0i 0i 0i
0g 2g 0g   8h 0h 5h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_09():
    puzzle_string = f"""
    finned_x_wing_09.sudoku
    9

3a 7a 8a   5b 6b 2b   1c 9c 4c
_a 2a 4a   0b 0b 0b   0c 0c 5c
5a _a 9a   4b 0b 8b   0c 0c 3c

2d 0d 0d   0e 4e 0e   5f 0f 7f
0d 9d 7d   2e 0e 5e   3f 4f 6f
4d 0d 5d   0e 0e 0e   0f 0f 9f

7g 4g 0g   0h 2h 1h   9i 5i 8i
9g 0g 2g   0h 5h 4h   6i 7i 1i
0g 5g 1g   0h 9h 7h   4i 3i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_10():
    puzzle_string = f"""
    finned_x_wing_10.sudoku
    9

3a _a _a   0b 2b 6b   0c 5c 0c
_a _a 6a   8b 5b 0b   3c 1c 9c
_a 5a _a   0b 1b 0b   2c 6c 0c

5d 0d 2d   6e 0e 0e   7f 3f 0f
4d 8d 0d   2e 3e 0e   5f 9f 6f
0d 0d 3d   0e 0e 5e   1f 0f 2f

1g 7g 9g   0h 6h 0h   0i 2i 5i
8g 3g 4g   5h 9h 2h   6i 7i 1i
0g 0g 5g   1h 7h 0h   9i 0i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_11():
    puzzle_string = f"""
    finned_x_wing_11.sudoku
    9

_a 2a _a   0b 0b 0b   0c 0c 9c
_a _a 9a   0b 0b 1b   0c 6c 3c
7a 3a _a   0b 0b 0b   4c 0c 0c

0d 0d 3d   7e 1e 0e   0f 0f 2f
0d 0d 0d   0e 8e 0e   0f 0f 0f
8d 0d 0d   0e 3e 2e   1f 0f 0f

0g 0g 7g   0h 0h 0h   0i 2i 4i
2g 6g 0g   4h 0h 0h   8i 0i 0i
1g 0g 0g   0h 0h 0h   0i 3i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_12():
    puzzle_string = f"""
    finned_x_wing_12.sudoku
    9

_a 7a 2a   0b 0b 0b   0c 0c 0c
3a _a _a   6b 9b 0b   4c 5c 0c
6a _a _a   2b 0b 0b   0c 0c 0c

0d 0d 6d   0e 0e 0e   0f 0f 5f
0d 5d 1d   7e 0e 6e   3f 2f 0f
7d 0d 0d   0e 0e 0e   6f 0f 0f

0g 0g 0g   0h 0h 4h   0i 0i 8i
0g 6g 4g   0h 5h 1h   0i 0i 7i
0g 0g 0g   0h 0h 0h   9i 1i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_13():
    puzzle_string = f"""
    finned_x_wing_13.sudoku
    9

1a _a _a   3b 8b 0b   0c 0c 0c
_a 7a _a   0b 0b 0b   0c 0c 1c
_a 2a _a   1b 0b 4b   3c 0c 7c

0d 0d 0d   0e 0e 1e   0f 0f 5f
8d 0d 0d   5e 0e 3e   0f 0f 6f
6d 0d 0d   7e 0e 0e   0f 0f 0f

7g 0g 3g   4h 0h 2h   0i 5i 0i
2g 0g 0g   0h 0h 0h   0i 9i 0i
0g 0g 0g   0h 3h 5h   0i 0i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_14():
    puzzle_string = f"""
    finned_x_wing_14.sudoku
    9

2a _a _a   7b 4b 1b   5c 3c 6c
_a _a _a   5b 2b 3b   0c 0c 7c
3a 5a 7a   6b 9b 8b   4c 2c 1c

4d 2d 0d   0e 7e 9e   0f 0f 5f
0d 0d 5d   0e 6e 2e   7f 4f 0f
7d 0d 0d   8e 5e 4e   0f 0f 2f

9g 7g 2g   4h 8h 5h   6i 1i 3i
5g 0g 0g   9h 1h 6h   2i 7i 0i
0g 1g 0g   2h 3h 7h   0i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_15():
    puzzle_string = f"""
    finned_x_wing_15.sudoku
    9

6a 8a 9a   5b 0b 2b   0c 4c 1c
7a 2a 1a   0b 0b 0b   5c 0c 8c
4a 3a 5a   0b 0b 0b   2c 0c 9c

2d 5d 3d   0e 0e 1e   6f 0f 4f
9d 0d 6d   0e 0e 0e   0f 0f 2f
8d 0d 7d   2e 0e 0e   9f 0f 5f

5g 9g 4g   0h 0h 0h   1i 2i 7i
3g 7g 2g   0h 0h 0h   8i 9i 6i
1g 6g 8g   7h 2h 9h   4i 5i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_16():
    puzzle_string = f"""
    finned_x_wing_16.sudoku
    9

7a 4a 9a   8b 1b 3b   2c 5c 6c
6a 5a 3a   9b 7b 2b   4c 1c 8c
_a 1a _a   0b 0b 0b   9c 3c 7c

3d 0d 7d   0e 0e 8e   5f 9f 0f
1d 0d 5d   0e 0e 0e   8f 7f 4f
9d 8d 4d   7e 0e 0e   0f 0f 3f

0g 3g 6g   0h 0h 0h   7i 4i 0i
4g 9g 0g   0h 0h 7h   0i 0i 5i
5g 7g 1g   2h 0h 4h   0i 8i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_17():
    puzzle_string = f"""
    finned_x_wing_17.sudoku
    9

3a _a _a   7b 4b 8b   5c 0c 0c
_a _a 1a   5b 2b 6b   3c 0c 4c
_a _a _a   1b 3b 9b   0c 0c 8c

0d 0d 8d   3e 0e 2e   0f 0f 7f
2d 0d 0d   0e 0e 4e   0f 0f 6f
4d 0d 0d   0e 0e 5e   2f 0f 0f

1g 0g 0g   2h 8h 7h   0i 0i 5i
9g 0g 6g   4h 5h 1h   8i 0i 0i
0g 0g 5g   6h 9h 3h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_cols_1_fin():
    puzzle_string = f"""
    finned_x_wing_cols_1_fin.sudoku
    9

_a _a _a   4b 0b 6b   0c 8c 9c
_a _a 6a   0b 7b 0b   0c 2c 4c
_a _a 9a   0b 0b 5b   0c 6c 0c

1d 7d 2d   0e 0e 0e   6f 0f 0f
6d 0d 0d   7e 1e 2e   0f 0f 8f
0d 0d 0d   6e 0e 0e   2f 1f 7f

0g 5g 0g   2h 0h 0h   9i 0i 0i
3g 6g 0g   0h 8h 0h   0i 0i 2i
9g 2g 0g   3h 0h 7h   8i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_finned_x_wing_rows_1_fin():
    puzzle_string = f"""
    finned_x_wing_rows_1_fin.sudoku
    9

6a _a _a   0b 7b 5b   0c 3c 0c
9a 8a 3a   4b 6b 0b   5c 0c 0c
5a _a 7a   0b 9b 0b   0c 0c 6c

3d 0d 1d   5e 0e 0e   7f 6f 0f
8d 5d 6d   7e 3e 0e   0f 2f 4f
0d 7d 9d   0e 0e 6e   3f 0f 0f

7g 6g 0g   0h 5h 0h   8i 9i 1i
1g 9g 5g   6h 8h 7h   2i 4i 3i
0g 3g 8g   9h 1h 0h   6i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_fishy_cycle():
    puzzle_string = f"""
    fishy_cycle.sudoku
    9

3a _a 8a   5b 0b 1b   2c 9c 7c
_a _a 9a   7b 3b 0b   1c 8c 5c
5a 7a 1a   8b 2b 9b   3c 4c 6c

0d 0d 6d   0e 0e 5e   0f 0f 8f
8d 3d 0d   0e 0e 0e   0f 5f 9f
0d 0d 5d   0e 0e 8e   6f 0f 0f

9g 1g 0g   0h 5h 7h   8i 0i 3i
0g 5g 7g   0h 8h 3h   9i 0i 0i
6g 8g 3g   9h 0h 2h   5i 7i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_fishy_cycle_0():
    puzzle_string = f"""
    fishy_cycle_0.sudoku
    9

_a 3a _a   0b 0b 0b   0c 8c 6c
1a _a _a   6b 0b 5b   0c 0c 0c
2a _a _a   0b 0b 1b   3c 0c 0c

7d 0d 0d   2e 0e 0e   0f 9f 0f
0d 0d 0d   5e 0e 8e   0f 0f 0f
0d 5d 0d   0e 0e 3e   0f 0f 7f

0g 0g 2g   1h 0h 0h   0i 0i 3i
0g 0g 0g   3h 0h 4h   0i 0i 8i
3g 8g 0g   0h 0h 0h   0i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_fishy_cycle_1():
    puzzle_string = f"""
    fishy_cycle_1.sudoku
    9

7a 8a 3a   9b 5b 6b   1c 4c 2c
6a _a _a   3b 2b 0b   9c 8c 7c
9a 2a _a   8b 0b 7b   6c 3c 5c

8d 0d 0d   0e 0e 9e   0f 0f 4f
0d 9d 2d   0e 0e 0e   8f 6f 0f
4d 0d 0d   0e 0e 8e   0f 9f 0f

2g 4g 9g   6h 0h 5h   3i 0i 8i
3g 0g 8g   0h 9h 2h   0i 0i 6i
0g 6g 7g   0h 8h 3h   0i 2i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_hidden_pair_1():
    puzzle_string = f"""
    hidden_pair_1.sudoku
    9

5a 4a 3a   0b 8b 0b   7c 6c 2c
2a 6a 8a   0b 7b 0b   3c 1c 9c
7a 9a 1a   0b 0b 6b   4c 8c 5c

1d 8d 2d   0e 0e 7e   0f 4f 6f
4d 5d 7d   6e 1e 0e   0f 3f 8f
9d 3d 6d   8e 0e 0e   0f 7f 1f

8g 2g 9g   7h 6h 3h   1i 5i 4i
3g 1g 5g   0h 0h 8h   6i 2i 7i
6g 7g 4g   0h 5h 0h   8i 9i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_hidden_pair_col():
    puzzle_string = f"""
    hidden_pair_col.sudoku
    9

9a 5a 4a   6b 3b 8b   7c 1c 2c
6a 7a 8a   0b 0b 0b   3c 9c 5c
1a 3a 2a   5b 0b 0b   6c 8c 4c

5d 4d 1d   0e 6e 0e   8f 2f 7f
8d 6d 7d   0e 0e 0e   1f 3f 9f
2d 9d 3d   0e 8e 0e   4f 5f 6f

3g 2g 6g   0h 0h 4h   5i 7i 8i
4g 8g 9g   0h 0h 0h   2i 6i 1i
7g 1g 5g   8h 2h 6h   9i 4i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_hidden_pair_fence():
    puzzle_string = f"""
    hidden_pair_fence.sudoku
    9

_a 9a 6a   0b 2b 0b   7c 3c 1c
8a 1a _a   0b 6b 3b   2c 0c 5c
2a 3a _a   1b 0b 0b   6c 0c 8c

0d 2d 0d   3e 9e 6e   8f 1f 7f
1d 6d 8d   5e 7e 4e   9f 2f 3f
9d 7d 3d   2e 8e 1e   4f 5f 6f

6g 5g 2g   0h 1h 0h   3i 7i 4i
7g 4g 1g   6h 3h 2h   5i 8i 9i
3g 8g 9g   0h 0h 0h   1i 6i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_hidden_pair_row():
    puzzle_string = f"""
    hidden_pair_row.sudoku
    9

1a 8a 2a   4b 6b 9b   3c 7c 5c
4a 9a 5a   7b 3b 1b   6c 2c 8c
6a 7a 3a   5b 2b 8b   4c 1c 9c

9d 4d 0d   0e 0e 2e   0f 5f 0f
0d 5d 6d   0e 1e 0e   9f 0f 2f
0d 2d 0d   9e 5e 0e   0f 0f 0f

5g 1g 9g   0h 0h 0h   2i 3i 4i
2g 3g 4g   1h 9h 5h   8i 6i 7i
8g 6g 7g   2h 4h 3h   5i 9i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_quad_5():
    puzzle_string = f"""
    hidden_quad_5.sudoku
    9

_a _a _a   2b 0b 0b   0c 0c 0c
_a _a 1a   9b 0b 4b   8c 0c 0c
_a _a 2a   0b 8b 0b   4c 3c 7c

0d 0d 0d   0e 0e 0e   0f 0f 1f
0d 2d 3d   0e 0e 0e   6f 9f 0f
4d 0d 0d   0e 0e 0e   0f 0f 3f

8g 6g 5g   3h 4h 0h   7i 0i 0i
2g 0g 9g   6h 0h 8h   3i 0i 0i
0g 0g 0g   0h 0h 2h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_quad_6():
    puzzle_string = f"""
    hidden_quad_6.sudoku
    9

4a 2a 6a   0b 0b 5b   8c 9c 3c
5a 7a 1a   3b 0b 0b   6c 4c 2c
8a 3a 9a   6b 0b 0b   5c 1c 7c

2d 1d 7d   0e 0e 0e   9f 3f 6f
6d 9d 4d   0e 0e 0e   7f 8f 5f
3d 8d 5d   0e 0e 0e   4f 2f 1f

1g 5g 3g   0h 0h 7h   2i 6i 8i
9g 6g 8g   0h 0h 1h   3i 7i 4i
7g 4g 2g   8h 0h 0h   1i 5i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_quad_7():
    puzzle_string = f"""
    hidden_quad_7.sudoku
    9

9a 3a 5a   4b 8b 1b   6c 2c 7c
8a 4a 6a   7b 5b 2b   3c 1c 9c
1a 2a 7a   6b 9b 3b   4c 8c 5c

0d 1d 0d   0e 0e 0e   7f 0f 6f
0d 0d 0d   0e 0e 0e   0f 0f 0f
4d 0d 9d   0e 0e 0e   0f 3f 0f

6g 8g 2g   9h 7h 4h   1i 5i 3i
7g 9g 1g   8h 3h 5h   2i 6i 4i
3g 5g 4g   2h 1h 6h   9i 7i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_0():
    puzzle_string = f"""
    hidden_unique_rectangle_0.sudoku
    9

_a _a _a   0b 0b 9b   3c 0c 6c
_a _a _a   0b 8b 0b   4c 1c 0c
_a 6a _a   0b 0b 0b   0c 0c 2c

0d 4d 0d   5e 0e 0e   6f 0f 0f
1d 0d 2d   0e 0e 0e   5f 0f 9f
0d 0d 5d   0e 0e 8e   0f 2f 0f

9g 0g 0g   0h 0h 0h   0i 3i 0i
0g 7g 8g   0h 3h 0h   0i 0i 0i
5g 0g 4g   9h 0h 0h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_1():
    puzzle_string = f"""
    hidden_unique_rectangle_1.sudoku
    9

6a 4a _a   0b 7b 3b   9c 8c 5c
_a 3a _a   0b 9b 0b   2c 6c 7c
_a 7a 9a   0b 0b 6b   4c 1c 3c

9d 2d 7d   6e 0e 0e   3f 5f 1f
3d 5d 8d   0e 1e 0e   6f 7f 4f
4d 1d 6d   7e 3e 5e   8f 0f 0f

7g 6g 3g   0h 0h 0h   1i 0i 8i
0g 8g 4g   0h 6h 0h   0i 3i 0i
1g 9g 0g   3h 0h 0h   0i 4i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_2():
    puzzle_string = f"""
    hidden_unique_rectangle_2.sudoku
    9

_a _a _a   0b 0b 0b   9c 0c 0c
_a _a 1a   6b 0b 2b   7c 0c 0c
_a 3a _a   9b 5b 0b   0c 0c 4c

0d 0d 2d   3e 0e 0e   0f 0f 6f
0d 7d 0d   0e 0e 0e   0f 8f 0f
6d 0d 0d   0e 0e 8e   5f 0f 0f

1g 0g 0g   0h 2h 9h   0i 7i 0i
0g 0g 9g   1h 0h 4h   8i 0i 0i
0g 0g 4g   0h 0h 0h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_3():
    puzzle_string = f"""
    hidden_unique_rectangle_3.sudoku
    9

_a _a 3a   1b 0b 9b   5c 6c 8c
_a _a _a   0b 6b 8b   2c 0c 3c
6a 8a _a   3b 2b 5b   0c 0c 0c

0d 0d 0d   0e 0e 6e   9f 0f 2f
0d 5d 0d   2e 0e 0e   8f 3f 6f
0d 6d 2d   8e 0e 3e   0f 0f 0f

0g 0g 0g   9h 0h 1h   6i 2i 4i
0g 0g 1g   6h 0h 0h   3i 0i 0i
4g 9g 6g   5h 3h 2h   1i 8i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_4():
    puzzle_string = f"""
    hidden_unique_rectangle_4.sudoku
    9

_a 2a _a   7b 0b 0b   4c 0c 0c
_a _a _a   0b 6b 0b   0c 9c 5c
_a _a _a   0b 1b 5b   8c 0c 7c

0d 0d 0d   5e 0e 0e   0f 0f 9f
0d 0d 8d   0e 0e 0e   3f 0f 0f
9d 0d 0d   0e 0e 8e   0f 0f 0f

3g 0g 7g   2h 5h 0h   0i 0i 0i
2g 1g 0g   0h 9h 0h   0i 0i 0i
0g 0g 6g   0h 0h 1h   0i 3i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_5():
    puzzle_string = f"""
    hidden_unique_rectangle_5.sudoku
    9

6a _a 2a   9b 5b 4b   3c 0c 0c
4a 3a 8a   6b 1b 7b   5c 9c 2c
9a 5a _a   3b 8b 2b   6c 4c 0c

8d 0d 0d   4e 9e 3e   2f 0f 0f
0d 9d 4d   5e 2e 6e   8f 7f 0f
5d 2d 0d   8e 7e 1e   4f 0f 9f

0g 8g 0g   7h 6h 5h   9i 0i 4i
7g 4g 5g   2h 3h 9h   1i 0i 0i
0g 6g 9g   1h 4h 8h   7i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_nec():
    puzzle_string = f"""
    hidden_unique_rectangle_nec.sudoku
    9

_a _a 4a   0b 0b 5b   6c 7c 8c
_a 8a _a   0b 6b 0b   4c 0c 2c
6a _a _a   0b 0b 8b   3c 0c 9c

1d 9d 3d   8e 0e 2e   7f 6f 0f
0d 0d 8d   0e 3e 0e   1f 2f 0f
0d 5d 0d   7e 0e 0e   8f 9f 3f

5g 0g 1g   6h 8h 0h   0i 3i 7i
8g 0g 0g   0h 0h 0h   0i 4i 1i
0g 3g 7g   2h 0h 0h   5i 8i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_nwc():
    puzzle_string = f"""
    hidden_unique_rectangle_nwc.sudoku
    9

3a 8a 9a   2b 1b 5b   4c 0c 0c
_a _a 4a   8b 9b 0b   1c 3c 0c
_a 1a _a   4b 0b 3b   8c 0c 0c

4d 5d 2d   0e 3e 1e   9f 8f 0f
1d 3d 0d   9e 8e 2e   5f 0f 4f
0d 0d 8d   0e 0e 4e   2f 1f 3f

0g 4g 1g   0h 2h 0h   3i 0i 0i
0g 2g 3g   1h 0h 9h   7i 4i 0i
0g 0g 0g   3h 4h 8h   6i 2i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_sec():
    puzzle_string = f"""
    hidden_unique_rectangle_sec.sudoku
    9

2a 1a _a   0b 0b 5b   0c 0c 0c
_a 7a 4a   0b 2b 0b   6c 5c 9c
_a _a _a   7b 4b 0b   1c 8c 2c

1d 4d 9d   0e 0e 0e   7f 2f 5f
0d 6d 0d   2e 1e 7e   9f 3f 4f
7d 2d 3d   4e 5e 9e   8f 1f 6f

4g 0g 1g   6h 8h 2h   5i 0i 0i
6g 5g 2g   0h 7h 0h   0i 0i 8i
0g 8g 7g   5h 0h 4h   2i 6i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_ser():
    puzzle_string = f"""
    hidden_unique_rectangle_ser.sudoku
    9

_a _a 2a   4b 8b 0b   0c 1c 3c
8a 7a 4a   1b 3b 6b   2c 5c 9c
_a _a _a   0b 0b 2b   8c 4c 0c

1d 2d 7d   0e 4e 9e   0f 8f 5f
0d 8d 5d   0e 0e 0e   9f 2f 0f
0d 6d 0d   2e 5e 8e   0f 7f 1f

2g 3g 0g   0h 0h 0h   0i 6i 0i
5g 4g 6g   7h 2h 3h   1i 9i 8i
7g 0g 0g   0h 6h 4h   5i 3i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_swc():
    puzzle_string = f"""
    hidden_unique_rectangle_swc.sudoku
    9

_a 2a 9a   3b 1b 6b   4c 0c 5c
_a _a 3a   7b 0b 2b   9c 1c 6c
6a _a 1a   4b 0b 0b   3c 2c 0c

0d 0d 2d   8e 0e 0e   1f 6f 3f
1d 8d 0d   6e 7e 3e   2f 0f 0f
9d 3d 6d   0e 0e 1e   8f 0f 0f

0g 1g 0g   0h 0h 7h   6i 0i 0i
3g 9g 0g   1h 6h 0h   7i 0i 2i
2g 6g 7g   9h 0h 8h   5i 0i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_hidden_unique_rectangle_swr():
    puzzle_string = f"""
    hidden_unique_rectangle_swr.sudoku
    9

_a 8a _a   0b 3b 0b   0c 5c 1c
1a _a 9a   5b 7b 0b   4c 6c 0c
5a 6a _a   0b 0b 0b   0c 0c 0c

0d 0d 2d   8e 0e 7e   5f 0f 0f
6d 0d 0d   2e 0e 3e   0f 0f 9f
0d 0d 1d   9e 0e 5e   3f 0f 0f

0g 0g 0g   0h 0h 0h   0i 0i 5i
0g 1g 6g   0h 5h 0h   8i 0i 0i
4g 0g 0g   0h 8h 0h   0i 7i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_jellyfish_0():
    puzzle_string = f"""
    jellyfish_0.sudoku
    9

_a _a 1a   9b 0b 2b   5c 0c 0c
_a _a 6a   0b 0b 0b   0c 0c 0c
2a 9a _a   0b 5b 0b   0c 0c 1c

5d 0d 0d   6e 0e 0e   3f 1f 9f
0d 0d 0d   0e 0e 0e   0f 0f 0f
1d 4d 3d   0e 0e 7e   0f 0f 5f

4g 0g 0g   0h 3h 0h   0i 7i 6i
0g 0g 0g   0h 0h 0h   1i 0i 0i
0g 0g 9g   7h 0h 1h   8i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_jellyfish_1():
    puzzle_string = f"""
    jellyfish_1.sudoku
    9

_a _a _a   4b 5b 9b   0c 0c 0c
5a _a 9a   3b 2b 0b   0c 7c 4c
4a 2a _a   7b 6b 0b   9c 3c 5c

0d 1d 3d   0e 9e 7e   5f 4f 2f
0d 5d 0d   0e 0e 0e   3f 1f 9f
9d 4d 2d   5e 1e 3e   8f 6f 7f

0g 7g 4g   9h 3h 6h   0i 5i 0i
1g 9g 6g   0h 7h 5h   4i 0i 3i
0g 0g 5g   1h 0h 0h   7i 9i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_jellyfish_2():
    puzzle_string = f"""
    jellyfish_2.sudoku
    9

9a 3a _a   0b 7b 0b   6c 8c 5c
7a _a _a   8b 0b 6b   0c 0c 3c
_a _a _a   0b 9b 3b   7c 0c 1c

1d 7d 0d   9e 6e 0e   5f 3f 2f
0d 9d 0d   0e 3e 0e   1f 6f 0f
2d 6d 3d   0e 0e 1e   0f 7f 0f

3g 0g 0g   0h 0h 5h   0i 0i 0i
4g 5g 7g   3h 0h 9h   0i 0i 6i
0g 1g 9g   0h 2h 0h   3i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_jellyfish_of_1_in_rows():
    puzzle_string = f"""
    jellyfish_of_1_in_rows.sudoku
    9

6a _a 9a   5b 7b 3b   0c 8c 2c
8a 7a _a   0b 9b 0b   6c 3c 5c
_a _a 5a   0b 6b 0b   9c 0c 7c

7d 6d 0d   9e 4e 2e   0f 5f 8f
9d 0d 0d   7e 8e 5e   0f 6f 0f
5d 8d 0d   3e 1e 6e   0f 0f 9f

4g 0g 7g   6h 5h 9h   8i 2i 0i
0g 5g 6g   0h 2h 0h   0i 9i 4i
2g 9g 8g   4h 3h 0h   5i 0i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_jellyfish_of_3_in_cols():
    puzzle_string = f"""
    jellyfish_of_3_in_cols.sudoku
    9

2a _a _a   4b 7b 5b   0c 0c 0c
9a _a 7a   0b 6b 8b   2c 5c 4c
_a 5a _a   9b 2b 0b   7c 0c 0c

5d 7d 0d   6e 9e 2e   0f 1f 8f
0d 2d 1d   8e 5e 7e   0f 9f 6f
8d 9d 6d   0e 4e 0e   5f 2f 7f

7g 8g 9g   2h 3h 6h   1i 4i 5i
1g 0g 2g   5h 8h 0h   6i 7i 0i
0g 0g 5g   7h 1h 0h   0i 0i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_locked_candidates_claiming_col():
    puzzle_string = f"""
    locked_candidates_claiming_col.sudoku
    9

5a _a _a   9b 8b 2b   1c 4c 3c
2a 9a 8a   4b 3b 1b   0c 0c 0c
4a _a _a   6b 7b 5b   2c 8c 9c

9d 0d 2d   5e 4e 7e   0f 0f 0f
0d 0d 0d   2e 9e 0e   0f 0f 0f
0d 0d 0d   1e 6e 0e   9f 0f 0f

7g 0g 0g   8h 2h 4h   0i 0i 1i
0g 0g 0g   7h 0h 9h   3i 0i 0i
0g 2g 0g   3h 0h 6h   0i 0i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_locked_candidates_claiming_row():
    puzzle_string = f"""
    locked_candidates_claiming_row.sudoku
    9

6a 9a 2a   3b 7b 8b   5c 1c 4c
_a _a 5a   6b 2b 0b   0c 3c 0c
_a 3a 8a   0b 4b 0b   2c 0c 0c

0d 0d 9d   0e 3e 0e   0f 0f 1f
0d 0d 1d   0e 5e 0e   3f 0f 0f
3d 0d 0d   1e 9e 0e   4f 0f 0f

0g 0g 4g   0h 1h 0h   7i 0i 0i
0g 8g 0g   4h 6h 2h   1i 0i 0i
0g 0g 0g   7h 8h 0h   0i 4i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_locked_candidates_pointing_col():
    puzzle_string = f"""
    locked_candidates_pointing_col.sudoku
    9

2a 6a _a   7b 0b 0b   0c 9c 0c
8a 1a _a   0b 2b 0b   7c 6c 0c
5a 7a _a   0b 4b 6b   1c 2c 0c

4d 8d 7d   0e 9e 0e   6f 0f 2f
3d 5d 1d   6e 8e 2e   4f 7f 9f
9d 2d 6d   4e 0e 7e   0f 0f 0f

6g 9g 8g   0h 3h 0h   2i 4i 7i
7g 4g 2g   0h 6h 0h   3i 5i 1i
1g 3g 5g   2h 7h 4h   9i 8i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_locked_candidates_pointing_row():
    puzzle_string = f"""
    locked_candidates_pointing_row.sudoku
    9

9a _a _a   2b 4b 0b   8c 3c 0c
6a _a _a   7b 8b 3b   2c 1c 9c
8a 2a 3a   1b 0b 9b   4c 0c 0c

0d 0d 0d   0e 9e 2e   0f 8f 0f
0d 8d 2d   0e 0e 0e   0f 9f 0f
0d 9d 0d   6e 7e 8e   0f 2f 0f

2g 0g 8g   9h 0h 4h   1i 0i 0i
7g 0g 9g   0h 2h 0h   0i 0i 8i
0g 3g 0g   8h 0h 7h   9i 0i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_medusa_coloring_3d():
    puzzle_string = f"""
    medusa_coloring_3d.sudoku
    9

_a 3a 8a   0b 1b 0b   0c 0c 0c
4a 5a 2a   7b 9b 6b   1c 8c 3c
1a _a _a   0b 0b 8b   5c 0c 0c

0d 2d 1d   0e 0e 7e   4f 9f 6f
7d 4d 5d   9e 6e 2e   8f 3f 1f
0d 6d 9d   0e 0e 0e   7f 2f 5f

0g 0g 0g   4h 0h 0h   0i 0i 8i
5g 8g 3g   6h 7h 9h   2i 1i 4i
0g 0g 4g   0h 8h 0h   0i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_medusa_coloring_3d_0():
    puzzle_string = f"""
    medusa_coloring_3d_0.sudoku
    9

3a _a _a   0b 0b 0b   8c 0c 0c
_a _a 4a   0b 9b 0b   0c 7c 0c
_a 7a 9a   0b 0b 2b   0c 0c 1c

0d 6d 0d   7e 0e 0e   0f 0f 4f
0d 0d 8d   0e 6e 0e   7f 0f 0f
5d 0d 0d   0e 0e 8e   0f 1f 0f

8g 0g 0g   5h 0h 0h   1i 6i 0i
0g 3g 0g   0h 1h 0h   2i 0i 0i
0g 0g 1g   0h 0h 0h   0i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_naked_pair_col():
    puzzle_string = f"""
    naked_pair_col.sudoku
    9
    9a 6a 1a   0b 0b 5b   7c 4c 8c
    7a 4a 5a   0b 0b 0b   0c 3c 2c
    2a 3a 8a   0b 7b 4b   5c 1c 0c
    
    8d 2d 9d   0e 5e 1e   3f 7f 0f
    1d 7d 3d   0e 0e 0e   0f 5f 0f
    4d 5d 6d   7e 9e 3e   2f 8f 1f
    
    6g 1g 7g   5h 8h 9h   4i 2i 3i
    5g 9g 4g   0h 0h 2h   8i 6i 7i
    3g 8g 2g   0h 0h 7h   1i 9i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_pair_fence():
    puzzle_string = f"""
    naked_pair_fence.sudoku
    9

5a 6a 7a   9b 3b 8b   2c 1c 4c
2a 9a 3a   4b 1b 5b   0c 6c 0c
4a 1a 8a   2b 7b 6b   5c 3c 9c

0d 2d 4d   8e 0e 3e   1f 7f 5f
0d 5d 0d   0e 0e 0e   0f 4f 0f
0d 8d 1d   5e 4e 0e   6f 0f 0f

0g 4g 0g   0h 8h 9h   0i 5i 0i
0g 3g 0g   7h 5h 0h   4i 8i 0i
8g 7g 5g   0h 0h 4h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_naked_pair_row():
    puzzle_string = f"""
    naked_pair_row.sudoku
    9

4a 8a 1a   7b 3b 2b   9c 5c 6c
6a 3a 2a   9b 5b 8b   4c 1c 7c
7a 9a 5a   6b 4b 1b   3c 2c 8c

0d 0d 0d   4e 0e 0e   6f 0f 0f
0d 0d 4d   8e 0e 6e   2f 0f 0f
0d 6d 7d   5e 0e 3e   8f 4f 1f

5g 7g 3g   2h 6h 4h   1i 8i 9i
0g 4g 6g   1h 0h 5h   7i 3i 2i
1g 2g 0g   3h 0h 0h   5i 6i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_4():
    puzzle_string = f"""
    naked_quad_4.sudoku
    9

_a _a _a   0b 7b 0b   0c 0c 0c
_a _a _a   2b 5b 0b   7c 0c 0c
7a _a _a   1b 0b 0b   2c 9c 6c

2d 0d 0d   0e 0e 0e   6f 0f 4f
0d 4d 7d   0e 0e 0e   5f 1f 0f
5d 0d 6d   0e 0e 0e   0f 0f 8f

1g 3g 8g   0h 0h 9h   0i 0i 7i
0g 0g 4g   0h 6h 1h   0i 0i 0i
0g 0g 0g   0h 4h 0h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_5():
    puzzle_string = f"""
    naked_quad_5.sudoku
    9

9a 4a _a   0b 3b 5b   0c 6c 0c
3a 5a _a   6b 0b 0b   0c 0c 0c
_a 8a _a   0b 4b 0b   0c 0c 5c

6d 0d 0d   1e 0e 0e   0f 0f 0f
0d 0d 0d   0e 7e 0e   0f 0f 0f
0d 0d 0d   0e 0e 9e   0f 0f 4f

5g 0g 0g   0h 9h 0h   0i 4i 0i
0g 0g 0g   0h 0h 7h   0i 8i 9i
0g 7g 0g   4h 8h 0h   0i 3i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_6():
    puzzle_string = f"""
    naked_quad_6.sudoku
    9

_a _a _a   0b 1b 0b   0c 5c 7c
_a _a _a   0b 0b 8b   4c 0c 0c
_a _a _a   9b 0b 5b   1c 0c 3c

0d 1d 2d   0e 0e 0e   0f 7f 6f
0d 0d 0d   0e 0e 0e   0f 0f 0f
3d 6d 0d   0e 0e 0e   8f 9f 0f

7g 0g 6g   8h 0h 2h   0i 0i 0i
0g 0g 9g   7h 0h 0h   0i 0i 0i
4g 3g 0g   0h 5h 0h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_7():
    puzzle_string = f"""
    naked_quad_7.sudoku
    9

_a _a 1a   2b 0b 5b   0c 9c 0c
5a _a 6a   0b 0b 4b   2c 7c 0c
2a _a _a   0b 0b 3b   0c 0c 0c

0d 0d 5d   0e 0e 0e   0f 8f 0f
0d 4d 9d   0e 0e 0e   1f 5f 0f
0d 2d 0d   5e 0e 0e   6f 0f 0f

0g 5g 0g   6h 0h 0h   0i 0i 0i
0g 6g 2g   3h 0h 0h   0i 1i 4i
9g 1g 3g   4h 0h 7h   8i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_col():
    puzzle_string = f"""
    naked_quad_col.sudoku
    9

_a _a 1a   4b 0b 0b   0c 0c 0c
_a _a 5a   2b 1b 8b   0c 9c 0c
_a 2a _a   9b 5b 0b   0c 0c 0c

4d 0d 7d   0e 0e 9e   0f 0f 0f
0d 5d 0d   7e 2e 1e   0f 8f 0f
1d 0d 2d   0e 4e 0e   7f 0f 9f

0g 0g 0g   6h 9h 5h   0i 1i 0i
0g 1g 0g   3h 7h 4h   9i 0i 0i
5g 0g 0g   1h 8h 2h   6i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_fence():
    puzzle_string = f"""
    naked_quad_fence.sudoku
    9

_a 5a _a   0b 0b 3b   0c 0c 0c
3a _a 9a   0b 4b 8b   0c 0c 0c
_a 1a _a   6b 0b 0b   0c 0c 0c

0d 9d 6d   0e 3e 0e   4f 0f 8f
0d 3d 8d   0e 0e 0e   7f 0f 0f
1d 0d 7d   8e 0e 0e   3f 5f 0f

0g 0g 0g   0h 0h 1h   0i 7i 0i
0g 0g 0g   4h 8h 5h   9i 0i 2i
0g 0g 0g   3h 0h 0h   0i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_quad_row():
    puzzle_string = f"""
    naked_quad_row.sudoku
    9

_a _a 9a   0b 3b 0b   0c 2c 6c
_a _a _a   0b 0b 0b   0c 0c 0c
_a 6a _a   0b 2b 0b   5c 1c 4c

0d 0d 7d   0e 0e 5e   0f 6f 0f
0d 8d 0d   0e 0e 0e   0f 3f 5f
0d 5d 0d   1e 0e 0e   4f 0f 0f

4g 9g 2g   0h 8h 0h   0i 5i 0i
0g 0g 0g   0h 0h 0h   0i 0i 0i
8g 3g 0g   0h 7h 0h   2i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_triple_col():
    puzzle_string = f"""
    naked_triple_col.sudoku
    9

7a 9a _a   5b 0b 0b   8c 0c 6c
_a _a 8a   6b 0b 7b   0c 0c 0c
_a 6a _a   8b 1b 0b   0c 0c 4c

6d 0d 0d   2e 0e 0e   0f 0f 0f
2d 0d 0d   1e 0e 8e   0f 0f 5f
0d 0d 0d   7e 0e 4e   0f 0f 9f

8g 0g 0g   4h 7h 5h   9i 6i 0i
9g 7g 6g   3h 2h 1h   4i 5i 8i
4g 0g 5g   9h 8h 6h   0i 3i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_triple_fence():
    puzzle_string = f"""
    naked_triple_fence.sudoku
    9

_a 3a _a   0b 0b 5b   1c 0c 0c
_a 7a 1a   9b 0b 4b   6c 2c 0c
_a _a 4a   0b 0b 0b   0c 0c 0c

0d 0d 5d   6e 4e 9e   0f 7f 0f
0d 0d 7d   5e 2e 1e   9f 0f 6f
0d 9d 6d   8e 7e 3e   2f 0f 0f

0g 0g 0g   0h 0h 0h   5i 0i 0i
0g 5g 3g   4h 0h 0h   7i 6i 0i
0g 0g 8g   3h 5h 0h   4i 9i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_naked_triple_row():
    puzzle_string = f"""
    naked_triple_row.sudoku
    9

7a 8a 2a   3b 5b 4b   1c 9c 6c
_a _a _a   2b 6b 7b   4c 5c 8c
4a 5a 6a   8b 9b 1b   3c 2c 7c

0d 0d 1d   5e 0e 0e   6f 0f 0f
5d 7d 0d   6e 0e 9e   2f 0f 1f
0d 6d 0d   0e 0e 8e   5f 0f 0f

6g 3g 7g   4h 8h 5h   9i 1i 2i
0g 4g 0g   0h 0h 6h   0i 3i 5i
0g 0g 5g   9h 0h 0h   0i 6i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_remote_pair_0():
    puzzle_string = f"""
    remote_pair_0.sudoku
    9

_a _a 2a   0b 0b 5b   0c 0c 6c
_a _a _a   6b 0b 2b   0c 0c 9c
3a 1a _a   0b 0b 0b   0c 0c 0c

2d 0d 4d   0e 8e 0e   0f 5f 0f
0d 0d 1d   0e 0e 0e   8f 0f 0f
0d 9d 0d   0e 2e 0e   4f 0f 1f

0g 0g 0g   0h 0h 0h   0i 4i 8i
7g 0g 0g   4h 0h 3h   0i 0i 0i
4g 0g 0g   1h 0h 0h   9i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_remote_pair_1():
    puzzle_string = f"""
    remote_pair_1.sudoku
    9

_a 8a 6a   4b 3b 9b   0c 0c 2c
_a 4a 1a   7b 8b 2b   0c 9c 6c
2a _a 9a   1b 5b 6b   4c 0c 8c

8d 1d 5d   3e 7e 4e   2f 6f 9f
6d 2d 0d   5e 9e 8e   0f 0f 4f
9d 0d 4d   2e 6e 1e   0f 8f 5f

1g 9g 2g   8h 4h 7h   6i 5i 3i
0g 6g 0g   9h 2h 5h   8i 4i 1i
4g 5g 8g   6h 1h 3h   9i 2i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_remote_pair_2():
    puzzle_string = f"""
    remote_pair_2.sudoku
    9

1a 2a 8a   9b 4b 6b   5c 3c 7c
3a 6a 7a   1b 2b 5b   4c 8c 9c
4a 9a 5a   3b 7b 8b   0c 0c 0c

8d 5d 4d   7e 0e 1e   0f 0f 0f
2d 1d 0d   8e 5e 0e   0f 7f 4f
0d 7d 3d   2e 0e 4e   1f 5f 8f

5g 4g 2g   6h 8h 0h   7i 0i 0i
0g 3g 0g   4h 1h 7h   8i 2i 5i
7g 8g 1g   5h 0h 2h   0i 4i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_remote_pair_row():
    puzzle_string = f"""
    remote_pair_row.sudoku
    9

1a 9a _a   2b 6b 5b   0c 3c 0c
6a _a 4a   0b 0b 9b   5c 0c 2c
5a 3a 2a   4b 7b 8b   0c 6c 0c

0d 5d 1d   0e 4e 6e   2f 9f 0f
2d 6d 0d   0e 9e 0e   0f 4f 5f
9d 4d 3d   7e 5e 2e   8f 1f 6f

0g 1g 5g   6h 2h 4h   0i 0i 0i
4g 0g 9g   5h 0h 0h   6i 2i 0i
0g 2g 6g   9h 8h 0h   0i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_jellyfish_0():
    puzzle_string = f"""
    shashimi_jellyfish_0.sudoku
    9

2a 9a _a   4b 0b 3b   6c 0c 5c
7a 4a _a   0b 6b 5b   2c 3c 0c
3a 5a 6a   2b 0b 1b   4c 0c 0c

0d 0d 0d   0e 1e 4e   3f 6f 2f
6d 3d 0d   7e 0e 2e   0f 0f 4f
4d 1d 2d   6e 3e 0e   5f 0f 0f

0g 6g 0g   1h 4h 0h   9i 2i 3i
0g 0g 4g   3h 2h 0h   0i 5i 6i
0g 2g 3g   0h 0h 6h   7i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_jellyfish_1():
    puzzle_string = f"""
    shashimi_jellyfish_1.sudoku
    9

_a _a 2a   0b 7b 0b   0c 0c 0c
6a _a _a   0b 1b 8b   0c 0c 4c
_a _a _a   0b 0b 0b   3c 7c 0c

0d 7d 0d   1e 0e 0e   6f 0f 8f
0d 0d 9d   0e 0e 0e   4f 0f 0f
8d 0d 5d   0e 0e 9e   0f 2f 0f

0g 2g 8g   0h 0h 0h   0i 0i 0i
5g 0g 0g   7h 3h 0h   0i 0i 6i
0g 0g 0g   0h 9h 0h   5i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_jellyfish_2():
    puzzle_string = f"""
    shashimi_jellyfish_2.sudoku
    9

_a _a 5a   0b 0b 7b   8c 6c 0c
_a _a 6a   0b 0b 0b   5c 0c 0c
4a _a _a   0b 5b 6b   2c 0c 7c

0d 0d 0d   3e 4e 0e   6f 5f 8f
5d 0d 0d   7e 6e 8e   0f 0f 2f
8d 6d 0d   0e 2e 5e   0f 7f 0f

1g 5g 7g   6h 0h 0h   0i 0i 3i
6g 4g 8g   0h 7h 3h   0i 0i 5i
3g 9g 2g   5h 0h 4h   7i 0i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_jellyfish_3():
    puzzle_string = f"""
    shashimi_jellyfish_3.sudoku
    9

_a 2a _a   6b 3b 0b   5c 8c 0c
8a 5a 6a   1b 0b 2b   3c 7c 0c
9a 3a _a   7b 8b 5b   0c 6c 2c

0d 8d 0d   2e 1e 7e   0f 9f 0f
1d 6d 2d   3e 0e 0e   7f 0f 8f
0d 7d 9d   0e 6e 8e   2f 1f 0f

6g 4g 5g   8h 2h 1h   9i 3i 7i
0g 1g 0g   9h 0h 6h   8i 0i 0i
0g 9g 8g   0h 0h 3h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_swordfish_0():
    puzzle_string = f"""
    shashimi_swordfish_0.sudoku
    9

_a _a 9a   0b 6b 4b   0c 0c 7c
8a _a _a   1b 0b 0b   5c 0c 0c
1a _a _a   3b 0b 5b   0c 9c 0c

0d 0d 0d   9e 0e 0e   0f 0f 5f
0d 0d 1d   0e 0e 0e   7f 0f 0f
2d 0d 0d   0e 0e 7e   0f 0f 0f

0g 2g 0g   7h 0h 1h   0i 0i 9i
0g 0g 5g   0h 0h 3h   0i 0i 4i
6g 0g 0g   4h 9h 0h   3i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_swordfish_1():
    puzzle_string = f"""
    shashimi_swordfish_1.sudoku
    9

_a _a _a   0b 3b 0b   0c 0c 8c
_a _a 3a   0b 9b 0b   0c 2c 0c
9a 4a _a   8b 0b 6b   5c 3c 0c

2d 3d 1d   6e 0e 0e   0f 7f 9f
0d 0d 5d   0e 0e 0e   3f 0f 2f
7d 9d 0d   0e 0e 3e   1f 5f 6f

0g 0g 6g   0h 0h 2h   0i 1i 3i
0g 2g 0g   3h 6h 0h   7i 0i 0i
3g 0g 0g   0h 0h 0h   2i 6i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_swordfish_2():
    puzzle_string = f"""
    shashimi_swordfish_2.sudoku
    9

_a _a _a   0b 0b 0b   0c 5c 0c
_a _a 6a   0b 1b 0b   0c 0c 2c
3a 5a _a   0b 0b 2b   1c 0c 0c

0d 1d 3d   0e 0e 5e   0f 6f 9f
0d 0d 5d   0e 0e 0e   8f 0f 0f
6d 9d 0d   1e 0e 0e   3f 2f 0f

0g 0g 8g   7h 0h 0h   0i 9i 4i
2g 0g 0g   0h 9h 0h   5i 0i 0i
0g 7g 0g   0h 0h 0h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_swordfish_3():
    puzzle_string = f"""
    shashimi_swordfish_3.sudoku
    9

_a _a 6a   2b 8b 5b   0c 1c 0c
_a 9a _a   0b 1b 3b   8c 0c 7c
8a 1a _a   7b 0b 9b   5c 3c 0c

0d 6d 0d   5e 0e 0e   0f 0f 1f
2d 0d 1d   0e 0e 0e   0f 0f 5f
0d 5d 0d   0e 0e 1e   0f 8f 0f

0g 4g 0g   1h 0h 2h   0i 0i 8i
1g 0g 0g   3h 9h 0h   0i 5i 0i
0g 2g 0g   8h 0h 7h   1i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_swordfish_4():
    puzzle_string = f"""
    shashimi_swordfish_4.sudoku
    9

_a 2a 7a   3b 9b 6b   5c 4c 0c
5a 6a 8a   8b 0b 0b   9c 0c 2c
4a 9a _a   0b 2b 5b   0c 6c 3c

0d 8d 2d   0e 5e 7e   4f 3f 0f
0d 0d 0d   9e 0e 2e   0f 5f 0f
0d 5d 0d   4e 8e 3e   2f 0f 0f

0g 1g 5g   2h 0h 8h   0i 9i 4i
2g 0g 9g   0h 0h 0h   0i 8i 5i
0g 0g 0g   5h 0h 9h   3i 2i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_swordfish_5():
    puzzle_string = f"""
    shashimi_swordfish_5.sudoku
    9

7a 2a _a   0b 1b 0b   3c 5c 4c
8a _a 3a   4b 5b 2b   7c 0c 6c
5a 4a _a   0b 0b 0b   0c 0c 8c

2d 0d 0d   0e 0e 0e   8f 7f 5f
0d 0d 8d   1e 7e 5e   0f 0f 3f
0d 5d 7d   0e 0e 0e   1f 0f 9f

0g 0g 5g   0h 0h 1h   0i 8i 7i
1g 7g 0g   5h 8h 0h   6i 0i 2i
6g 8g 2g   0h 4h 0h   5i 0i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_sword_fish_cols_1_fin():
    puzzle_string = f"""
    shashimi_sword_fish_cols_1_fin.sudoku
    9

_a 4a 7a   2b 3b 0b   8c 9c 6c
_a 9a 3a   6b 8b 0b   0c 0c 1c
_a 6a _a   0b 9b 0b   0c 0c 3c

6d 3d 0d   0e 7e 0e   9f 1f 8f
0d 7d 1d   9e 6e 8e   3f 5f 0f
9d 8d 0d   3e 0e 0e   6f 7f 0f

7g 5g 0g   0h 0h 6h   2i 3i 9i
3g 1g 6g   7h 2h 9h   4i 8i 5i
0g 2g 9g   0h 5h 3h   1i 6i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_sword_fish_cols_2_fins():
    puzzle_string = f"""
    shashimi_sword_fish_cols_2_fins.sudoku
    9

_a _a _a   8b 4b 0b   5c 2c 0c
5a _a 4a   3b 0b 0b   9c 0c 8c
_a 8a _a   0b 0b 5b   0c 0c 4c

4d 5d 9d   0e 7e 0e   0f 0f 1f
8d 0d 0d   0e 0e 0e   0f 4f 5f
1d 3d 6d   4e 5e 8e   2f 7f 9f

3g 4g 0g   9h 0h 0h   0i 5i 0i
2g 0g 8g   5h 0h 6h   4i 0i 0i
0g 6g 5g   0h 0h 4h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_sword_fish_rows_1_fin():
    puzzle_string = f"""
    shashimi_sword_fish_rows_1_fin.sudoku
    9

5a 8a 6a   2b 4b 1b   3c 9c 7c
_a _a 9a   7b 8b 0b   2c 0c 6c
_a 2a 7a   9b 0b 6b   8c 0c 0c

6d 0d 8d   0e 9e 0e   7f 0f 0f
2d 9d 0d   6e 0e 7e   0f 8f 0f
7d 0d 0d   8e 1e 0e   9f 6f 0f

9g 7g 0g   4h 6h 8h   1i 2i 0i
8g 0g 0g   0h 2h 0h   6i 7i 9i
0g 6g 2g   0h 7h 9h   0i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_sword_fish_rows_2_fins():
    puzzle_string = f"""
    shashimi_sword_fish_rows_2_fins.sudoku
    9

_a 7a _a   9b 1b 0b   2c 6c 3c
_a _a _a   0b 0b 6b   0c 7c 1c
1a 6a _a   0b 3b 0b   5c 8c 0c

0d 2d 0d   0e 0e 0e   8f 3f 0f
0d 4d 0d   0e 2e 0e   0f 1f 0f
0d 1d 6d   0e 0e 0e   0f 9f 2f

0g 9g 4g   0h 5h 0h   0i 2i 7i
2g 5g 7g   3h 0h 0h   0i 4i 0i
6g 0g 1g   0h 0h 2h   0i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_00():
    puzzle_string = f"""
    shashimi_x_wing_00.sudoku
    9

1a _a _a   0b 8b 0b   6c 0c 0c
_a _a _a   6b 0b 0b   8c 0c 0c
_a 6a _a   1b 0b 3b   0c 0c 2c

0d 0d 0d   7e 0e 0e   0f 0f 9f
4d 0d 9d   0e 0e 0e   1f 0f 3f
3d 0d 0d   0e 0e 9e   0f 0f 0f

5g 0g 0g   4h 0h 8h   0i 9i 0i
0g 0g 7g   0h 0h 2h   0i 0i 0i
0g 0g 3g   0h 5h 0h   0i 0i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_01():
    puzzle_string = f"""
    shashimi_x_wing_01.sudoku
    9

1a _a 8a   0b 0b 5b   0c 0c 4c
_a _a 5a   7b 0b 4b   0c 8c 9c
_a _a _a   0b 0b 0b   5c 0c 0c

0d 0d 0d   0e 0e 7e   0f 0f 2f
0d 9d 0d   0e 8e 0e   0f 7f 0f
6d 0d 0d   3e 0e 0e   0f 0f 0f

0g 0g 1g   0h 0h 0h   0i 0i 0i
9g 8g 0g   2h 0h 3h   7i 0i 0i
2g 0g 0g   6h 0h 0h   9i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_02():
    puzzle_string = f"""
    shashimi_x_wing_02.sudoku
    9

_a 9a _a   5b 0b 0b   0c 0c 0c
_a 6a _a   0b 7b 2b   8c 0c 4c
_a _a _a   9b 8b 4b   0c 0c 0c

3d 2d 0d   0e 0e 0e   4f 0f 6f
0d 0d 6d   0e 0e 0e   2f 0f 0f
7d 0d 4d   0e 0e 0e   0f 1f 9f

0g 0g 0g   3h 9h 1h   0i 0i 0i
9g 0g 7g   8h 4h 0h   0i 2i 0i
0g 0g 0g   0h 0h 7h   0i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_03():
    puzzle_string = f"""
    shashimi_x_wing_03.sudoku
    9

5a _a _a   0b 2b 0b   1c 0c 9c
2a _a 9a   3b 0b 0b   0c 5c 4c
_a _a _a   0b 0b 8b   0c 0c 6c

0d 1d 0d   0e 0e 4e   0f 0f 0f
0d 0d 7d   0e 0e 0e   5f 0f 0f
0d 0d 0d   2e 0e 0e   0f 1f 0f

1g 0g 0g   9h 0h 0h   0i 0i 0i
4g 5g 0g   0h 0h 2h   9i 0i 1i
9g 0g 3g   0h 6h 0h   0i 0i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_04():
    puzzle_string = f"""
    shashimi_x_wing_04.sudoku
    9

7a 2a 8a   0b 1b 0b   9c 0c 5c
_a 9a _a   0b 0b 0b   8c 0c 0c
_a _a 3a   0b 9b 8b   0c 4c 0c

0d 0d 9d   8e 2e 0e   7f 0f 3f
8d 7d 0d   0e 3e 9e   0f 5f 0f
2d 3d 1d   0e 0e 6e   4f 8f 9f

0g 1g 0g   9h 4h 0h   5i 0i 8i
9g 8g 2g   0h 0h 0h   0i 0i 4i
0g 0g 0g   0h 8h 0h   0i 9i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_05():
    puzzle_string = f"""
    shashimi_x_wing_05.sudoku
    9

5a 9a _a   4b 0b 0b   8c 3c 2c
_a _a 4a   0b 0b 2b   7c 1c 5c
1a 2a _a   8b 5b 0b   6c 9c 4c

2d 7d 0d   1e 0e 0e   0f 4f 6f
3d 4d 0d   0e 0e 0e   0f 7f 1f
9d 6d 1d   7e 4e 5e   2f 8f 3f

7g 1g 2g   6h 8h 4h   3i 5i 9i
0g 0g 9g   5h 0h 0h   4i 0i 7i
4g 5g 0g   0h 7h 9h   1i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_06():
    puzzle_string = f"""
    shashimi_x_wing_06.sudoku
    9

7a _a 5a   3b 0b 0b   9c 2c 4c
4a _a 6a   5b 2b 0b   7c 3c 8c
3a 2a _a   0b 7b 4b   6c 5c 1c

5d 4d 1d   2e 9e 3e   8f 7f 6f
0d 3d 0d   7e 4e 0e   5f 1f 2f
2d 0d 7d   0e 1e 5e   4f 9f 3f

8g 7g 3g   4h 5h 2h   1i 6i 9i
0g 0g 4g   0h 3h 7h   2i 8i 5i
0g 5g 2g   0h 0h 0h   3i 4i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_07():
    puzzle_string = f"""
    shashimi_x_wing_07.sudoku
    9

4a 7a _a   6b 9b 0b   5c 0c 1c
9a 6a _a   8b 5b 1b   0c 0c 0c
5a 1a _a   0b 0b 4b   0c 9c 6c

2d 9d 6d   0e 1e 0e   4f 0f 5f
8d 5d 7d   4e 0e 0e   1f 6f 0f
3d 4d 1d   5e 6e 0e   2f 7f 0f

1g 8g 5g   9h 0h 0h   6i 0i 0i
6g 3g 0g   2h 0h 5h   0i 1i 0i
7g 2g 0g   1h 8h 6h   0i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_08():
    puzzle_string = f"""
    shashimi_x_wing_08.sudoku
    9

4a 7a _a   6b 9b 0b   5c 0c 1c
9a 6a _a   8b 5b 1b   0c 0c 0c
5a 1a _a   0b 0b 4b   0c 9c 6c

2d 9d 6d   0e 1e 0e   4f 0f 5f
8d 5d 7d   4e 0e 0e   1f 6f 0f
3d 4d 1d   5e 6e 0e   2f 7f 0f

1g 8g 5g   9h 0h 0h   6i 0i 0i
6g 3g 0g   2h 0h 5h   0i 1i 0i
7g 2g 0g   1h 8h 6h   0i 5i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_09():
    puzzle_string = f"""
    shashimi_x_wing_09.sudoku
    9

1a _a _a   0b 9b 7b   5c 0c 4c
_a 4a 9a   5b 1b 6b   7c 2c 0c
5a 7a _a   0b 0b 4b   0c 9c 1c

2d 9d 8d   4e 6e 5e   1f 0f 0f
7d 1d 4d   9e 0e 0e   2f 5f 6f
0d 0d 5d   1e 7e 2e   8f 4f 9f

9g 5g 0g   0h 2h 0h   4i 1i 0i
0g 2g 1g   7h 4h 9h   0i 0i 5i
4g 0g 0g   0h 5h 1h   9i 0i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_col_1_fin():
    puzzle_string = f"""
    shashimi_x_wing_col_1_fin.sudoku
    9

3a _a 4a   6b 1b 0b   0c 7c 0c
_a _a 1a   0b 0b 0b   6c 4c 9c
_a 6a 8a   0b 4b 0b   0c 0c 0c

1d 4d 6d   0e 0e 8e   9f 2f 7f
0d 3d 0d   0e 2e 6e   4f 5f 0f
5d 0d 2d   4e 9e 0e   0f 0f 6f

6g 0g 3g   0h 7h 0h   5i 9i 4i
4g 0g 0g   0h 0h 0h   0i 6i 0i
0g 1g 0g   0h 6h 4h   0i 0i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_col_2_fins():
    puzzle_string = f"""
    shashimi_x_wing_col_2_fins.sudoku
    9

7a _a 3a   5b 4b 0b   0c 8c 6c
4a _a 5a   9b 8b 6b   0c 0c 0c
8a _a 6a   0b 0b 7b   4c 0c 5c

1d 5d 4d   0e 6e 0e   0f 7f 8f
9d 3d 8d   7e 0e 0e   5f 6f 0f
2d 6d 7d   8e 5e 0e   3f 1f 0f

6g 8g 9g   4h 0h 0h   0i 5i 0i
5g 0g 2g   1h 0h 8h   6i 0i 0i
3g 0g 1g   6h 9h 5h   8i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_row_1_fin():
    puzzle_string = f"""
    shashimi_x_wing_row_1_fin.sudoku
    9

7a _a _a   0b 0b 9b   0c 3c 2c
_a 9a 3a   2b 0b 0b   5c 6c 7c
2a _a 6a   7b 3b 0b   0c 4c 0c

0d 1d 9d   4e 8e 7e   2f 5f 0f
0d 2d 5d   1e 9e 6e   7f 8f 0f
0d 7d 8d   3e 5e 2e   0f 9f 0f

0g 6g 0g   9h 7h 3h   0i 2i 5i
9g 0g 7g   0h 2h 0h   3i 1i 0i
5g 3g 2g   8h 0h 0h   0i 7i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_shashimi_x_wing_row_2_fins():
    puzzle_string = f"""
    shashimi_x_wing_row_2_fins.sudoku
    9

_a 9a 7a   1b 0b 4b   0c 0c 3c
4a _a _a   0b 3b 7b   0c 9c 0c
_a 3a _a   6b 0b 9b   4c 8c 7c

7d 0d 0d   0e 9e 8e   0f 0f 0f
9d 5d 0d   2e 6e 0e   0f 7f 4f
0d 0d 0d   7e 0e 0e   0f 0f 9f

0g 1g 0g   0h 7h 2h   9i 0i 0i
0g 2g 9g   0h 1h 6h   7i 0i 5i
6g 7g 0g   9h 0h 5h   2i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_simple_coloring_0():
    puzzle_string = f"""
    simple_coloring_0.sudoku
    9

3a 5a 6a   2b 0b 0b   9c 0c 4c
4a 2a 9a   5b 3b 0b   0c 6c 0c
_a _a 7a   9b 4b 6b   5c 2c 3c

0d 0d 5d   4e 0e 0e   0f 0f 0f
6d 9d 3d   1e 7e 2e   4f 5f 8f
0d 4d 0d   0e 0e 5e   0f 0f 0f

5g 6g 0g   8h 0h 4h   7i 3i 9i
0g 3g 4g   7h 5h 9h   6i 0i 2i
9g 7g 0g   0h 0h 0h   0i 4i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_simple_coloring_1():
    puzzle_string = f"""
    simple_coloring_1.sudoku
    9

6a _a 1a   4b 0b 5b   9c 2c 8c
8a 4a _a   9b 1b 2b   7c 6c 0c
2a _a 9a   0b 0b 0b   1c 0c 4c

0d 1d 0d   0e 0e 4e   0f 0f 0f
9d 8d 6d   7e 2e 3e   5f 4f 1f
4d 0d 0d   1e 0e 0e   0f 0f 0f

1g 6g 8g   0h 0h 7h   4i 9i 0i
7g 9g 4g   0h 8h 1h   0i 0i 6i
0g 2g 0g   6h 4h 9h   8i 1i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_simple_coloring_trap_0():
    puzzle_string = f"""
    simple_coloring_trap_0.sudoku
    9

5a _a _a   0b 2b 7b   0c 0c 4c
_a _a 4a   0b 0b 0b   5c 0c 0c
_a 7a 6a   0b 0b 4b   0c 3c 0c

0d 0d 0d   0e 0e 0e   0f 2f 3f
0d 0d 7d   0e 3e 0e   6f 0f 0f
8d 3d 0d   0e 0e 0e   0f 0f 0f

0g 5g 0g   6h 0h 0h   3i 8i 0i
0g 0g 8g   0h 0h 0h   4i 0i 0i
6g 0g 0g   4h 8h 0h   0i 0i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sue_de_coq_0():
    puzzle_string = f"""
    sue_de_coq_0.sudoku
    9

_a 7a _a   0b 9b 6b   4c 0c 0c
_a _a _a   0b 0b 5b   6c 0c 0c
_a _a _a   0b 0b 0b   0c 2c 0c

0d 0d 0d   6e 0e 4e   0f 5f 1f
0d 4d 0d   8e 0e 1e   0f 9f 0f
8d 9d 0d   2e 0e 3e   0f 0f 0f

0g 3g 0g   0h 0h 0h   0i 0i 0i
0g 0g 7g   5h 0h 0h   0i 0i 0i
0g 0g 9g   1h 0h 2h   0i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sue_de_coq_1():
    puzzle_string = f"""
    sue_de_coq_1.sudoku
    9

_a _a 8a   0b 0b 0b   0c 0c 0c
_a 4a 2a   0b 8b 0b   6c 0c 0c
_a 9a _a   5b 0b 4b   0c 1c 0c

0d 0d 5d   0e 0e 9e   1f 4f 0f
0d 0d 0d   0e 0e 0e   0f 0f 0f
0d 3d 4d   2e 0e 0e   7f 0f 0f

8g 7g 0g   1h 0h 2h   0i 6i 0i
0g 0g 6g   0h 7h 5h   3i 8i 0i
0g 0g 0g   0h 0h 0h   9i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sue_de_coq_2():
    puzzle_string = f"""
    sue_de_coq_2.sudoku
    9

_a _a _a   0b 5b 8b   0c 2c 0c
2a 8a _a   6b 1b 0b   0c 0c 0c
_a _a 1a   2b 9b 0b   0c 3c 8c

7d 6d 2d   5e 8e 1e   4f 9f 3f
5d 1d 4d   0e 2e 0e   7f 8f 6f
0d 0d 8d   4e 7e 6e   2f 1f 5f

0g 2g 0g   0h 3h 0h   8i 0i 0i
0g 0g 0g   8h 4h 5h   0i 6i 2i
8g 0g 0g   1h 6h 2h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sue_de_coq_col():
    puzzle_string = f"""
    sue_de_coq_col.sudoku
    9

_a _a _a   0b 9b 3b   0c 6c 0c
3a 9a 1a   0b 6b 0b   0c 4c 0c
_a _a 6a   0b 0b 0b   9c 0c 3c

4d 1d 7d   9e 5e 2e   8f 3f 6f
0d 3d 0d   0e 4e 0e   0f 2f 0f
8d 6d 2d   0e 0e 7e   4f 5f 9f

0g 0g 8g   0h 0h 0h   2i 0i 0i
0g 7g 3g   0h 2h 0h   6i 8i 5i
0g 2g 0g   5h 0h 0h   3i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sue_de_coq_row():
    puzzle_string = f"""
    sue_de_coq_row.sudoku
    9

_a 4a _a   0b 9b 8b   7c 5c 6c
8a 9a 7a   6b 4b 5b   3c 1c 2c
_a _a 5a   1b 0b 7b   4c 9c 8c

0d 0d 4d   5e 8e 0e   0f 7f 0f
0d 8d 0d   0e 0e 0e   0f 6f 4f
0d 1d 0d   0e 6e 4e   8f 0f 0f

0g 7g 0g   8h 5h 2h   6i 4i 0i
4g 2g 6g   9h 7h 3h   0i 8i 0i
0g 5g 8g   4h 1h 6h   0i 0i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_0():
    puzzle_string = f"""
    swordfish_0.sudoku
    9

2a _a _a   0b 0b 0b   0c 0c 0c
7a _a 5a   0b 0b 6b   0c 0c 1c
3a _a 9a   0b 8b 0b   2c 0c 7c

0d 0d 0d   0e 0e 5e   0f 0f 0f
1d 0d 8d   3e 0e 9e   7f 0f 2f
0d 0d 0d   1e 0e 0e   0f 0f 0f

4g 0g 6g   0h 1h 0h   9i 0i 3i
8g 0g 0g   2h 0h 0h   6i 0i 4i
0g 0g 0g   0h 0h 0h   0i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_1():
    puzzle_string = f"""
    swordfish_1.sudoku
    9
    
8a 3a 4a   7b 2b 0b   0c 1c 5c
2a 1a 5a   8b 0b 0b   0c 7c 0c
_a 9a _a   0b 5b 1b   0c 2c 8c

0d 7d 2d   6e 3e 5e   0f 8f 4f
0d 4d 3d   9e 8e 7e   0f 5f 2f
5d 8d 0d   0e 1e 0e   7f 3f 0f

3g 0g 0g   5h 0h 0h   8i 4i 0i
4g 0g 0g   0h 0h 8h   5i 9i 3i
0g 5g 8g   0h 4h 0h   2i 6i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_2():
    puzzle_string = f"""
    swordfish_2.sudoku
    9

2a _a _a   0b 0b 0b   0c 0c 0c
_a _a 4a   9b 0b 6b   0c 3c 0c
6a 3a _a   0b 0b 4b   0c 0c 5c

0d 0d 0d   0e 0e 3e   0f 1f 6f
0d 0d 3d   0e 0e 0e   2f 0f 0f
7d 4d 0d   1e 0e 0e   0f 0f 0f

1g 0g 0g   3h 0h 0h   0i 9i 2i
0g 5g 0g   2h 0h 7h   4i 0i 0i
0g 0g 0g   0h 0h 0h   0i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_3():
    puzzle_string = f"""
    swordfish_3.sudoku
    9

5a 7a 1a   3b 0b 0b   0c 0c 0c
6a 2a _a   0b 4b 0b   0c 0c 0c
4a _a _a   0b 0b 7b   1c 0c 0c

0d 0d 4d   0e 1e 0e   0f 2f 0f
7d 0d 0d   8e 0e 5e   0f 0f 4f
0d 8d 0d   0e 9e 0e   7f 0f 0f

0g 0g 3g   9h 0h 0h   0i 0i 5i
0g 0g 0g   0h 2h 0h   0i 4i 1i
0g 0g 0g   0h 0h 3h   2i 7i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_4():
    puzzle_string = f"""
    swordfish_4.sudoku
    9

_a _a _a   7b 0b 0b   0c 0c 5c
_a 5a _a   0b 6b 0b   9c 0c 0c
4a _a 9a   0b 8b 0b   0c 7c 0c

8d 0d 7d   0e 0e 0e   0f 0f 0f
0d 1d 6d   0e 0e 0e   4f 2f 0f
0d 0d 0d   0e 0e 0e   3f 0f 7f

0g 7g 0g   0h 9h 0h   1i 0i 3i
0g 0g 2g   0h 5h 0h   0i 4i 0i
9g 0g 0g   0h 0h 1h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_5():
    puzzle_string = f"""
    swordfish_5.sudoku
    9

_a _a 1a   8b 7b 9b   0c 0c 5c
5a 9a 8a   0b 0b 3b   7c 2c 1c
_a 7a 6a   5b 2b 1b   8c 9c 0c

0d 1d 9d   7e 0e 5e   3f 0f 0f
7d 0d 5d   0e 0e 0e   0f 1f 0f
0d 0d 4d   1e 0e 2e   5f 7f 0f

0g 5g 7g   2h 0h 0h   9i 4i 0i
0g 8g 3g   9h 0h 7h   2i 5i 6i
9g 0g 2g   0h 5h 0h   1i 0i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_6():
    puzzle_string = f"""
    swordfish_6.sudoku
    9

_a _a 6a   3b 9b 0b   7c 0c 4c
4a 2a 1a   0b 7b 8b   3c 0c 9c
7a 9a 3a   0b 0b 4b   8c 0c 0c

0d 7d 8d   9e 1e 5e   4f 0f 2f
0d 1d 2d   8e 4e 6e   9f 0f 7f
9d 0d 4d   0e 3e 0e   1f 8f 0f

2g 0g 0g   4h 0h 0h   6i 9i 1i
0g 4g 9g   0h 2h 0h   5i 7i 0i
1g 0g 0g   0h 0h 9h   2i 4i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_of_5_in_rows():
    puzzle_string = f"""
    swordfish_of_5_in_rows.sudoku
    9

3a _a 6a   0b 4b 8b   2c 7c 9c
9a _a _a   7b 2b 6b   0c 0c 3c
2a 8a 7a   3b 9b 0b   6c 0c 4c

8d 9d 1d   6e 3e 4e   7f 2f 5f
4d 0d 0d   8e 7e 9e   1f 3f 6f
7d 6d 3d   2e 0e 0e   4f 9f 8f

5g 0g 0g   0h 8h 2h   3i 6i 0i
1g 0g 0g   0h 6h 3h   0i 4i 0i
6g 3g 0g   4h 0h 7h   9i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_swordfish_of_8_in_cols():
    puzzle_string = f"""
    swordfish_of_8_in_cols.sudoku
    9

6a 8a _a   0b 3b 4b   0c 0c 2c
3a _a _a   0b 0b 0b   0c 0c 0c
5a 7a _a   0b 9b 2b   0c 3c 6c

0d 0d 0d   2e 0e 3e   0f 0f 0f
2d 9d 0d   5e 0e 7e   0f 6f 3f
0d 0d 0d   9e 0e 8e   0f 0f 0f

1g 4g 0g   0h 2h 9h   0i 7i 5i
0g 0g 0g   4h 0h 1h   0i 0i 9i
9g 0g 0g   3h 0h 0h   0i 4i 1i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_00():
    puzzle_string = f"""
    unique_rectangle_type3_00.sudoku
    9

9a 3a _a   0b 0b 8b   0c 0c 0c
_a _a _a   3b 0b 0b   0c 8c 5c
6a _a _a   0b 1b 0b   0c 9c 4c

0d 5d 0d   0e 0e 0e   0f 1f 9f
0d 0d 6d   0e 0e 0e   4f 0f 0f
1d 7d 0d   0e 0e 0e   0f 2f 0f

7g 6g 0g   0h 9h 0h   0i 0i 1i
5g 8g 0g   0h 0h 3h   0i 0i 0i
0g 0g 0g   1h 0h 0h   0i 3i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_01():
    puzzle_string = f"""
    unique_rectangle_type3_01.sudoku
    9

8a _a _a   2b 0b 0b   6c 1c 0c
_a _a 5a   0b 0b 1b   0c 0c 0c
_a _a 7a   0b 3b 0b   0c 0c 0c

0d 6d 0d   4e 0e 0e   0f 0f 8f
0d 0d 3d   0e 9e 0e   1f 0f 0f
5d 0d 0d   0e 0e 6e   0f 3f 0f

0g 0g 0g   0h 5h 0h   4i 0i 0i
0g 0g 0g   7h 0h 0h   3i 0i 0i
0g 3g 6g   0h 0h 8h   0i 0i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_02():
    puzzle_string = f"""
    unique_rectangle_type3_02.sudoku
    9

_a _a 5a   0b 6b 0b   0c 4c 0c
2a 4a 7a   0b 0b 0b   0c 1c 0c
6a _a _a   4b 0b 0b   0c 0c 9c

0d 0d 9d   0e 0e 0e   0f 0f 2f
4d 0d 0d   3e 0e 6e   0f 0f 7f
8d 0d 0d   0e 0e 0e   5f 0f 0f

7g 0g 0g   0h 0h 3h   0i 0i 8i
0g 3g 0g   0h 0h 0h   4i 5i 6i
0g 2g 0g   0h 9h 0h   3i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_03():
    puzzle_string = f"""
    unique_rectangle_type3_03.sudoku
    9

_a _a 3a   0b 0b 0b   7c 0c 0c
_a _a _a   0b 0b 8b   0c 0c 0c
5a 4a _a   0b 0b 0b   6c 3c 0c

1d 7d 0d   0e 0e 6e   0f 5f 0f
0d 8d 0d   3e 0e 5e   0f 6f 0f
0d 6d 0d   9e 0e 0e   0f 2f 7f

0g 1g 4g   0h 0h 0h   0i 9i 5i
0g 0g 0g   2h 0h 0h   0i 0i 0i
0g 0g 6g   0h 0h 0h   3i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_04():
    puzzle_string = f"""
    unique_rectangle_type3_04.sudoku
    9

_a _a _a   8b 0b 0b   0c 6c 1c
8a 1a _a   0b 0b 3b   0c 0c 0c
_a 3a _a   0b 4b 0b   0c 9c 5c

7d 0d 0d   0e 0e 0e   0f 3f 9f
0d 0d 2d   0e 0e 0e   5f 0f 0f
3d 4d 0d   0e 0e 0e   0f 0f 6f

4g 2g 0g   0h 3h 0h   0i 5i 0i
0g 0g 0g   1h 0h 0h   0i 4i 8i
1g 6g 0g   0h 0h 8h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_05():
    puzzle_string = f"""
    unique_rectangle_type3_05.sudoku
    9

_a _a 5a   2b 0b 0b   0c 0c 0c
_a 9a _a   0b 0b 7b   4c 0c 2c
_a _a 3a   0b 6b 0b   0c 0c 0c

4d 0d 0d   0e 0e 1e   0f 9f 0f
0d 0d 6d   0e 8e 0e   2f 0f 0f
0d 5d 0d   4e 0e 0e   0f 0f 6f

0g 0g 0g   0h 5h 0h   1i 0i 0i
6g 0g 4g   9h 0h 0h   0i 8i 0i
0g 0g 0g   0h 0h 3h   6i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_06():
    puzzle_string = f"""
    unique_rectangle_type3_06.sudoku
    9

8a _a _a   7b 0b 0b   0c 0c 2c
_a _a _a   5b 2b 6b   0c 0c 0c
_a 5a 7a   0b 0b 4b   0c 0c 3c

7d 0d 0d   0e 0e 0e   5f 0f 0f
0d 8d 0d   0e 0e 0e   0f 3f 0f
0d 0d 4d   0e 0e 0e   0f 0f 7f

9g 0g 0g   6h 0h 0h   7i 1i 0i
0g 0g 0g   4h 9h 3h   0i 0i 0i
4g 0g 0g   0h 0h 2h   0i 0i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_07():
    puzzle_string = f"""
    unique_rectangle_type3_07.sudoku
    9

_a 9a _a   2b 0b 0b   7c 6c 1c
4a 7a 1a   8b 9b 6b   3c 2c 5c
6a 3a 2a   1b 5b 7b   9c 8c 4c

1d 0d 9d   4e 0e 0e   6f 3f 0f
0d 4d 6d   9e 0e 0e   1f 5f 0f
0d 0d 3d   0e 0e 1e   8f 4f 9f

3g 1g 0g   7h 0h 0h   2i 9i 6i
9g 6g 4g   3h 1h 2h   5i 7i 8i
2g 0g 7g   0h 0h 9h   4i 1i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_east_col():
    puzzle_string = f"""
    unique_rectangle_type3_east_col.sudoku
    9

6a _a _a   2b 8b 5b   3c 0c 0c
7a 3a 2a   1b 9b 6b   5c 8c 4c
8a _a 5a   3b 4b 7b   0c 6c 2c

0d 8d 0d   6e 2e 4e   0f 3f 5f
5d 2d 0d   9e 1e 3e   6f 0f 8f
0d 6d 3d   5e 7e 8e   0f 2f 0f

2g 5g 8g   0h 3h 0h   0i 0i 6i
3g 0g 1g   0h 6h 2h   8i 5i 0i
0g 0g 6g   8h 5h 0h   2i 0i 3i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_east_fence():
    puzzle_string = f"""
    unique_rectangle_type3_east_fence.sudoku
    9

5a 2a 9a   7b 3b 6b   4c 1c 8c
6a 7a 8a   0b 0b 1b   2c 0c 0c
3a 4a 1a   8b 2b 9b   7c 6c 5c

2d 9d 5d   6e 0e 0e   0f 4f 0f
0d 6d 3d   0e 0e 2e   5f 8f 0f
0d 8d 4d   0e 0e 5e   0f 2f 6f

9g 3g 7g   1h 6h 4h   8i 5i 2i
4g 5g 6g   2h 0h 0h   0i 7i 1i
8g 1g 2g   0h 0h 7h   6i 0i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_north_row():
    puzzle_string = f"""
    unique_rectangle_type3_north_row.sudoku
    9

9a 8a _a   0b 0b 0b   5c 7c 1c
3a _a _a   8b 0b 0b   2c 9c 6c
7a 2a _a   0b 9b 0b   8c 3c 4c

8d 0d 9d   0e 0e 0e   4f 1f 2f
5d 0d 0d   1e 0e 8e   9f 6f 3f
6d 0d 0d   0e 0e 0e   7f 8f 5f

4g 9g 7g   0h 1h 0h   6i 5i 8i
1g 6g 8g   0h 0h 5h   3i 2i 9i
2g 5g 3g   0h 8h 0h   1i 4i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_south_row():
    puzzle_string = f"""
    unique_rectangle_type3_south_row.sudoku
    9

_a 9a 3a   0b 5b 0b   6c 0c 7c
_a 6a _a   9b 0b 0b   1c 0c 5c
4a _a _a   0b 0b 6b   8c 0c 9c

6d 0d 0d   7e 2e 9e   3f 5f 8f
3d 7d 8d   0e 4e 0e   9f 6f 2f
5d 2d 9d   6e 8e 3e   4f 7f 1f

0g 0g 0g   8h 0h 0h   7i 9i 6i
9g 8g 0g   0h 6h 7h   5i 1i 0i
7g 0g 6g   0h 9h 0h   2i 8i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_unique_rectangle_type3_west_fence():
    puzzle_string = f"""
    unique_rectangle_type3_west_fence.sudoku
    9

1a _a 3a   8b 0b 0b   7c 4c 2c
8a 5a 7a   1b 4b 2b   6c 3c 9c
2a 4a _a   0b 0b 3b   1c 8c 5c

4d 0d 8d   0e 0e 7e   5f 2f 0f
0d 7d 5d   0e 0e 8e   4f 6f 0f
0d 0d 2d   4e 0e 0e   9f 7f 8f

5g 2g 1g   3h 6h 4h   8i 9i 7i
7g 3g 4g   5h 8h 9h   2i 1i 6i
0g 8g 0g   0h 0h 1h   3i 5i 4i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_0():
    puzzle_string = f"""
    wxyz_wing_0.sudoku
    9

_a 6a 7a   0b 3b 1b   0c 0c 9c
_a 3a _a   0b 0b 0b   0c 4c 0c
8a _a 4a   0b 0b 0b   0c 0c 0c

4d 0d 0d   2e 0e 0e   0f 0f 0f
9d 0d 0d   6e 0e 8e   0f 0f 3f
0d 0d 0d   0e 0e 9e   0f 0f 8f

0g 0g 0g   0h 0h 0h   6i 0i 1i
0g 7g 0g   0h 0h 0h   0i 5i 0i
3g 0g 0g   1h 5h 0h   7i 9i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_19():
    puzzle_string = f"""
    wxyz_wing_19.sudoku
    9

9a _a 3a   8b 0b 1b   0c 0c 6c
8a _a 6a   0b 7b 0b   0c 0c 1c
1a 5a 7a   6b 0b 2b   0c 4c 0c

2d 3d 9d   1e 6e 0e   4f 0f 7f
6d 1d 8d   0e 0e 0e   2f 0f 0f
4d 7d 5d   2e 0e 0e   6f 1f 0f

5g 6g 4g   9h 1h 3h   0i 0i 2i
3g 9g 2g   0h 8h 0h   1i 6i 4i
7g 8g 1g   4h 2h 6h   9i 3i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_4():
    puzzle_string = f"""
    wxyz_wing_4.sudoku
    9

_a _a _a   0b 0b 0b   0c 2c 0c
_a _a _a   0b 5b 2b   1c 0c 9c
9a 4a _a   3b 0b 0b   0c 0c 0c

5d 0d 0d   0e 0e 0e   0f 6f 1f
0d 2d 0d   0e 9e 0e   0f 4f 0f
6d 8d 0d   0e 0e 0e   0f 0f 5f

0g 0g 0g   0h 0h 3h   0i 5i 7i
2g 0g 8g   6h 4h 0h   0i 0i 0i
0g 3g 0g   0h 0h 0h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_5():
    puzzle_string = f"""
    wxyz_wing_5.sudoku
    9

_a _a 2a   4b 0b 0b   0c 8c 9c
_a _a _a   8b 3b 2b   0c 4c 1c
8a 4a _a   0b 0b 5b   3c 2c 7c

4d 0d 3d   0e 0e 0e   9f 0f 8f
0d 5d 0d   0e 0e 8e   4f 6f 3f
6d 0d 8d   3e 0e 4e   1f 0f 2f

1g 6g 4g   2h 8h 3h   7i 9i 5i
9g 8g 5g   7h 6h 1h   2i 3i 4i
0g 0g 7g   5h 4h 9h   8i 1i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_6():
    puzzle_string = f"""
    wxyz_wing_6.sudoku
    9

_a _a _a   0b 0b 0b   8c 7c 4c
_a _a 3a   0b 0b 4b   9c 5c 6c
9a 4a _a   0b 0b 8b   2c 1c 3c

3d 0d 0d   1e 4e 9e   7f 2f 8f
1d 0d 4d   0e 5e 7e   3f 6f 9f
0d 7d 9d   3e 0e 6e   5f 4f 1f

5g 3g 0g   4h 0h 2h   1i 9i 7i
4g 9g 0g   0h 0h 0h   6i 0i 2i
0g 0g 2g   0h 0h 0h   4i 0i 5i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_cols_2_fences():
    puzzle_string = f"""
    wxyz_wing_cols_2_fences.sudoku
    9

6a 3a 2a   8b 0b 0b   1c 0c 0c
7a 1a 5a   2b 6b 0b   8c 4c 0c
4a 8a 9a   0b 5b 0b   6c 2c 0c

1d 5d 8d   7e 2e 6e   9f 3f 4f
2d 4d 6d   0e 0e 0e   7f 8f 0f
9d 7d 3d   0e 0e 8e   2f 0f 6f

3g 2g 1g   0h 7h 0h   4i 6i 8i
5g 6g 7g   0h 8h 0h   3i 9i 2i
8g 9g 4g   6h 3h 2h   5i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_cols_3_fences():
    puzzle_string = f"""
    wxyz_wing_cols_3_fences.sudoku
    9

9a _a 7a   2b 0b 0b   5c 0c 0c
6a 2a _a   5b 7b 8b   1c 9c 0c
_a 5a 1a   0b 0b 0b   0c 0c 7c

0d 9d 0d   0e 4e 0e   7f 0f 0f
0d 0d 0d   3e 0e 5e   0f 0f 9f
0d 0d 2d   7e 9e 0e   0f 5f 0f

0g 0g 0g   0h 0h 0h   8i 3i 5i
0g 6g 0g   4h 5h 0h   9i 7i 1i
0g 0g 0g   0h 0h 7h   4i 6i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_rows_2_fences():
    puzzle_string = f"""
    wxyz_wing_rows_2_fences.sudoku
    9

5a 7a 3a   0b 0b 2b   4c 8c 1c
_a _a 9a   7b 4b 5b   2c 3c 6c
4a 6a 2a   3b 1b 8b   5c 7c 9c

0d 5d 1d   0e 7e 0e   6f 0f 8f
2d 0d 6d   0e 0e 0e   7f 0f 3f
0d 4d 7d   0e 0e 0e   9f 1f 0f

6g 0g 5g   0h 3h 7h   8i 0i 4i
7g 3g 8g   0h 0h 4h   1i 0i 0i
0g 2g 4g   8h 0h 0h   3i 0i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_wxyz_wing_rows_3_fences():
    puzzle_string = f"""
    wxyz_wing_rows_3_fences.sudoku
    9

8a _a _a   7b 9b 0b   0c 2c 0c
_a 9a 5a   0b 1b 2b   7c 0c 0c
_a 7a 2a   3b 0b 0b   9c 0c 0c

0d 0d 9d   2e 0e 1e   0f 0f 0f
0d 0d 0d   0e 5e 9e   0f 0f 0f
0d 0d 8d   4e 3e 7e   6f 9f 0f

0g 0g 7g   9h 4h 8h   1i 5i 3i
5g 8g 3g   1h 7h 6h   2i 4i 9i
9g 4g 1g   5h 2h 3h   8i 7i 6i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_w_wing_type_d_0():
    puzzle_string = f"""
    w_wing_type_d_0.sudoku
    9

_a _a _a   8b 0b 0b   2c 0c 0c
3a 6a _a   0b 0b 5b   1c 4c 7c
_a _a _a   0b 3b 0b   0c 0c 0c

0d 2d 0d   0e 0e 0e   0f 0f 0f
0d 4d 0d   5e 2e 9e   0f 8f 0f
0d 0d 0d   0e 0e 0e   0f 9f 0f

0g 0g 0g   0h 6h 0h   0i 0i 0i
7g 9g 3g   4h 0h 0h   0i 5i 6i
0g 0g 2g   0h 0h 3h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_w_wing_type_d_6():
    puzzle_string = f"""
    w_wing_type_d_6.sudoku
    9

7a _a 6a   0b 0b 3b   9c 1c 8c
_a _a 9a   0b 0b 6b   7c 0c 0c
_a 5a _a   9b 7b 0b   6c 2c 0c

0d 0d 0d   8e 6e 0e   4f 7f 0f
0d 0d 0d   3e 9e 7e   0f 0f 0f
0d 0d 7d   0e 4e 5e   3f 0f 0f

0g 6g 8g   7h 1h 9h   0i 3i 0i
9g 7g 0g   0h 3h 0h   1i 0i 0i
2g 1g 3g   6h 0h 4h   0i 9i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_chain():
    puzzle_string = f"""
    xy_chain.sudoku
    9

6a _a _a   1b 9b 5b   0c 3c 2c
2a 1a 3a   7b 0b 8b   5c 0c 9c
_a 9a 5a   0b 0b 2b   1c 0c 0c

0d 3d 1d   4e 0e 7e   0f 0f 0f
4d 0d 6d   5e 0e 9e   0f 0f 3f
0d 0d 9d   0e 0e 3e   4f 8f 0f

3g 0g 7g   9h 5h 1h   6i 2i 0i
9g 6g 2g   0h 7h 4h   0i 0i 0i
1g 5g 0g   0h 0h 6h   0i 0i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_chain_0():
    puzzle_string = f"""
    xy_chain_0.sudoku
    9

6a _a 1a   3b 9b 8b   2c 5c 0c
9a 5a 2a   4b 7b 1b   6c 8c 3c
_a 3a _a   2b 5b 6b   9c 0c 0c

5d 0d 3d   9e 6e 4e   7f 2f 0f
2d 0d 7d   1e 3e 5e   4f 0f 0f
0d 6d 0d   8e 2e 7e   3f 0f 5f

3g 0g 0g   7h 0h 9h   5i 4i 0i
0g 0g 5g   6h 0h 2h   1i 3i 9i
0g 0g 0g   5h 0h 3h   8i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_chain_1():
    puzzle_string = f"""
    xy_chain_1.sudoku
    9

5a 7a 1a   3b 2b 4b   8c 9c 6c
9a 6a 3a   0b 0b 8b   7c 2c 4c
_a 8a _a   6b 7b 9b   3c 1c 5c

3d 9d 7d   0e 0e 5e   0f 4f 0f
1d 5d 0d   0e 3e 2e   0f 7f 0f
0d 2d 0d   9e 0e 7e   5f 3f 1f

7g 3g 0g   0h 8h 1h   0i 6i 0i
0g 4g 0g   7h 9h 6h   1i 5i 3i
6g 1g 0g   2h 0h 3h   0i 8i 7i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_chain_2():
    puzzle_string = f"""
    xy_chain_2.sudoku
    9

_a _a 1a   0b 0b 0b   0c 0c 0c
_a _a 8a   4b 0b 0b   6c 3c 0c
_a 2a 9a   0b 0b 1b   0c 7c 0c

0d 6d 0d   0e 0e 3e   0f 0f 0f
5d 0d 0d   0e 0e 0e   0f 0f 2f
0d 0d 0d   8e 0e 0e   0f 4f 0f

0g 7g 0g   9h 0h 0h   3i 8i 0i
0g 1g 4g   0h 0h 6h   7i 0i 0i
0g 0g 0g   0h 0h 0h   9i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_00():
    puzzle_string = f"""
    xy_wing_00.sudoku
    9

_a _a _a   3b 9b 0b   0c 7c 6c
9a _a _a   0b 0b 0b   2c 8c 0c
8a 3a _a   0b 0b 0b   1c 0c 0c

0d 6d 0d   0e 2e 0e   0f 0f 0f
0d 0d 0d   1e 7e 3e   0f 0f 0f
0d 0d 0d   0e 8e 0e   0f 3f 0f

0g 0g 3g   0h 0h 0h   0i 5i 2i
0g 2g 8g   0h 0h 0h   0i 0i 4i
7g 4g 0g   0h 3h 1h   0i 0i 0i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_cols_2_fences():
    puzzle_string = f"""
    xy_wing_cols_2_fences.sudoku
    9

3a 1a 2a   4b 6b 9b   8c 5c 7c
5a 4a 7a   0b 0b 3b   1c 9c 6c
6a 8a 9a   5b 7b 1b   4c 0c 0c

4d 3d 6d   0e 9e 0e   2f 7f 0f
2d 9d 1d   6e 0e 7e   3f 8f 0f
7d 5d 8d   3e 0e 0e   9f 6f 0f

9g 7g 3g   0h 0h 6h   5i 0i 8i
8g 6g 4g   9h 0h 0h   7i 1i 0i
1g 2g 5g   7h 0h 0h   6i 0i 9i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_north_east_3_fences():
    puzzle_string = f"""
    xy_wing_north_east_3_fences.sudoku
    9

7a _a _a   8b 3b 0b   6c 1c 2c
6a 1a 3a   2b 4b 7b   5c 8c 9c
8a _a _a   1b 0b 6b   3c 4c 7c

0d 8d 6d   0e 0e 0e   0f 5f 3f
5d 9d 7d   6e 1e 3e   8f 2f 4f
3d 0d 0d   5e 8e 0e   0f 7f 6f

0g 6g 8g   9h 0h 0h   0i 3i 5i
4g 7g 5g   3h 6h 8h   2i 9i 1i
9g 3g 0g   0h 0h 0h   0i 6i 8i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_north_west_3_fences():
    puzzle_string = f"""
    xy_wing_north_west_3_fences.sudoku
    9

5a 8a 1a   0b 4b 0b   6c 2c 7c
9a 4a 7a   6b 2b 1b   5c 3c 8c
6a 2a 3a   0b 0b 8b   4c 9c 1c

0d 0d 0d   0e 8e 0e   2f 0f 0f
0d 0d 8d   2e 9e 6e   1f 5f 0f
2d 0d 5d   0e 1e 0e   0f 8f 0f

8g 0g 2g   1h 0h 0h   0i 6i 0i
0g 0g 0g   8h 3h 2h   9i 0i 5i
3g 0g 0g   0h 6h 0h   8i 1i 2i

    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_rows_2_fences():
    puzzle_string = f"""
    xy_wing_rows_2_fences.sudoku
    9
2a _a _a   3b 5b 4b   0c 0c 1c
4a 8a 6a   9b 1b 7b   3c 2c 5c
1a 5a 3a   2b 6b 8b   9c 7c 4c

7d 0d 0d   0e 2e 6e   0f 9f 0f
0d 2d 0d   0e 9e 0e   7f 1f 0f
9d 0d 0d   1e 7e 0e   0f 4f 2f

5g 0g 0g   7h 3h 2h   4i 0i 0i
3g 4g 2g   6h 8h 9h   1i 5i 7i
0g 0g 0g   5h 4h 1h   2i 3i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_south_east_3_fences():
    puzzle_string = f"""
    xy_wing_south_east_3_fences.sudoku
    9
_a 5a _a   4b 9b 2b   0c 0c 8c
_a 8a 9a   1b 7b 5b   0c 2c 3c
_a _a _a   3b 6b 8b   0c 5c 9c

0d 2d 0d   5e 1e 3e   9f 4f 7f
9d 0d 5d   7e 8e 0e   2f 0f 1f
0d 1d 7d   9e 2e 0e   0f 8f 5f

0g 6g 0g   8h 5h 1h   0i 9i 4i
5g 9g 4g   2h 3h 7h   8i 1i 6i
0g 0g 0g   6h 4h 9h   5i 0i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_xy_wing_south_west_3_fences():
    puzzle_string = f"""
    xy_wing_south_west_3_fences.sudoku
    9
3a 4a 2a   5b 8b 1b   6c 9c 7c
6a 8a 1a   0b 0b 7b   0c 0c 3c
_a 9a _a   6b 0b 3b   0c 1c 0c

8d 0d 6d   0e 0e 4e   2f 0f 1f
0d 1d 9d   8e 7e 0e   3f 6f 4f
4d 0d 3d   1e 6e 0e   0f 8f 9f

0g 6g 0g   0h 0h 9h   1i 3i 0i
1g 0g 0g   0h 0h 8h   9i 0i 6i
9g 3g 0g   2h 1h 6h   0i 4i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_x_chain():
    puzzle_string = f"""
    x_chain.sudoku
    9
7a 2a 3a   1b 6b 0b   0c 0c 0c
6a 5a 8a   0b 2b 4b   0c 0c 0c
1a 4a 9a   5b 0b 7b   2c 6c 0c

0d 6d 1d   0e 5e 3e   0f 2f 0f
3d 0d 5d   2e 7e 0e   6f 0f 4f
0d 7d 2d   6e 0e 0e   5f 3f 0f

2g 1g 7g   0h 0h 5h   0i 9i 6i
0g 3g 4g   7h 9h 6h   1i 0i 2i
0g 0g 6g   0h 1h 2h   3i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_x_chain_0():
    puzzle_string = f"""
    x_chain_0.sudoku
    9
    4a 8a _a   1b 0b 0b   0c 9c 7c
    _a 3a _a   0b 0b 2b   0c 1c 0c
    _a _a _a   0b 0b 0b   5c 0c 6c
    
    0d 0d 0d   5e 2e 0e   0f 0f 0f
    7d 0d 0d   6e 0e 1e   0f 0f 8f
    0d 0d 0d   0e 7e 8e   0f 0f 0f
    
    8g 0g 6g   0h 0h 0h   0i 0i 0i
    0g 5g 0g   2h 0h 0h   6i 0i 0i
    9g 4g 0g   0h 0h 5h   0i 7i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())

#
# avoidable_rectangle_type1_north_east_in_cols
# _a _a _a   2b 5b 0b   6c 0c 0c
# _a _a 6a   0b 0b 8b   0c 0c 0c
# _a _a _a   7b 0b 9b   0c 0c 1c
#
# 0d 8d 0d   0e 0e 0e   0f 1f 0f
# 1d 2d 5d   0e 0e 0e   3f 9f 6f
# 0d 4d 0d   0e 0e 0e   0f 7f 0f
#
# 2g 0g 0g   9h 0h 3h   0i 0i 0i
# 0g 0g 0g   4h 0h 0h   5i 0i 0i
# 0g 0g 3g   0h 8h 6h   0i 0i 0i
#
# avoidable_rectangle_type1_north_east_in_rows
# _a _a 7a   0b 1b 6b   0c 2c 0c
# _a _a _a   0b 0b 0b   6c 0c 0c
# 8a 5a _a   0b 0b 2b   0c 9c 0c
#
# 7d 0d 0d   0e 2e 9e   0f 5f 0f
# 0d 0d 0d   0e 0e 0e   0f 0f 0f
# 0d 4d 0d   1e 8e 0e   0f 0f 6f
#
# 0g 9g 0g   5h 0h 0h   0i 4i 2i
# 0g 0g 3g   0h 0h 0h   0i 0i 0i
# 0g 8g 0g   9h 4h 0h   7i 0i 0i
#
# avoidable_rectangle_type1_north_west_in_cols
# _a _a 9a   0b 7b 3b   0c 0c 0c
# 2a _a _a   4b 0b 8b   0c 0c 0c
# _a _a _a   6b 0b 0b   9c 0c 0c
#
# 0d 8d 0d   0e 0e 0e   0f 1f 0f
# 9d 4d 5d   0e 0e 0e   7f 3f 2f
# 0d 2d 0d   0e 0e 0e   0f 6f 0f
#
# 0g 0g 7g   0h 0h 1h   0i 0i 0i
# 0g 0g 0g   5h 0h 4h   0i 0i 3i
# 0g 0g 0g   9h 6h 0h   5i 0i 0i
#
# avoidable_rectangle_type1_north_west_in_rows
# _a 8a _a   0b 0b 0b   0c 0c 0c
# 6a 2a _a   0b 0b 4b   0c 0c 0c
# 1a 3a 7a   0b 0b 5b   0c 8c 0c
#
# 3d 5d 0d   2e 0e 0e   0f 1f 0f
# 0d 0d 6d   0e 0e 0e   3f 0f 0f
# 0d 9d 0d   0e 0e 7e   0f 4f 6f
#
# 0g 1g 0g   7h 0h 0h   4i 9i 2i
# 0g 0g 0g   1h 0h 0h   0i 6i 7i
# 0g 0g 0g   0h 0h 0h   0i 5i 0i
#
#
# avoidable_rectangle_type1_south_east_in_cols
# _a 5a 2a   0b 0b 0b   0c 0c 1c
# 6a 9a 1a   0b 3b 0b   8c 0c 0c
# _a 3a _a   0b 0b 0b   0c 0c 0c
#
# 0d 0d 8d   2e 0e 5e   9f 0f 0f
# 0d 1d 0d   0e 0e 0e   0f 8f 0f
# 0d 0d 5d   6e 0e 9e   1f 0f 0f
#
# 0g 0g 0g   0h 0h 0h   0i 1i 0i
# 0g 0g 4g   0h 2h 0h   6i 5i 9i
# 5g 0g 0g   0h 0h 0h   3i 7i 0i
#
#
# avoidable_rectangle_type1_south_east_in_rows
# _a _a _a   3b 0b 2b   0c 1c 0c
# _a _a _a   0b 9b 4b   0c 0c 3c
# 4a 7a _a   0b 0b 0b   0c 0c 2c
#
# 0d 0d 1d   5e 0e 0e   0f 2f 0f
# 0d 0d 7d   0e 1e 0e   8f 0f 0f
# 0d 8d 0d   0e 0e 3e   5f 0f 0f
#
# 5g 0g 0g   0h 0h 0h   0i 6i 9i
# 2g 0g 0g   9h 8h 0h   0i 0i 0i
# 0g 6g 0g   1h 0h 5h   0i 0i 0i
#
# avoidable_rectangle_type1_south_west_in_rows
# 8a 4a _a   0b 0b 7b   0c 0c 0c
# _a _a 3a   0b 0b 5b   0c 0c 6c
# 1a _a 7a   6b 0b 0b   0c 4c 0c
#
# 0d 0d 0d   0e 0e 9e   0f 8f 0f
# 0d 0d 9d   0e 0e 0e   6f 0f 0f
# 0d 7d 0d   3e 0e 0e   0f 0f 0f
#
# 0g 9g 0g   0h 0h 4h   2i 0i 8i
# 5g 0g 0g   7h 0h 0h   9i 0i 0i
# 0g 0g 0g   2h 0h 0h   0i 3i 7i
#
# avoidable_rectangle_type1_0
# _a 6a _a   0b 0b 0b   0c 3c 9c
# _a 8a _a   3b 2b 0b   0c 0c 0c
# 9a _a _a   5b 0b 6b   0c 0c 0c
#
# 2d 0d 0d   0e 0e 4e   6f 0f 0f
# 0d 0d 7d   0e 5e 0e   2f 0f 0f
# 0d 0d 5d   6e 0e 0e   0f 0f 8f
#
# 0g 0g 0g   4h 0h 8h   0i 0i 5i
# 0g 0g 0g   0h 3h 1h   0i 4i 0i
# 7g 1g 0g   0h 0h 0h   0i 8i 0i
