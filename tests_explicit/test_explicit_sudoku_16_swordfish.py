import pytest

from tech import tech
from tests_explicit.test_small_explicit import solve


@pytest.mark.skip("EXPLICITLY")
def test_sudoku_explicit_sword_fish_cols():
    actual = \
        f"""
        123456789a 123456789a 123456789a    123456789b 123456789b ________9b    __3_5____c ___45____c 123456789c
        123456789a 123456789a 123456789a    123456789b 123456789b __34_____b    __3____8_c ___4___8_c 123456789c
        123456789a 123456789a 123456789a    123456789b 123456789b _____6___b    ______7_9c 1_______9c 123456789c
        
        123456789d 123456789d 123456789d    123456789e 123456789e _______8_e    1________f _____6___f 123456789f
        123456789d 123456789d 123456789d    123456789e 123456789e __3_5____e    ____5_7__f _2_______f 123456789f
        123456789d 123456789d 123456789d    123456789e 123456789e ______7__e    _______89f _______89f 123456789f
        
        123456789g 123456789g 123456789g    123456789h 123456789h 1________h    _____6___i ______7__i 123456789i
        123456789g 123456789g 123456789g    123456789h 123456789h __345____h    _2_______i 1___5____i 123456789i
        123456789g 123456789g 123456789g    123456789h 123456789h _2_______h    ___4_____i __3______i 123456789i
        """

    expected = \
        f"""
        1234_6789a 1234_6789a 1234_6789a    1234_6789b 1234_6789b ________9b    __3_5____c ___45____c 1234_6789c
        123456789a 123456789a 123456789a    123456789b 123456789b __34_____b    __3____8_c ___4___8_c 123456789c
        123456789a 123456789a 123456789a    123456789b 123456789b _____6___b    ______7_9c 1_______9c 123456789c
        
        123456789d 123456789d 123456789d    123456789e 123456789e _______8_e    1________f _____6___f 123456789f
        1234_6789d 1234_6789d 1234_6789d    1234_6789e 1234_6789e __3_5____e    ____5_7__f _2_______f 1234_6789f
        123456789d 123456789d 123456789d    123456789e 123456789e ______7__e    _______89f _______89f 123456789f
        
        123456789g 123456789g 123456789g    123456789h 123456789h 1________h    _____6___i ______7__i 123456789i
        1234_6789g 1234_6789g 1234_6789g    1234_6789h 1234_6789h __345____h    _2_______i 1___5____i 1234_6789i
        123456789g 123456789g 123456789g    123456789h 123456789h _2_______h    ___4_____i __3______i 123456789i
        """
    if solve(9, actual, expected, tech.SwordFish()):
        return
    assert False

@pytest.mark.skip("EXPLICITLY")
def test_sudoku_explicit_sword_fish_rows():
    actual = \
        f"""
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
        123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
        _23456789a _23456789a 123456789a    _23456789b 123456789b _23456789b    123456789c _23456789c _23456789c
        
        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
        _23456789d _23456789d 123456789d    _23456789e 123456789e _23456789e    123456789f _23456789f _23456789f
        123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
        
        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
        _23456789g _23456789g 123456789g    _23456789h 123456789h _23456789h    123456789i _23456789i _23456789i
        123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
        """

    expected = \
        f"""
        123456789a 123456789a _23456789a    123456789b _23456789b 123456789b    _23456789c 123456789c 123456789c
        123456789a 123456789a _23456789a    123456789b _23456789b 123456789b    _23456789c 123456789c 123456789c
        _23456789a _23456789a 123456789a    _23456789b 123456789b _23456789b    123456789c _23456789c _23456789c
        
        123456789d 123456789d _23456789d    123456789e _23456789e 123456789e    _23456789f 123456789f 123456789f
        _23456789d _23456789d 123456789d    _23456789e 123456789e _23456789e    123456789f _23456789f _23456789f
        123456789d 123456789d _23456789d    123456789e _23456789e 123456789e    _23456789f 123456789f 123456789f
        
        123456789g 123456789g _23456789g    123456789h _23456789h 123456789h    _23456789i 123456789i 123456789i
        _23456789g _23456789g 123456789g    _23456789h 123456789h _23456789h    123456789i _23456789i _23456789i
        123456789g 123456789g _23456789g    123456789h _23456789h 123456789h    _23456789i 123456789i 123456789i
        """
    if solve(9, actual, expected, tech.SwordFish()):
        return
    assert False
