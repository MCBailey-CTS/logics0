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

    
    ('abstractpainting_001', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_002', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_003', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_004', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_005', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_006', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_007', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_009', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_011', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_015', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_016', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_017', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_018', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_019', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_025', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_027', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_028', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_029', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_030', AbstractPainting, Solving.abstractpainting_techniques()),
    ('abstractpainting_036', AbstractPainting, Solving.abstractpainting_techniques()),
    


])
def test_default_puzzle(puzzle_string, constructor, techniques):
    if "\n" in puzzle_string:
        pytest.skip(puzzle_string)
    result = getattr(Constants, puzzle_string)
    assert default_test_puzzle(result(), constructor, techniques)
