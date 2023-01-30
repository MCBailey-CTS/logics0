import numpy
import pytest

from Constants import Constants
from Loc import Loc
from _defaults import default_test_puzzle, default_test_explicit_actual_expected
from puzzles import *
from solving import Solving
from tech import tech
from techniques.AlmostLockedCandidatesClaiming import AlmostLockedCandidatesClaiming
from techniques.AvoidableRectangleType1 import AvoidableRectangleType1
from techniques.AvoidableRectangleType2 import AvoidableRectangleType2
from techniques.Bug import Bug
from techniques.CrossHatch import CrossHatch
from techniques.FinnedXWing import FinnedXWing
from techniques.HiddenSingle import HiddenSingle
from techniques.HiddenUniqueRectangle import HiddenUniqueRectangle
from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
from techniques.LockedCandidatesPointing import LockedCandidatesPointing
# from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# from techniques.LockedCandidatesPointing import LockedCandidatesPointing
from techniques.NakedPair import NakedPair
from techniques.ShashimiXWing import ShashimiXWing
from techniques.UniqueRectangleType1 import UniqueRectangleType1
from techniques.UniqueRectangleType2 import UniqueRectangleType2
from techniques.UniqueRectangleType3 import UniqueRectangleType3
from techniques.UniqueRectangleType4 import UniqueRectangleType4
from techniques.WWing import WWing
from techniques.WxyzWing import WxyzWing
from techniques.XyWing import XyWing

EXPLICITLY = "EXPLICITLY"
from colorama import Fore

# @pytest.mark.parametrize("constructor, technique, actual, expected", [



#     (Mathrax,
#      CrossHatch(),
#      Constants.mathrax_cross_hatch_actual.__name__,
#      Constants.mathrax_cross_hatch_expected.__name__),
#     (Mathrax,
#      tech.MathraxMathSubtraction(),
#      Constants.mathrax_01minus_actual.__name__,
#      Constants.mathrax_01minus_expected.__name__),
#     (Mathrax,
#      tech.MathraxMath04XWing(),
#      Constants.mathrax_04plus_actual.__name__,
#      Constants.mathrax_04plus_expected.__name__),
#     (Mathrax,
#      tech.MathraxMathMultiplication(),
#      Constants.mathrax_06x04x_actual.__name__,
#      Constants.mathrax_06x04x_expected.__name__),
# ])
# def test_default_actual_expected(constructor, technique, actual, expected):
#     if "\n" in actual or "\n" in expected:
#         pytest.skip('Explicitly')
#     assert default_test_explicit_actual_expected(constructor, technique, getattr(Constants, actual)(),
#                                                  getattr(Constants, expected)())
# @staticmethod
# def mathrax_explicit_cross_hatch_actual():
#     return f"""
#     mathrax_explicit_cross_hatch_actual.mathrax
#     4
#     __3_ ... 1234 ... 1234 ... 1234
#     .... ... .... ... .... ... ....
#     1234 ... 1234 ... 1234 ... 1234
#     .... ... .... ... .... ... ....
#     1234 ... 1234 ... 1234 ... 1234
#     .... ... .... ... .... ... ....
#     1234 ... 1234 ... 1234 ... 1234
#     """
#
# @staticmethod
# def mathrax_explicit_cross_hatch_expected():
#     return f"""
#     mathrax_explicit_cross_hatch_expected.mathrax
#     4
#     __3_ ... 12_4 ... 12_4 ... 12_4
#     .... ... .... ... .... ... ....
#     12_4 ... 1234 ... 1234 ... 1234
#     .... ... .... ... .... ... ....
#     12_4 ... 1234 ... 1234 ... 1234
#     .... ... .... ... .... ... ....
#     12_4 ... 1234 ... 1234 ... 1234
#     """
#
# @staticmethod
# def mathrax_explicit_hidden_single_actual():
#     return f"""
#     mathrax_explicit_hidden_single_actual.mathrax
#     4
#     123_ ... 123_ ... 123_ ... 1234
#     .... ... .... ... .... ... ....
#     1234 ... 1234 ... 123_ ... 1234
#     .... ... .... ... .... ... ....
#     1234 ... 1234 ... 123_ ... 1234
#     .... ... .... ... .... ... ....
#     1234 ... 1234 ... 1234 ... 1234
#     """
#
# @staticmethod
# def mathrax_explicit_hidden_single_expected():
#     return f"""
#     mathrax_explicit_hidden_single_expected.mathrax
#     4
#     123_ ... 123_ ... 123_ ... ___4
#     .... ... .... ... .... ... ....
#     1234 ... 1234 ... 123_ ... 1234
#     .... ... .... ... .... ... ....
#     1234 ... 1234 ... 123_ ... 1234
#     .... ... .... ... .... ... ....
#     1234 ... 1234 ... ___4 ... 1234
#     """



# @staticmethod
# def mathrax_cross_hatch_actual():
#     return f""" 
#     mathrax_cross_hatch_actual.mathrax
#     4
#     1___ ... 1234 ... ___4 ... __3_
#     .... 04+ .... 01- .... ... ....
#     _2__ ... 1234 ... 1234 ... 1234
#     .... 01- .... ... .... 01- ....
#     ___4 ... 1234 ... 1234 ... 1234
#     .... ... .... 01- .... ... ....
#     __3_ ... 1234 ... 1234 ... 1234
#     """

# @staticmethod
# def mathrax_cross_hatch_expected():
#     return f"""
#     mathrax_cross_hatch_expected.mathrax
#     4
#     1___ ... _2__ ... ___4 ... __3_
#     .... 04+ .... 01- .... ... ....
#     _2__ ... 1_34 ... 1_3_ ... 1__4
#     .... 01- .... ... .... 01- ....
#     ___4 ... 1_3_ ... 123_ ... 12__
#     .... ... .... 01- .... ... ....
#     __3_ ... 1__4 ... 12__ ... 12_4
#     """


# @staticmethod
# def mathrax_04plus_actual():
#     return f"""
#     mathrax_04plus_actual.mathrax
#     4
#     1___ ... 1234 ... ___4 ... __3_
#     .... 04+ .... ... .... ... ....
#     _2__ ... 1234 ... 1234 ... 1234
#     .... ... .... ... .... ... ....
#     ___4 ... 1234 ... 1234 ... 1234
#     .... ... .... ... .... ... ....
#     __3_ ... 1234 ... 1234 ... 1234
#     """

# @staticmethod
# def mathrax_04plus_expected():
#     return f"""
#     mathrax_04plus_expected.mathrax
#     4
#     1___ ... 1234 ... ___4 ... __3_
#     .... 04+ .... ... .... ... ....
#     _2__ ... 1234 ... 1_34 ... 1_34
#     .... ... .... ... .... ... ....
#     ___4 ... 1_34 ... 1234 ... 1234
#     .... ... .... ... .... ... ....
#     __3_ ... 1_34 ... 1234 ... 1234
#     """

# @staticmethod
# def mathrax_01minus_actual():
#     return f"""
#     mathrax_01minus_actual.mathrax
#     4
#     1___ ... _2__ ... ___4 ... __3_
#     .... ... .... 01- .... ... ....
#     _2__ ... 1_34 ... 1_3_ ... 1__4
#     .... 01- .... ... .... 01- ....
#     ___4 ... 1_3_ ... 123_ ... 12__
#     .... ... .... 01- .... ... ....
#     __3_ ... 1__4 ... 12__ ... 12_4
#     """

# @staticmethod
# def mathrax_01minus_expected():
#     return f"""
#     mathrax_01minus_expected.mathrax
#     4
#     1___ ... _2__ ... ___4 ... __3_
#     .... ... .... 01- .... ... ....
#     _2__ ... __3_ ... 1_3_ ... 1__4
#     .... 01- .... ... .... 01- ....
#     ___4 ... 1_3_ ... _23_ ... _2__
#     .... ... .... 01- .... ... ....
#     __3_ ... 1__4 ... _2__ ... 12_4
#     """

# @staticmethod
# def mathrax_02division_actual():
#     return f"""
#     mathrax_02division_actual.mathrax
#     6
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     ...... ... ...... ... ...... 03- ...... ... ...... ... ......
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     ...... ... ...... ... ...... ... ...... 02/ ...... 07+ ......
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     ...... ... ...... ... ...... ... ...... ... ...... ... ......
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     ...... 04x ...... 08+ ...... 03- ...... ... ...... ... ......
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     ...... 06x ...... ... ...... 08+ ...... ... ...... ... ......
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     """

# @staticmethod
# def mathrax_02division_expected():
#     return f"""
#         mathrax_02division_expected.mathrax
#         6
#         123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#         ...... ... ...... ... ...... 03- ...... ... ...... ... ......
#         123456 ... 123456 ... 123456 ... 1234_6 ... 1234_6 ... 123456
#         ...... ... ...... ... ...... ... ...... 02/ ...... 07+ ......
#         123456 ... 123456 ... 123456 ... 1234_6 ... 1234_6 ... 123456
#         ...... ... ...... ... ...... ... ...... ... ...... ... ......
#         123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#         ...... 04x ...... 08+ ...... 03- ...... ... ...... ... ......
#         123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#         ...... 06x ...... ... ...... 08+ ...... ... ...... ... ......
#         123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#         """

# @staticmethod
# def mathrax_06x04x_actual():
#     return f"""
#     mathrax_06x04x_actual.mathrax
#     6
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     ...... ... ...... ... ...... 03- ...... ... ...... ... ......
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     ...... ... ...... ... ...... ... ...... 02/ ...... 07+ ......
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     ...... ... ...... ... ...... ... ...... ... ...... ... ......
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     ...... 04x ...... 08+ ...... 03- ...... ... ...... ... ......
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     ...... 06x ...... ... ...... 08+ ...... ... ...... ... ......
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     """

# @staticmethod
# def mathrax_06x04x_expected():
#     return f"""
#     mathrax_06x04x_expected.mathrax
#     6
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     ...... ... ...... ... ...... 03- ...... ... ...... ... ......
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     ...... ... ...... ... ...... ... ...... 02/ ...... 07+ ......
#     123456 ... 123456 ... 123456 ... 123456 ... 123456 ... 123456
#     ...... ... ...... ... ...... ... ...... ... ...... ... ......
#     12_4__ ... 12_4__ ... 123456 ... 123456 ... 123456 ... 123456
#     ...... 04x ...... 08+ ...... 03- ...... ... ...... ... ......
#     12____ ... 12____ ... 123456 ... 123456 ... 123456 ... 123456
#     ...... 06x ...... ... ...... 08+ ...... ... ...... ... ......
#     __3__6 ... __3__6 ... 123456 ... 123456 ... 123456 ... 123456
#     """
