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


def test_sudoku_first_lesson():
    puzzle_string = f"""
    first_lesson.sudoku
    9
    7a 5a 1a 2b 8b 9b 3c 6c 4c
    6a 2a 3a 1b 4b 7b 5c 9c 8c
    9a 4a 8a 3b 5b 6b 1c 2c 7c
    3d 8d 7d 4e 9e 5e 6f 1f 2f
    2d 1d 4d 6e 3e 8e 7f 5f 9f
    5d 9d 6d 7e 2e 1e 4f 8f 3f
    8g 7g 9g 5h 1h 3h 2i 4i 6i
    1g 3g 2g 0h 6h 4h 8i 7i 5i
    4g 6g 5g 8h 7h 2h 9i 3i 1i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_second_lesson_0():
    puzzle_string = f"""
    second_lesson_0.sudoku
    9
    3a 5a 8a 2b 0b 1b 4c 6c 7c
    2a 1a 6a 4b 0b 7b 9c 8c 5c
    4a 9a 7a 8b 0b 5b 2c 1c 3c
    6d 4d 3d 5e 0e 2e 7f 9f 1f
    9d 7d 5d 3e 0e 4e 6f 2f 8f
    1d 8d 2d 9e 0e 6e 5f 3f 4f
    7g 2g 9g 1h 0h 3h 8i 4i 6i
    8g 6g 1g 7h 0h 9h 3i 5i 2i
    5g 3g 4g 6h 0h 8h 1i 7i 9i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_easiest_0():
    puzzle_string = f"""
    easiest_0.sudoku
    9
    _a 3a 1a 8b 0b 2b 5c 9c 4c
    6a _a 8a 9b 0b 4b 0c 2c 7c
    2a 9a 4a 7b 1b 5b 0c 6c 3c
    8d 4d 6d 0e 0e 9e 0f 5f 1f
    3d 0d 9d 2e 5e 1e 4f 0f 6f
    1d 2d 0d 4e 0e 0e 3f 7f 9f
    9g 8g 0g 1h 2h 3h 6i 4i 5i
    5g 1g 0g 6h 0h 7h 9i 0i 8i
    4g 6g 3g 5h 0h 8h 7i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_easy_as_pie_0():
    puzzle_string = f"""
    easy_as_pie_0.sudoku
    9
    _a 4a 6a 8b 0b 1b 2c 0c 7c
    _a 9a 1a 4b 0b 7b 8c 0c 5c
    _a 0a 3a 5b 2b 9b 4c 1c 6c
    4d 0d 0d 2e 0e 0e 0f 7f 8f
    0d 6d 0d 3e 1e 8e 0f 4f 0f
    9d 3d 0d 0e 0e 5e 0f 0f 2f
    6g 8g 4g 1h 7h 2h 9i 0i 0i
    1g 0g 7g 9h 0h 3h 6i 8i 0i
    3g 0g 9g 6h 0h 4h 7i 2i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_picnic_0():
    puzzle_string = f"""
    picnic_0.sudoku
    9
    4a _a 2a 0b 8b 9b 0c 7c 3c
    7a 9a 1a 4b 0b 6b 0c 5c 0c
    _a 0a _a 0b 0b 0b 4c 0c 9c
    8d 1d 7d 0e 0e 5e 0f 0f 0f
    0d 6d 0d 8e 9e 7e 0f 2f 0f
    0d 0d 0d 6e 0e 0e 5f 8f 7f
    3g 0g 5g 0h 0h 0h 0i 0i 0i
    0g 8g 0g 7h 0h 3h 1i 9i 4i
    1g 7g 0g 2h 6h 0h 8i 0i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_picnic_1():
    puzzle_string = f"""
    picnic_1.sudoku
    9
    _a 0a 6a 3b 2b 7b 0c 8c 0c
    4a _a 0a 0b 5b 1b 0c 7c 6c
    _a 2a _a 4b 8b 0b 0c 3c 1c
    0d 3d 1d 0e 0e 0e 8f 2f 7f
    0d 0d 0d 0e 3e 0e 0f 0f 0f
    8d 7d 4d 0e 0e 0e 3f 9f 0f
    9g 4g 0g 0h 7h 5h 0i 6i 0i
    3g 6g 0g 2h 1h 0h 0i 0i 8i
    0g 5g 0g 6h 9h 3h 7i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_picnic_2():
    puzzle_string = f"""
    picnic_2.sudoku
    9
    _a 7a _a 5b 1b 3b 0c 2c 9c
    3a _a 9a 0b 6b 2b 0c 0c 1c
    5a 2a _a 0b 0b 0b 0c 3c 6c
    0d 0d 0d 0e 3e 0e 1f 4f 8f
    4d 0d 0d 0e 2e 0e 0f 0f 7f
    1d 6d 3d 0e 7e 0e 0f 0f 0f
    9g 1g 0g 0h 0h 0h 0i 8i 4i
    8g 0g 0g 4h 9h 0h 5i 0i 2i
    7g 5g 0g 2h 8h 6h 0i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch()])


def test_sudoku_simple_0():
    puzzle_string = f"""
    simple_0.sudoku
    9
    _a 4a _a 7b 8b 0b 0c 0c 0c
    6a _a 1a 0b 0b 4b 2c 0c 0c
    5a 7a _a 2b 6b 0b 0c 0c 0c
    0d 3d 0d 5e 0e 8e 0f 0f 6f
    1d 0d 0d 0e 0e 0e 0f 0f 7f
    7d 0d 0d 4e 0e 3e 0f 8f 0f
    0g 0g 0g 0h 4h 9h 0i 5i 8i
    0g 0g 6g 8h 0h 0h 3i 0i 2i
    0g 0g 0g 0h 3h 2h 0i 1i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])




























