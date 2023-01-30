
from tests_explicit.test_small_explicit import solve
from techniques.HiddenSingle import HiddenSingle



def test_sudoku_4x4_hidden_single_rows():
    actual = \
        f"""
        123_a 123_a   123_b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        123_a 123_a   123_b ___4b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, HiddenSingle()):
        return
    assert False


def test_sudoku_4x4_hidden_single_cols():
    actual = \
        f"""
        123_a ____a   ____b ____b
        123_a ____a   ____b ____b

        123_c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        123_a ____a   ____b ____b
        123_a ____a   ____b ____b

        123_c ____c   ____d ____d
        ___4c ____c   ____d ____d
        """
    if solve(4, actual, expected, HiddenSingle()):
        return
    assert False



def test_sudoku_4x4_hidden_single_fences():
    actual = \
        f"""
        123_a 123_a   ____b ____b
        123_a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        123_a 123_a   ____b ____b
        123_a ___4a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, HiddenSingle()):
        return
    assert False
