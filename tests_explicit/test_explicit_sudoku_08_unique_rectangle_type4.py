


from techniques.UniqueRectangleType4 import UniqueRectangleType4
from tests_explicit.test_small_explicit import solve


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



def test_sudoku_explicit_unique_rectangle_type4_goofy_east():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _23456789b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _23456789b    _________c _________c _________c
        _________a _________a _________a    _________b 12_______b _________b    _________c _________c _________c
        
        _________d _________d _________d    _________e 12_______e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _23456789e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _23456789e    _________f _________f _________f
        
        _________g _________g _________g    _________h _________h _23456789h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _23456789h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _23456789h    _________i _________i _________i        
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _23456789b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _23456789b    _________c _________c _________c
        _________a _________a _________a    _________b 12_______b 1_3456789b    _________c _________c _________c
        
        _________d _________d _________d    _________e 12_______e 1_3456789e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _23456789e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _23456789e    _________f _________f _________f
        
        _________g _________g _________g    _________h _________h _23456789h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _23456789h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _23456789h    _________i _________i _________i        
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type4_goofy_north():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        
        _23456789d _23456789d _________d    _________e _23456789e _23456789e    _23456789f _23456789f _23456789f
        _________d _________d 12_______d    12_______e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        
        _23456789d _23456789d 1_3456789d    1_3456789e _23456789e _23456789e    _23456789f _23456789f _23456789f
        _________d _________d 12_______d    12_______e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False


# _actual

#
# sudoku_explicit_unique_rectangle_type4_goofy_south_expected

#
def test_sudoku_explicit_unique_rectangle_type4_goofy_south():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        
        _________d _________d 12_______d    12_______e _________e _________e    _________f _________f _________f
        _23456789d _23456789d _________d    _________e _23456789e _23456789e    _23456789f _23456789f _23456789f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        
        _________d _________d 12_______d    12_______e _________e _________e    _________f _________f _________f
        _23456789d _23456789d 1_3456789d    1_3456789e _23456789e _23456789e    _23456789f _23456789f _23456789f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False



def test_sudoku_explicit_unique_rectangle_type4_goofy_west():
    actual = \
        f"""
        _________a _________a _________a    _23456789b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _23456789b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b 12_______b _________b    _________c _________c _________c
        
        _________d _________d _________d    _________e 12_______e _________e    _________f _________f _________f
        _________d _________d _________d    _23456789e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _23456789e _________e _________e    _________f _________f _________f
        
        _________g _________g _________g    _23456789h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _23456789h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _23456789h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _23456789b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _23456789b _________b _________b    _________c _________c _________c
        _________a _________a _________a    1_3456789b 12_______b _________b    _________c _________c _________c
        
        _________d _________d _________d    1_3456789e 12_______e _________e    _________f _________f _________f
        _________d _________d _________d    _23456789e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _23456789e _________e _________e    _________f _________f _________f
        
        _________g _________g _________g    _23456789h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _23456789h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _23456789h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type4_normal_east():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    ________9c _________c _________c
        _________a _________a _________a    _________b _________b _________b    __34_____c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _____6___c _________c _________c
        
        _________d _________d _________d    _________e _________e _________e    _______8_f _________f _________f
        _________d _________d _________d    _________e _________e _________e    ______7__f _________f _________f
        _________d _________d _________d    _________e _________e _________e    ____5____f _________f _________f
        
        _________g _________g _________g    _________h _________h _________h    _23______i _________i _________i
        _________g 12_______g _________g    _________h _________h _________h    12_4_____i _________i _________i
        _________g 12_______g _________g    _________h _________h _________h    1234_____i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    ________9c _________c _________c
        _________a _________a _________a    _________b _________b _________b    __34_____c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _____6___c _________c _________c
        
        _________d _________d _________d    _________e _________e _________e    _______8_f _________f _________f
        _________d _________d _________d    _________e _________e _________e    ______7__f _________f _________f
        _________d _________d _________d    _________e _________e _________e    ____5____f _________f _________f
        
        _________g _________g _________g    _________h _________h _________h    _23______i _________i _________i
        _________g 12_______g _________g    _________h _________h _________h    1__4_____i _________i _________i
        _________g 12_______g _________g    _________h _________h _________h    1_34_____i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False



def test_sudoku_explicit_unique_rectangle_type4_normal_south():
    actual = \
        f"""
        ___4__7__a ___4__7__a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        __34567__g __34567__g __3__6___g    ________9h _____67__h 1________h    _______8_i _2__56___i _23______i
        """

    expected = \
        f"""
        ___4__7__a ___4__7__a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        __3456___g __3456___g __3__6___g    ________9h _____67__h 1________h    _______8_i _2__56___i _23______i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False


def test_sudoku_explicit_unique_rectangle_type4_normal_west():
    actual = \
        f"""
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c
        
        _________d _________d _________d    12_______e _________e _________e    _________f _________f _________f
        _________d _________d _________d    12_______e _________e _________e    _________f _________f _________f
        _________d _________d _23456789d    _________e _________e _________e    _________f _________f _________f
        
        _________g _________g _23456789g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _23456789g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _23456789g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _23456789a    _________b _________b _________b    _________c _________c _________c
        
        _________d _________d 1_3456789d    12_______e _________e _________e    _________f _________f _________f
        _________d _________d 1_3456789d    12_______e _________e _________e    _________f _________f _________f
        _________d _________d _23456789d    _________e _________e _________e    _________f _________f _________f
        
        _________g _________g _23456789g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _23456789g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _23456789g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False
#

#

def test_sudoku_explicit_unique_rectangle_type4_normal_north():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        
        _23456789d _23456789d _23456789d    _________e _23456789e _________e    _23456789f _23456789f _23456789f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        
        _________g _________g _________g    12_______h _________h 12_______h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        
        _23456789d _23456789d _23456789d    1_3456789e _23456789e 1_3456789e    _23456789f _23456789f _23456789f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        
        _________g _________g _________g    12_______h _________h 12_______h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, UniqueRectangleType4()):
        return
    assert False



















