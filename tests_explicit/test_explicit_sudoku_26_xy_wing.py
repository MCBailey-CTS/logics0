# from pytest import mark
from techniques.XyWing import XyWing
from tests_explicit.test_small_explicit import solve


def test_sudoku_4x4_xy_wing_2_fences_in_rows():
    actual = \
        f"""
        ____a 12__a   ____b 1_3_b
        _23_a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        12_4a 12__a   ____b 1_3_b
        _23_a ____a   ____b 12_4b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyWing()):
        return
    assert False


def test_sudoku_4x4_xy_wing_2_fences_in_cols():
    actual = \
        f"""
        ____a ____a   _2_4b ____b
        ____a ____a   ____b 1__4b

        ____c ____c   ____d 12__d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   _2_4b 1_34b
        ____a ____a   ____b 1__4b

        ____c ____c   1_34d 12__d
        ____c ____c   1_34d ____d
        """
    if solve(4, actual, expected, XyWing()):
        return
    assert False


# @mark.skip("EXPLICITLY")
def test_sudoku_4x4_xy_wing_3_fences_ne():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a 1_3_a   12__b ____b

        ____c ____c   _23_d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a 1_3_a   12__b ____b

        ____c 12_4c   _23_d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyWing()):
        return
    assert False


def test_sudoku_4x4_xy_wing_3_fences_nw():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a 1__4a   12__b ____b

        ____c _2_4c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a 1__4a   12__b ____b

        ____c _2_4c   1_34d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyWing()):
        return
    assert False


def test_sudoku_4x4_xy_wing_3_fences_se():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   __34b ____b

        ____c 1__4c   1_3_d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a 123_a   __34b ____b

        ____c 1__4c   1_3_d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyWing()):
        return
    assert False


def test_sudoku_4x4_xy_wing_3_fences_sw():
    actual = \
        f"""
        ____a ____a   ____b ____b
        __34a ____a   ____b ____b

        _2_4c ____c   _23_d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        __34a ____a   12_4b ____b

        _2_4c ____c   _23_d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, XyWing()):
        return
    assert False