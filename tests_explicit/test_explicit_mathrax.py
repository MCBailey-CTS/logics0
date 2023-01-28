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

@pytest.mark.parametrize("constructor, technique, actual, expected", [



    (Mathrax,
     CrossHatch(),
     Constants.mathrax_cross_hatch_actual.__name__,
     Constants.mathrax_cross_hatch_expected.__name__),
    (Mathrax,
     tech.MathraxMathSubtraction(),
     Constants.mathrax_01minus_actual.__name__,
     Constants.mathrax_01minus_expected.__name__),
    (Mathrax,
     tech.MathraxMath04XWing(),
     Constants.mathrax_04plus_actual.__name__,
     Constants.mathrax_04plus_expected.__name__),
    (Mathrax,
     tech.MathraxMathMultiplication(),
     Constants.mathrax_06x04x_actual.__name__,
     Constants.mathrax_06x04x_expected.__name__),
])
def test_default_actual_expected(constructor, technique, actual, expected):
    if "\n" in actual or "\n" in expected:
        pytest.skip('Explicitly')
    assert default_test_explicit_actual_expected(constructor, technique, getattr(Constants, actual)(),
                                                 getattr(Constants, expected)())
