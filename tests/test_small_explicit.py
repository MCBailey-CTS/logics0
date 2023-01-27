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





