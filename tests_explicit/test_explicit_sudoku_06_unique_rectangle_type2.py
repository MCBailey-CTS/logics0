
from techniques.UniqueRectangleType2 import UniqueRectangleType2
from tests_explicit.test_small_explicit import solve


def test_sudoku_4x4_ur2_normal_east():
    actual = \
        f"""
        ____a _23_a   123_b 123_b
        ____a _23_a   ____b 123_b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        ____a _23_a   _23_b 123_b
        ____a _23_a   _234b 123_b
        ____c ____c   ____d _234d
        ____c ____c   ____d _234d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_goofy_east():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   12__b 123_b
        ____c ____c   12__d 123_d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b 12_4b
        ____a ____a   12__b 123_b
        ____c ____c   12__d 123_d
        ____c ____c   ____d 12_4d
        """

    if solve(4, actual, expected, UniqueRectangleType2()):
        return

    assert False


def test_sudoku_4x4_ur2_chute_normal_north():
    actual = \
        f"""
        ____a 123_a   ____b ____b
        123_a 123_a   ____b ____b
        12__c 12__c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        12_4a 12__a   ____b ____b
        123_a 123_a   12_4b 12_4b
        12__c 12__c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_goofy_north():
    actual = \
        f"""
        ____a 123_a   123_b ____b
        ____a _23_a   _23_b ____b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        _234a 123_a   123_b _234b
        ____a _23_a   _23_b ____b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_normal_west():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b
        123_c 123_c   12__d ____d
        ____c 123_c   12__d ____d
        """
    expected = \
        f"""
        ____a 12_4a   ____b ____b
        ____a 12_4a   ____b ____b
        12__c 123_c   12__d ____d
        12_4c 123_c   12__d ____d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_goofy_west():
    actual = \
        f"""
        ____a ____a   ____b ____b
        123_a 12__a   ____b ____b
        123_c 12__c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        12_4a ____a   ____b ____b
        123_a 12__a   ____b ____b
        123_c 12__c   ____d ____d
        12_4c ____c   ____d ____d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return

    assert False


def test_sudoku_4x4_ur2_chute_normal_south():
    actual = \
        f"""
        12__a 12__a   ____b ____b
        ____a ____a   ____b ____b
        123_c 123_c   ____d ____d
        123_c ____c   ____d ____d
        """
    expected = \
        f"""
        12__a 12__a   ____b ____b
        ____a ____a   ____b ____b
        123_c 123_c   12_4d 12_4d
        12__c 12_4c   ____d ____d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_goofy_south():
    actual = \
        f"""
        ____a 12__a   12__b ____b
        ____a 123_a   123_b ____b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        ____a 12__a   12__b ____b
        12_4a 123_a   123_b 12_4b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_normal_east_control():
    actual = \
        f"""
        ____a _23_a   123_b 123_b
        ____a ____a   ____b ____b
        ____c _23_c   ____d 123_d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_goofy_east_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a 12__a   ____b 123_b
        ____c 12__c   ____d 123_d
        ____c ____c   ____d ____d
        """

    expected = None

    if solve(4, actual, expected, UniqueRectangleType2()):
        return

    assert False


def test_sudoku_4x4_ur2_chute_normal_north_control():
    actual = \
        f"""
        ____a ____a   123_b ____b
        123_a ____a   123_b ____b
        12__c ____c   12__d ____d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_goofy_north_control():
    actual = \
        f"""
        ____a 123_a   123_b ____b
        ____a ____a   ____b ____b
        ____c _23_c   ____d ____d
        ____c ____c   _23_d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_normal_west_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   12__b ____b
        123_c 123_c   ____d ____d
        ____c 123_c   12__d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_goofy_west_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        123_a ____a   12__b ____b
        123_c ____c   12__d ____d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return

    assert False


def test_sudoku_4x4_ur2_chute_normal_south_control():
    actual = \
        f"""
        12__a 12__a   ____b ____b
        ____a ____a   ____b ____b
        ____c 123_c   123_d ____d
        123_c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ur2_chute_goofy_south_control():
    actual = \
        f"""
        ____a 12__a   12__b ____b
        ____a ____a   ____b ____b
        ____c 123_c   123_d ____d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, UniqueRectangleType2()):
        return
    assert False

# sudoku_explicit_unique_rectangle_type2_goofy_east_actual
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a _2__5____a _2__5__8_a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d _2__5____d _2__5__8_d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_unique_rectangle_type2_goofy_east_expected
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 1234567_9a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a _2__5____a _2__5__8_a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 1234567_9a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d _2__5____d _2__5__8_d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 1234567_9d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 1234567_9d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 1234567_9g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 1234567_9g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 1234567_9g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_unique_rectangle_type2_goofy_north_actual
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a __345____a    __345____b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a __3_5____a    __3_5____b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_unique_rectangle_type2_goofy_north_expected
# 9 $ $ $ $ $ $ $ $
# 123_56789a 123_56789a __345____a    __345____b 123_56789b 123_56789b    123_56789c 123_56789c 123_56789c
# 123456789a 123456789a __3_5____a    __3_5____b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_unique_rectangle_type2_goofy_south_actual
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g ______7_9g    ______7_9h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g ______789g    ______789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_unique_rectangle_type2_goofy_south_expected
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g ______7_9g    ______7_9h 123456789h 123456789h    123456789i 123456789i 123456789i
# 1234567_9g 1234567_9g ______789g    ______789h 1234567_9h 1234567_9h    1234567_9i 1234567_9i 1234567_9i
#
# sudoku_explicit_unique_rectangle_type2_goofy_west_actual
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123______d 12_______d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123______g 12_______g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_unique_rectangle_type2_goofy_west_expected
# 9 $ $ $ $ $ $ $ $
# 123456789a 12_456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 12_456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 12_456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 12_456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123______d 12_______d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 12_456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123______g 12_______g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 12_456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 12_456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_unique_rectangle_type2_normal_east_actual
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 12_______d    123456789e 123456789e 123456789e    123456789f 123456789f 123______f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 12_______d    123456789e 123456789e 123456789e    123456789f 123456789f 123______f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_unique_rectangle_type2_normal_east_expected
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 12_456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 12_456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 12_456789c
#
# 123456789d 123456789d 12_______d    123456789e 123456789e 123456789e    12_456789f 12_456789f 123______f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    12_456789f 12_456789f 12_456789f
# 123456789d 123456789d 12_______d    123456789e 123456789e 123456789e    12_456789f 12_456789f 123______f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 12_456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 12_456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 12_456789i
#
# sudoku_explicit_unique_rectangle_type2_normal_north_actual
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a   123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a   123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a   123456789b 123456789b 123456789b    1_3____8_c 1_3____8_c 123456789c
# 123456789d 123456789d 123456789d   123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d   123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d   123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789g 123456789g 123456789g   123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g   123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g   123456789h 123456789h 123456789h    __3____8_i __3____8_i 123456789i
# sudoku_explicit_unique_rectangle_type2_normal_north_expected
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a   123456789b 123456789b 123456789b    _23456789c _23456789c _23456789c
# 123456789a 123456789a 123456789a   123456789b 123456789b 123456789b    _23456789c _23456789c _23456789c
# _23456789a _23456789a _23456789a   _23456789b _23456789b _23456789b    1_3____8_c 1_3____8_c _23456789c
# 123456789d 123456789d 123456789d   123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d   123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d   123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789g 123456789g 123456789g   123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g   123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g   123456789h 123456789h 123456789h    __3____8_i __3____8_i 123456789i
# sudoku_explicit_unique_rectangle_type2_normal_south_actual
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    12_______e 123456789e 12_______e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    12_4_____h 123456789h 12_4_____h    123456789i 123456789i 123456789i
#
# sudoku_explicit_unique_rectangle_type2_normal_south_expected
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    12_______e 123456789e 12_______e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123_56789h 123_56789h 123_56789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123_56789h 123_56789h 123_56789h    123456789i 123456789i 123456789i
# 123_56789g 123_56789g 123_56789g    12_4_____h 123_56789h 12_4_____h    123_56789i 123_56789i 123_56789i
#
# sudoku_explicit_unique_rectangle_type2_normal_west_actual
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123______d    123456789e 123456789e 123456789e    123456789f 123456789f 12_______f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123______d    123456789e 123456789e 123456789e    123456789f 123456789f 12_______f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_unique_rectangle_type2_normal_west_expected
# 9 $ $ $ $ $ $ $ $
# 123456789a 123456789a 12_456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 12_456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 12_456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 12_456789d 12_456789d 123______d    123456789e 123456789e 123456789e    123456789f 123456789f 12_______f
# 12_456789d 12_456789d 12_456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 12_456789d 12_456789d 123______d    123456789e 123456789e 123456789e    123456789f 123456789f 12_______f
#
# 123456789g 123456789g 12_456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 12_456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 12_456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i




