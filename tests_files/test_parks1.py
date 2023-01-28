import pytest

from Constants import Constants
from _defaults import default_test_puzzle
from puzzles import *
from solving import Solving

# from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# from techniques.LockedCandidatesPointing import LockedCandidatesPointing

EXPLICITLY = "EXPLICITLY"


@pytest.mark.parametrize("puzzle_string, constructor, techniques", [


   
    ('parks1_001', Parks1, Solving.parks1_techniques()),
    ('parks1_002', Parks1, Solving.parks1_techniques()),
    ('parks1_003', Parks1, Solving.parks1_techniques()),
    ('parks1_006', Parks1, Solving.parks1_techniques()),
    ('parks1_007', Parks1, Solving.parks1_techniques()),
    ('parks1_008', Parks1, Solving.parks1_techniques()),
    ('parks1_beach_001', Parks1, Solving.parks1_techniques()),
    ('parks1_beach_002', Parks1, Solving.parks1_techniques()),
    ('parks1_beach_003', Parks1, Solving.parks1_techniques()),
    ('parks1_beach_004', Parks1, Solving.parks1_techniques()),
    ('parks1_maui_001', Parks1, Solving.parks1_techniques()),
    ('parks1_spring_001', Parks1, Solving.parks1_techniques()),
    ('parks1_spring_002', Parks1, Solving.parks1_techniques()),
    ('parks1_spring_003', Parks1, Solving.parks1_techniques()),
    ('parks1_spring_004', Parks1, Solving.parks1_techniques()),
    ('parks1_spring_005', Parks1, Solving.parks1_techniques()),
    ('parks1_spring_006', Parks1, Solving.parks1_techniques()),
    ('parks1_spring_007', Parks1, Solving.parks1_techniques()),
    ('parks1_spring_008', Parks1, Solving.parks1_techniques()),

    
    ("parks1_011", Parks1, Solving.parks1_techniques()),
    ("parks1_012", Parks1, Solving.parks1_techniques()),
    ("parks1_013", Parks1, Solving.parks1_techniques()),
    ("parks1_014", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_009", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_010", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_011", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_012", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_013", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_014", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_015", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_017", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_018", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_019", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_020", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_021", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_022", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_023", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_024", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_025", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_026", Parks1, Solving.parks1_techniques()),
    ('parks1_005', Parks1, Solving.parks1_techniques()),
    ("parks1_spring_028", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_029", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_030", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_031", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_032", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_033", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_034", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_039", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_045", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_047", Parks1, Solving.parks1_techniques()),
    ("parks1_spring_062", Parks1, Solving.parks1_techniques()),
    ("parks1_winter_049", Parks1, Solving.parks1_techniques()),


])
def test_default_puzzle(puzzle_string, constructor, techniques):
    if "\n" in puzzle_string:
        pytest.skip(puzzle_string)
    result = getattr(Constants, puzzle_string)
    assert default_test_puzzle(result(), constructor, techniques)