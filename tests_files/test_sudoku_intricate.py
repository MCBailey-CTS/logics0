from _defaults import default_test_puzzle
from puzzles import Sudoku
from techniques.CrossHatch import CrossHatch
from techniques.HiddenSingle import HiddenSingle
from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
from techniques.LockedCandidatesPointing import LockedCandidatesPointing
from techniques.NakedPair import NakedPair


def test_sudoku_intricate_0():
    puzzle_string = f"""
    intricate_0.sudoku
    9
    _a _a 1a _b _b _b _c _c _c
    _a _a 8a 5b _b 3b _c _c 9c
    _a _a 9a _b _b _b 2c 5c _c
    0d 0d 0d 6e 0e 0e 0f 0f 1f
    1d 0d 6d 9e 0e 8e 5f 0f 3f
    3d 0d 0d 0e 0e 4e 0f 0f 0f
    0g 4g 3g 0h 0h 0h 1i 0i 0i
    2g 0g 0g 1h 0h 7h 3i 0i 0i
    0g 0g 0g 0h 0h 0h 9i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()])


def test_sudoku_intricate_1():
    puzzle_string = f"""
    intricate_1.sudoku
    9
    1a 7a _a _b _b 9b 3c 8c 5c
    5a 6a _a _b 3b _b _c _c _c
    8a 3a 9a _b 7b _b 6c _c _c
    0d 2d 0d 0e 5e 3e 4f 0f 8f
    0d 5d 0d 2e 8e 4e 0f 3f 0f
    3d 4d 8d 0e 9e 0e 5f 2f 0f
    4g 8g 5g 9h 1h 7h 2i 6i 3i
    2g 1g 3g 0h 0h 0h 7i 0i 9i
    6g 9g 7g 3h 0h 0h 8i 0i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()])


def test_sudoku_intricate_2():
    puzzle_string = f"""
    intricate_2.sudoku
    9
    _a 9a _a 6b _b _b _c 7c 3c
    _a _a 7a 3b _b _b 9c _c 8c
    _a _a _a 8b 7b 9b 2c _c 6c
    7d 5d 0d 4e 2e 8e 0f 6f 0f
    2d 0d 0d 7e 0e 0e 0f 8f 4f
    4d 8d 0d 1e 0e 0e 0f 2f 0f
    0g 0g 5g 0h 0h 3h 0i 0i 0i
    0g 0g 4g 0h 0h 7h 8i 0i 0i
    1g 7g 0g 0h 0h 4h 0i 3i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), LockedCandidatesClaiming()])


def test_sudoku_intricate_3():
    puzzle_string = f"""
    intricate_3.sudoku
    9
    _a 4a 9a _b 7b 3b 5c _c _c
    5a 7a 8a _b 1b 6b _c 3c _c
    _a 3a 1a _b _b 5b _c _c 7c
    4d 1d 2d 5e 3e 8e 0f 7f 0f
    9d 5d 3d 7e 6e 2e 0f 0f 4f
    7d 8d 6d 1e 9e 4e 2f 5f 3f
    8g 0g 5g 3h 4h 0h 7i 6i 0i
    3g 0g 7g 6h 5h 0h 0i 0i 0i
    1g 6g 4g 0h 0h 7h 3i 0i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()])


def test_sudoku_intricate_4():
    puzzle_string = f"""
    intricate_4.sudoku
    9
    _a 3a 1a _b 7b _b 9c _c 2c
    7a 9a 5a _b _b _b 1c _c 8c
    _a _a 6a _b 1b 9b _c _c 7c
    9d 7d 2d 0e 0e 6e 4f 8f 1f
    6d 4d 3d 7e 8e 1e 0f 0f 9f
    5d 1d 8d 4e 9e 2e 6f 7f 3f
    0g 0g 9g 1h 0h 7h 0i 0i 0i
    3g 0g 4g 9h 0h 8h 7i 1i 0i
    1g 0g 7g 0h 6h 0h 8i 9i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), LockedCandidatesPointing()])


def test_sudoku_intricate_5():
    puzzle_string = f"""
    intricate_5.sudoku
    9
    6a _a _a 9b _b 7b _c _c _c
    _a _a 7a _b 2b _b _c _c _c
    2a 5a _a 3b _b 1b _c _c _c
    1d 0d 0d 0e 0e 0e 9f 8f 0f
    0d 8d 6d 0e 0e 0e 5f 2f 0f
    0d 2d 4d 0e 0e 0e 0f 0f 3f
    0g 0g 0g 4h 0h 5h 0i 7i 8i
    0g 0g 0g 0h 8h 0h 1i 0i 0i
    0g 0g 0g 6h 0h 3h 0i 0i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesPointing()])


def test_sudoku_intricate_6():
    puzzle_string = f"""
    intricate_6.sudoku
    9
    6a _a 5a 8b _b 3b 1c _c 4c
    8a _a _a 4b _b 2b 3c 6c _c
    _a 3a 4a _b 6b 1b 8c 9c _c
    0d 4d 8d 0e 0e 9e 6f 3f 0f
    0d 6d 2d 3e 0e 4e 5f 0f 0f
    0d 0d 3d 6e 0e 0e 4f 0f 0f
    4g 5g 9g 2h 3h 6h 7i 1i 8i
    0g 0g 6g 1h 4h 0h 9i 5i 3i
    3g 0g 0g 9h 0h 5h 2i 4i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()])


def test_sudoku_intricate_7():
    puzzle_string = f"""
    intricate_7.sudoku
    9
    9a _a _a _b _b _b _c _c _c
    _a 8a _a 7b 3b _b _c 6c 9c
    _a _a _a _b _b 2b _c 7c 1c
    0d 0d 0d 6e 0e 0e 0f 3f 5f
    0d 0d 0d 4e 0e 5e 0f 0f 0f
    2d 6d 0d 0e 0e 8e 0f 0f 0f
    4g 5g 0g 2h 0h 0h 0i 0i 0i
    6g 3g 0g 0h 9h 7h 0i 8i 0i
    0g 0g 0g 0h 0h 0h 0i 0i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()])


def test_sudoku_intricate_8():
    puzzle_string = f"""
    intricate_8.sudoku
    9
    _a 5a _a _b 8b _b _c _c 7c
    1a 3a 7a _b _b 9b _c _c _c
    9a 8a _a 7b _b _b _c _c _c
    0d 4d 0d 2e 1e 8e 0f 5f 0f
    0d 0d 0d 0e 0e 0e 0f 0f 0f
    0d 7d 0d 4e 9e 5e 0f 2f 0f
    0g 0g 0g 0h 0h 7h 0i 9i 5i
    0g 0g 0g 6h 0h 0h 2i 4i 3i
    5g 0g 0g 0h 3h 0h 0i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()])