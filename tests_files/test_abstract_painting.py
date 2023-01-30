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
#     ('abstractpainting_001', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_002', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_003', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_004', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_005', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_006', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_007', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_009', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_011', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_015', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_016', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_017', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_018', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_019', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_025', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_027', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_028', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_029', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_030', AbstractPainting, Solving.abstractpainting_techniques()),
#     ('abstractpainting_036', AbstractPainting, Solving.abstractpainting_techniques()),
#
#
#
# ])
# def test_default_puzzle(puzzle_string, constructor, techniques):
#     if "\n" in puzzle_string:
#         pytest.skip(puzzle_string)
#     result = getattr(Constants, puzzle_string)
#     assert default_test_puzzle(result(), constructor, techniques)















# @staticmethod
# def abstractpainting_001():
#     return f"""
#     001.abstractpainting
#     4
#     10a 10b 10b 10b 03
#     10a 10a 10b 10b 02
#     10c 10c 10c 10c 04
#     10d 10d 10c 10c 02
#     01   02   04   04   $
#     """

# @staticmethod
# def abstractpainting_002():
#     return f"""
#     002.abstractpainting
#     4
#     10a 10a 10e 10e 02
#     10b 10a 10e 10e 03
#     10b 10b 10b 10d 04
#     10b 10c 10c 10d 02
#     03 01 03 04 $$
#     """




# @staticmethod
# def abstractpainting_003():
#     return f"""
#     003.abstractpainting
#     4
#     10a 10a 10a 10b 3
#     10a 10a 10a 10b 3
#     10c 10c 10d 10d 2
#     10c 10c 10d 10d 2
#     2 2 4 2        $
#     """



# @staticmethod
# def abstractpainting_004():
#     return f"""
#     004.abstractpainting
#     4
#     10a 10a 10c 10c 2
#     10a 10a 10c 10c 2
#     10b 10a 10c 10d ?
#     10b 10b 10b 10d 3
#     2 1 4 2 $
#     """


# @staticmethod
# def abstractpainting_005():
#     return f"""
#     005.abstractpainting
#     4
#     10a 10c 10d 10d 3
#     10a 10c 10d 10d 3
#     10a 10d 10d 10e ?
#     10b 10b 10e 10e 2
#     1 4 3 2 $
#     """


# @staticmethod
# def abstractpainting_006():
#     return f"""
#     006.abstractpainting
#     4
#     10a 10a 10d 10d 4
#     10a 10a 10d 10d 4
#     10b 10a 10d 10e 3
#     10b 10c 10c 10e 1
#     4 ? 3 2 $
#     """




# @staticmethod
# def abstractpainting_007():
#     return f"""
#     007.abstractpainting
#     4
#     10a 10a 10e 10e 2
#     10a 10a 10d 10e 3
#     10b 10b 10d 10d 2
#     10c 10c 10d 10d 4
#     3 ? 3 2             $$
        
        
        
        
#     """


# @staticmethod
# def abstractpainting_008():
#     return f"""
#     008.abstractpainting
#     4
#     10a 10a 10a 10e 4
#     10a 10a 10a 10e 4
#     10b 10b 10b 10e 1
#     10c 10c 10d 10d ?
#     3 3 2 3          $
#     """




# @staticmethod
# def abstractpainting_009():
#     return f"""
#     009.abstractpainting
#     4
#     10a 10e 10e 10e 1
#     10a 10d 10d 10d 4
#     10a 10a 10c 10c 4
#     10b 10b 10c 10c ?
#     3 2 3 3
#     """











# @staticmethod
# def abstractpainting_018():
#     return f"""
#     018.abstractpainting
#     5
#     10a 10a 10e 10f 10f 4
#     10a 10a 10e 10f 10f 4
#     10b 10b 10b 10f 10f 2
#     10b 10b 10d 10d 10d ?
#     10c 10c 10d 10d 10d 3
#     2 2 2 5 5 $
#     """

# @staticmethod
# def abstractpainting_019():
#     return f"""
#     019.abstractpainting
#     5
#     10a 10a 10a 10a 10a 5
#     10b 10b 10b 10f 10f 2
#     10c 10c 10b 10f 10f ?
#     10d 10e 10e 10f 10g 4
#     10d 10d 10e 10g 10g 3
#     1 2 3 5 5 $
#     """

# @staticmethod
# def abstractpainting_025():
#     return f"""
#     025.abstractpainting
#     5
#     10a 10a 10f 10f 10f 2
#     10b 10a 10d 10f 10f ?
#     10b 10a 10d 10d 10d 5
#     10b 10b 10c 10d 10e 3
#     10b 10c 10c 10e 10e 1
#     5 4 ? 2 1 $
#     """

# @staticmethod
# def abstractpainting_027():
#     return f"""
#     027.abstractpainting
#     5
#     10a 10a 10d 10d 10d 3
#     10a 10b 10d 10d 10d 4
#     10b 10b 10c 10e 10e 4
#     10b 10c 10c 10e 10f ?
#     10b 10c 10c 10e 10f ?
#     3 2 2 5 3 $
#     """

# @staticmethod
# def abstractpainting_028():
#     return f"""
#     028.abstractpainting
#     5
#     10a 10a 10a 10e 10f 4
#     10a 10b 10b 10e 10f ?
#     10b 10b 10c 10e 10e 3
#     10b 10c 10c 10e 10e 4
#     10b 10c 10d 10d 10d 4
#     2 3 4 5 ? $
#     """

# @staticmethod
# def abstractpainting_029():
#     return f"""
#     029.abstractpainting
#     5
#     10a 10a 10a 10a 10c 4
#     10b 10b 10a 10a 10c 2
#     10d 10f 10f 10f 10g 1
#     10d 10d 10f 10f 10g ?
#     10d 10e 10e 10e 10e 5
#     ? 3 3 3 1 $
#     """

# @staticmethod
# def abstractpainting_030():
#     return f"""
#     030.abstractpainting
#     5
#     10a 10a 10a 10f 10f ?
#     10a 10a 10f 10f 10f 5
#     10a 10c 10d 10d 10e 2
#     10b 10c 10d 10d 10e 1
#     10b 10b 10b 10d 10e 1
#     3 2 ? 2 5 $
#     """

# @staticmethod
# def abstractpainting_031():
#     return f"""
#     031.abstractpainting
#     6
#     10a 10a 10b 10d 10d 10d 4
#     10b 10b 10b 10e 10e 10k 3
#     10c 10b 10i 10j 10j 10k ?
#     10c 10b 10i 10j 10j 10k ?
#     10f 10f 10f 10f 10h 10h 4
#     10f 10f 10g 10g 10h 10h ?
#     3 5 3 4 3 1     $
#     """








# @staticmethod
# def abstractpainting_010():
#     return f"""
#     010.abstractpainting
#     4
#     10a 10a 10c 10c 2
#     10b 10a 10a 10e 3
#     10b 10b 10e 10e 2
#     10d 10d 10e 10e 2
#     ? 2 3 3 $
#     """








# @staticmethod
# def abstractpainting_011():
#     return f"""
#     011.abstractpainting
#     5
#     10a 10a 10g 10g 10g 5
#     10b 10b 10g 10h 10h 1
#     10b 10b 10b 10e 10e 2
#     10c 10d 10e 10e 10f 4
#     10c 10d 10e 10e 10f 4
#     1 3 4 4 ? $
#     """







# @staticmethod
# def abstractpainting_012():
#     return f"""
#     012.abstractpainting
#     5
#     10a 10a 10a 10g 10g 5
#     10a 10a 10a 10g 10g 5
#     10b 10b 10e 10e 10g 1
#     10c 10c 10d 10e 10f 2
#     10c 10c 10d 10e 10f 2
#     4 4 2 2  ? $
#     """

    




# @staticmethod
# def abstractpainting_013():
#     return f"""
#     013.abstractpainting
#     5
#     10a 10c 10c 10c 10d 4
#     10a 10a 10a 10c 10d 4
#     10a 10a 10f 10f 10f 5
#     10b 10b 10e 10e 10f 1
#     10b 10b 10b 10e 10f ?
#     3 3 3 3 3          $
#     """


# @staticmethod
# def abstractpainting_014():
#     return f"""
#     014.abstractpainting
#     5
#     10a 10a 10a 10g 10g 5
#     10b 10a 10a 10g 10g 5
#     10b 10e 10e 10f 10f 3
#     10b 10b 10c 10d 10d 2
#     10b 10b 10c 10c 10c 2
#     5 4 ? 3 3 $
#     """



# @staticmethod
# def abstractpainting_015():
#     return f"""
#     015.abstractpainting
#     5
#     10a 10e 10e 10g 10g 2
#     10a 10e 10e 10e 10f 3
#     10a 10e 10f 10f 10f 1
#     10a 10b 10b 10d 10d 4
#     10b 10b 10c 10c 10d 3
#     1 ? 3 2 2 $
#     """


# @staticmethod
# def abstractpainting_016():
#     return f"""
#     016.abstractpainting
#     5
#     10a 10a 10e 10e 10f 2
#     10a 10a 10e 10e 10f ?
#     10a 10b 10c 10c 10f 2
#     10b 10b 10c 10c 10d 3
#     10b 10b 10d 10d 10d 5
#     5 5 1 1 2 $
#     """


# @staticmethod
# def abstractpainting_017():
#     return f"""
#     017.abstractpainting
#     5
#     10a 10a 10e 10e 10e 2
#     10a 10a 10a 10e 10e ?
#     10a 10b 10d 10d 10d 5
#     10b 10b 10c 10c 10d 3
#     10b 10b 10c 10c 10d 3
#     5 5 2 1 3    $
#     """










# @staticmethod
# def abstractpainting_035():
#     return f"""
#     035.abstractpainting
#     6
#     10a 10a 10b 10b 10c 10c 4
#     10a 10a 10b 10b 10h 10h 2
#     10a 10d 10d 10h 10h 10i 4
#     10a 10d 10d 10h 10i 10i 5
#     10e 10e 10f 10g 10i 10i 3
#     10e 10f 10f 10g 10g 10g 3
#     4 4 ? ? 4 ?     $
#     """



# @staticmethod
# def abstractpainting_036():
#     return f"""
#     036.abstractpainting
#     6
#     10a 10a 10b 10b 10c 10c ?
#     10a 10b 10b 10b 10c 10c 5
#     10d 10e 10f 10g 10g 10g 1
#     10d 10e 10f 10f 10g 10h ?
#     10d 10e 10f 10h 10g 10h 3
#     10e 10e 10e 10h 10h 10h 6
#     1 5 3 4 3 ?     $
#     """



# @staticmethod
# def abstractpainting_051():
#     return f"""
#     051.abstractpainting
#     7
#     10a 10a 10a 10a 10f 10g 10g 6
#     10a 10a 10f 10f 10f 10g 10g 4
#     10b 10d 10d 10e 10f 10g 10h 3
#     10b 10b 10d 10e 10h 10h 10h 5
#     10b 10e 10e 10e 10i 10j 10j 2
#     10b 10c 10c 10i 10i 10j 10j ?
#     10c 10c 10i 10i 10i 10j 10j 3
#     ? 3 ? 3 ? 4 ?      $
#     """




# @staticmethod
# def abstractpainting_101():
#     return f"""
#     101.abstractpainting
#     8
#     10a 10b 10h 10h 10h 10h 10l 10l 4
#     10a 10b 10h 10h 10h 10l 10l 10l ?
#     10b 10b 10g 10g 10i 10l 10m 10n 1
#     10b 10b 10b 10i 10i 10l 10m 10n ?
#     10c 10c 10c 10i 10j 10j 10k 10k 5
#     10d 10c 10i 10i 10j 10k 10k 10k ?
#     10d 10c 10f 10f 10f 10k 10j 10j 7
#     10d 10e 10e 10e 10j 10j 10j 10j ?
#     4 ? ? 4 ? 3 2 ?       $
#     """


# @staticmethod
# def abstractpainting_151():
#     return f"""
#     151.abstractpainting
#     9
#     10a 10l 10l 10n 10o 10o 10p 10p 10t 5
#     10a 10a 10m 10n 10p 10p 10p 10p 10t ?
#     10a 10a 10m 10m 10q 10q 10r 10r 10t ?
#     10b 10b 10f 10f 10q 10q 10r 10r 10s 4
#     10b 10c 10c 10f 10f 10f 10i 10r 10s 6
#     10b 10c 10c 10e 10e 10h 10i 10k 10k 3
#     10b 10c 10e 10e 10g 10h 10i 10j 10j 4
#     10b 10c 10d 10d 10g 10h 10i 10i 10j ?
#     10d 10d 10d 10d 10h 10h 10i 10j 10j ?
#     ? 7 5 4 ? 7 ? ? ?       $
#     """

# @staticmethod
# def abstractpainting_191():
#     return f"""
#     191.abstractpainting
#     10
#     10a 10i 10i 10i 10i 10p 10s 10s 10s 10s ?
#     10a 10i 10i 10j 10j 10p 10r 10r 10r 10r 6
#     10b 10b 10k 10k 10m 10p 10p 10p 10r 10r ?
#     10b 10b 10k 10l 10m 10m 10p 10p 10q 10q ?
#     10c 10b 10l 10l 10m 10m 10m 10m 10q 10q 9
#     10c 10b 10l 10l 10n 10n 10n 10o 10o 10q ?
#     10d 10e 10l 10l 10n 10n 10o 10o 10o 10o ?
#     10d 10e 10e 10e 10f 10g 10g 10g 10h 10h ?
#     10d 10d 10e 10f 10f 10f 10g 10g 10h 10h 4
#     10d 10d 10e 10f 10f 10f 10g 10g 10h 10h ?
#     6 4 ? 5 ? 5 ? ? 4 ?         $
#     """




























