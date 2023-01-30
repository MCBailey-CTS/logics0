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

# @pytest.mark.parametrize("puzzle_string, constructor, techniques", [
#
#
#
#     ('lighthouses_001', Lighthouses, Solving.lighthouses_techniques()),
#     ('lighthouses_002', Lighthouses, Solving.lighthouses_techniques()),
#
#
# ])
# def test_default_puzzle(puzzle_string, constructor, techniques):
#     if "\n" in puzzle_string:
#         pytest.skip(puzzle_string)
#     result = getattr(Constants, puzzle_string)
#     assert default_test_puzzle(result(), constructor, techniques)





# @staticmethod
# def lighthouses_001():
#     return f"""
#     001.lighthouses
#     5
#     +- +- +- +- +-
#     03 +- +- +- +-
#     +- +- +- +- +-
#     +- +- 02 +- +-
#     +- +- +- +- 01
#     """

# @staticmethod
# def lighthouses_002():
#     return f"""
#     002.lighthouses
#     5
#     02 +- +- +- +-
#     +- +- +- +- +-
#     +- +- 00 +- 01
#     +- +- +- +- +-
#     +- +- 00 +- 01
#     """

# @staticmethod
# def lighthouses_003():
#     return f"""
#     003.lighthouses
#     5
#     +- +- +- +- 02
#     +- +- +- +- +-
#     +- +- 00 +- +-
#     +- +- +- +- +-
#     02 +- 01 +- +-
#     """

# @staticmethod
# def lighthouses_004():
#     return f"""
#     004.lighthouses
#     5
#     +- +- 01 +- +-
#     02 +- +- +- +-
#     +- +- 01 +- +-
#     +- +- +- +- +-
#     +- +- +- +- 03
#     """

# @staticmethod
# def lighthouses_005():
#     return f"""
#     005.lighthouses
#     6
#     +- +- +- +- +- +-
#     01 +- +- +- +- 01
#     +- +- +- +- +- +-
#     02 +- +- +- 01 +-
#     +- +- +- +- +- +-
#     +- +- 04 +- +- +-
#     """

# @staticmethod
# def lighthouses_006():
#     return f"""
#     006.lighthouses
#     6
#     +- +- +- +- +- 02
#     +- +- +- +- +- +-
#     00 +- +- +- +- +-
#     +- +- 01 +- +- +-
#     +- +- +- +- +- +-
#     +- +- +- 02 +- 01
#     """







# @staticmethod
# def lighthouses_007():
#     return f"""
#     007.lighthouses
#     6
#     02 +- +- +- +- +-
#     +- +- +- +- +- +-
#     +- +- 01 +- +- +-
#     00 +- +- +- +- +-
#     +- +- +- +- +- +-
#     01 +- +- +- +- 03
#     """





# @staticmethod
# def lighthouses_008():
#     return f"""
#     008.lighthouses
#     6
#     01 +- +- +- +- 01
#     +- +- +- +- +- +-
#     +- +- +- +- +- 00
#     +- +- +- 03 +- +-
#     +- +- +- +- +- +-
#     +- +- +- +- +- +-
#     """



# @staticmethod
# def lighthouses_009():
#     return f"""
#     009.lighthouses
#     7
#     02 +- 01 +- +- +- +-
#     +- +- +- +- +- +- +-
#     02 +- 01 +- +- +- +-
#     +- +- +- +- +- +- +-
#     +- +- 02 +- +- +- +-
#     +- +- +- +- +- +- +-
#     +- +- 02 +- 05 +- +-
#     """




# @staticmethod
# def lighthouses_010():
#     return f"""
#     010.lighthouses
#     7
#     +- 01 +- 00 +- 02 +-
#     +- +- +- +- +- +- +-
#     +- +- 03 +- +- +- +-
#     +- +- +- +- +- +- +-
#     02 +- +- +- +- +- +-
#     +- +- +- +- +- +- +-
#     +- +- +- 01 +- +- +-
#     """


# @staticmethod
# def lighthouses_011():
#     return f"""
#     011.lighthouses
#     7
#     +- +- +- +- 01 +- +-
#     +- +- +- +- +- +- +-
#     +- +- 00 +- +- 01 +-
#     +- +- +- +- +- +- +-
#     +- +- 03 +- +- +- +-
#     +- +- +- +- +- +- +-
#     03 +- 01 +- +- +- +-
#     """




# @staticmethod
# def lighthouses_012():
#     return f"""
#     012.lighthouses
#     7
#     01 +- +- +- +- +- 03
#     +- +- +- +- +- +- +-
#     +- 01 +- +- +- +- 02
#     +- +- +- +- +- +- +-
#     +- +- 01 +- +- +- +-
#     +- +- +- +- +- +- +-
#     +- +- +- +- 04 +- +-
#     """



# @staticmethod
# def lighthouses_013():
#     return f"""
#     013.lighthouses
#     8
#     +- +- +- +- +- +- +- 00
#     +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- 01
#     00 +- 03 +- +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     03 +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     +- +- +- +- 03 +- +- 01
#     """




# @staticmethod
# def lighthouses_014():
#     return f"""
#     014.lighthouses
#     8
#     +- +- +- 01 +- 01 +- +-
#     +- +- +- +- +- +- +- +-
#     +- +- 04 +- +- +- +- +-
#     02 +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- 03
#     +- +- +- +- +- 00 +- +-
#     +- +- +- +- +- +- +- 02
#     +- +- +- +- 03 +- +- +-
#     """






# @staticmethod
# def lighthouses_015():
#     return f"""
#     015.lighthouses
#     8
#     +- +- +- +- +- +- +- +-
#     +- 04 +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     +- +- +- 00 +- 00 +- +-
#     +- +- +- +- +- +- +- 03
#     +- +- +- 01 +- +- +- +-
#     +- +- +- +- +- 01 +- +-
#     """





# @staticmethod
# def lighthouses_016():
#     return f"""
#     016.lighthouses
#     8
#     +- +- +- 02 +- 02 +- +-
#     +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- 01 +-
#     03 +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- 02
#     +- +- +- +- +- 02 +- +-
#     +- +- +- +- +- +- +- 01
#     +- 02 +- +- +- +- +- +-
#     """




# @staticmethod
# def lighthouses_017():
#     return f"""
#     017.lighthouses
#     8
#     +- +- +- 01 +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     04 +- +- +- +- +- +- 02
#     +- +- +- +- +- +- +- +-
#     +- +- +- +- +- 04 +- +-
#     +- +- +- +- +- +- +- +-
#     +- +- +- +- +- 03 +- +-
#     +- +- +- +- +- +- +- 00
#     """

# @staticmethod
# def lighthouses_018():
#     return f"""
#     018.lighthouses
#     8
#     +- +- +- +- +- +- +- 01
#     +- +- +- +- +- 01 +- +-
#     00 +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     03+ - +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +-
#     +- 01 +- 02 +- 01 +- +-
#     """







# @staticmethod
# def lighthouses_019():
#     return f"""
#     019.lighthouses
#     9
#     +- +- +- +- +- +- +- 02 +-
#     +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +-
#     +- 04 +- +- +- +- +- +- 01
#     +- +- +- +- +- +- +- +- +-
#     +- +- +- 01 +- +- +- +- +-
#     +- +- +- +- +- +- 03 +- 01
#     +- +- +- +- +- +- +- +- +-
#     +- +- +- +- 01 +- +- +- +-
#     """





# @staticmethod
# def lighthouses_020():
#     return f"""
#     020.lighthouses
#     9
#     +- 03 +- +- +- +- +- +- 04
#     +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- 04
#     +- +- +- 02 +- +- +- +- +-
#     01 +- +- +- +- +- +- +- +-
#     +- +- 01 +- 01 +- +- +- +-
#     +- +- +- +- +- +- +- +- +-
#     +- 01 +- +- +- +- +- +- +-
#     +- +- +- +- +- 01 +- +- +-
#     """





# @staticmethod
# def lighthouses_021():
#     return f"""
#     021.lighthouses
#     9
#     03 +- +- +- +- +- +- +- 02
#     +- +- +- +- +- +- 01 +- +-
#     +- +- +- +- +- +- +- +- 02
#     +- +- 02 +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- 01
#     +- +- +- +- +- +- +- +- +-
#     +- +- +- 03 +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +-
#     +- 02 +- 01 +- +- +- +- 01
#     """




# @staticmethod
# def lighthouses_022():
#     return f"""
#     022.lighthouses
#     9
#     02 +- +- +- 01 +- +- +- +-
#     +- +- 03 +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +-
#     02 +- +- +- +- +- +- 01 +-
#     +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- 02
#     +- +- 04 +- +- +- +- +- +-
#     +- +- +- +- +- +- +- 00 +-
#     """


# @staticmethod
# def lighthouses_023():
#     return f"""
#     023.lighthouses
#     9
#     +- +- +- +- +- +- +- +- +-
#     +- +- 03 +- 04 +- +- +- +-
#     +- +- +- +- +- +- +- +- +-
#     +- +- 01 +- +- +- +- +- +-
#     +- +- +- +- 03+ - +- +- +-
#     +- +- +- +- +- +- +- +- +-
#     04 +- +- +- +- +- +- +- 03
#     +- +- +- +- +- +- +- +- +-
#     +- 1+- +- +- +- +- 03 +-
#     """


# @staticmethod
# def lighthouses_024():
#     return f"""
#     024.lighthouses
#     9
#     02 +- +- +- +- +- +- +- 03
#     +- +- +- +- +- +- 03 +- +-
#     +- +- +- +- 04 +- +- +- +-
#     +- +- +- +- +- +- +- +- +-
#     01 +- +- +- +- +- +- +- +-
#     +- +- 03 +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +-
#     +- +- +- 02 +- 02 +- +- +-
#     +- +- +- +- +- +- +- +- +-
#     """






# @staticmethod
# def lighthouses_025():
#     return f"""
#     025.lighthouses
#     9
#     02 +- +- +- +- 01 +- +- +-
#     +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- 02 +-
#     +- +- +- +- +- 01 +- +- +-
#     +- +- +- +- +- +- +- +- 02
#     +- +- +- +- +- +- 01 +- +-
#     +- +- 01 +- 00 +- +- +- +-
#     +- +- +- +- +- +- +- +- +-
#     +- 01 +- 01 +- +- +- +- +-
#     """


# @staticmethod
# def lighthouses_026():
#     return f"""
#     026.lighthouses
#     10
#     +- +- +- +- +- +- +- +- +- 01
#     +- +- +- +- +- +- 01 +- +- +-
#     02 +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- 02 +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- 01
#     +- +- +- 03 +- +- +- 03 +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     01 +- 02 +- 03 +- +- 02 +- +-
#     """




# @staticmethod
# def lighthouses_027():
#     return f"""
#     027.lighthouses
#     10
#     +- +- +- +- +- +- +- 02 +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- 03 +- +- +- +- +- 01 +- 00
#     +- +- +- +- +- 02 +- +- +- +-
#     +- +- +- +- +- +- +- +- 02 +-
#     +- +- +- 02 +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- 02 +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- 00 +- +- +-
#     """

# @staticmethod
# def lighthouses_028():
#     return f"""
#     028.lighthouses
#     10
#     +- +- +- +- 01 +- +- +- +- +-
#     01 +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- 02 +- +- +- 01
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- 04 +- +- 02 +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- +- 01 +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- 02
#     00 +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- 03 +- +-
#     """


# @staticmethod
# def lighthouses_029():
#     return f"""
#     029.lighthouses
#     10
#     03 +- +- +- +- +- +- +- 05 +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- 01 +- +- +- +- +-
#     02 +- 01 +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- 01
#     02 +- +- +- +- 04 +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- +- 03 +- +- +- +- +- +-
#     """

# @staticmethod
# def lighthouses_030():
#     return f"""
#     030.lighthouses
#     10
#     +- +- 06 +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     02 +- +- +- +- +- +- +- 02 +-
#     +- +- +- 01 +- +- +- +- +- +-
#     +- +- +- +- +- 06 +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- 02 +- +- +- +- +- 03 +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- 02 +- +- +- +- +-
#     """


# @staticmethod
# def lighthouses_031():
#     return f"""
#     031.lighthouses
#     10
#     +- +- +- +- +- +- +- +- +- 03
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- 02 +- +- +- +-
#     +- +- +- 04 +- +- +- 00 +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- 04 +- +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- 03 +- 03 +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     01 +- +- +- +- +- +- +- +- +-
#     """


# @staticmethod
# def lighthouses_032():
#     return f"""
#     032.lighthouses
#     11
#     +- +- 01 +- 02 +- +- +- 01 +- +-
#     04 +- +- +- +- +- +- +- +- +- +-
#     +- +- 02 +- +- +- +- +- +- +- +-
#     02 +- +- +- +- +- +- +- +- +- +-
#     +- +- 02 +- 03 +- 02 +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- 02 +- +- +- +- 03
#     +- +- +- +- +- +- +- +- +- +- +-
#     +- +- 02 +- +- +- +- +- +- +- +-
#     02 +- +- +- +- +- +- +- +- +- +-
#     +- +- 03 +- +- +- +- 04 +- +- +-
#     """

# @staticmethod
# def lighthouses_033():
#     return f"""
#     033.lighthouses
#     11
#     +- +- +- +- +- +- +- +- +- +- 00
#     +- +- +- +- +- +- +- 02 +- +- +-
#     01 +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +- 03
#     +- +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- 01 +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +- 03
#     +- +- +- +- +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- 03 +-
#     +- +- 02 +- 03 +- +- +- +- +- +-
#     """







