import pytest
from colorama import Fore
from pytest import mark, fail
from Loc import Loc
from puzzles import Sudoku
from tech import tech
from techniques.AvoidableRectangleType1 import AvoidableRectangleType1
from techniques.AvoidableRectangleType2 import AvoidableRectangleType2
from techniques.CrossHatch import CrossHatch
from techniques.HiddenUniqueRectangle import HiddenUniqueRectangle
from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
from techniques.UniqueRectangleType1 import UniqueRectangleType1
import numpy
from techniques.UniqueRectangleType2 import UniqueRectangleType2
from techniques.UniqueRectangleType4 import UniqueRectangleType4
from techniques.WxyzWing import WxyzWing
from techniques.XyWing import XyWing


def test_sudoku_9x9_locked_candidates_claiming_col():
    if solve(9,
             f"""
            _________a _________a _________a    _________b _________b _________b    _________c _________c _________c 
            _________a _________a _________a    _________b _________b _________b    _________c _________c _________c 
            _________a _________a _________a    _________b 12_456789b _________b    _________c _________c _________c 

            _________d _________d _________d    _________e 12_456789e _________e    _________f _________f _________f 
            _________d _________d _________d    _________e 12_456789e _________e    _________f _________f _________f 
            _________d _________d _________d    _________e 12_456789e _________e    _________f _________f _________f 

            _________g _________g _________g    _________h 12_456789h _________h    _________i _________i _________i 
            _________g _________g _________g    _________h 12_456789h _________h    _________i _________i _________i 
            _________g _________g _________g    _________h 12_456789h _________h    _________i _________i _________i 
            """
            , f"""
        _________a _________a _________a    12_456789b _________b 12_456789b    _________c _________c _________c 
        _________a _________a _________a    12_456789b _________b 12_456789b    _________c _________c _________c 
        _________a _________a _________a    12_456789b 12_456789b 12_456789b    _________c _________c _________c 

        _________d _________d _________d    _________e 12_456789e _________e    _________f _________f _________f 
        _________d _________d _________d    _________e 12_456789e _________e    _________f _________f _________f 
        _________d _________d _________d    _________e 12_456789e _________e    _________f _________f _________f 

        _________g _________g _________g    _________h 12_456789h _________h    _________i _________i _________i 
        _________g _________g _________g    _________h 12_456789h _________h    _________i _________i _________i 
        _________g _________g _________g    _________h 12_456789h _________h    _________i _________i _________i 
        """, LockedCandidatesClaiming()):
        return
    assert False


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


def test_sudoku_4x4_hur_row_ne():
    if solve(4,
             f"""
            _234c 1234c   1234d _234d
            ____c 12__c   1234d ____d

            ____a ____a   _234b ____b
            ____a ____a   _234b ____b
            """,
             f"""
            _234c 1234c   1_34d _234d
            ____c 12__c   1234d ____d

            ____a ____a   _234b ____b
            ____a ____a   _234b ____b
            """, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_ne_control():
    if solve(4,
             f"""
            _234c 1234c   1234d _234d
            ____c ____c   1234d ____d

            ____a ____a   _234b ____b
            12__a ____a   _234b ____b
            """,
             None, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_nw():
    if solve(4,
             f"""
            1234d _234d  _234c 1234c
            1234d ____d  ____c 12__c   

            _234b ____b  ____a ____a   
            _234b ____b  ____a ____a
            """,
             f"""
            1_34d _234d  _234c 1234c
            1234d ____d  ____c 12__c   

            _234b ____b  ____a ____a   
            _234b ____b  ____a ____a  
            """, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_nw_control():
    if solve(4,
             f"""
            1234d _234d  _234c 1234c
            _234d ____d  ____c 12__c   

            1234b ____b  ____a 12__a   
            _234b ____b  ____a ____a
            """, None, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_se():
    if solve(4,
             f"""
            ____a ____a   _234b ____b
            ____a ____a   _234b ____b

            ____c 12__c   1234d ____d
            _234c 1234c   1234d _234d
            """,
             f"""
            ____a ____a   _234b ____b
            ____a ____a   _234b ____b

            ____c 12__c   1234d ____d
            _234c 1234c   1_34d _234d
            """, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_se_control():
    if solve(4,
             f"""
            ____a ____a   1234b ____b
            ____a ____a   _234b ____b

            ____c 12__c   1234d ____d
            _234c 1234c   1234d _234d
            """, None, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_sw():
    if solve(4,
             f"""
            _234b ____b  ____a ____a   
            _234b ____b  ____a ____a   

            1234d ____d  ____c 12__c   
            1234d _234d  _234c 1234c   
            """,
             f"""
            _234b ____b  ____a ____a   
            _234b ____b  ____a ____a   

            1234d ____d  ____c 12__c   
            1_34d _234d  _234c 1234c
            """, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_4x4_hur_row_sw_control():
    if solve(4,
             f"""
            _234b ____b  ____a ____a   
            _234b ____b  ____a ____a   

            1234d 12__d  ____c ____c   
            1234d _234d  _234c 1234c
            """, None, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_ne():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_ne_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, None, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_nw():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_nw_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, None, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_se():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_se_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, None, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_sw():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, HiddenUniqueRectangle()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_hur_col_sw_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, None, HiddenUniqueRectangle()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_north_control():
    if solve(6,
             f"""
            ______a _23456a ______a   _23456b _23456b _23456b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ______c   ______d ______d ______d
            ______c ______c ______c   ______d ______d ______d

            ______e ______e 12____e   ______f ______f ______f
            12____e ______e ______e   ______f ______f ______f
            """, None, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_south_control():
    if solve(6,
             f"""
            ______a ______a ______a   ______b ______b ______b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ____56c   ______d ______d ____56d
            ______c ______c ______c   ______d ______d ______d

            12345_e 12345_e 12345_e   ______f 12345_f ______f
            ______e ______e ______e   ______f ______f ______f
            """, None, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_west_control():
    actual = \
        f"""
        ______a 123_56a   ______b ______b   ______c ______c
        ______a ______a   __34__b ______b   ______c ______c
        ______a ______a   ______b ______b   ______c ______c

        ______d 123_56d   __34__e ______e   ______f ______f
        ______d 123_56d   ______e ______e   ______f ______f
        ______d 123_56d   ______e ______e   ______f ______f
        """

    expected = None
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_eat_control():
    actual = \
        f"""
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c

        ______d ______d   ______e 1____6e   ______f 123456f
        ______d ______d   ______e ______e   ______f 123456f
        ______d ______d   ______e 1____6e   ______f 123456f
        """

    expected = None
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_north_control():
    if solve(6,
             f"""
            123456a _23456a 123456a   123456b _23456b _23456b
            ______a ______a 12____a   12____b ______b ______b

            ______c ______c ______c   ______d ______d ______d
            ______c ______c ______c   ______d ______d ______d

            ______e ______e ______e   ______f ______f ______f
            ______e ______e ______e   ______f ______f ______f
            """, None, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_south_control():
    if solve(6,
             f"""
            ______a ______a ______a   ______b ______b ______b
            ______a ______a ______a   ______b ____56b ______b

            ______c ______c ____56c   ______d ______d ______d
            12345_c 12345_c 123456c   123456d 12345_d 12345_d

            ______e ______e ______e   ______f ______f ______f
            ______e ______e ______e   ______f ______f ______f
            """, None, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_west_control():
    actual = \
        f"""
        ______a ______a   123_56b ______b   ______c ______c
        ______a ______a   123_56b ______b   ______c ______c
        ______a ______a   123456b __34__b   ______c ______c

        ______d ______d   123456e ______e   __34__f ______f
        ______d ______d   123_56e ______e   ______f ______f
        ______d _____6d   123_56e ______e   ______f ______f
        """

    expected = None
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_east_control():
    actual = \
        f"""
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b 1____6b   ______c 123456c

        ______d ______d   ______e 1____6e   ______f 123456f
        ______d ______d   ______e ______e   ______f _23456f
        ______d ______d   ______e ______e   ______f _23456f
        """

    expected = None
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_north():
    if solve(6,
             f"""
            ______a _23456a ______a   _23456b _23456b _23456b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ______c   ______d ______d ______d
            ______c ______c ______c   ______d ______d ______d

            ______e ______e ______e   ______f ______f ______f
            12____e ______e 12____e   ______f ______f ______f
            """,
             f"""
            1_3456a _23456a 1_3456a   _23456b _23456b _23456b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ______c   ______d ______d ______d
            ______c ______c ______c   ______d ______d ______d

            ______e ______e ______e   ______f ______f ______f
            12____e ______e 12____e   ______f ______f ______f
            """, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_south():
    if solve(6,
             f"""
            ______a ______a ______a   ______b ______b ______b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ______c   ____56d ______d ____56d
            ______c ______c ______c   ______d ______d ______d

            12345_e 12345_e 12345_e   ______f 12345_f ______f
            ______e ______e ______e   ______f ______f ______f
            """,
             f"""
            ______a ______a ______a   ______b ______b ______b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ______c   ____56d ______d ____56d
            ______c ______c ______c   ______d ______d ______d

            12345_e 12345_e 12345_e   1234_6f 12345_f 1234_6f
            ______e ______e ______e   ______f ______f ______f
            """, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_west():
    actual = \
        f"""
        ______a 123_56a   ______b ______b   ______c ______c
        ______a ______a   __34__b ______b   ______c ______c
        ______a ______a   __34__b ______b   ______c ______c

        ______d 123_56d   ______e ______e   ______f ______f
        ______d 123_56d   ______e ______e   ______f ______f
        ______d 123_56d   ______e ______e   ______f ______f
        """

    expected = \
        f"""
        ______a 123_56a   ______b ______b   ______c ______c
        ______a 12_456a   __34__b ______b   ______c ______c
        ______a 12_456a   __34__b ______b   ______c ______c

        ______d 123_56d   ______e ______e   ______f ______f
        ______d 123_56d   ______e ______e   ______f ______f
        ______d 123_56d   ______e ______e   ______f ______f
        """
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_normal_eat():
    actual = \
        f"""
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c

        ______d ______d   ______e 1____6e   ______f 123456f
        ______d ______d   ______e ______e   ______f _23456f
        ______d ______d   ______e 1____6e   ______f 123456f
        """

    expected = \
        f"""
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c

        ______d ______d   ______e 1____6e   ______f 12345_f
        ______d ______d   ______e ______e   ______f _23456f
        ______d ______d   ______e 1____6e   ______f 12345_f
        """
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_north():
    if solve(6,
             f"""
            _23456a _23456a 123456a   123456b _23456b _23456b
            ______a ______a 12____a   12____b ______b ______b

            ______c ______c ______c   ______d ______d ______d
            ______c ______c ______c   ______d ______d ______d

            ______e ______e ______e   ______f ______f ______f
            ______e ______e ______e   ______f ______f ______f
            """,
             f"""
            _23456a _23456a 1_3456a   1_3456b _23456b _23456b
            ______a ______a 12____a   12____b ______b ______b

            ______c ______c ______c   ______d ______d ______d
            ______c ______c ______c   ______d ______d ______d

            ______e ______e ______e   ______f ______f ______f
            ______e ______e ______e   ______f ______f ______f
            """, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_south():
    if solve(6,
             f"""
            ______a ______a ______a   ______b ______b ______b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ____56c   ____56d ______d ______d
            12345_c 12345_c 123456c   123456d 12345_d 12345_d

            ______e ______e ______e   ______f ______f ______f
            ______e ______e ______e   ______f ______f ______f
            """,
             f"""
            ______a ______a ______a   ______b ______b ______b
            ______a ______a ______a   ______b ______b ______b

            ______c ______c ____56c   ____56d ______d ______d
            12345_c 12345_c 1234_6c   1234_6d 12345_d 12345_d

            ______e ______e ______e   ______f ______f ______f
            ______e ______e ______e   ______f ______f ______f
            """, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_6x6_ur4_goofy_west():
    actual = \
        f"""
        ______a ______a   123_56b ______b   ______c ______c
        ______a ______a   123_56b ______b   ______c ______c
        ______a ______a   123456b __34__b   ______c ______c

        ______d ______d   123456e __34__e   ______f ______f
        ______d ______d   123_56e ______e   ______f ______f
        ______d _____6d   123_56e ______e   ______f ______f
        """

    expected = \
        f"""
        ______a ______a   123_56b ______b   ______c ______c
        ______a ______a   123_56b ______b   ______c ______c
        ______a ______a   12_456b __34__b   ______c ______c

        ______d ______d   12_456e __34__e   ______f ______f
        ______d ______d   123_56e ______e   ______f ______f
        ______d _____6d   123_56e ______e   ______f ______f
        """
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


#
def test_sudoku_6x6_ur4_goofy_east():
    actual = \
        f"""
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   1____6c 123456c

        ______d ______d   ______e ______e   1____6f 123456f
        ______d ______d   ______e ______e   ______f _23456f
        ______d ______d   ______e ______e   ______f _23456f
        """

    expected = \
        f"""
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   ______c _23456c
        ______a ______a   ______b ______b   1____6c 12345_c

        ______d ______d   ______e ______e   1____6f 12345_f
        ______d ______d   ______e ______e   ______f _23456f
        ______d ______d   ______e ______e   ______f _23456f
        """
    if solve(6, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_4x4_ur1_row_ne():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c __34c   ____d 1234d
            ____c __34c   ____d __34d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c __34c   ____d 12__d
            ____c __34c   ____d __34d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_ne_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c __34c   ____d 1234d
            __34c ____c   ____d __34d
            """,
             None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_nw():
    if solve(4,
             f"""
            ____a 1234a   _23_b ____b
            ____a _23_a   _23_b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a 1__4a   _23_b ____b
            ____a _23_a   _23_b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_nw_control():
    if solve(4,
             f"""
            ____a 1234a   _23_b ____b
            ____a _23_a   ____b ____b

            ____c ____c   _23_d ____d
            ____c ____c   ____d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_se():
    if solve(4,
             f"""
            ____a 12__a   ____b 12__b
            ____a 12__a   ____b 1234b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a 12__a   ____b 12__b
            ____a 12__a   ____b __34b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_se_control():
    if solve(4,
             f"""
            ____a 12__a   ____b 12__b
            ____a ____a   ____b 1234b

            ____c 12__c   12__d ____d
            ____c ____c   ____d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_sw():
    if solve(4,
             f"""
            ____a __34a   __34b ____b
            ____a 1234a   __34b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a __34a   __34b ____b
            ____a 12__a   __34b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_row_sw_control():
    if solve(4,
             f"""
            ____a __34a   __34b ____b
            ____a 1234a   ____b __34b

            ____c ____c   ____d ____d
            ____c ____c   __34d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_ne():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   1__4b 1234b

            ____c ____c   1__4d 1__4d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   1__4b _23_b

            ____c ____c   1__4d 1__4d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_ne_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a 1__4a   1__4b 1234b

            ____c 1__4c   ____d 1__4d
            ____c ____c   ____d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_nw():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            1234a __34a   ____b ____b

            __34c __34c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            12__a __34a   ____b ____b

            __34c __34c   ____d ____d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_nw_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            1234a ____a   __34b ____b

            __34c __34c   __34d ____d
            ____c ____c   ____d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_se():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   12__b 12__b

            ____c ____c   12__d 1234d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   12__b 12__b

            ____c ____c   12__d __34d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_se_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a 12__a   12__b 12__b

            ____c 12__c   ____d 1234d
            ____c ____c   ____d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_sw():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   12__b 12__b

            ____c ____c   1234d 12__d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   12__b 12__b

            ____c ____c   __34d 12__d
            ____c ____c   ____d ____d
            """, UniqueRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ur1_col_sw_control():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a 12__a   12__b ____b

            ____c 12__c   1234d ____d
            ____c ____c   ____d ____d
            """, None, UniqueRectangleType1()):
        return
    assert False


def test_cross_hatch():
    actual = \
        f"""
        1___a ____a   ____b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    expected = \
        f"""
        1___a _234a   _234b _234b
        _234a _234a   ____b ____b

        _234c ____c   ____d ____d
        _234c ____c   ____d ____d
            """
    if solve(4, actual, expected, CrossHatch()):
        return
    assert False


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


def to_sudoku(length: int, actual: str, _id: str) -> Sudoku:
    newcan = "".join(str(num + 1) for num in range(length))

    underscore = "".join('_' for _ in range(length))
    string = actual
    string = string.replace('\n', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ', -1) \
        .replace('  ', ' ', -1).replace('  ', ' ', -1).replace('  ', ' ', -1).replace(underscore, newcan).strip()

    temp = numpy.array(string.split(' '), str) \
        # .reshape((length, length))

    # if reshape is None:
    temp = temp.reshape((length, length))

    # else:
    #     temp = temp.reshape(reshape)

    return Sudoku(temp, length, _id)


def solve(length, actual, expected, technique):
    actual0 = to_sudoku(length, actual, '_actual')

    edits = technique.solve0(actual0)

    if expected is None:
        return edits == 0

    expected0 = to_sudoku(length, expected, '_expected')

    if actual0 == expected0:
        return True

    # for r in range(len(actual)):
    #     for c in range(len(actual)):
    #         if actual0.grid[r][c] != expected0.grid[r][c]:
    #             expected0.override_loc_color([Loc(r, c)], Fore.CYAN)

    print(actual0.to_string())
    print(expected0.to_string())
    return False


# def grid_fence(length, string: str) -> tuple[numpy.ndarray, numpy.ndarray]:

# actual0 = \
#     f"""
#         ____a ____a   ____b ____b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#
# from colorama import Fore
#
#
# def test_sudoku_4x4_():
#     actual = \
#         f"""
#         ____a ____a   ____b ____b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         ____a ____a   ____b ____b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_sudoku_6x6_3x2():
#     actual = \
#         f"""
#         ______a ______a ______a   ______b ______b ______b
#         ______a ______a ______a   ______b ______b ______b
#
#         ______c ______c ______c   ______d ______d ______d
#         ______c ______c ______c   ______d ______d ______d
#
#         ______e ______e ______e   ______f ______f ______f
#         ______e ______e ______e   ______f ______f ______f
#         """
#
#     expected = \
#         f"""
#         ______a ______a ______a   ______b ______b ______b
#         ______a ______a ______a   ______b ______b ______b
#
#         ______c ______c ______c   ______d ______d ______d
#         ______c ______c ______c   ______d ______d ______d
#
#         ______e ______e ______e   ______f ______f ______f
#         ______e ______e ______e   ______f ______f ______f
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_sudoku_6x6_2x3():
#     actual = \
#         f"""
#         ______a ______a   ______b ______b   ______c ______c
#         ______a ______a   ______b ______b   ______c ______c
#         ______a ______a   ______b ______b   ______c ______c
#
#         ______d ______d   ______e ______e   ______f ______f
#         ______d ______d   ______e ______e   ______f ______f
#         ______d ______d   ______e ______e   ______f ______f
#         """
#
#     expected = \
#         f"""
#         ______a ______a   ______b ______b   ______c ______c
#         ______a ______a   ______b ______b   ______c ______c
#         ______a ______a   ______b ______b   ______c ______c
#
#         ______d ______d   ______e ______e   ______f ______f
#         ______d ______d   ______e ______e   ______f ______f
#         ______d ______d   ______e ______e   ______f ______f
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_sudoku_6x6_w_wing():
#     actual = \
#         f"""
#         ____a ____a   ____b ____b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         ____a ____a   ____b ____b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
@mark.skip("EXPLICITLY")
def test_almost_locked_candidates_claiming_row():
    actual = \
        f"""
        __34a 12__a   ____b ____b
        ____a ____a   12__b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        __34a 12__a   ____b ____b
        ____a ____a   12__b __34b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, tech.AlmostLockedCandidatesClaiming()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_almost_locked_candidates_pointing_row():
    actual = \
        f"""
        ____a 12__a   ____b ____b
        ____a ____a   12__b __34b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        __34a 12__a   ____b ____b
        ____a ____a   12__b __34b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, tech.AlmostLockedCandidatesPointing()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_ur3_north_row():
    actual = \
        f"""
        123_a 12_4a   __34b ____b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        12__c 12__c   ____d ____d
        """

    expected = \
        f"""
        123_a 12_4a   __34b 12__b
        ____a ____a   ____b ____b

        ____c ____c   ____d ____d
        12__c 12__c   ____d ____d
        """
    if solve(actual, expected, None):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_xy_chain_west():
    actual = \
        f"""
        ____a ____a   ____b ____b
        ____a 12__a   ____b _23_b

        ____c ____c   ____d ____d
        1__4c ____c   ____d __34d
        """

    expected = \
        f"""
        _234a ____a   ____b ____b
        _234a 12__a   ____b _23_b

        ____c _234c   ____d ____d
        1__4c _234c   ____d __34d
        """
    if solve(4, actual, expected, tech.XyChain()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_xyz_wing_fences2_row_chute():
    actual = \
        f"""
        ____a 123_a   1_3_b ____b
        _23_a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        12_4a 123_a   1_3_b ____b
        _23_a ____a   ____b ____b

        ____c ____c   ____d ____d
        ____c ____c   ____d ____d
        """
    if solve(4, actual, expected, None):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_wxyz_fences2_south():
    actual = \
        f"""
        _234a 1__4a   ____b ____b
        ____a 1_3_a   ____b ____b

        ____c ____c   ____d ____d
        2_4_c ____c   ____d ____d
        """

    expected = \
        f"""
        _234a 1__4a   ____b ____b
        123_a 1_3_a   ____b ____b

        ____c ____c   ____d ____d
        2_4_c ____c   ____d ____d
        """
    if solve(4, actual, expected, None):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_sudoku_4x4_wxyz_fences2_north():
    actual = \
        f"""
        ____a ____a   ____b ____b
        _23_a ____a   ____b ____b

        12__c 1__4c   ____d ____d
        ____c __34c   ____d ____d
        """

    expected = \
        f"""
        ____a ____a   ____b ____b
        _23_a ____a   ____b ____b

        12__c 1__4c   ____d ____d
        12_4c __34c   ____d ____d
        """
    if solve(4, actual, expected, WxyzWing()):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_shashimi_x_wing_east_fins1():
    actual = \
        f"""
        _234a ____a   234_b ____b
        ____a ____a   ____b ____b

        _234c ____c   ____d _234d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        _234a ____a   234_b ____b
        ____a ____a   _234b ____b

        _234c ____c   ____d _234d
        ____c ____c   ____d _234d
        """
    if solve(4, actual, expected, None):
        return
    assert False


@mark.skip("EXPLICITLY")
def test_finned_x_wing_east_fins1():
    actual = \
        f"""
        _234a ____a   234_b ____b
        ____a ____a   ____b ____b

        _234c ____c   ____d ____d
        ____c ____c   ____d ____d
        """

    expected = \
        f"""
        _234a ____a   234_b ____b
        ____a ____a   ____b ____b

        _234c ____c   ____d ____d
        ____c ____c   ____d _234d
        """
    if solve(4, actual, expected, None):
        return
    assert False


####################################################
####################################################
####################################################
####################################################


####################################################
####################################################
####################################################
####################################################


####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################


#
# def test_sudoku_6x6_3x2():
#     actual = \
#         f"""
#         ______a ______a ______a   ______b ______b ______b
#         ______a ______a ______a   ______b ______b ______b
#
#         ______c ______c ______c   ______d ______d ______d
#         ______c ______c ______c   ______d ______d ______d
#
#         ______e ______e ______e   ______f ______f ______f
#         ______e ______e ______e   ______f ______f ______f
#         """
#


# def test_sudoku_6x6_3x2():
#     actual = \
#         f"""
#         ______a ______a ______a   ______b ______b ______b
#         ______a ______a ______a   ______b ______b ______b
#
#         ______c ______c ______c   ______d ______d ______d
#         ______c ______c ______c   ______d ______d ______d
#
#         ______e ______e ______e   ______f ______f ______f
#         ______e ______e ______e   ______f ______f ______f
#         """
#
#     expected = \
#         f"""
#         ______a ______a ______a   ______b ______b ______b
#         ______a ______a ______a   ______b ______b ______b
#
#         ______c ______c ______c   ______d ______d ______d
#         ______c ______c ______c   ______d ______d ______d
#
#         ______e ______e ______e   ______f ______f ______f
#         ______e ______e ______e   ______f ______f ______f
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#
#
# def test_sudoku_6x6_2x3():
#     actual = \
#         f"""
#         ______a ______a   ______b ______b   ______c ______c
#         ______a ______a   ______b ______b   ______c ______c
#         ______a ______a   ______b ______b   ______c ______c
#
#         ______d ______d   ______e ______e   ______f ______f
#         ______d ______d   ______e ______e   ______f ______f
#         ______d ______d   ______e ______e   ______f ______f
#         """
#
#     expected = \
#         f"""
#         ______a ______a   ______b ______b   ______c ______c
#         ______a ______a   ______b ______b   ______c ______c
#         ______a ______a   ______b ______b   ______c ______c
#
#         ______d ______d   ______e ______e   ______f ______f
#         ______d ______d   ______e ______e   ______f ______f
#         ______d ______d   ______e ______e   ______f ______f
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
#

# def test_sudoku_4x4_():
#     actual = \
#         f"""
#         ____a ____a   ____b ____b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#
#     expected = \
#         f"""
#         ____a ____a   ____b ____b
#         ____a ____a   ____b ____b
#
#         ____c ____c   ____d ____d
#         ____c ____c   ____d ____d
#         """
#     if solve(actual, expected, None):
#         return
#     assert False
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


@mark.skip("EXPLICITLY")
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


@mark.skip("EXPLICITLY")
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


@mark.skip("EXPLICITLY")
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


@mark.skip("EXPLICITLY")
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


def test_sudoku_4x4_ar1_row_ne_control():
    if solve(4, f"""
                ____a ____a   ____b ____b
                ____a ___4a   __3_b ____b

                ____c ____c   ____d 1234d
                ____c __3_c   ____d ___4d
                """, None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_nw():
    if solve(4,
             f"""
            ____a 1234a   _2__b ____b
            ____a _2__a   __3_b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a 12_4a   _2__b ____b
            ____a _2__a   __3_b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_nw_control():
    if solve(4, f"""
            ____a 1234a   _2__b ____b
            ____a ____a   __3_b ____b

            ____c _2__c   ____d ____d
            ____c ____c   ____d ____d""",
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_se():
    if solve(4,
             f"""
            ____a 1___a   ____b _2__b
            ____a _2__a   ____b 1234b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a 1___a   ____b _2__b
            ____a _2__a   ____b _234b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_se_control():
    if solve(4, f"""
            ____a 1___a   ____b _2__b
            ____a ____a   ____b 1234b

            ____c _2__c   ____d ____d
            ____c ____c   ____d ____d""",
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_sw():
    if solve(4,
             f"""
            ____a ___4a   __3_b ____b
            ____a 1234a   ___4b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ___4a   __3_b ____b
            ____a 12_4a   ___4b ____b

            ____c ____c   ____d ____d
            ____c ____c   ____d ____d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_sw_control():
    if solve(4, f"""
            ____a ____a   __3_b ____b
            ____a 1234a   ___4b ____b

            ____c ___4c   ____d ____d
            ____c ____c   ____d ____d""",
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_ne():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   1___b 1234b

            ____c ____c   ___4d 1___d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   1___b 123_b

            ____c ____c   ___4d 1___d
            ____c ____c   ____d ____d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_ne_control():
    if solve(4, f"""
            ____a 1___a   ____b 1234b
            ____a ____a   ____b ____b

            ____c ___4c   ____d 1___d
            ____c ____c   ____d ____d
            """,
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_nw():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            1234a ___4a   ____b ____b

            ___4c __3_c   ____d ____d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            12_4a ___4a   ____b ____b

            ___4c __3_c   ____d ____d
            ____c ____c   ____d ____d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_nw_control():
    if solve(4, f"""
            ____a ____a   ____b ____b
            1234a ___4a   ____b ____b

            ____c __3_c   ____d ____d
            ___4c ____c   ____d ____d
            """,
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_se():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ___4b 1___b

            ____c ____c   ____d ____d
            ____c ____c   1___d 1234d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ___4b 1___b

            ____c ____c   ____d ____d
            ____c ____c   1___d 123_d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_se_control():
    if solve(4, f"""
            ____a ____a   ____b ____b
            ____a ___4a   ____b 1___b

            ____c ____c   ____d ____d
            ____c 1___c   ____d 1234d""",
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_sw():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   1___b 2___b

            ____c ____c   1234d 1___d
            ____c ____c   ____d ____d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   1___b 2___b

            ____c ____c   1_34d 1___d
            ____c ____c   ____d ____d
            """, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_col_sw_control():
    if solve(4, f"""
            ____a ____a   ____b ____b
            ____a 1___a   ____b 2___b

            ____c 1234c   ____d 1___d
            ____c ____c   ____d ____d""",
             None, AvoidableRectangleType1()):
        return
    assert False


def test_sudoku_4x4_ar1_row_ne():
    if solve(4,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ___4c   ____d 1234d
            ____c __3_c   ____d ___4d
            """,
             f"""
            ____a ____a   ____b ____b
            ____a ____a   ____b ____b

            ____c ___4c   ____d 12_4d
            ____c __3_c   ____d ___4d
            """, AvoidableRectangleType1()):
        return
    assert False
