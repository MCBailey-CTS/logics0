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

  
    ('robot_fences_001', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_002', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_003', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_004', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_005', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_006', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_007', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_008', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_009', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_010', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_011', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_012', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_013', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_014', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_015', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_016', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_017', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_018', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_019', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_020', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_022', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_023', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_025', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_028', RobotFences, Solving.robot_fences_techniques()),
    ('robot_fences_030', RobotFences, Solving.robot_fences_techniques()),
    

])
def test_default_puzzle(puzzle_string, constructor, techniques):
    if "\n" in puzzle_string:
        pytest.skip(puzzle_string)
    result = getattr(Constants, puzzle_string)
    assert default_test_puzzle(result(), constructor, techniques)