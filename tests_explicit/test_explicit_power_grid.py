
# from tests_explicit.test_small_explicit import solve
# from techniques.CrossHatch import CrossHatch

# def test_explicit_power_grid_():
#     actual = \
#         f"""
        
#         """
#     expected = \
#         f"""
        
#         """
#     if solve(4, actual, expected, None):
#         return
#     assert False

from techniques.PowerGridLength9Power6 import  PowerGridTouchingPower, PowerGridBothPowersSolved, \
    PowerGridLength9Power7, PowerGridHiddenPowerPair, PowerGridOnePowerSolvedBadMath, PowerGrid2Solved, PowerGrid1Solved1Unsolved, PowerGridRequirePower


def test_row_():
    actual = \
        f"""
        ______a ______a ______a   ______b ______b ______b
        ______a ______a ______a   ______b ______b ______b

        ______c ______c ______c   ______d ______d ______d
        ______c ______c ______c   ______d ______d ______d

        ______e ______e ______e   ______f ______f ______f
        ______e ______e ______e   ______f ______f ______f
        """

    expected = \
        f"""
        ______a ______a ______a   ______b ______b ______b
        ______a ______a ______a   ______b ______b ______b

        ______c ______c ______c   ______d ______d ______d
        ______c ______c ______c   ______d ______d ______d

        ______e ______e ______e   ______f ______f ______f
        ______e ______e ______e   ______f ______f ______f
        """
    if solve(actual, expected, None):
        return
    assert False