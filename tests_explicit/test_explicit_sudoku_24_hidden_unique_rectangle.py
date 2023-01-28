from pytest import mark
from techniques.HiddenUniqueRectangle import HiddenUniqueRectangle
from tests_explicit.test_small_explicit import solve


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