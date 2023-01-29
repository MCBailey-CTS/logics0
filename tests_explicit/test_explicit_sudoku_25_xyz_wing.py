from tech import tech
from techniques.XyzWing import XyzWing
from tests_explicit.test_small_explicit import solve


def test_sudoku_4x4_xyz_wing_north():
    actual = \
        f"""
        ____a 1_3_a   ____b ____b
        ____a ____a   ____b ____b

        ____c 123_c   ____d ____d
        _23_c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a 1_3_a   ____b ____b
        ____a ____a   ____b ____b

        ____c 123_c   ____d ____d
        _23_c 12_4c   ____d ____d
        """
    if solve(4, actual, expected, XyzWing()):
        return
    assert False

def test_sudoku_4x4_xyz_wing_south():
    actual = \
        f"""
        ____a ____a   ____b 1__4b
        ____a ____a   12_4b ____b

        ____c ____c   _2_4d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   123_b 1__4b
        ____a ____a   12_4b ____b

        ____c ____c   _2_4d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyzWing()):
        return
    assert False


def test_sudoku_4x4_xyz_wing_east():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c 123_c   1_3_d ____d
        _23_c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b

        12_4c 123_c   1_3_d ____d
        _23_c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyzWing()):
        return
    assert False


def test_sudoku_4x4_xyz_wing_west():
    actual = \
        f"""
        1_3_a ____a   123_b ____b
        ____a ____a   ____b _23_b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        1_3_a ____a   123_b 12_4b
        ____a ____a   ____b _23_b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyzWing()):
        return
    assert False