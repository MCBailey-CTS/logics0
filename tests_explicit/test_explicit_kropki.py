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

    (Kropki,
     tech.KropkiBlack(),
     Constants.kropki_explicit_black_actual.__name__,
     Constants.kropki_explicit_black_expected.__name__),
    (Kropki,
     tech.KropkiWhite(),
     Constants.kropki_explicit_white_actual.__name__,
     Constants.kropki_explicit_white_expected.__name__),
    (Kropki,
     tech.KropkiEmpty(),
     Constants.kropki_explicit_empty_actual.__name__,
     Constants.kropki_explicit_empty_expected.__name__),
    (Kropki,
     tech.KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty1_actual.__name__,
     Constants.kropki_explicit_dominating_empty1_expected.__name__),
    (Kropki,
     tech.KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty3_actual.__name__,
     Constants.kropki_explicit_dominating_empty3_expected.__name__),
    (Kropki,
     tech.KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty4_actual.__name__,
     Constants.kropki_explicit_dominating_empty4_expected.__name__),
    (Kropki,
     tech.KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty5_actual.__name__,
     Constants.kropki_explicit_dominating_empty5_expected.__name__),
    (Kropki,
     tech.KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty6_actual.__name__,
     Constants.kropki_explicit_dominating_empty6_expected.__name__),
    (Kropki,
     tech.KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty7_actual.__name__,
     Constants.kropki_explicit_dominating_empty7_expected.__name__),
    (Kropki,
     tech.KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty8_actual.__name__,
     Constants.kropki_explicit_dominating_empty8_expected.__name__),
    (Kropki,
     tech.KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty9_actual.__name__,
     Constants.kropki_explicit_dominating_empty9_expected.__name__),
    (Kropki,
     tech.KropkiDiamondWwwe(),
     Constants.kropki_explicit_diamond_wwwe_actual.__name__,
     Constants.kropki_explicit_diamond_wwwe_expected.__name__),

   
])
def test_default_actual_expected(constructor, technique, actual, expected):
    if "\n" in actual or "\n" in expected:
        pytest.skip('Explicitly')
    assert default_test_explicit_actual_expected(constructor, technique, getattr(Constants, actual)(),
                                                 getattr(Constants, expected)())
