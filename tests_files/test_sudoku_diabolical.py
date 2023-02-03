import pytest

from _defaults import default_test_puzzle
from puzzles import Sudoku
from solving import Solving

@pytest.mark.skip("skipped")
def test_diabolical_0():
    puzzle_string = f"""
    diabolical_0.sudoku
    9
    
    _a 0a _a   4b 0b 0b   7c 0c 0c
    _a 2a _a   0b 0b 6b   0c 1c 0c
    _a 0a _a   0b 3b 0b   0c 4c 2c
    
    3d 5d 2d   9e 0e 0e   0f 0f 7f
    4d 0d 0d   0e 0e 0e   0f 0f 9f
    9d 0d 0d   0e 0e 8e   3f 6f 4f
    
    8g 6g 0g   0h 7h 0h   0i 0i 0i
    0g 4g 0g   1h 0h 0h   0i 7i 0i
    0g 0g 7g   0h 0h 5h   0i 0i 0i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_nightmare_0():
    puzzle_string = f"""
    nightmare_0.sudoku
    9
    
    4a 5a 3a   7b 0b 9b   2c 0c 6c
    _a 0a 1a   0b 0b 0b   0c 0c 3c
    8a _a 0a   0b 0b 0b   0c 4c 0c
    
    5d 0d 8d   4e 0e 0e   0f 7f 0f
    0d 4d 0d   0e 0e 0e   0f 3f 0f
    0d 7d 0d   0e 0e 2e   4f 0f 5f
    
    0g 2g 0g   0h 0h 0h   0i 0i 4i
    6g 0g 0g   0h 0h 0h   3i 0i 0i
    7g 0g 4g   5h 0h 6h   8i 2i 0i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_maelstrom_0():
    puzzle_string = f"""
    maelstrom_0.sudoku
    9
    
    4a _a 0a   0b 0b 0b   0c 6c 0c
    _a 0a 7a   0b 8b 0b   5c 0c 3c
    3a 2a _a   0b 9b 0b   7c 0c 0c
    
    9d 0d 0d   0e 5e 8e   0f 0f 0f
    0d 0d 0d   9e 0e 1e   0f 0f 0f
    0d 0d 0d   6e 2e 0e   0f 0f 5f
    
    0g 0g 6g   0h 7h 0h   0i 1i 4i
    8g 0g 1g   0h 6h 0h   3i 0i 0i
    0g 7g 0g   0h 0h 0h   0i 0i 6i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())
