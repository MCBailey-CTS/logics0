import pytest

from _defaults import default_test_puzzle
from puzzles import Sudoku
from solving import Solving
from tech import tech
from techniques.Bug import Bug
from techniques.CrossHatch import CrossHatch
from techniques.HiddenSingle import HiddenSingle
from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
from techniques.LockedCandidatesPointing import LockedCandidatesPointing
from techniques.NakedPair import NakedPair
from techniques.UniqueRectangleType1 import UniqueRectangleType1
from techniques.UniqueRectangleType2 import UniqueRectangleType2
from techniques.UniqueRectangleType4 import UniqueRectangleType4


@pytest.mark.skip("skipped")
def test_difficult_01():
    puzzle_string = f"""
    difficult_01.sudoku
    9
    8a 6a _a   _b 7b _b   _c 3c 4c
    2a 1a 7a   6b 4b 3b   8c 9c 5c
    3a 4a _a   8b _b _b   _c 7c _c
    
    1d 7d 3d   5e 2e 4e   9f 6f 8f
    4d 9d 6d   3e 8e 7e   5f 1f 2f
    5d 8d 2d   1e 6e 9e   3f 4f 7f
    
    9g 2g _g   7h 5h 6h   _i 8i 3i
    6g 5g _g   4h 3h _h   7i 2i 9i
    7g 3g _g   _h _h _h   _i 5i _i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), LockedCandidatesPointing(), LockedCandidatesClaiming(), UniqueRectangleType4(), tech.XWing()])


@pytest.mark.skip("skipped")
def test_difficult_04():
    puzzle_string = f"""
    difficult_04.sudoku
    9
    
    3a _a 0a   9b 0b 0b   4c 0c 1c
    _a 0a 7a   0b 3b 0b   8c 0c 0c
    _a 0a _a   0b 0b 0b   0c 5c 6c
    
    0d 0d 0d   8e 5e 4e   0f 0f 0f
    0d 8d 0d   0e 0e 0e   0f 4f 0f
    0d 0d 0d   3e 2e 6e   0f 0f 0f
    
    9g 7g 0g   0h 0h 0h   0i 0i 0i
    0g 0g 3g   0h 4h 0h   2i 0i 0i
    2g 0g 4g   0h 0h 8h   0i 0i 9i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_difficult_05():
    puzzle_string = f"""
    difficult_05.sudoku
    9
    
    6a 4a _a   0b 0b 0b   9c 8c 2c
    8a _a 0a   0b 0b 0b   0c 0c 0c
    _a 0a 7a   0b 0b 8b   0c 0c 0c
    
    4d 0d 0d   7e 0e 0e   0f 2f 5f
    0d 0d 8d   2e 0e 1e   3f 0f 0f
    1d 5d 0d   0e 0e 6e   0f 0f 9f
    
    0g 0g 0g   4h 0h 0h   5i 0i 0i
    0g 0g 0g   0h 0h 0h   0i 0i 8i
    9g 7g 5g   0h 0h 0h   0i 6i 3i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_difficult_08():
    puzzle_string = f"""
    difficult_08.sudoku
    9
    
    _a 0a 8a   0b 1b 4b   0c 0c 3c
    _a 0a _a   0b 0b 0b   0c 8c 0c
    6a 2a _a   0b 0b 7b   9c 0c 4c
    
    7d 0d 3d   1e 0e 0e   0f 0f 0f
    4d 0d 0d   0e 0e 0e   0f 0f 8f
    0d 0d 0d   0e 0e 9e   5f 0f 7f
    
    8g 0g 4g   9h 0h 0h   0i 3i 6i
    0g 3g 0g   0h 0h 0h   0i 0i 0i
    5g 0g 0g   6h 4h 0h   8i 0i 0i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_difficult_15():
    puzzle_string = f"""
    difficult_15.sudoku
    9
    
    3a _a 0a   0b 0b 0b   0c 0c 0c
    1a _a 0a   6b 0b 4b   0c 0c 0c
    4a _a 5a   0b 0b 3b   8c 7c 0c
    
    0d 0d 3d   0e 5e 0e   0f 0f 7f
    0d 0d 0d   0e 0e 0e   0f 0f 0f
    6d 0d 0d   0e 3e 0e   5f 0f 0f
    
    0g 7g 6g   2h 0h 0h   3i 0i 5i
    0g 0g 0g   1h 0h 8h   0i 0i 4i
    0g 0g 0g   0h 0h 0h   0i 0i 2i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_difficult_20():
    puzzle_string = f"""
    difficult_20.sudoku
    9
    
    _a 0a _a   9b 1b 0b   0c 7c 0c
    _a 0a 4a   0b 5b 7b   2c 8c 0c
    _a 0a _a   0b 0b 6b   0c 9c 0c
    
    0d 0d 5d   0e 0e 0e   1f 4f 2f
    0d 0d 0d   0e 0e 0e   0f 0f 0f
    8d 2d 6d   0e 0e 0e   7f 0f 0f
    
    0g 5g 0g   6h 0h 0h   0i 0i 0i
    0g 9g 2g   7h 8h 0h   4i 0i 0i
    0g 3g 0g   0h 9h 1h   0i 0i 0i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_difficult_21():
    puzzle_string = f"""
    difficult_21.sudoku
    9
    
    _a 0a 4a   3b 0b 0b   0c 8c 6c
    _a 2a _a   0b 7b 0b   5c 4c 3c
    _a 3a _a   0b 0b 0b   7c 0c 0c
    
    0d 0d 5d   0e 0e 7e   4f 0f 0f
    0d 0d 0d   0e 8e 0e   0f 0f 0f
    0d 0d 9d   6e 0e 0e   2f 0f 0f
    
    0g 0g 7g   0h 0h 0h   0i 6i 0i
    3g 4g 6g   0h 1h 0h   0i 2i 0i
    1g 5g 0g   0h 0h 3h   9i 0i 0i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_difficult_31():
    puzzle_string = f"""
    difficult_31.sudoku
    9
    
    8a 3a 4a   1b 2b 7b   5c 6c 9c
    5a 9a 7a   6b 3b 4b   0c 8c 0c
    1a 2a 6a   5b 8b 9b   7c 4c 3c
    
    0d 8d 5d   9e 0e 1e   0f 0f 0f
    0d 7d 0d   3e 0e 5e   0f 9f 8f
    9d 6d 0d   2e 0e 8e   0f 5f 0f
    
    6g 1g 8g   7h 5h 0h   9i 0i 4i
    7g 5g 0g   4h 9h 0h   8i 1i 6i
    0g 4g 9g   8h 1h 6h   0i 7i 5i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_00():
    puzzle_string = f"""
    difficult_00.sudoku
    9
    7a _a 0a 6b 0b 0b 0c 9c 0c
    _a 0a _a 0b 0b 0b 0c 0c 0c
    5a _a 6a 8b 0b 1b 4c 0c 0c
    0d 0d 3d 9e 0e 0e 8f 7f 4f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    9d 2d 4d 0e 0e 3e 5f 0f 0f
    0g 0g 2g 4h 0h 9h 3i 0i 6i
    0g 0g 0g 0h 0h 0h 0i 0i 0i
    0g 8g 0g 0h 0h 7h 0i 0i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_02():
    puzzle_string = f"""
    difficult_02.sudoku
    9
    _a 0a 9a 0b 0b 0b 6c 0c 0c
    _a 7a 4a 0b 0b 1b 0c 0c 0c
    1a _a 0a 4b 0b 0b 0c 0c 0c
    0d 0d 3d 8e 7e 0e 9f 0f 2f
    7d 0d 0d 0e 0e 0e 0f 0f 8f
    4d 0d 2d 0e 6e 3e 7f 0f 0f
    0g 0g 0g 0h 0h 9h 0i 0i 5i
    0g 0g 0g 7h 0h 0h 3i 8i 0i
    0g 0g 1g 0h 0h 0h 2i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_03():
    puzzle_string = f"""
    difficult_03.sudoku
    9
    _a 0a _a 0b 0b 5b 9c 0c 3c
    _a 1a _a 7b 2b 0b 0c 0c 5c
    8a _a 0a 0b 9b 3b 0c 1c 0c
    0d 3d 0d 9e 0e 0e 0f 0f 0f
    0d 0d 4d 0e 0e 0e 3f 0f 0f
    0d 0d 0d 0e 0e 8e 0f 9f 0f
    0g 9g 0g 2h 4h 0h 0i 0i 7i
    5g 0g 0g 0h 7h 9h 0i 6i 0i
    2g 0g 3g 5h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_06():
    puzzle_string = f"""
    difficult_06.sudoku
    9
    1a 8a 5a 3b 4b 7b 9c 6c 2c
    _a 0a _a 0b 0b 0b 0c 0c 3c
    3a 9a _a 1b 0b 0b 0c 0c 8c
    0d 2d 0d 0e 7e 0e 0f 0f 1f
    0d 0d 0d 4e 0e 3e 0f 8f 5f
    5d 3d 0d 0e 1e 0e 0f 9f 7f
    7g 0g 0g 0h 0h 6h 0i 2i 4i
    0g 0g 0g 7h 0h 0h 0i 0i 9i
    0g 0g 3g 2h 8h 0h 5i 7i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_07():
    puzzle_string = f"""
    difficult_07.sudoku
    9
    8a 7a 4a 2b 3b 9b 6c 5c 1c
    3a 5a 2a 1b 6b 7b 9c 4c 8c
    1a 9a 6a 0b 0b 0b 2c 7c 3c
    6d 0d 3d 4e 7e 2e 0f 9f 5f
    7d 2d 5d 9e 1e 8e 4f 3f 6f
    9d 4d 0d 3e 5e 6e 7f 0f 2f
    5g 6g 0g 7h 0h 0h 3i 2i 9i
    4g 0g 9g 0h 2h 3h 5i 0i 7i
    2g 3g 7g 0h 9h 0h 0i 0i 4i
    requires a remote pair
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_09():
    puzzle_string = f"""
    difficult_09.sudoku
    9
    _a 1a _a 7b 8b 0b 6c 0c 0c
    6a 5a _a 0b 0b 0b 0c 0c 8c
    _a 8a 7a 0b 9b 6b 0c 0c 4c
    4d 3d 1d 0e 0e 0e 5f 8f 0f
    7d 2d 8d 0e 4e 0e 0f 0f 3f
    9d 6d 5d 8e 0e 3e 4f 2f 0f
    0g 7g 2g 4h 6h 8h 3i 9i 0i
    8g 4g 3g 0h 5h 0h 0i 0i 0i
    0g 9g 6g 0h 3h 7h 8i 4i 0i
    unique rectangle type 1
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_10():
    puzzle_string = f"""
    difficult_10.sudoku
    9
    _a 2a _a 1b 0b 4b 0c 7c 0c
    _a 0a _a 0b 0b 7b 0c 0c 2c
    1a _a 0a 2b 0b 0b 4c 0c 6c
    8d 1d 2d 9e 0e 0e 7f 0f 4f
    9d 5d 0d 0e 0e 0e 0f 2f 0f
    3d 0d 6d 0e 0e 2e 9f 0f 0f
    2g 6g 3g 0h 0h 1h 5i 4i 9i
    7g 8g 5g 4h 0h 0h 0i 0i 0i
    4g 9g 1g 5h 0h 6h 0i 0i 7i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_11():
    puzzle_string = f"""
    difficult_11.sudoku
    9
    _a 0a 6a 9b 2b 0b 4c 8c 5c
    _a 8a _a 4b 0b 7b 9c 2c 6c
    _a 4a _a 5b 8b 6b 7c 3c 1c
    0d 6d 0d 1e 7e 2e 0f 4f 0f
    8d 2d 7d 3e 4e 5e 6f 1f 9f
    1d 3d 4d 8e 6e 9e 2f 5f 7f
    0g 9g 3g 0h 0h 8h 0i 6i 4i
    4g 5g 0g 6h 9h 0h 0i 7i 0i
    6g 0g 8g 0h 0h 4h 0i 9i 0i
    Unique Rectangle Type 3
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_12():
    puzzle_string = f"""
    difficult_12.sudoku
    9
    7a _a 0a 0b 0b 0b 0c 0c 0c
    _a 1a _a 4b 0b 6b 0c 0c 0c
    5a 2a _a 0b 0b 3b 0c 6c 0c
    3d 0d 0d 0e 0e 0e 0f 1f 6f
    0d 0d 5d 9e 0e 1e 3f 0f 0f
    8d 6d 0d 0e 0e 0e 0f 0f 2f
    0g 5g 0g 8h 0h 0h 0i 2i 1i
    0g 0g 0g 1h 0h 2h 0i 8i 0i
    0g 0g 0g 0h 0h 0h 0i 0i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), tech.NakedTriple()])


def test_sudoku_difficult_13():
    puzzle_string = f"""
    difficult_13.sudoku
    9
    4a 7a 2a 1b 5b 3b 0c 0c 9c
    _a 0a _a 7b 8b 6b 3c 2c 4c
    8a 6a 3a 4b 9b 2b 7c 1c 5c
    0d 2d 0d 0e 0e 0e 0f 4f 8f
    0d 0d 6d 9e 4e 8e 2f 0f 0f
    0d 8d 4d 0e 0e 0e 0f 0f 0f
    0g 4g 8g 0h 0h 1h 5i 9i 0i
    0g 9g 1g 5h 7h 4h 0i 0i 2i
    2g 0g 0g 8h 6h 9h 4i 0i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()])


def test_sudoku_difficult_14():
    puzzle_string = f"""
    difficult_14.sudoku
    9
    _a 0a _a 7b 4b 1b 3c 6c 8c
    7a 8a 1a 2b 6b 3b 4c 5c 9c
    3a 4a 6a 9b 8b 5b 7c 2c 1c
    0d 5d 0d 0e 1e 6e 0f 0f 0f
    0d 0d 0d 0e 3e 2e 0f 1f 0f
    1d 0d 0d 5e 9e 7e 0f 4f 0f
    6g 7g 4g 3h 5h 8h 1i 9i 2i
    0g 3g 0g 1h 2h 9h 6i 7i 4i
    2g 1g 9g 6h 7h 4h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_difficult_16():
    puzzle_string = f"""
    difficult_16.sudoku
    9
    _a 9a 4a 6b 2b 0b 0c 8c 1c
    1a 3a 2a 0b 5b 0b 6c 9c 7c
    8a _a 6a 0b 1b 0b 4c 2c 0c
    9d 6d 3d 5e 8e 1e 2f 7f 4f
    2d 8d 5d 0e 4e 0e 1f 3f 6f
    4d 1d 7d 2e 3e 6e 9f 5f 8f
    0g 4g 1g 0h 9h 0h 0i 6i 2i
    3g 0g 8g 1h 6h 2h 0i 4i 9i
    6g 2g 9g 0h 7h 0h 8i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_17():
    puzzle_string = f"""
    difficult_17.sudoku
    9
    8a _a 1a 0b 0b 9b 7c 3c 0c
    6a 5a 3a 8b 7b 1b 9c 2c 4c
    7a 9a _a 0b 3b 0b 1c 8c 0c
    0d 7d 8d 0e 0e 0e 2f 9f 1f
    0d 6d 5d 1e 9e 0e 8f 4f 0f
    9d 1d 0d 0e 8e 0e 6f 5f 0f
    1g 8g 7g 9h 5h 3h 4i 6i 2i
    5g 0g 6g 0h 1h 8h 3i 7i 9i
    0g 3g 9g 7h 0h 0h 5i 1i 8i
    uniqe rec3
    remote pair
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


def test_sudoku_difficult_18():
    puzzle_string = f"""
    difficult_18.sudoku
    9
    3a _a 4a 9b 5b 0b 0c 0c 0c
    _a 9a _a 0b 0b 0b 0c 6c 5c
    _a 0a _a 0b 0b 0b 0c 0c 0c
    9d 3d 0d 2e 0e 0e 0f 0f 4f
    4d 0d 8d 3e 0e 6e 1f 0f 9f
    6d 0d 0d 0e 0e 9e 0f 2f 7f
    0g 0g 0g 0h 0h 0h 0i 0i 0i
    1g 7g 0g 0h 0h 0h 0i 4i 0i
    0g 0g 0g 0h 3h 7h 2i 0i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()])


def test_sudoku_difficult_19():
    puzzle_string = f"""
    difficult_19.sudoku
    9
    _a 0a _a 0b 0b 0b 8c 5c 2c
    6a _a 0a 4b 0b 0b 3c 0c 0c
    5a _a 0a 0b 9b 0b 0c 0c 0c
    0d 0d 9d 0e 0e 6e 4f 0f 0f
    0d 5d 0d 0e 3e 0e 0f 1f 0f
    0d 0d 7d 1e 0e 0e 6f 0f 0f
    0g 0g 0g 0h 7h 0h 0i 0i 8i
    0g 0g 5g 0h 0h 8h 0i 0i 3i
    1g 4g 8g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_22():
    puzzle_string = f"""
    difficult_22.sudoku
    9
    _a 0a 3a 2b 0b 8b 0c 0c 4c
    6a 4a _a 0b 0b 7b 0c 2c 0c
    _a 0a _a 0b 0b 4b 8c 0c 9c
    0d 2d 0d 0e 0e 0e 0f 4f 0f
    9d 0d 0d 0e 0e 0e 0f 0f 3f
    0d 3d 0d 0e 0e 0e 0f 8f 0f
    3g 0g 5g 8h 0h 0h 0i 0i 0i
    0g 6g 0g 7h 0h 0h 0i 5i 2i
    2g 0g 0g 6h 0h 5h 1i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), tech.XWing()])


def test_sudoku_difficult_23():
    puzzle_string = f"""
    difficult_23.sudoku
    9
    5a 7a _a 0b 0b 2b 8c 0c 0c
    _a 0a _a 0b 3b 0b 7c 0c 0c
    _a 1a _a 0b 0b 6b 0c 3c 0c
    0d 0d 0d 0e 0e 0e 9f 5f 1f
    9d 0d 0d 4e 0e 1e 0f 0f 6f
    1d 8d 5d 0e 0e 0e 0f 0f 0f
    0g 9g 0g 2h 0h 0h 0i 4i 0i
    0g 0g 8g 0h 1h 0h 0i 0i 0i
    0g 0g 2g 5h 0h 0h 0i 9i 3i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()])


def test_sudoku_difficult_24():
    puzzle_string = f"""
    difficult_24.sudoku
    9
    _a 0a _a 5b 0b 1b 0c 7c 0c
    _a 0a 2a 9b 0b 0b 8c 0c 0c
    7a _a 6a 2b 0b 0b 4c 0c 0c
    5d 0d 3d 0e 0e 0e 0f 1f 0f
    0d 0d 0d 3e 0e 5e 0f 0f 0f
    0d 9d 0d 0e 0e 0e 3f 0f 2f
    0g 0g 5g 0h 0h 7h 6i 0i 9i
    0g 0g 4g 0h 0h 2h 5i 0i 0i
    0g 6g 0g 4h 0h 8h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_25():
    puzzle_string = f"""
    difficult_25.sudoku
    9
    _a 8a _a 6b 0b 0b 0c 0c 1c
    4a 7a _a 5b 0b 0b 0c 6c 0c
    _a 0a 3a 0b 0b 9b 0c 0c 0c
    0d 2d 0d 0e 0e 0e 0f 0f 6f
    0d 6d 0d 9e 0e 4e 0f 8f 0f
    5d 0d 0d 0e 0e 0e 0f 3f 0f
    0g 0g 0g 7h 0h 0h 2i 0i 0i
    0g 5g 0g 0h 0h 3h 0i 7i 9i
    8g 0g 0g 0h 0h 2h 0i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), LockedCandidatesClaiming(), tech.NakedTriple()])


def test_sudoku_difficult_26():
    puzzle_string = f"""
    difficult_26.sudoku
    9
    3a _a 0a 7b 0b 0b 4c 0c 6c
    _a 6a _a 9b 0b 8b 0c 0c 0c
    8a _a 0a 1b 0b 0b 0c 0c 3c
    2d 0d 3d 0e 0e 0e 0f 5f 0f
    0d 0d 0d 3e 0e 2e 0f 0f 0f
    0d 4d 0d 0e 0e 0e 1f 0f 2f
    1g 0g 0g 0h 0h 4h 0i 0i 9i
    0g 0g 0g 5h 0h 3h 0i 7i 0i
    6g 0g 7g 0h 0h 1h 0i 0i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_27():
    puzzle_string = f"""
    difficult_27.sudoku
    9
    _a 0a _a 0b 0b 0b 0c 6c 0c
    _a 3a _a 0b 5b 0b 7c 0c 2c
    _a 0a 1a 7b 0b 8b 0c 0c 3c
    0d 9d 0d 0e 0e 0e 0f 0f 7f
    0d 0d 5d 3e 0e 9e 8f 0f 0f
    8d 0d 0d 0e 0e 0e 0f 4f 0f
    9g 0g 0g 4h 0h 1h 6i 0i 0i
    5g 0g 2g 0h 3h 0h 0i 1i 0i
    0g 6g 0g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_28():
    puzzle_string = f"""
    difficult_28.sudoku
    9
    _a 7a _a 9b 0b 0b 0c 6c 0c
    _a 0a _a 0b 0b 5b 4c 0c 0c
    9a _a 4a 1b 7b 0b 0c 0c 0c
    1d 0d 2d 0e 0e 0e 9f 4f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 5d 6d 0e 0e 0e 7f 0f 8f
    0g 0g 0g 0h 6h 2h 1i 0i 5i
    0g 0g 9g 7h 0h 0h 0i 0i 0i
    0g 6g 0g 0h 0h 3h 0i 8i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_29():
    puzzle_string = f"""
    difficult_29.sudoku
    9
    7a 3a 4a 0b 2b 0b 1c 5c 6c
    5a 6a 2a 0b 1b 0b 8c 9c 7c
    9a 8a 1a 6b 5b 7b 2c 3c 4c
    4d 1d 6d 0e 3e 5e 0f 2f 0f
    3d 9d 5d 0e 0e 0e 4f 0f 1f
    8d 2d 7d 0e 4e 0e 5f 6f 3f
    6g 4g 9g 5h 7h 0h 3i 1i 0i
    1g 5g 3g 0h 0h 0h 0i 0i 0i
    2g 7g 8g 0h 9h 0h 6i 4i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_30():
    puzzle_string = f"""
    difficult_30.sudoku
    9
    9a 8a 1a 0b 0b 7b 4c 2c 0c
    4a 7a 6a 0b 2b 8b 0c 5c 0c
    3a 2a 5a 0b 0b 0b 0c 8c 7c
    0d 4d 9d 0e 0e 3e 2f 7f 0f
    7d 1d 2d 0e 0e 0e 0f 3f 9f
    0d 6d 3d 2e 7e 9e 0f 4f 0f
    2g 9g 8g 7h 0h 0h 3i 6i 4i
    1g 5g 4g 6h 3h 2h 7i 9i 8i
    6g 3g 7g 8h 9h 4h 5i 1i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_32():
    puzzle_string = f"""
    difficult_32.sudoku
    9
    7a 3a 4a 0b 2b 0b 1c 5c 6c
    5a 6a 2a 0b 1b 0b 8c 9c 7c
    9a 8a 1a 6b 5b 7b 2c 3c 4c
    4d 1d 6d 0e 3e 5e 0f 2f 0f
    3d 9d 5d 0e 0e 0e 4f 0f 1f
    8d 2d 7d 0e 4e 0e 5f 6f 3f
    6g 4g 9g 5h 7h 0h 3i 1i 0i
    1g 5g 3g 0h 0h 0h 0i 0i 0i
    2g 7g 8g 0h 9h 0h 6i 4i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_33():
    puzzle_string = f"""
    difficult_33.sudoku
    9
    9a 8a 1a 0b 0b 7b 4c 2c 0c
    4a 7a 6a 0b 2b 8b 0c 5c 0c
    3a 2a 5a 0b 0b 0b 0c 8c 7c
    0d 4d 9d 0e 0e 3e 2f 7f 0f
    7d 1d 2d 0e 0e 0e 0f 3f 9f
    0d 6d 3d 2e 7e 9e 0f 4f 0f
    2g 9g 8g 7h 0h 0h 3i 6i 4i
    1g 5g 4g 6h 3h 2h 7i 9i 8i
    6g 3g 7g 8h 9h 4h 5i 1i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()])


def test_sudoku_difficult_34():
    puzzle_string = f"""
    difficult_34.sudoku
    9
    _a 0a _a 6b 0b 7b 0c 5c 4c
    _a 0a _a 0b 8b 0b 9c 0c 0c
    5a _a 0a 4b 0b 0b 6c 7c 0c
    9d 3d 0d 1e 0e 0e 0f 0f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 0d 0d 0e 0e 9e 0f 2f 6f
    0g 5g 7g 0h 0h 1h 0i 0i 8i
    0g 0g 3g 0h 4h 0h 0i 0i 0i
    2g 8g 0g 9h 0h 3h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming(), UniqueRectangleType4(),
                                Bug()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_35():
    puzzle_string = f"""
    difficult_35.sudoku
    9
    _a 0a 2a 0b 0b 9b 0c 0c 0c
    _a 0a 5a 3b 4b 0b 0c 1c 0c
    _a 0a _a 7b 0b 0b 0c 0c 8c
    0d 4d 7d 0e 0e 0e 0f 0f 3f
    3d 0d 9d 1e 0e 4e 6f 0f 5f
    2d 0d 0d 0e 0e 0e 9f 4f 0f
    7g 0g 0g 0h 0h 6h 0i 0i 0i
    0g 5g 0g 0h 1h 7h 3i 0i 0i
    0g 0g 0g 2h 0h 0h 4i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_difficult_36():
    puzzle_string = f"""
    difficult_36.sudoku
    9
    _a 0a _a 7b 0b 0b 0c 0c 9c
    _a 1a _a 0b 3b 0b 0c 6c 0c
    3a _a 0a 0b 9b 0b 4c 0c 0c
    0d 0d 3d 6e 0e 0e 2f 4f 0f
    0d 8d 0d 0e 0e 0e 0f 1f 0f
    0d 5d 4d 0e 0e 3e 8f 0f 0f
    0g 0g 1g 0h 2h 0h 0i 0i 5i
    0g 3g 0g 0h 8h 0h 0i 7i 0i
    6g 0g 0g 0h 0h 4h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku,
                               [CrossHatch(), LockedCandidatesPointing(), Bug(), tech.NakedTriple()])


@pytest.mark.skip("skipped")
def test_sudoku_difficult_37():
    puzzle_string = f"""
    difficult_37.sudoku
    9
    _a 0a 5a 0b 0b 8b 0c 7c 3c
    _a 0a _a 0b 0b 0b 0c 0c 0c
    _a 7a 2a 4b 0b 0b 1c 0c 0c
    0d 2d 4d 0e 7e 0e 0f 0f 6f
    0d 8d 0d 2e 0e 5e 0f 3f 0f
    5d 0d 0d 0e 4e 0e 7f 1f 0f
    0g 0g 8g 0h 0h 1h 9i 6i 0i
    0g 0g 0g 0h 0h 0h 0i 0i 0i
    4g 1g 0g 9h 0h 0h 8i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.NakedTriple()])


def test_sudoku_difficult_38():
    puzzle_string = f"""
    difficult_38.sudoku
    9
    _a 4a _a _b _b _b _c _c _c
    2a _a 9a 8b _b _b 7c _c _c
    _a _a _a 7b _b 2b _c 1c _c
    _d 2d 4d 5e _e _e _f 3f _f
    1d 8d _d 2e _e 9e _f 6f 7f
    _d 3d _d _e _e 1e 5f 8f _f
    _g 5g _g 3h _h 7h _i _i _i
    _g _g 2g _h _h 4h 8i _i 3i
    _g _g _g _h _h _h _i 5i _i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), Bug()])


def test_sudoku_difficult_39():
    puzzle_string = f"""
    difficult_39.sudoku
    9
    _a 3a _a _b 9b _b 8c _c 7c
    8a _a _a 1b _b _b 6c _c 3c
    2a _a _a _b _b 8b _c _c _c
    _d _d 3d _e _e _e 5f _f _f
    6d _d _d _e _e _e _f _f 1f
    _d _d 2d _e _e _e 7f _f _f
    _g _g _g 8h _h _h _i _i 4i
    7g _g 1g _h _h 3h _i _i 8i
    9g _g 5g _h 7h _h _i 1i _i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_40():
    puzzle_string = f"""
    unique_rectangle_type1_05.sudoku
    9
    _a 4a _a 0b 7b 5b 1c 2c 0c
    5a _a 2a 9b 4b 0b 7c 3c 0c
    _a 0a 7a 2b 0b 0b 4c 9c 5c
    7d 5d 1d 0e 0e 0e 9f 0f 2f
    2d 3d 8d 1e 9e 0e 5f 0f 7f
    4d 9d 6d 5e 2e 7e 8f 1f 3f
    8g 2g 4g 6h 5h 9h 3i 7i 1i
    1g 7g 5g 4h 3h 2h 6i 8i 9i
    0g 6g 0g 7h 1h 8h 2i 5i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair(), UniqueRectangleType1()])


def test_sudoku_difficult_41():
    puzzle_string = f"""
    unique_rectangle_type2_00.sudoku
    9
    _a 0a _a 0b 0b 0b 0c 0c 0c
    9a _a 2a 7b 0b 0b 0c 0c 0c
    1a 3a _a 0b 0b 0b 9c 5c 0c
    0d 0d 0d 4e 5e 0e 7f 8f 0f
    4d 5d 0d 9e 0e 7e 0f 1f 6f
    0d 6d 8d 0e 1e 2e 0f 0f 0f
    0g 1g 7g 0h 0h 0h 0i 2i 9i
    0g 0g 0g 0h 0h 8h 4i 0i 5i
    0g 0g 0g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_42():
    puzzle_string = f"""
    unique_rectangle_type2_01.sudoku
    9
    _a 0a _a 0b 0b 0b 2c 0c 0c
    7a 5a _a 0b 3b 4b 0c 0c 0c
    3a _a 8a 9b 0b 0b 0c 0c 0c
    0d 0d 6d 0e 7e 0e 0f 8f 0f
    4d 7d 0d 0e 8e 0e 0f 1f 6f
    0d 8d 0d 0e 4e 0e 9f 0f 0f
    0g 0g 0g 0h 0h 6h 3i 0i 2i
    0g 0g 0g 7h 2h 0h 0i 4i 8i
    0g 0g 1g 0h 0h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_43():
    puzzle_string = f"""
    unique_rectangle_type2_02.sudoku
    9
    3a _a 0a 0b 0b 5b 0c 0c 2c
    _a 0a 7a 0b 1b 8b 0c 0c 0c
    _a 9a 5a 4b 0b 6b 3c 0c 0c
    9d 0d 0d 0e 0e 7e 0f 0f 0f
    0d 4d 0d 0e 0e 0e 0f 2f 0f
    0d 0d 0d 1e 0e 0e 0f 0f 4f
    0g 0g 8g 9h 0h 1h 4i 3i 0i
    0g 0g 0g 5h 3h 0h 1i 0i 0i
    7g 0g 0g 6h 0h 0h 0i 0i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_44():
    puzzle_string = f"""
    unique_rectangle_type2_03.sudoku
    9
    _a 0a _a 2b 0b 0b 9c 0c 0c
    8a _a 0a 0b 6b 0b 5c 0c 2c
    7a _a 0a 0b 0b 8b 0c 0c 0c
    2d 0d 1d 5e 0e 0e 0f 0f 0f
    6d 0d 0d 8e 0e 9e 0f 0f 3f
    0d 0d 0d 0e 0e 1e 7f 0f 8f
    0g 0g 0g 7h 0h 0h 0i 0i 5i
    1g 0g 9g 0h 5h 0h 0i 0i 6i
    0g 0g 8g 0h 0h 6h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_45():
    puzzle_string = f"""
    unique_rectangle_type2_04.sudoku
    9
    _a 0a 9a 0b 5b 0b 0c 0c 0c
    _a 4a 3a 0b 0b 0b 8c 0c 0c
    6a _a 0a 0b 0b 9b 0c 0c 4c
    3d 8d 7d 0e 0e 4e 2f 0f 0f
    0d 2d 0d 0e 0e 0e 0f 6f 0f
    0d 0d 5d 2e 0e 0e 9f 3f 7f
    1g 0g 0g 5h 0h 0h 0i 0i 9i
    0g 0g 6g 0h 0h 0h 5i 2i 0i
    0g 0g 0g 0h 1h 0h 6i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_46():
    puzzle_string = f"""
    unique_rectangle_type2_05.sudoku
    9
    _a 0a _a 0b 4b 0b 3c 5c 0c
    _a 0a 8a 0b 0b 1b 0c 6c 0c
    _a 0a 3a 0b 2b 9b 7c 0c 0c
    0d 0d 0d 4e 5e 0e 0f 8f 0f
    0d 0d 0d 2e 0e 3e 0f 0f 0f
    0d 1d 0d 0e 8e 6e 0f 0f 0f
    0g 0g 6g 1h 3h 0h 2i 0i 0i
    0g 4g 0g 8h 0h 0h 5i 0i 0i
    0g 2g 5g 0h 9h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_47():
    puzzle_string = f"""
    unique_rectangle_type2_06.sudoku
    9
    9a 8a _a 0b 0b 4b 0c 7c 0c
    _a 3a 1a 8b 9b 0b 0c 0c 0c
    _a 0a _a 0b 0b 0b 0c 0c 0c
    0d 5d 0d 0e 7e 1e 9f 0f 6f
    4d 0d 0d 5e 0e 9e 0f 0f 1f
    1d 0d 8d 3e 6e 0e 0f 4f 0f
    0g 0g 0g 0h 0h 0h 0i 0i 0i
    0g 0g 0g 0h 3h 6h 2i 1i 0i
    0g 1g 0g 9h 0h 0h 0i 6i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_48():
    puzzle_string = f"""
    unique_rectangle_type2_07.sudoku
    9
    _a 0a _a 4b 0b 0b 0c 0c 2c
    _a 0a _a 0b 7b 8b 0c 0c 4c
    6a _a 0a 3b 0b 0b 0c 9c 0c
    4d 2d 0d 0e 0e 0e 0f 8f 0f
    0d 0d 7d 0e 2e 0e 4f 0f 0f
    0d 1d 0d 0e 0e 0e 0f 5f 6f
    0g 3g 0g 0h 0h 7h 0i 0i 1i
    8g 0g 0g 2h 1h 0h 0i 0i 0i
    2g 0g 0g 0h 0h 3h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_49():
    puzzle_string = f"""
    unique_rectangle_type2_08.sudoku
    9
    _a 3a 4a 0b 7b 8b 2c 5c 6c
    6a _a 5a 2b 4b 0b 0c 3c 7c
    _a 2a _a 5b 6b 3b 0c 1c 4c
    0d 7d 0d 0e 5e 0e 4f 2f 3f
    5d 0d 2d 0e 3e 4e 7f 6f 9f
    3d 4d 0d 0e 2e 7e 5f 8f 1f
    4g 9g 1g 3h 8h 2h 6i 7i 5i
    0g 6g 0g 4h 1h 5h 3i 9i 2i
    2g 5g 3g 7h 9h 6h 1i 4i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_50():
    puzzle_string = f"""
    unique_rectangle_type2_09.sudoku
    9
    5a 4a _a 0b 9b 0b 0c 0c 0c
    _a 9a _a 3b 0b 0b 0c 0c 6c
    _a 0a _a 5b 0b 0b 0c 1c 9c
    9d 0d 3d 6e 0e 0e 5f 0f 0f
    4d 0d 0d 0e 0e 0e 0f 0f 1f
    0d 0d 7d 0e 0e 1e 6f 0f 3f
    1g 2g 0g 0h 0h 5h 0i 0i 0i
    7g 0g 0g 0h 0h 9h 0i 2i 0i
    0g 0g 0g 0h 3h 0h 0i 7i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_51():
    puzzle_string = f"""
    unique_rectangle_type2_10.sudoku
    9
    _a 0a _a 0b 2b 0b 0c 9c 8c
    2a 7a _a 0b 0b 8b 0c 0c 0c
    5a _a 0a 0b 0b 1b 0c 2c 0c
    1d 0d 5d 7e 0e 0e 3f 0f 0f
    7d 0d 0d 0e 0e 0e 0f 0f 9f
    0d 0d 8d 0e 0e 5e 1f 0f 2f
    0g 6g 0g 2h 0h 0h 0i 0i 3i
    0g 0g 0g 8h 0h 0h 0i 6i 7i
    4g 3g 0g 0h 1h 0h 0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_52():
    puzzle_string = f"""
    unique_rectangle_type2_11.sudoku
    9
    4a 2a 3a 9b 8b 6b 0c 0c 1c
    6a 5a 9a 7b 2b 1b 3c 8c 4c
    7a 8a 1a 5b 3b 4b 0c 0c 2c
    3d 0d 5d 1e 4e 2e 0f 0f 8f
    2d 1d 0d 8e 9e 3e 0f 0f 0f
    9d 4d 8d 6e 5e 7e 1f 2f 3f
    1g 9g 0g 3h 6h 8h 2i 0i 0i
    5g 0g 2g 4h 1h 9h 8i 3i 0i
    8g 3g 0g 2h 7h 5h 0i 1i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_53():
    puzzle_string = f"""
    unique_rectangle_type2_12.sudoku
    9
    3a 1a _a 0b 0b 0b 5c 6c 9c
    7a 6a _a 0b 0b 0b 8c 4c 3c
    4a 9a _a 3b 6b 0b 7c 1c 2c
    6d 8d 7d 2e 0e 0e 4f 9f 1f
    1d 2d 4d 9e 8e 6e 3f 5f 7f
    9d 5d 3d 4e 1e 7e 6f 2f 8f
    8g 4g 6g 0h 0h 2h 0i 3i 5i
    0g 3g 9g 0h 0h 0h 0i 7i 6i
    0g 7g 1g 6h 0h 0h 0i 8i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()])


def test_sudoku_difficult_54():
    puzzle_string = f"""
    unique_rectangle_type4_00.sudoku
    9
    2a _a 0a 6b 0b 9b 7c 0c 0c
    _a 4a _a 1b 0b 0b 0c 0c 9c
    _a 6a 1a 0b 0b 0b 0c 0c 0c
    0d 0d 0d 9e 0e 0e 3f 6f 0f
    3d 0d 6d 0e 0e 0e 1f 0f 7f
    0d 8d 9d 0e 0e 1e 0f 0f 0f
    0g 0g 0g 0h 0h 0h 2i 5i 0i
    6g 0g 0g 0h 0h 2h 0i 4i 0i
    0g 0g 2g 8h 0h 3h 0i 0i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_55():
    puzzle_string = f"""
    unique_rectangle_type4_01.sudoku
    9
    _a 0a 7a 0b 2b 0b 0c 6c 0c
    _a 4a _a 0b 1b 0b 0c 0c 8c
    _a 6a 3a 7b 0b 0b 4c 1c 0c
    0d 2d 0d 0e 0e 0e 0f 8f 0f
    0d 0d 1d 0e 5e 0e 2f 0f 0f
    0d 5d 0d 0e 0e 0e 0f 4f 0f
    0g 1g 4g 0h 0h 2h 6i 7i 0i
    6g 0g 0g 0h 3h 0h 0i 5i 0i
    0g 7g 0g 0h 4h 0h 8i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_56():
    puzzle_string = f"""
    unique_rectangle_type4_02.sudoku
    9
    _a 4a _a 0b 0b 5b 6c 7c 0c
    _a 1a _a 8b 0b 7b 0c 0c 0c
    _a 0a 6a 0b 4b 0b 0c 0c 1c
    0d 3d 0d 2e 0e 0e 0f 0f 0f
    8d 0d 0d 0e 0e 0e 0f 0f 7f
    0d 0d 0d 0e 0e 4e 0f 2f 0f
    9g 0g 0g 0h 2h 0h 3i 0i 0i
    0g 0g 0g 4h 0h 3h 0i 9i 0i
    0g 5g 1g 6h 0h 0h 0i 8i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_57():
    puzzle_string = f"""
    unique_rectangle_type4_03.sudoku
    9
    _a 0a 7a 4b 1b 0b 0c 0c 5c
    _a 0a _a 0b 0b 7b 9c 0c 0c
    8a _a 0a 0b 0b 0b 4c 0c 0c
    6d 0d 0d 0e 0e 1e 2f 4f 0f
    4d 0d 1d 0e 2e 0e 5f 0f 3f
    0d 7d 2d 6e 0e 0e 0f 0f 9f
    0g 0g 8g 0h 0h 0h 0i 0i 2i
    0g 0g 3g 9h 0h 0h 0i 0i 0i
    7g 0g 0g 0h 3h 6h 8i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_58():
    puzzle_string = f"""
    unique_rectangle_type4_04.sudoku
    9
    _a 3a _a 0b 9b 0b 8c 0c 7c
    8a _a 0a 1b 0b 0b 6c 0c 3c
    2a _a 0a 0b 0b 8b 0c 0c 0c
    0d 0d 3d 0e 0e 0e 5f 0f 0f
    6d 0d 0d 0e 0e 0e 0f 0f 1f
    0d 0d 2d 0e 0e 0e 7f 0f 0f
    0g 0g 0g 8h 0h 0h 0i 0i 4i
    7g 0g 1g 0h 0h 3h 0i 0i 8i
    9g 0g 5g 0h 7h 0h 0i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])


def test_sudoku_difficult_59():
    puzzle_string = f"""
    unique_rectangle_type4_05.sudoku
    9
    6a 9a 2a 5b 0b 0b 7c 3c 8c
    5a 3a 8a 2b 9b 7b 4c 6c 1c
    7a _a 0a 3b 8b 6b 5c 9c 2c
    0d 8d 0d 0e 0e 0e 6f 0f 0f
    1d 0d 0d 0e 0e 0e 9f 0f 4f
    0d 0d 5d 0e 0e 0e 1f 8f 0f
    8g 5g 9g 4h 7h 2h 3i 1i 6i
    4g 2g 6g 1h 5h 3h 8i 7i 9i
    3g 0g 0g 0h 6h 0h 2i 4i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()])
