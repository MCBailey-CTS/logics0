


from techniques.UniqueRectangleType1 import UniqueRectangleType1
from tests.test_small_explicit import solve


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