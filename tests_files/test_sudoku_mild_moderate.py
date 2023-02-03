from _defaults import default_test_puzzle
from puzzles import Sudoku
from techniques.CrossHatch import CrossHatch
from techniques.HiddenSingle import HiddenSingle
from techniques.NakedPair import NakedPair


def test_sudoku_mild_0():
    puzzle_string = f"""
    mild_0.sudoku
    9
    _a 4a 3a 8b 0b 0b 0c 0c 0c
    5a _a 0a 0b 0b 0b 0c 0c 0c
    2a 1a _a 0b 0b 6b 0c 9c 4c
    4d 2d 0d 9e 0e 0e 6f 3f 0f
    3d 0d 5d 0e 0e 0e 4f 0f 1f
    0d 8d 1d 0e 0e 4e 0f 2f 9f
    8g 7g 0g 4h 0h 0h 0i 6i 5i
    0g 0g 0g 0h 0h 0h 0i 0i 2i
    0g 0g 0g 0h 0h 2h 3i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_mild_1():
    puzzle_string = f"""
    mild_1.sudoku
    9
    4a 3a _a 0b 6b 2b 5c 0c 8c
    _a 0a 2a 4b 7b 0b 0c 6c 0c
    _a 0a _a 0b 0b 0b 4c 0c 0c
    0d 0d 0d 0e 0e 0e 0f 0f 4f
    8d 0d 0d 7e 1e 5e 0f 0f 2f
    1d 0d 0d 0e 0e 0e 0f 0f 0f
    0g 0g 9g 0h 0h 0h 0i 0i 0i
    0g 6g 0g 0h 2h 9h 3i 0i 0i
    2g 0g 4g 1h 8h 0h 0i 9i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_mild_2():
    puzzle_string = f"""
    mild_2.sudoku
    9
    8a 6a _a 0b 5b 0b 0c 0c 0c
    _a 0a _a 0b 0b 3b 8c 1c 6c
    _a 0a _a 0b 1b 0b 0c 0c 0c
    0d 4d 0d 0e 0e 0e 0f 6f 2f
    0d 0d 7d 2e 0e 9e 3f 0f 0f
    2d 8d 0d 0e 0e 0e 0f 5f 0f
    0g 0g 0g 0h 2h 0h 0i 0i 0i
    7g 1g 3g 6h 0h 0h 0i 0i 0i
    0g 0g 0g 0h 9h 0h 0i 3i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_mild_3():
    puzzle_string = f"""
    mild_3.sudoku
    9
    5a 9a _a 4b 6b 0b 0c 0c 1c
    _a 3a 6a 8b 0b 7b 0c 0c 5c
    _a 0a _a 0b 0b 0b 0c 0c 0c
    0d 0d 0d 0e 0e 0e 3f 2f 0f
    0d 0d 0d 7e 4e 9e 0f 0f 0f
    0d 1d 7d 0e 0e 0e 0f 0f 0f
    0g 0g 0g 0h 0h 0h 0i 0i 0i
    2g 0g 0g 6h 0h 8h 1i 7i 0i
    3g 0g 0g 0h 2h 1h 0i 5i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_mild_4():
    puzzle_string = f"""
    mild_4.sudoku
    9
    4a _a 0a 0b 5b 7b 2c 8c 0c
    _a 1a _a 0b 2b 0b 4c 0c 0c
    _a 0a _a 0b 0b 0b 0c 0c 9c
    9d 6d 0d 0e 7e 0e 0f 4f 1f
    0d 7d 0d 0e 0e 0e 0f 3f 0f
    8d 3d 0d 0e 1e 0e 0f 5f 7f
    3g 0g 0g 0h 0h 0h 0i 0i 0i
    0g 0g 8g 0h 6h 0h 0i 2i 0i
    0g 5g 6g 3h 8h 0h 0i 0i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), HiddenSingle()])


def test_sudoku_moderate_0():
    puzzle_string = f"""
    moderate_0.sudoku
    9
    1a _a 2a 0b 0b 0b 4c 0c 0c
    _a 3a 9a 0b 8b 0b 0c 7c 0c
    _a 7a 8a 0b 0b 0b 0c 0c 0c
    7d 0d 0d 8e 0e 6e 0f 0f 1f
    0d 5d 0d 0e 0e 0e 0f 8f 0f
    8d 0d 0d 5e 0e 2e 0f 0f 9f
    0g 0g 0g 0h 0h 0h 8i 6i 0i
    0g 1g 0g 0h 6h 0h 3i 5i 0i
    0g 0g 7g 0h 0h 0h 9i 0i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, [CrossHatch(), NakedPair()])