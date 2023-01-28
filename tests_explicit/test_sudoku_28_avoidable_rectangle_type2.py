from techniques.AvoidableRectangleType2 import AvoidableRectangleType2
from tests_explicit.test_small_explicit import solve
from pytest import mark, fail


def test_sudoku_4x4_ar2_normal_east():
    actual = \
        f"""
        ____a __3_a   ____b 12__b
        ____a _2__a   ____b 1_3_b
        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        ____a __3_a   _234b 12__b
        ____a _2__a   _234b 1_3_b
        ____c ____c   ____d _234d
        ____c ____c   ____d _234d
        """
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ar2_goofy_east():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   _2__b 1_3_b
        ____c ____c   __3_d 12__d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b _234b
        ____a ____a   _2__b 1_3_b
        ____c ____c   __3_d 12__d
        ____c ____c   ____d _234d
        """

    if solve(4, actual, expected, AvoidableRectangleType2()):
        return

    assert False


def test_sudoku_4x4_ar2_normal_east_control():
    actual = \
        f"""
        ____a __3_a   ____b 12__b
        ____a ____a   ____b ____b
        ____c _2__c   ____d 1_3_d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ar2_goofy_east_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a _2__a   ____b 1_3_b
        ____c __3_c   ____d 12__d
        ____c ____c   ____d ____d
        """

    expected = None

    if solve(4, actual, expected, AvoidableRectangleType2()):
        return

    assert False


def test_sudoku_4x4_ar2_chute_normal_north():
    actual = \
        f"""
        ____a ____a   ____b ____b
        1_3_a _23_a   ____b ____b
        _2__c 1___c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        12_4a 12_4a   ____b ____b
        1_3_a _23_a   12_4b 12_4b
        _2__c 1___c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ar2_chute_goofy_north():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b
        ____c _23_c   1_3_d ____d
        ____c 1___c   _2__d ____d
        """
    expected = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   ____b ____b
        12_4c _23_c   1_3_d 12_4d
        ____c 1___c   _2__d ____d
        """
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ar2_chute_normal_north_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        1_3_a 1_3_a   ____b ____b
        _2__c 1___c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


def test_sudoku_4x4_ar2_chute_goofy_north_control():
    actual = \
        f"""
       ____a ____a   ____b ____b
        ____a ____a   ____b ____b
        ____c _23_c   1_3_d ____d
        ____c 1___c   ____d _2__d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_ar2_chute_normal_west():
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
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_ar2_chute_goofy_west():
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
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return

    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_ar2_chute_normal_south():
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
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_ar2_chute_goofy_south():
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
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_ar2_chute_normal_west_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a ____a   12__b ____b
        123_c 123_c   ____d ____d
        ____c 123_c   12__d ____d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_ar2_chute_goofy_west_control():
    actual = \
        f"""
        ____a ____a   ____b ____b
        123_a ____a   12__b ____b
        123_c ____c   12__d ____d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return

    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_ar2_chute_normal_south_control():
    actual = \
        f"""
        12__a 12__a   ____b ____b
        ____a ____a   ____b ____b
        ____c 123_c   123_d ____d
        123_c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_ar2_chute_goofy_south_control():
    actual = \
        f"""
        ____a 12__a   12__b ____b
        ____a ____a   ____b ____b
        ____c 123_c   123_d ____d
        ____c ____c   ____d ____d
        """
    expected = None
    if solve(4, actual, expected, AvoidableRectangleType2()):
        return
    assert False

