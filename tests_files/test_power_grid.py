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
#     ('power_grid_001', PowerGrid, Solving.power_grid_techniques()),
#     ('power_grid_002', PowerGrid, Solving.power_grid_techniques()),
#     ('power_grid_003', PowerGrid, Solving.power_grid_techniques()),
#     ('power_grid_004', PowerGrid, Solving.power_grid_techniques()),
#     ('power_grid_005', PowerGrid, Solving.power_grid_techniques()),
#     ('power_grid_006', PowerGrid, Solving.power_grid_techniques()),
#     ('power_grid_011', PowerGrid, Solving.power_grid_techniques()),
#     ('power_grid_012', PowerGrid, Solving.power_grid_techniques()),
#     ('power_grid_013', PowerGrid, Solving.power_grid_techniques()),
#     ('power_grid_014', PowerGrid, Solving.power_grid_techniques()),
#
#
# ])
# def test_default_puzzle(puzzle_string, constructor, techniques):
#     if "\n" in puzzle_string:
#         pytest.skip(puzzle_string)
#     result = getattr(Constants, puzzle_string)
#     assert default_test_puzzle(result(), constructor, techniques)



# @staticmethod
# def power_grid_001():
#     return f"""
#     001.power_grid
#     9
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 02
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     05 01 06 01 05 05 01 06 01 $$
#     """

# @staticmethod
# def power_grid_002():
#     return f"""
#     002.power_grid
#     9
#     10 10 10 10 10 10 10 10 10 03
#     10 10 10 10 10 10 10 10 10 04
#     10 10 10 10 10 10 10 10 10 05
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     04 03 03 07 01 05 01 06 01 $$     
#     """

# @staticmethod
# def power_grid_003():
#     return f"""
#     003.power_grid
#     9
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 03
#     10 10 10 10 10 10 10 10 10 04
#     04 03 03 03 04 04 04 03 03 $$
#     diagonal        
#     """

# @staticmethod
# def power_grid_004():
#     return f"""
#             004.power_grid
#             9
#             10 10 10 10 10 10 10 10 10 03
#             10 10 10 10 10 10 10 10 10 03
#             10 10 10 10 10 10 10 10 10 05
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 06
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 06
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 05
#             01 01 02 01 01 01 01 03 04 $$     
#             """

# @staticmethod
# def power_grid_005():
#     return f"""
#             005.power_grid
#             9
#             10 10 10 10 10 10 10 10 10 06
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 05
#             10 10 10 10 10 10 10 10 10 04
#             10 10 10 10 10 10 10 10 10 03
#             10 10 10 10 10 10 10 10 10 03
#             10 10 10 10 10 10 10 10 10 03
#             02 06 01 01 01 01 01 01 03 $$
#             diagonal     
#             """

# @staticmethod
# def power_grid_006():
#     return f"""
#             006.power_grid
#             9
#             10 10 10 10 10 10 10 10 10 05
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 02
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 02
#             03 03 01 01 06 01 05 01 06 $$      
#             """

# @staticmethod
# def power_grid_007():
#     return f"""
#             007.power_grid
#             9
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 05
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 06
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 02
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             01 01 01 01 01 01 03 04 04 $$     
#             """

# @staticmethod
# def power_grid_008():
#     return f"""
#             008.power_grid
#             9
#             10 10 10 10 10 10 10 10 10 02
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 06
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 05
#             01 01 01 01 01 01 03 03 03 $$     
#             diagonal
#             """

# @staticmethod
# def power_grid_009():
#     return f"""
#             009.power_grid
#             9
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 01
#             10 10 10 10 10 10 10 10 10 05
#             10 10 10 10 10 10 10 10 10 03
#             10 10 10 10 10 10 10 10 10 01
#             02 01 01 01 01 01 02 01 01 $$        
#             """

# @staticmethod
# def power_grid_010():
#     return f"""
#     010.power_grid
#     9
#     10 10 10 10 10 10 10 10 10 02
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 02
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     01 01 01 01 01 01 03 05 01 $$
#     """

# @staticmethod
# def power_grid_011():
#     return f"""
#     011.power_grid
#     9
#     10 10 10 10 10 10 10 10 10 ??
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 05
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 ??
#     10 10 10 10 10 10 10 10 10 05
#     10 10 10 10 10 10 10 10 10 05
#     06 01 06 01 05 01 01 01 01 $$
#     """

# @staticmethod
# def power_grid_012():
#     return f"""
#     012.power_grid
#     9
#     10 10 10 10 10 10 10 10 10 03
#     10 10 10 10 10 10 10 10 10 04
#     10 10 10 10 10 10 10 10 10 05
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 05
#     03 ?? 01 05 01 ?? 01 01 02 $$
#     """

# @staticmethod
# def power_grid_013():
#     return f"""
#     013.power_grid
#     9
#     10 10 10 10 10 10 10 10 10 05
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 02
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 02
#     03 03 ?? 01 06 ?? 05 01 06 $$
#     diagonel
#     """

# @staticmethod
# def power_grid_014():
#     return f"""
#     014.power_grid
#     9
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 ??
#     10 10 10 10 10 10 10 10 10 05
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 03
#     10 10 10 10 10 10 10 10 10 03
#     05 01 01 ?? 01 01 02 01 02 $$
#     diagonel
#     """

# @staticmethod
# def power_grid_015():
#     return f"""
#     015.power_grid
#     9
#     10 10 10 10 10 10 10 10 10 02
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 ??
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 02
#     ?? 01 01 01 03 03 03 01 01 $$
#     """

# @staticmethod
# def power_grid_016():
#     return f"""
#     016.power_grid
#     9
#     10 10 10 10 10 10 10 10 10 04
#     10 10 10 10 10 10 10 10 10 03
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 05
#     10 10 10 10 10 10 10 10 10 01
#     01 01 02 01 02 01 ?? ?? 02 $$
#     """

# @staticmethod
# def power_grid_017():
#     return f"""
#     017.power_grid
#     9
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 ??
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 ??
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 07
#     10 10 10 10 10 10 10 10 10 01
#     01 01 02 01 01 01 05 01 06 $$
#     """

# @staticmethod
# def power_grid_018():
#     return f"""
#     018.power_grid
#     9
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 02
#     10 10 10 10 10 10 10 10 10 01 
#     10 10 10 10 10 10 10 10 10 01
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 02
#     10 10 10 10 10 10 10 10 10 06
#     10 10 10 10 10 10 10 10 10 01
#     01 01 ?? 01 01 ?? 01 01 01 $$
#     """
