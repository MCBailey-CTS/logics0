import pytest

from _defaults import default_test_puzzle
from puzzles import Sudoku
from solving import Solving


@pytest.mark.skip("skipped")
def test_devious_1():
    puzzle_string = f"""
    devious_1.sudoku
    9
    _a 0a 3a   9b 0b 4b   0c 0c 0c
    5a _a 4a   2b 3b 0b   0c 0c 0c
    _a 8a _a   0b 0b 0b   0c 0c 5c
    
    0d 0d 0d   0e 4e 0e   3f 5f 0f
    3d 0d 0d   0e 0e 0e   0f 0f 6f
    0d 1d 2d   0e 6e 0e   0f 0f 0f
    
    6g 0g 0g   0h 0h 0h   0i 1i 0i
    0g 0g 0g   0h 1h 3h   6i 0i 9i
    0g 0g 0g   5h 0h 6h   8i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_2():
    puzzle_string = f"""
    devious_2.sudoku
    9
    _a 0a _a   0b 0b 0b   7c 0c 0c
    _a 8a _a   0b 0b 6b   0c 0c 1c
    9a 7a _a   0b 0b 0b   0c 5c 3c
    
    0d 0d 8d   2e 0e 0e   3f 6f 0f
    0d 0d 0d   7e 0e 4e   0f 0f 0f
    0d 5d 3d   0e 0e 8e   4f 0f 0f
    
    4g 9g 0g   0h 0h 0h   0i 2i 8i
    6g 0g 0g   1h 0h 0h   0i 7i 0i
    0g 0g 7g   0h 0h 0h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_3():
    puzzle_string = f"""
    devious_3.sudoku
    9
    1a _a 0a   7b 0b 0b   0c 0c 0c
    _a 2a _a   9b 0b 5b   0c 6c 0c
    _a 0a 9a   0b 0b 0b   8c 0c 0c
    
    6d 7d 0d   0e 0e 4e   9f 0f 8f
    0d 0d 8d   0e 0e 0e   2f 0f 0f
    2d 0d 1d   8e 0e 0e   0f 7f 6f
    
    0g 0g 3g   0h 0h 0h   6i 0i 0i
    0g 4g 0g   1h 0h 8h   0i 3i 0i
    0g 0g 0g   0h 0h 7h   0i 0i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_4():
    puzzle_string = f"""
    devious_4.sudoku
    9
    _a 0a _a   6b 7b 5b   2c 0c 0c
    _a 0a _a   0b 2b 0b   0c 0c 8c
    _a 3a _a   4b 0b 1b   0c 0c 0c
    
    0d 7d 5d   0e 4e 0e   6f 8f 0f
    0d 0d 6d   0e 0e 0e   3f 0f 0f
    0d 4d 9d   0e 1e 0e   7f 2f 0f
    
    0g 0g 0g   7h 0h 4h   0i 9i 0i
    4g 0g 0g   0h 3h 0h   0i 0i 0i
    0g 0g 1g   2h 6h 8h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_5():
    puzzle_string = f"""
    devious_5.sudoku
    9
    _a 0a 8a   0b 0b 7b   0c 0c 0c
    3a _a 0a   6b 0b 0b   0c 8c 0c
    _a 0a 5a   1b 8b 0b   0c 4c 0c
    
    0d 0d 4d   0e 7e 0e   0f 6f 1f
    0d 0d 6d   0e 0e 0e   3f 0f 0f
    9d 1d 0d   0e 4e 0e   8f 0f 0f
    
    0g 5g 0g   0h 3h 8h   9i 0i 0i
    0g 2g 0g   0h 0h 1h   0i 0i 3i
    0g 0g 0g   7h 0h 0h   6i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_6():
    puzzle_string = f"""
    devious_6.sudoku
    9
    
    6a _a 0a   0b 0b 3b   5c 0c 0c
    8a _a 0a   4b 0b 0b   0c 0c 3c
    _a 5a 2a   0b 6b 0b   0c 0c 0c
    
    0d 0d 0d   0e 0e 9e   2f 0f 4f
    5d 7d 0d   0e 2e 0e   0f 9f 6f
    2d 0d 8d   6e 0e 0e   0f 0f 0f
    
    0g 0g 0g   0h 1h 0h   7i 4i 0i
    7g 0g 0g   0h 0h 8h   0i 0i 5i
    0g 0g 5g   7h 0h 0h   0i 0i 1i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_7():
    puzzle_string = f"""
    devious_7.sudoku
    9
    
    _a 0a 6a   0b 0b 4b   0c 0c 0c
    8a _a 0a   0b 0b 6b   0c 0c 0c
    _a 9a _a   5b 0b 0b   1c 8c 0c
    
    0d 7d 0d   0e 2e 0e   0f 0f 0f
    6d 3d 1d   0e 0e 0e   7f 2f 9f
    0d 0d 0d   0e 9e 0e   0f 3f 0f
    
    0g 2g 3g   0h 0h 7h   0i 1i 0i
    0g 0g 0g   2h 0h 0h   0i 0i 5i
    0g 0g 0g   1h 0h 0h   2i 0i 0i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_devious_8():
    puzzle_string = f"""
    devious_8.sudoku
    9
    
    3a _a 0a   0b 0b 9b   0c 0c 0c
    _a 5a 9a   8b 0b 0b   1c 0c 0c
    _a 1a _a   0b 5b 0b   4c 9c 0c
    
    0d 4d 0d   2e 0e 0e   0f 5f 0f
    0d 0d 0d   5e 0e 8e   0f 0f 0f
    0d 6d 0d   0e 0e 3e   0f 4f 0f
    
    0g 3g 6g   0h 8h 0h   0i 2i 0i
    0g 0g 5g   0h 0h 2h   9i 1i 0i
    0g 0g 0g   7h 0h 0h   0i 0i 5i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())