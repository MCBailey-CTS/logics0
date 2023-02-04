from pytest import mark
from techniques.XyWing import XyWing
from tests_explicit.test_small_explicit import solve



@mark.skip("EXPLICITLY")

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

@mark.skip("EXPLICITLY")

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


# sudoku_explicit_xy_wing_2_fences_col_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 1___5____f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    1_3______i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i __3_5____i 123456789i
#
# sudoku_explicit_xy_wing_2_fences_col_chute_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    _23456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    _23456789f 1___5____f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    _23456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    1_3______i _23456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i _23456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i __3_5____i 123456789i
#
# sudoku_explicit_xy_wing_2_fences_row_chute_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 12_______d    123456789e 123456789e 123456789e    1_3______f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _23______d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_2_fences_row_chute_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 12_456789d 12_456789d 12_______d    123456789e 123456789e 123456789e    1_3______f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# _23______d 123456789d 123456789d    123456789e 123456789e 123456789e    12_456789f 12_456789f 12_456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_north_east_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 1___5____d    123456789e 123456789e 123456789e    123456789f 123456789f ____5___9f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 1_______9i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_north_east_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 1___5____d    123456789e 123456789e 123456789e    123456789f 123456789f ____5___9f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g _23456789g    123456789h 123456789h 123456789h    123456789i 123456789i 1_______9i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_north_west_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b _______89b    ______78_c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e ______7_9e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_north_west_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b _______89b    ______78_c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e ______7_9e    123456_89f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_south_east_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    ______78_b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# __3____8_g 123456789g 123456789g    __3___7__h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_south_east_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 1234567_9a 123456789a 123456789a    ______78_b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# __3____8_g 123456789g 123456789g    __3___7__h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_south_west_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e _2_____8_e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 1______8_h 123456789h    12_______i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_xy_wing_south_west_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e _2_____8_e 123456789e    1_3456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 1______8_h 123456789h    12_______i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i










































