from tech import tech
from tests_explicit.test_small_explicit import solve
from pytest import mark

@mark.skip("skipped")

def test_sudoku_explicit_x_wing_col():
    actual = \
        f"""
        _________a 12345678_a _________a    12345678_b _________b _________b    _________c _________c _________c
        _________a 12345678_a _________a    12345678_b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        
        _________d 12345678_d _________d    12345678_e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d 12345678_d _________d    12345678_e _________e _________e    _________f _________f _________f
        
        _________g 12345678_g _________g    12345678_h _________h _________h    _________i _________i _________i
        _________g 12345678_g _________g    12345678_h _________h _________h    _________i _________i _________i
        _________g 12345678_g _________g    12345678_h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        _________a 12345678_a _________a    12345678_b _________b _________b    _________c _________c _________c
        _________a 12345678_a _________a    12345678_b _________b _________b    _________c _________c _________c
        12345678_a _________a 12345678_a    _________b 12345678_b 12345678_b    12345678_c 12345678_c 12345678_c
        
        _________d 12345678_d _________d    12345678_e _________e _________e    _________f _________f _________f
        12345678_d _________d 12345678_d    _________e 12345678_e 12345678_e    12345678_f 12345678_f 12345678_f
        _________d 12345678_d _________d    12345678_e _________e _________e    _________f _________f _________f
        
        _________g 12345678_g _________g    12345678_h _________h _________h    _________i _________i _________i
        _________g 12345678_g _________g    12345678_h _________h _________h    _________i _________i _________i
        _________g 12345678_g _________g    12345678_h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, tech.XWing()):
        return
    assert False
@mark.skip("skipped")

def test_sudoku_explicit_x_wing_row():
    actual = \
        f"""
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        _________a _________a _________a    _________b _________b _________b    _________c _________c _________c
        
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        _________d _________d _________d    _________e _________e _________e    _________f _________f _________f
        ____56___d _______8_d ___4_____d    1___5____e ______7__e ________9e    1____6___f __3______f _2_______f
        
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        _2__5____g ___4_____g _______8_g    ____56___h ________9h 1________h    _2___6___i ______7__i __3______i
        _________g _________g _________g    _________h _________h _________h    _________i _________i _________i
        """

    expected = \
        f"""
        1234_6789a _________a _________a    1234_6789b _________b _________b    _________c _________c _________c
        1234_6789a _________a _________a    1234_6789b _________b _________b    _________c _________c _________c
        1234_6789a _________a _________a    1234_6789b _________b _________b    _________c _________c _________c
        
        1234_6789d _________d _________d    1234_6789e _________e _________e    _________f _________f _________f
        1234_6789d _________d _________d    1234_6789e _________e _________e    _________f _________f _________f
        ____56___d _______8_d ___4_____d    1___5____e ______7__e ________9e    1____6___f __3______f _2_______f
        
        1234_6789g _________g _________g    1234_6789h _________h _________h    _________i _________i _________i
        _2__5____g ___4_____g _______8_g    ____56___h ________9h 1________h    _2___6___i ______7__i __3______i
        1234_6789g _________g _________g    1234_6789h _________h _________h    _________i _________i _________i
        """
    if solve(9, actual, expected, tech.XWing()):
        return
    assert False
