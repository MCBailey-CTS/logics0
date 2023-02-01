import pytest

from _defaults import default_test_puzzle
from puzzles import *
from solving import Solving
EXPLICITLY = "EXPLICITLY"


def test_skyscrapers_001():
    puzzle_string = f"""
        001.skyscrapers
        4
        1234 1234 1234 1234 04 01
        1234 1234 1234 1234 02 02
        1234 1234 1234 1234 03 02
        1234 1234 1234 1234 01 02
        03   02   02   01 $ $ 
        01   03   02   02   $ $
        """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


def test_skyscrapers_002():
    puzzle_string = f"""
    002.skyscrapers
    4
    _ _ _ _ 3 1
    _ _ _ _ 2 2
    _ _ _ _ 1 3
    _ _ _ _ 2 2
    2 2 4 1 $ $
    2 2 1 4 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


def test_skyscrapers_003():
    puzzle_string = f"""
    003.skyscrapers
    4
    _ _ _ _ 2 3
    _ _ _ _ 3 1
    _ _ _ _ 2 2
    _ _ _ _ 1 2
    4 1 2 2 $ $
    1 4 2 2 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_004():
    puzzle_string = f"""
    004.skyscrapers
    4
    _ _ _ _ 2 2
    _ _ _ _ 3 2
    _ _ _ _ 1 3
    _ _ _ _ 2 1
    3 1 2 2 $ $
    2 3 3 1 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


def test_skyscrapers_005():
    puzzle_string = f"""
    005.skyscrapers
    4
    _ _ _ _ ? ?
    _ _ _ _ 3 ?
    _ _ _ _ ? 2
    _ _ _ _ ? ?
    3 1 ? 2 $ $
    1 3 ? 2 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_006():
    puzzle_string = f"""
    006.skyscrapers
    4
     _ _ _ _ 2 3
     _ _ _ _ 2 2
     _ _ _ _ ? ?
     _ _ _ _ ? 2
     3 ? ? 2 $ $
     ? 3 ? ? $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_007():
    puzzle_string = f"""
    007.skyscrapers
    4
     _ _ _ _ ? 1
     _ _ _ _ 2 ?
     _ _ _ _ 1 2
     _ _ _ _ 2 ?
     2 2 ? ? $ $
     ? ? 1 ? $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_008():
    puzzle_string = f"""
    008.skyscrapers
    4
     _ _ _ _ ? ?
     _ _ _ _ 3 ?
     _ _ _ _ 2 ?
     _ _ _ _ 2 ?
     ? ? 3 ? $ $
     ? 1 ? 3 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_009():
    puzzle_string = f"""
    009.skyscrapers
    4
    . . . . ? 3
    . . . . 3 ?
    . . . . ? 3
    . . . . ? ?
    ? 2 3 ? ? ?
    ? ? ? ? ? ?
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_010():
    puzzle_string = f"""
    010.skyscrapers
    5
    _ _ _ _ _ 3 2
    _ _ _ _ _ 1 4
    _ _ _ _ _ 2 1
    _ _ _ _ _ 3 3
    _ _ _ _ _ 2 4
    2 3 3 1 2 $ $
    3 1 2 3 3 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_011():
    puzzle_string = f"""
    011.skyscrapers
    5
    _ _ _ _ _ 2 4
    _ _ _ _ _ 4 2
    _ _ _ _ _ 3 2
    _ _ _ _ _ 2 1
    _ _ _ _ _ 1 3
    4 1 2 2 3 $ $
    1 4 2 2 2 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_012():
    puzzle_string = f"""
    012.skyscrapers
    5
    _ _ _ _ _ 2 4
    _ _ _ _ _ 1 2
    _ _ _ _ _ 5 1
    _ _ _ _ _ 3 2
    _ _ _ _ _ 2 2
    2 1 2 4 3 $ $
    2 3 1 2 3 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_013():
    puzzle_string = f"""
    013.skyscrapers
    5
    _ _ _ _ _ 0 2
    _ _ _ _ _ 3 1
    _ _ _ _ _ 2 2
    _ _ _ _ _ 1 3
    _ _ _ _ _ 0 3
    4 0 0 1 0 $ $
    0 0 0 2 4 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_014():
    puzzle_string = f"""
    014.skyscrapers
    5
    _ _ _ _ _ ? 2
    _ _ _ _ _ 2 ?
    _ _ _ _ _ 3 3
    _ _ _ _ _ 3 ?
    _ _ _ _ _ ? ?
    1 ? 2 3 ? $ $
    ? 1 ? 2 2 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_015():
    puzzle_string = f"""
    015.skyscrapers
    5
    _ _ _ _ _ 2 0
    _ _ _ _ _ 2 3
    _ _ _ _ _ 4 2
    _ _ _ _ _ 1 0
    _ _ _ _ _ 4 0
    3 1 2 0 2 $ $
    2 0 4 0 0 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_016():
    puzzle_string = f"""
    016.skyscrapers
    5
    _ _ _ _ _ 3 0
    _ _ _ _ _ 2 0
    _ _ _ _ _ 3 1
    _ _ _ _ _ 0 0
    _ _ _ _ _ 0 2
    4 0 0 4 0 $ $
    1 0 3 0 0 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_017():
    puzzle_string = f"""
    017.skyscrapers
    5
    _ _ _ _ _ 0 0
    _ _ _ _ _ 2 3
    _ _ _ _ _ 0 0
    _ _ _ _ _ 0 1
    _ _ _ _ _ 0 0
    0 0 5 2 0 $ $
    0 4 0 0 0 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_018():
    puzzle_string = f"""
    018.skyscrapers
    6
    _ _ _ _ _ _ 3 1
    _ _ _ _ _ _ 2 3
    _ _ _ _ _ _ 3 2
    _ _ _ _ _ _ 2 3
    _ _ _ _ _ _ 1 2
    _ _ _ _ _ _ 3 2
    5 2 2 4 3 1 $ $
    2 2 3 1 3 3 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_019():
    puzzle_string = f"""
    019.skyscrapers
    6
    _ _ _ _ _ _ 2 3
    _ _ _ _ _ _ 1 5
    _ _ _ _ _ _ 3 2
    _ _ _ _ _ _ 5 2
    _ _ _ _ _ _ 4 3
    _ _ _ _ _ _ 2 1
    2 1 3 4 2 3 $ $
    2 5 3 2 3 1 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_020():
    puzzle_string = f"""
    020.skyscrapers
    6
    _ _ _ _ _ _ 2 3
    _ _ _ _ _ _ 3 3
    _ _ _ _ _ _ 1 3
    _ _ _ _ _ _ 3 1
    _ _ _ _ _ _ 2 3
    _ _ _ _ _ _ 4 2
    2 1 5 2 4 2 $ $
    3 4 2 5 1 2 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_021():
    puzzle_string = f"""
    021.skyscrapers
    6
    _ _ _ _ _ _ 3 4
    _ _ _ _ _ _ 1 4
    _ _ _ _ _ _ 3 3
    _ _ _ _ _ _ 4 1
    _ _ _ _ _ _ 2 2
    _ _ _ _ _ _ 4 2
    2 2 1 3 5 4 $ $
    3 2 5 2 1 2 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_022():
    puzzle_string = f"""
    022.skyscrapers
    6
    _ _ _ _ _ _ 2 1
    _ _ _ _ _ _ 4 2
    _ _ _ _ _ _ 2 2
    _ _ _ _ _ _ 3 4
    _ _ _ _ _ _ 1 3
    _ _ _ _ _ _ 2 4
    2 3 4 3 2 1 $ $
    2 1 2 4 3 4 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_023():
    puzzle_string = f"""
    023.skyscrapers
    6
    _ _ _ _ _ _ 3 3
    _ _ _ _ _ _ 0 0
    _ _ _ _ _ _ 2 2
    _ _ _ _ _ _ 2 3
    _ _ _ _ _ _ 4 2
    _ _ _ _ _ _ 4 1
    0 3 1 0 4 4 $ $
    4 0 0 0 2 1 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_024():
    puzzle_string = f"""
    024.skyscrapers
    6
    _ _ _ _ _ _ 4 0
    _ _ _ _ _ _ 0 4
    _ _ _ _ _ _ 4 0
    _ _ _ _ _ _ 0 4
    _ _ _ _ _ _ 0 0
    _ _ _ _ _ _ 0 0
    0 3 4 0 0 4 $ $
    3 3 0 4 0 2 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_025():
    puzzle_string = f"""
    025.skyscrapers
    6
    _ _ _ _ _ _ 0 4
    _ _ _ _ _ _ 0 0
    _ _ _ _ _ _ 0 2
    _ _ _ _ _ _ 5 2
    _ _ _ _ _ _ 2 0
    _ _ _ _ _ _ 2 1
    0 2 2 3 4 0 $ $
    0 0 0 2 0 0 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_026():
    puzzle_string = f"""
    026.skyscrapers
    6
    _ _ _ _ _ _ 1 0
    _ _ _ _ _ _ 0 2
    _ _ _ _ _ _ 4 0
    _ _ _ _ _ _ 2 3
    _ _ _ _ _ _ 0 0
    _ _ _ _ _ _ 4 2
    1 0 0 3 2 3 $ $
    3 2 0 2 1 3 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_027():
    puzzle_string = f"""
    027.skyscrapers
    7
    _ _ _ _ _ _ _ 5 1
    _ _ _ 2 _ _ _ 3 2
    _ 5 2 _ _ _ _ 2 2
    _ _ _ _ _ _ _ 4 4
    _ _ _ _ _ 4 _ 0 2
    _ _ _ _ _ _ _ 2 4
    _ _ _ _ _ _ _ 2 3
    4 3 4 0 0 2 1 $ $
    2 1 2 2 3 3 4 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_028():
    puzzle_string = f"""
    028.skyscrapers
    7
    _ _ _ _ _ _ _ 3 0
    _ _ 3 _ _ _ _ 0 4
    _ _ _ _ _ _ _ 3 0
    _ _ _ _ 1 _ _ 0 0
    4 _ _ _ _ _ _ 0 3
    _ _ _ _ _ _ _ 0 2
    _ _ _ _ _ _ 3 1 3
    0 6 3 0 0 1 0 $ $
    0 0 3 3 0 5 0 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_029():
    puzzle_string = f"""
    029.skyscrapers
    7
    _ 4 _ _ _ _ _ 2 4
    _ _ _ _ _ _ _ 3 0
    _ _ _ _ _ _ _ 0 0
    _ _ _ _ _ _ _ 0 0
    _ _ _ 3 _ _ _ 3 3
    _ _ _ _ _ _ _ 4 0
    _ _ 2 _ _ _ _ 0 3
    0 2 0 0 0 5 0 $ $
    3 4 4 0 2 0 4 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_030():
    puzzle_string = f"""
    030.skyscrapers
    7
    _ 5 _ _ _ _ _ 2 3
    _ _ 2 _ _ _ _ 0 0
    _ _ 3 _ _ _ _ 3 0
    _ _ _ _ _ _ _ 2 4
    _ _ _ _ _ 3 _ 0 2
    _ _ _ _ _ _ _ 0 2
    _ _ _ _ _ _ _ 2 3
    0 2 0 0 3 0 0 $ $
    2 4 3 2 0 0 0 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_001():
    puzzle_string = f"""
    tcbig_001.skyscrapers
    7
    _ _ _ _ _ _ _ 2 ?
    _ _ 6 _ 1 _ 4 ? 2
    2 _ _ _ _ 5 _ 3 2
    _ _ 1 _ _ 4 _ 1 4
    _ _ _ _ _ _ 3 ? 2
    _ _ _ _ _ _ _ 3 3
    _ _ _ _ 5 _ _ 2 3
    2 4 3 3 3 2 1 $ $
    3 1 2 3 2 ? ? $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_002():
    puzzle_string = f"""
    tcbig_002.skyscrapers
    7
    1234567 1234567 1234567 1234567 1234567 1234567 1234567 1 2
    1234567 1234567 1234567 1234567 __3____ 1234567 1234567 2 3
    1234567 1234567 1234567 1234567 1234567 1234567 1234567 3 1
    1234567 __3____ 1234567 1234567 1______ ___4___ 1234567 ? 2
    1234567 _2_____ 1234567 1234567 1234567 1234567 1234567 2 3
    1234567 1234567 ____5__ 1______ 1234567 1234567 1234567 4 3
    1234567 1234567 1234567 1234567 1234567 1234567 1234567 4 2
       1       2       4       2       4       4       ?    ? ?
       5       3       3       2       2       1       ?    ? ?
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_003():
    puzzle_string = f"""
    tcbig_003.skyscrapers
    7
    3 . . 6 . . . ? 2
    . . . . . 4 . 3 4
    . . 6 . 1 . 7 4 1
    . 1 . . . 3 . 2 ?
    . . 7 . . . . 3 3
    . . . . . . . ? 3
    . . . . 4 . . ? 3
    4 3 3 2 3 1 3 $ $
    1 ? 2 ? ? ? 3 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_004():
    puzzle_string = f"""
    tcbig_004.skyscrapers
    7
    . . . . . . . 2 5
    . 5 . . . . . 3 5
    . . . 1 . . . 1 4
    . . . . 2 . . 2 2
    . . . . . . . 3 1
    . . . . . . . 4 2
    . . . . . . . 3 2
    2 1 2 ? 5 3 4 $ $
    5 ? 3 4 1 2 2 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_013():
    puzzle_string = f"""
    tcbig_013.skyscrapers
    7
    _ _ _ _ _ _ _ 3 2
    _ _ _ _ _ _ _ 2 1
    _ _ _ _ _ _ _ 3 3
    _ _ _ _ _ _ _ 3 0
    _ _ _ _ _ _ _ 2 2
    _ _ _ _ _ _ _ 1 3
    _ _ _ _ _ _ _ 0 4
    3 2 4 3 2 1 2 $ $
    2 0 3 2 5 3 0 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_019():
    puzzle_string = f"""
    tcbig_019.skyscrapers
    7
    _ _ _ _ _ _ _ 2 2
    _ _ _ _ _ _ _ 3 0
    _ _ _ _ _ _ _ 4 1
    _ _ _ _ _ _ _ 3 0
    _ _ _ _ _ _ _ 1 0
    _ _ _ _ _ _ _ ? 2
    _ _ _ _ _ _ _ ? 2
    2 3 3 2 1 0 0 $ $
    3 1 0 0 3 2 2 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_030():
    puzzle_string = f"""
    tcbig_030.skyscrapers
    7
    _ _ _ _ _ _ _ 2 3
    _ _ _ _ _ _ _ 2 0
    _ _ _ _ _ _ _ 1 5
    _ _ _ _ _ _ _ 2 2
    _ _ _ _ _ _ _ 3 0
    _ _ _ _ _ _ _ 4 1
    _ _ _ _ _ _ _ 4 3
    0 1 0 4 4 2 4 $ $
    4 4 2 0 3 0 0 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_033():
    puzzle_string = f"""
    tcbig_033.skyscrapers
    7
    _ _ _ _ _ _ _ 3 1
    _ _ _ _ _ _ _ 0 3
    _ _ _ _ _ _ _ 0 2
    _ _ _ _ _ _ _ 0 5
    _ _ _ _ _ _ _ 0 2
    _ _ _ _ _ _ _ 4 3
    _ _ _ _ _ _ _ 3 3
    3 2 5 2 2 3 ? $ $
    2 0 1 0 0 2 3 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_039():
    puzzle_string = f"""
    tcbig_039.skyscrapers
    7
    _ _ _ _ _ _ _ 3 2
    _ _ _ _ _ _ _ 2 2
    _ _ _ _ _ _ _ 3 2
    _ _ _ _ _ _ _ ? 3
    _ _ _ _ _ _ _ 2 4
    _ _ _ _ _ _ _ ? 1
    _ _ _ _ _ _ _ 3 2
    ? 3 1 4 2 2 2 $ $
    3 2 2 ? 3 5 ? $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_046():
    puzzle_string = f"""
    tcbig_046.skyscrapers
    7
    . . . . . . . 4 1
    . . . . . . . 3 3
    4 . . . . 1 . 2 3
    . . . 3 4 . . 2 ?
    . . . . . 6 . 4 3
    . . 1 . . . . ? 2
    . . . . . . . 2 2
    ? 3 ? 2 4 3 ? ? ?
    2 3 3 4 2 1 3 ? ?
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_062():
    puzzle_string = f"""
    tcbig_062.skyscrapers
    8
    _ _ 3 _ _ _ _ _ 1 3
    5 _ _ _ _ _ _ _ 2 5
    _ 4 _ _ _ 2 _ 5 2 3
    _ _ _ _ _ _ 6 _ ? 2
    _ _ _ _ 3 _ _ 2 ? ?
    1 _ _ 4 _ _ _ _ 3 2
    _ _ _ _ 6 _ _ _ 5 1
    _ _ _ _ _ _ _ _ 3 3
    1 2 ? 2 3 3 3 3 $ $
    ? 3 5 3 1 3 ? 2 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_068():
    puzzle_string = f"""
    tcbig_068.skyscrapers
    8
    _ 3 _ _ _ _ _ _ 2 2
    _ _ _ _ _ _ _ 6 3 3
    4 _ _ _ _ _ 1 _ 4 1
    _ _ 5 _ 1 _ _ _ ? 4
    _ 4 _ _ _ _ 3 _ ? 2
    5 _ 4 _ _ 8 _ _ 3 3
    _ _ 3 _ _ _ 2 _ 3 4
    _ _ _ _ _ _ _ _ 1 ?
    ? ? 2 4 3 3 1 ? $ $
    1 ? ? 3 2 2 ? 3 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_087():
    puzzle_string = f"""
    tcbig_087.skyscrapers
    8
    _ _ 3 _ _ _ _ _ 3 2
    4 _ _ _ _ 2 _ _ 4 3
    _ _ _ _ 3 _ _ 4 2 3
    3 _ 4 _ _ _ _ _ 3 ?
    _ 3 _ _ _ _ _ _ 3 2
    _ _ _ 2 _ _ _ _ ? 4
    _ _ _ _ _ 7 _ _ 4 1
    _ _ _ _ 6 _ 2 _ 2 3
    4 3 3 1 2 3 4 2 $ $
    2 ? ? 4 3 3 ? 2 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_093():
    puzzle_string = f"""
    tcbig_093.skyscrapers
    9
    _ _ _ _ _ _ _ 1 _ 5 1
    _ 1 _ _ _ 2 _ _ _ 2 ?
    _ _ _ _ 6 _ _ _ 4 2 ?
    2 _ _ 3 _ _ _ 4 _ 4 4
    _ 8 _ _ 5 _ _ _ 3 3 2
    _ _ _ 1 _ 3 _ _ _ ? ?
    _ _ 6 _ _ 1 _ 5 _ 1 2
    _ _ 4 _ _ _ _ _ _ 2 4
    _ _ _ _ _ 7 _ _ _ 4 4
    4 4 ? 2 5 2 3 4 1 $ $
    ? ? 2 4 1 3 2 ? 3 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_100():
    puzzle_string = f"""
    tcbig_100.skyscrapers
    9
    5 _ _ _ _ _ 2 _ _ 3 4
    _ _ _ _ _ 5 _ 8 _ 1 3
    _ _ _ _ _ 4 _ _ _ ? ?
    7 _ 9 _ _ 1 4 6 _ ? 4
    _ _ 5 _ 2 _ _ _ _ 3 2
    _ 5 _ 6 _ 8 _ _ _ 6 2
    _ _ 7 _ _ _ 6 _ _ 2 ?
    2 _ _ _ 3 _ _ _ _ 4 1
    _ _ 3 _ _ _ _ _ _ 3 2
    2 ? 2 3 1 ? 4 3 5 $ $
    3 3 3 ? 4 4 1 3 2 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tcbig_119():
    puzzle_string = f"""
    tcbig_119.skyscrapers
    9
    _ _ _ _ _ _ _ 6 _ 4 2
    _ 2 _ _ _ _ _ _ 1 ? ?
    _ _ _ _ _ _ _ _ _ ? ?
    _ 7 _ 4 9 _ 3 _ _ 2 2
    1 _ _ _ _ 5 _ 3 _ 3 5
    _ _ _ _ _ _ _ _ _ 3 1
    3 _ _ _ 8 _ _ 5 _ 5 2
    _ _ 6 _ _ 2 _ _ 5 3 4
    _ _ 4 _ _ _ 6 _ _ ? 3
    2 4 3 ? ? 4 ? 2 2 $ $
    3 1 3 ? ? ? ? ? ? $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


def test_skyscrapers_tc_001():
    puzzle_string = f"""
    tc_001.skyscrapers
    4
    _ _ _ _ 2 1
    _ _ _ _ 1 4
    _ _ _ _ 2 3
    _ _ _ _ 2 2
    2 3 4 1 $ $
    2 2 1 2 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


def test_skyscrapers_tc_002():
    puzzle_string = f"""
    tc_002.skyscrapers
    4
    _ _ _ _ 1 4
    _ _ _ _ 2 3
    _ _ _ _ 2 2
    _ _ _ _ 2 1
    1 2 3 4 $ $
    2 2 2 1 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_003():
    puzzle_string = f"""
    tc_003.skyscrapers
    4
    . . . . 2 2
    . . . . 3 2
    . . . . 1 3
    . . . . 2 1
    2 1 2 2 . .
    2 4 3 1 . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_004():
    puzzle_string = f"""
    tc_004.skyscrapers
    4
    . . . . 1 2
    . . . . 2 2
    . . . . 2 3
    . . . . 3 1
    1 3 2 2 . .
    3 2 3 1 . .
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_005():
    puzzle_string = f"""
    tc_005.skyscrapers
    4
    . . . . 1 4
    . . . . 2 3
    . . . . 2 2
    . . . . 2 1
    1 2 3 4 $ $
    2 2 2 1 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_006():
    puzzle_string = f"""
    tc_006.skyscrapers
    4
    . . . . 2 3
    . . . . 3 2
    . . . . 2 1
    . . . . 1 2
    4 1 2 2 . .
    1 4 2 2 . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_007():
    puzzle_string = f"""
    tc_007.skyscrapers
    4
    . . . . 2 2
    . . . . 3 1
    . . . . 2 2
    . . . . 1 3
    2 1 3 2 . .
    1 3 2 3 . .
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_008():
    puzzle_string = f"""
    tc_008.skyscrapers
    4
    . . . . 2 2
    . . . . 1 2
    . . . . 3 1
    . . . . 2 3
    2 4 1 3 . .
    2 1 2 2 . .
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_009():
    puzzle_string = f"""
    tc_009.skyscrapers
    4
    . . . . 3 1
    . . . . 2 2
    . . . . 1 3
    . . . . 2 2
    2 2 4 1 . .
    2 2 1 4 . .
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_010():
    puzzle_string = f"""
    tc_010.skyscrapers
    4
    . . . . 2 2
    . . . . 1 3
    . . . . 2 2
    . . . . 3 1
    2 3 1 3 . .
    3 2 3 1 . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_011():
    puzzle_string = f"""
    tc_011.skyscrapers
    4
    . . . . 1 4
    . . . . 3 ?
    . . . . 3 1
    . . . . 2 ?
    1 2 ? 3 . .
    2 1 3 ? . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_012():
    puzzle_string = f"""
    tc_012.skyscrapers
    4
    . . . . 3 2
    . . . . 3 1
    . . . . ? ?
    . . . . 2 ?
    3 2 1 2 . .
    2 1 3 3 . .
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_013():
    puzzle_string = f"""
    tc_013.skyscrapers
    4
    _ _ _ _ 2 3
    _ _ _ _ 2 2
    _ _ _ _ ? 1
    _ _ _ _ ? ?
    4 ? 2 3 $ $
    1 2 2 2 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_014():
    puzzle_string = f"""
    tc_014.skyscrapers
    4
    . . . . 1 .
    . . . . 2 3
    . . . . . 1
    . . . . 3 2
    1 2 2 . . .
    4 . 1 2 . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_015():
    puzzle_string = f"""
    tc_015.skyscrapers
    4
    . . . . 1 3
    . . . . 2 ?
    . . . . 3 1
    . . . . 2 ?
    1 4 ? ? . .
    4 1 2 2 . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_016():
    puzzle_string = f"""
    tc_016.skyscrapers
    5
    . . . . . 2 3
    . . . . . 3 1
    . . . . . 4 2
    . . . . . 2 2
    . . . . . 1 4
    3 3 1 2 2 . .
    1 2 2 2 4 . .
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_017():
    puzzle_string = f"""
    tc_017.skyscrapers
    5
    . . . . . 2 2
    . . . . . 1 2
    . . . . . 3 1
    . . . . . 3 3
    . . . . . 2 3
    2 3 3 1 3 . .
    2 1 2 3 2 . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_018():
    puzzle_string = f"""
    tc_018.skyscrapers
    5
    . . . . . 1 3
    . . . . . 4 2
    . . . . . 2 3
    . . . . . 3 3
    . . . . . 3 1
    1 2 3 2 3 . .
    3 3 2 3 1 . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_019():
    puzzle_string = f"""
    tc_019.skyscrapers
    5
    _ _ _ _ _ 1 3
    _ _ _ _ _ 3 1
    _ _ _ _ _ 3 3
    _ _ _ _ _ 2 3
    _ _ _ _ _ 4 2
    1 2 3 4 2 $ $
    3 2 2 1 2 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_025():
    puzzle_string = f"""
    tc_025.skyscrapers
    5
    . . . . . ? 3
    . . . . . 2 ?
    . . . . . ? 3
    . . . . . 3 ?
    . . . . . 3 ?
    1 2 2 2 3 . .
    4 3 4 ? 2 . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_026():
    puzzle_string = f"""
    tc_026.skyscrapers
    5
    . . . . . 1 3
    . . . . . ? 1
    . . . . . 3 2
    . . . . . ? ?
    . . . . . 2 3
    ? 3 2 3 2 . .
    4 2 ? 2 3 . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_027():
    puzzle_string = f"""
    tc_027.skyscrapers
    5
    . . . . . 2 3
    . . . . . 2 2
    . . . . . 1 3
    . . . . . 3 2
    . . . . . 4 1
    ? ? 2 ? 4 . .
    2 4 ? ? 1 . .
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_028():
    puzzle_string = f"""
    tc_028.skyscrapers
    5
    . . . . . 2 3
    . . . . . 3 2
    . . . . . 4 1
    . . . . . ? ?
    . . . . . 3 2
    ? 1 3 2 2 . .
    ? ? 1 3 3 . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_029():
    puzzle_string = f"""
    tc_029.skyscrapers
    5
    . . . . . 2 2
    . . . . . 3 2
    . . . . . 2 4
    . . . . . 3 ?
    . . . . . 1 2
    2 ? 2 1 ? . .
    ? ? 4 3 2 . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_030():
    puzzle_string = f"""
    tc_030.skyscrapers
    5
    _ _ _ _ _ 3 ?
    _ _ _ _ _ 2 ?
    _ _ _ _ _ 1 3
    _ _ _ _ _ ? 2
    _ _ _ _ _ ? ?
    3 5 2 4 1 $ $
    2 1 2 ? 2 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_031():
    puzzle_string = f"""
    tc_031.skyscrapers
    5
    . . . . . 5 1
    . . . . . ? 2
    . . . . . ? 2
    . . . . . 1 3
    . . . . . ? 3
    ? 3 3 2 1 . .
    2 2 1 ? 4 . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_032():
    puzzle_string = f"""
    tc_032.skyscrapers
    5
    . . . . . ? 3
    . . . . . 2 3
    . . . . . ? 1
    . . . . . 3 2
    . . . . . ? 3
    3 1 ? 2 2 . .
    ? ? 3 2 ? . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_033():
    puzzle_string = f"""
    tc_033.skyscrapers
    5
    _ _ _ _ _ 0 3
    _ _ _ _ _ 2 2
    _ _ _ _ _ 4 0
    _ _ _ _ _ 2 2
    _ _ _ _ _ 0 5
    3 1 0 2 0 $ $
    0 2 3 0 3 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_034():
    puzzle_string = f"""
    tc_034.skyscrapers
    5
    . . . . . 3 ?
    . . . . . 2 3
    . . . . . ? ?
    . . . . . ? 2
    . . . . . 1 4
    3 3 2 1 2 . .
    ? 2 2 ? ? . .
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_038():
    puzzle_string = f"""
    tc_038.skyscrapers
    5
    _ _ _ _ _ 2 3
    _ _ _ _ _ ? 3
    _ _ _ _ _ 3 2
    _ _ _ _ _ ? ?
    _ _ _ _ _ 2 ?
    2 ? 3 2 2 $ $
    ? 4 1 ? 2 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_039():
    puzzle_string = f"""
    tc_039.skyscrapers
    5
    _ _ _ _ _ 3 2
    _ _ _ _ _ 4 1
    _ _ _ _ _ 2 2
    _ _ _ _ _ 0 0
    _ _ _ _ _ 2 2
    4 2 4 1 2 $ $
    0 0 0 0 0 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_046():
    puzzle_string = f"""
    tc_046.skyscrapers
    5
    . . . . . ? 3
    . . . . . 2 2
    . . . . . 4 ?
    . . . . . ? 2
    . . . . . ? 3
    ? 3 3 ? ? $ $
    4 2 1 2 3 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_051():
    puzzle_string = f"""
    tc_051.skyscrapers
    5
    _ _ _ _ _ ? 4
    _ _ _ _ _ 3 ?
    _ _ _ _ _ ? ?
    _ _ _ _ _ 4 1
    _ _ _ _ _ ? 2
    ? ? ? 3 3 $ $
    4 ? 2 1 2 $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_052():
    puzzle_string = f"""
    tc_052.skyscrapers
    5
    _ _ _ _ _ ? 3
    _ _ _ _ _ 3 ?
    _ _ _ _ _ 3 3
    _ _ _ _ _ ? 2
    _ _ _ _ _ 3 ?
    2 ? 3 ? 2 $ $
    2 4 ? ? ? $ $
    """
    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_056():
    puzzle_string = f"""
    tc_056.skyscrapers
    5
    _ _ _ _ _ 2 3
    _ _ _ _ _ 1 ?
    _ _ _ _ _ ? ?
    _ _ _ _ _ 4 ?
    _ _ _ _ _ 2 2
    ? ? 2 ? 4 $ $
    3 ? 3 ? 2 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_057():
    puzzle_string = f"""
    tc_057.skyscrapers
    5
    . . . . . 4 ?
    . . . . . 2 3
    . . . . . ? ?
    . . . . . 1 2
    . . . . . ? ?
    ? 2 ? ? 4 $ $
    2 4 3 ? ? $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_062():
    puzzle_string = f"""
    tc_062.skyscrapers
    6
    _ _ _ _ _ _ 2 2
    _ _ _ _ _ _ 3 2
    _ _ _ _ _ _ 0 4
    _ _ _ _ _ _ 2 0
    _ _ _ _ _ _ 1 3
    _ _ _ _ _ _ 4 1
    0 3 2 1 4 0 $ $
    2 3 0 5 0 1 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_068():
    puzzle_string = f"""
    tc_068.skyscrapers
    6
    _ _ _ _ _ _ 3 0
    _ _ _ _ _ _ 1 5
    _ _ _ _ _ _ 3 2
    _ _ _ _ _ _ 0 1
    _ _ _ _ _ _ 2 4
    _ _ _ _ _ _ 2 3
    2 0 2 1 2 3 $ $
    3 0 2 3 2 2 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_087():
    puzzle_string = f"""
    tc_087.skyscrapers
    6
    _ _ _ _ _ _ 3 0
    _ _ _ _ _ _ 2 0
    _ _ _ _ _ _ 1 6
    _ _ _ _ _ _ 2 0
    _ _ _ _ _ _ 0 3
    _ _ _ _ _ _ 3 2
    0 4 3 4 0 1 $ $
    0 0 3 0 3 0 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_093():
    puzzle_string = f"""
    tc_093.skyscrapers
    6
    _ _ _ _ _ _ 3 ?
    _ _ _ _ _ _ 1 3
    _ _ _ _ _ _ 4 ?
    _ _ _ _ _ _ 2 ?
    _ _ _ _ _ _ ? 4
    _ _ _ _ _ _ 2 3
    2 3 ? 3 2 ? $ $
    ? 2 4 ? ? 4 $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_100():
    puzzle_string = f"""
    tc_100.skyscrapers
    6
    _ _ _ _ _ _ 4 2
    _ _ _ _ _ _ ? 3
    _ _ _ _ _ _ ? ?
    _ _ _ _ _ _ 3 ?
    _ _ _ _ _ _ 4 1
    _ _ _ _ _ _ 2 3
    ? 4 ? 3 ? 4 $ $
    ? 1 2 2 ? ? $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_119():
    puzzle_string = f"""
    tc_119.skyscrapers
    6
    _ _ _ _ _ _ 3 2
    _ _ _ _ _ _ 1 4
    _ _ _ _ _ _ 2 ?
    _ _ _ _ _ _ 3 ?
    _ _ _ _ _ _ ? 4
    _ _ _ _ _ _ 3 ?
    ? 4 2 1 4 2 $ $
    ? ? 2 ? ? ? $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_130():
    puzzle_string = f"""
    tc_130.skyscrapers
    6
    _ _ _ _ _ _ ? 4
    _ _ _ _ _ _ ? 2
    _ _ _ _ _ _ 4 ?
    _ _ _ _ _ _ ? ?
    _ _ _ _ _ _ ? 3
    _ _ _ _ _ _ ? 2
    3 3 ? ? 4 ? $ $
    ? ? 3 4 3 ? $ $
    """

    assert default_test_puzzle(puzzle_string, Skyscrapers, Solving.skyscrapers_techniques())


@pytest.mark.skip("EXPLICITLY")
def test_skyscrapers_tc_135():
    puzzle_string = f"""
    tc_135.skyscrapers
    6
    _ _ _ _ _ _ ? 3
    _ _ _ _ _ _ 2 2
    _ _ _ _ _ _ ? ?
    _ _ _ _ _ _ ? ?
    _ _ _ _ _ _ ? 3
    _ _ _ _ _ _ ? 4
    ? 5 1 ? 3 ? $ $
    2 ? ? ? 4 ? $ $
    """
