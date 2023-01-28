from techniques.AvoidableRectangleType1 import AvoidableRectangleType1
from tests.test_small_explicit import solve


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







def test0():
    if solve(9,
             f"""
            123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    ______7__f 123456789f _2_____8_f 

123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    _______8_i 123456789i ______7__i 
            """,
             f"""
            123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 
123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c 

123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f 
123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    ______7__f 123456789f _2_______f 

123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i 
123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    _______8_i 123456789i ______7__i 
            """, AvoidableRectangleType1()):
        return
    assert False


def test1():
    if solve(9,
             f"""
 
            """,
             f"""
             
            """, AvoidableRectangleType1()):
        return
    assert False
