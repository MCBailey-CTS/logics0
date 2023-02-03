
import pytest

from _defaults import default_test_puzzle
from puzzles import Sudoku
from solving import Solving


@pytest.mark.skip("skipped")
def test_annoying_00():
    puzzle_string = f"""
    annoying_00.sudoku
    9
    _a 0a _a   0b 0b 5b   0c 6c 0c
    4a _a 5a   0b 2b 0b   7c 1c 0c
    _a 7a _a   8b 0b 0b   0c 0c 3c
    
    0d 0d 7d   0e 5e 0e   0f 0f 9f
    0d 0d 0d   9e 0e 4e   0f 0f 0f
    9d 0d 0d   0e 6e 0e   1f 0f 0f
    
    7g 0g 0g   0h 0h 6h   0i 9i 0i
    0g 5g 6g   0h 9h 0h   2i 0i 7i
    0g 3g 0g   1h 0h 0h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_02():
    puzzle_string = f"""
    annoying_02.sudoku
    9
    _a 5a 1a   8b 9b 6b   0c 2c 4c
    _a 9a 6a   0b 2b 4b   0c 8c 0c
    4a 8a 2a   3b 0b 0b   0c 9c 6c
    
    6d 2d 7d   4e 3e 8e   9f 1f 5f
    5d 4d 3d   6e 1e 9e   2f 7f 8f
    9d 1d 8d   0e 0e 2e   4f 6f 3f
    
    2g 6g 4g   0h 8h 3h   0i 5i 9i
    8g 7g 0g   0h 4h 0h   6i 3i 0i
    1g 3g 0g   0h 6h 0h   8i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_05():
    puzzle_string = f"""
    annoying_05.sudoku
    9
    6a 8a _a   0b 0b 0b   3c 0c 2c
    2a 5a 3a   7b 0b 6b   1c 0c 0c
    _a 0a _a   2b 8b 3b   6c 5c 0c
    
    1d 6d 2d   0e 0e 4e   7f 0f 0f
    5d 7d 8d   1e 3e 2e   9f 4f 6f
    4d 3d 9d   8e 6e 7e   5f 2f 1f
    
    8g 0g 5g   6h 2h 0h   4i 0i 0i
    0g 2g 0g   3h 0h 5h   8i 6i 0i
    3g 0g 6g   0h 7h 8h   2i 1i 5i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_06():
    puzzle_string = f"""
    annoying_06.sudoku
    9
    7a _a 0a   0b 0b 9b   5c 0c 0c
    _a 5a 8a   0b 3b 2b   0c 0c 0c
    9a _a 6a   0b 0b 5b   0c 0c 0c
    
    5d 0d 0d   0e 9e 0e   0f 0f 0f
    0d 4d 0d   2e 0e 8e   0f 3f 0f
    0d 0d 0d   0e 7e 0e   0f 0f 6f
    
    0g 0g 0g   1h 0h 0h   4i 0i 9i
    0g 0g 0g   0h 2h 0h   1i 0i 0i
    0g 0g 1g   9h 0h 0h   0i 0i 2i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_07():
    puzzle_string = f"""
    annoying_07.sudoku
    9
    3a _a 7a   2b 5b 0b   6c 0c 4c
    _a 0a 5a   0b 0b 0b   0c 7c 3c
    _a 0a _a   0b 7b 3b   0c 8c 5c
    
    0d 0d 2d   7e 3e 0e   0f 0f 1f
    6d 3d 0d   0e 9e 0e   0f 2f 7f
    5d 7d 0d   0e 0e 2e   3f 0f 0f
    
    0g 5g 6g   8h 4h 0h   0i 3i 0i
    0g 0g 3g   0h 6h 0h   0i 0i 0i
    8g 9g 4g   3h 2h 1h   7i 5i 6i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_11():
    puzzle_string = f"""
    annoying_11.sudoku
    9
    _a 0a 6a   4b 7b 9b   3c 0c 2c
    9a 3a _a   5b 8b 2b   0c 4c 6c
    _a 2a _a   6b 1b 3b   0c 9c 0c
    
    0d 6d 0d   0e 0e 7e   4f 0f 0f
    8d 4d 9d   3e 0e 6e   0f 7f 1f
    0d 7d 5d   0e 0e 4e   0f 6f 0f
    
    6g 9g 0g   7h 4h 5h   0i 0i 0i
    0g 1g 0g   2h 6h 8h   0i 0i 0i
    7g 0g 2g   9h 3h 1h   6i 0i 4i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_13():
    puzzle_string = f"""
    annoying_13.sudoku
    9
    _a 6a 7a   0b 0b 0b   0c 5c 0c
    _a 3a 2a   5b 7b 6b   8c 0c 9c
    5a 8a 9a   0b 1b 0b   0c 7c 6c
    
    6d 0d 5d   7e 0e 0e   0f 2f 8f
    9d 7d 3d   0e 4e 0e   1f 6f 5f
    8d 2d 0d   6e 0e 0e   7f 0f 3f
    
    2g 0g 0g   0h 6h 0h   0i 8i 7i
    3g 0g 6g   4h 8h 7h   5i 0i 2i
    7g 0g 8g   0h 0h 0h   6i 3i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_17():
    puzzle_string = f"""
    annoying_17.sudoku
    9
    _a 7a 5a   2b 4b 3b   0c 0c 1c
    3a 2a _a   1b 6b 7b   5c 4c 0c
    4a 6a 1a   0b 0b 0b   3c 2c 7c
    
    5d 1d 7d   0e 0e 4e   0f 3f 0f
    0d 3d 4d   0e 0e 1e   9f 7f 5f
    0d 8d 0d   7e 3e 5e   0f 1f 4f
    
    7g 9g 3g   4h 0h 0h   1i 0i 2i
    0g 4g 2g   0h 1h 0h   7i 0i 3i
    1g 5g 0g   3h 7h 2h   4i 0i 0i
    
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_22():
    puzzle_string = f"""
    annoying_22.sudoku
    9
    _a 3a 4a   5b 0b 0b   0c 0c 0c
    _a 0a 6a   9b 0b 3b   4c 0c 7c
    5a _a 0a   0b 6b 4b   0c 0c 0c
    
    0d 9d 0d   0e 0e 0e   0f 0f 0f
    4d 0d 2d   0e 7e 0e   9f 0f 1f
    0d 0d 0d   0e 0e 0e   0f 2f 0f
    
    0g 0g 0g   6h 2h 0h   0i 0i 8i
    1g 0g 8g   7h 0h 9h   3i 0i 0i
    0g 0g 0g   0h 0h 8h   2i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_23():
    puzzle_string = f"""
    annoying_23.sudoku
    9
    _a 6a _a   0b 9b 0b   0c 3c 0c
    _a 0a _a   0b 0b 8b   0c 0c 1c
    _a 0a 7a   0b 6b 0b   2c 0c 0c
    
    2d 4d 0d   0e 0e 6e   7f 8f 0f
    0d 0d 0d   5e 0e 3e   0f 0f 0f
    0d 8d 9d   2e 0e 0e   0f 1f 5f
    
    0g 0g 4g   0h 5h 0h   1i 0i 0i
    9g 0g 0g   4h 0h 0h   0i 0i 0i
    0g 5g 0g   0h 3h 0h   0i 9i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_25():
    puzzle_string = f"""
    annoying_25.sudoku
    9
    6a _a 0a   0b 8b 0b   0c 2c 9c
    _a 0a _a   0b 2b 6b   8c 7c 0c
    _a 0a 4a   0b 0b 3b   0c 0c 0c
    
    0d 4d 0d   0e 0e 0e   0f 0f 1f
    0d 0d 3d   0e 0e 0e   5f 0f 0f
    9d 0d 0d   0e 0e 0e   0f 3f 0f
    
    0g 0g 0g   7h 0h 0h   2i 0i 0i
    0g 2g 9g   6h 3h 0h   0i 0i 0i
    5g 7g 0g   0h 9h 0h   0i 0i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_26():
    puzzle_string = f"""
    annoying_26.sudoku
    9
    _a 7a _a   4b 2b 8b   0c 0c 1c
    _a 0a 3a   0b 0b 0b   0c 0c 0c
    2a 8a _a   0b 1b 0b   0c 0c 0c
    
    6d 0d 0d   0e 5e 0e   0f 0f 0f
    0d 0d 5d   3e 0e 4e   2f 0f 0f
    0d 0d 0d   0e 6e 0e   0f 0f 4f
    
    0g 0g 0g   0h 4h 0h   0i 9i 5i
    0g 0g 0g   0h 0h 0h   8i 0i 0i
    9g 0g 0g   5h 3h 2h   0i 6i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_27():
    puzzle_string = f"""
    annoying_27.sudoku
    9
    _a 0a _a   9b 8b 0b   4c 0c 0c
    2a _a 0a   0b 0b 0b   0c 0c 0c
    _a 0a _a   0b 5b 4b   9c 7c 0c
    
    8d 3d 0d   0e 0e 2e   0f 0f 9f
    0d 4d 1d   0e 0e 0e   7f 2f 0f
    9d 0d 0d   8e 0e 0e   0f 4f 5f
    
    0g 2g 6g   4h 1h 0h   0i 0i 0i
    0g 0g 0g   0h 0h 0h   0i 0i 4i
    0g 0g 8g   0h 3h 9h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_28():
    puzzle_string = f"""
    annoying_28.sudoku
    9
    5a _a 0a   0b 4b 6b   0c 0c 0c
    1a _a 0a   3b 5b 2b   8c 7c 0c
    _a 2a _a   0b 0b 0b   0c 0c 0c
    
    8d 0d 0d   5e 0e 3e   9f 0f 0f
    0d 0d 0d   0e 0e 0e   0f 0f 0f
    0d 0d 5d   6e 0e 1e   0f 0f 7f
    
    0g 0g 0g   0h 0h 0h   0i 4i 0i
    0g 3g 8g   1h 7h 9h   0i 0i 6i
    0g 0g 0g   4h 6h 0h   0i 0i 8i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_29():
    puzzle_string = f"""
    annoying_29.sudoku
    9
    _a 0a _a   0b 8b 0b   1c 0c 0c
    _a 0a 3a   0b 0b 0b   6c 0c 5c
    9a 1a _a   0b 0b 0b   0c 4c 0c
    
    0d 4d 0d   0e 9e 0e   0f 0f 7f
    0d 9d 0d   1e 0e 5e   0f 2f 0f
    2d 0d 0d   0e 6e 0e   0f 9f 0f
    
    0g 7g 0g   0h 0h 0h   0i 5i 4i
    4g 0g 8g   0h 0h 0h   7i 0i 0i
    0g 0g 9g   0h 5h 0h   0i 0i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_30():
    puzzle_string = f"""
    annoying_30.sudoku
    9
    _a 7a 5a   6b 0b 0b   0c 0c 0c
    2a _a 0a   0b 0b 0b   8c 0c 0c
    1a _a 3a   0b 0b 8b   0c 0c 2c
    
    0d 1d 0d   2e 0e 9e   0f 0f 0f
    0d 0d 8d   0e 0e 0e   5f 0f 0f
    0d 0d 0d   1e 0e 6e   0f 3f 0f
    
    5g 0g 0g   4h 0h 0h   1i 0i 6i
    0g 0g 6g   0h 0h 0h   0i 0i 9i
    0g 0g 0g   0h 0h 2h   7i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_32():
    puzzle_string = f"""
    annoying_32.sudoku
    9
    _a 7a 5a   2b 0b 0b   1c 0c 0c
    _a 9a 3a   6b 0b 1b   8c 0c 0c
    _a 0a 4a   0b 0b 0b   0c 0c 0c
    
    0d 1d 0d   0e 0e 4e   0f 0f 0f
    0d 0d 9d   5e 0e 2e   4f 0f 0f
    0d 0d 0d   8e 0e 0e   0f 3f 0f
    
    0g 0g 0g   0h 0h 0h   3i 0i 0i
    0g 0g 2g   3h 0h 9h   7i 1i 0i
    0g 0g 8g   0h 0h 7h   6i 4i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_33():
    puzzle_string = f"""
    annoying_33.sudoku
    9
    _a 4a _a   0b 0b 0b   0c 0c 0c
    6a 5a _a   0b 3b 0b   0c 0c 1c
    _a 0a _a   8b 0b 0b   2c 0c 0c
    
    0d 3d 0d   0e 2e 0e   9f 0f 0f
    0d 2d 9d   3e 0e 4e   6f 5f 0f
    0d 0d 7d   0e 6e 0e   0f 3f 0f
    
    0g 0g 4g   0h 0h 6h   0i 0i 0i
    7g 0g 0g   0h 8h 0h   0i 9i 6i
    0g 0g 0g   0h 0h 0h   0i 7i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_annoying_35():
    puzzle_string = f"""
    annoying_35.sudoku
    9
    _a 5a 9a   0b 0b 0b   0c 0c 0c
    8a _a 0a   0b 0b 0b   0c 7c 1c
    _a 0a _a   0b 0b 8b   2c 5c 0c
    
    6d 0d 0d   0e 3e 0e   7f 0f 0f
    7d 8d 0d   6e 0e 1e   0f 4f 5f
    0d 0d 4d   0e 7e 0e   0f 0f 8f
    
    0g 2g 3g   1h 0h 0h   0i 0i 0i
    5g 7g 0g   0h 0h 0h   0i 0i 3i
    0g 0g 0g   0h 0h 0h   1i 9i 0i
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())




@pytest.mark.skip("skipped")
def test_sudoku_annoying_01():
    puzzle_string = f"""
    annoying_01.sudoku
    9
    9 4 2 5 6 1 7 8 3
    . 8 . 7 . 4 . . 1
    1 . 7 . 8 . 5 4 .
    8 . . 1 . 9 . 7 .
    . . . 6 . 7 . . 8
    7 9 . 3 . 8 . . 4
    . . 9 4 . . 8 . 7
    . 7 . 8 . 5 4 3 .
    4 . 8 . 7 . . 1 .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_03():
    puzzle_string = f"""
    annoying_03.sudoku
    9
    2 4 9 5 3 7 1 6 8
    7 1 . . 2 8 . 3 4
    . . . . 4 1 2 . 7
    . 9 2 1 7 . 8 4 3
    4 3 7 8 9 2 6 1 5
    . . 1 3 . 4 7 2 9
    1 . . 4 8 . . 7 2
    . 7 4 2 1 . . 8 6
    . 2 . 7 . 3 4 . 1
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_04():
    puzzle_string = f"""
    annoying_04.sudoku
    9
    . 5 4 . . 6 7 . .
    3 . . . . . . 6 .
    6 . 7 2 . . . . .
    . 6 . . 8 9 1 . 5
    8 . 9 5 . 2 6 . 7
    4 . 5 6 3 . 8 2 9
    . . . . 6 4 9 . .
    . . . . 2 . . . 6
    . . 6 9 . . 2 8 .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_08():
    puzzle_string = f"""
    annoying_08.sudoku
    9
    . 5 2 8 . . . 4 .
    . 3 4 2 . . . 7 9
    . 7 6 1 . . . 2 5
    . 1 9 . 8 . . 5 .
    . 2 7 9 3 . 4 1 8
    . 4 8 . 1 . 9 6 .
    2 8 . . . 1 . 9 4
    4 9 1 . 2 8 5 3 .
    7 6 . . . 9 2 8 1
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_09():
    puzzle_string = f"""
    annoying_09.sudoku
    9
    . 5 . 8 3 . 7 . 6
    8 . 7 4 . 1 3 . .
    3 . 2 7 5 . . 8 .
    . . . . . . 8 . .
    . 3 . 9 . 5 . 7 .
    . . 5 . . . . . .
    . . . . 9 . 5 3 7
    5 . 3 1 . 7 2 . 8
    7 . . 5 . 3 . 4 .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_10():
    puzzle_string = f"""
    annoying_10.sudoku
    9
    3 4 . . 2 . 1 7 .
    2 . 9 1 . 4 3 5 8
    . . 1 . . 3 2 4 .
    . . . 6 3 5 4 1 2
    1 2 3 4 9 7 6 8 5
    4 . . 8 1 2 9 3 7
    . 3 . 2 . 1 . . 4
    6 . 4 3 . . 5 2 1
    . 1 2 . 4 . . . 3
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_12():
    puzzle_string = f"""
    annoying_12.sudoku
    9
    5 . 2 . 6 9 3 7 8
    9 3 8 . . 5 6 4 1
    6 . 7 3 8 . 2 5 9
    1 8 4 6 5 . . . 2
    2 6 5 . . . 4 8 .
    3 7 9 . . 8 1 6 5
    4 5 1 . . 2 8 . 6
    7 9 3 8 1 6 5 2 4
    8 2 6 5 . . . 1 .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_14():
    puzzle_string = f"""
    annoying_14.sudoku
    9
    9 . . 2 . 7 . 6 .
    . . . . . . 9 . .
    . . 7 9 4 6 . . 1
    8 2 . 4 . . . 9 .
    5 7 9 8 1 . 4 . 6
    . 3 4 . . 9 . 8 .
    4 . . 7 9 8 2 . .
    . . 8 . . . . 4 9
    . 9 . 3 . 4 . . .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_15():
    puzzle_string = f"""
    annoying_15.sudoku
    9
    4 3 5 1 8 9 . . .
    6 9 7 2 4 5 3 8 1
    1 2 8 6 3 7 4 5 9
    3 8 . . . 1 . 9 .
    9 . 1 . 2 3 8 . 4
    7 . . . . 8 1 3 .
    2 1 3 . . 6 7 4 8
    5 7 6 8 1 4 9 2 3
    8 4 9 3 7 2 5 1 6
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_16():
    puzzle_string = f"""
    annoying_16.sudoku
    9
    4 1 7 9 8 2 5 6 3
    8 5 2 6 . . 9 7 1
    3 6 9 1 5 7 4 8 2
    5 7 1 4 6 . 3 2 .
    6 . 4 5 . . . . 7
    . 3 8 . . 1 6 5 4
    . 8 5 . 1 . 7 . 6
    1 4 6 . . 5 . . .
    7 . 3 8 . 6 . . 5
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_18():
    puzzle_string = f"""
    annoying_18.sudoku
    9
    . . 7 . . . . . .
    4 . 9 1 7 . 5 . .
    2 . 8 . 6 . 9 . 7
    . . . 4 . 6 . . .
    6 . 5 2 . 8 7 . 9
    . . . 7 . 5 . . .
    1 . 3 6 5 . 8 . 2
    . . 6 . . 7 3 . 1
    . . . . . 1 6 . .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_19():
    puzzle_string = f"""
    annoying_19.sudoku
    9
    . . . . 3 . . 7 .
    7 . 8 1 . 6 . . .
    3 . 1 . . . 8 . .
    9 . . 3 . 2 . . .
    . 3 . . . . . 4 .
    . . . 6 . 5 . . 9
    . . 4 . . . 9 . 3
    . . 3 2 . 4 7 . 5
    . 8 . . 5 3 . . .
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_20():
    puzzle_string = f"""
    annoying_20.sudoku
    9
    4..|9..|.7.
    .76|.85|...
    ..5|...|...
    ---+---+---
    1.4|2..|...
    .8.|1.9|.5.
    ...|..3|4.1
    ---+---+---
    ...|...|7..
    ...|36.|59.
    .2.|..7|..8
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_21():
    puzzle_string = f"""
    annoying_21.sudoku
    9
    .4.|2.5|.3.
    8..|97.|4..
    ...|...|.92
    ---+---+---
    ..4|...|.78
    ...|...|...
    71.|...|3..
    ---+---+---
    58.|...|...
    ..2|.13|..5
    .9.|8.6|.2.
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_24():
    puzzle_string = f"""
    annoying_24.sudoku
    9
    6..|5..|2..
    7..|..6|.49
    .9.|4.7|3..
    ---+---+---
    .3.|...|62.
    4..|...|..7
    .26|...|.3.
    ---+---+---
    ..1|3.5|.8.
    37.|1..|..6
    ..2|..9|..3
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_31():
    puzzle_string = f"""
    annoying_31.sudoku
    9
    ..5|8.4|.31
    3..|.5.|...
    ..9|.6.|.5.
    ---+---+---
    9..|..7|..8
    5..|...|..2
    2..|5..|..9
    ---+---+---
    .9.|.1.|8..
    ...|.8.|..7
    86.|9.3|4..
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())


@pytest.mark.skip("skipped")
def test_sudoku_annoying_36():
    puzzle_string = f"""
    annoying_36.sudoku
    9
    ...|...|..3
    .4.|..3|1.5
    .1.|4..|69.
    ---+---+---
    8..|9.4|...
    .57|...|46.
    ...|7.6|..2
    ---+---+---
    .89|..1|.5.
    5.1|3..|.8.
    7..|...|...
    """
    assert default_test_puzzle(puzzle_string, Sudoku, Solving.sudoku_techniques())