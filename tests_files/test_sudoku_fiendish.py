import pytest

from _defaults import default_test_puzzle
from puzzles import Sudoku
from solving import Solving


@pytest.mark.skip("skipped")
def test_fiendish_0():
    puzzle_string = f"""
    fiendish_0.sudoku
    9
    
    _a 8a _a   3b 0b 0b   0c 0c 0c
    _a 6a _a   0b 4b 2b   0c 0c 8c
    3a _a 0a   8b 0b 0b   5c 4c 0c
    
    0d 3d 0d   0e 0e 0e   0f 0f 9f
    0d 4d 0d   1e 0e 8e   0f 7f 0f
    7d 0d 0d   0e 0e 0e   0f 2f 0f
    
    0g 2g 7g   0h 0h 4h   0i 0i 5i
    8g 0g 0g   2h 3h 0h   0i 6i 0i
    0g 0g 0g   0h 0h 9h   0i 8i 0i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())
