
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

@pytest.mark.parametrize("puzzle_string, constructor, techniques", [

   
    (Constants.kropki_001.__name__, Kropki, [
        tech.KropkiBlack(),
        tech.KropkiWhite(),
        tech.KropkiEmpty(),
        CrossHatch(),
        tech.KropkiBw(),
    ]),
    (Constants.kropki_002.__name__, Kropki, [
        tech.KropkiBlack(),
        tech.KropkiWhite(),
        tech.KropkiEmpty(),
        CrossHatch(),
        tech.KropkiBw(),
    ]),
    (Constants.kropki_003.__name__, Kropki,
     [
         tech.KropkiBlack(),
         tech.KropkiWhite(),
         tech.KropkiEmpty(),
         CrossHatch(),
         tech.KropkiBw(),
     ]
     ),
    # (Constants.kropki_004.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_005.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_006.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_007.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_008.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_009.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_010.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_011.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_012.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_013.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_014.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_015.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_016.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_017.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_018.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_019.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_020.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_021.__name__, Kropki, Solving.kropki_techniques()),
    # (Constants.kropki_022.__name__, Kropki, Solving.kropki_techniques()),
])
def test_default_puzzle(puzzle_string, constructor, techniques):
    if "\n" in puzzle_string:
        pytest.skip(puzzle_string)
    result = getattr(Constants, puzzle_string)
    assert default_test_puzzle(result(), constructor, techniques)