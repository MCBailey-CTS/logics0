import pytest

from Constants import Constants
from _defaults import default_test_puzzle
from puzzles import *
from solving import Solving

# from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# from techniques.LockedCandidatesPointing import LockedCandidatesPointing

EXPLICITLY = "EXPLICITLY"


@pytest.mark.parametrize("puzzle_string, constructor, techniques", [


    ('tenner_easier_002', Tenner, Solving.tenner_techniques()),
    ('tenner_easier_003', Tenner, Solving.tenner_techniques()),
    ('tenner_easier_004', Tenner, Solving.tenner_techniques()),
    ('tenner_001', Tenner, Solving.tenner_techniques()),
    ('tenner_002', Tenner, Solving.tenner_techniques()),
    ('tenner_003', Tenner, Solving.tenner_techniques()),
    ('tenner_004', Tenner, Solving.tenner_techniques()),
    ('tenner_005', Tenner, Solving.tenner_techniques()),
    ('tenner_006', Tenner, Solving.tenner_techniques()),
    ('tenner_008', Tenner, Solving.tenner_techniques()),
    ('tenner_009', Tenner, Solving.tenner_techniques()),
    ('tenner_019', Tenner, Solving.tenner_techniques()),
    ('tenner_easier_001', Tenner, Solving.tenner_techniques()),


])
def test_default_puzzle(puzzle_string, constructor, techniques):
    # if "\n" in puzzle_string:
    #     pytest.skip(puzzle_string)
    result = getattr(Constants, puzzle_string)
    # puzzle = Tenner(puzzle_string)
    if default_test_puzzle(result(), constructor, techniques):
        return
    assert False

#
# def test_tenner_004():
#     if default_test_puzzle(
#             f"""
#             0_________ 0123456789 _____5____ 0123456789 0123456789 0123456789 _1________ 0123456789 _________9 __2_______
#             ________8_ _1________ 0_________ 0123456789 _______7__ _________9 _____5____ 0123456789 0123456789 ______6___
#             _________9 0123456789 ________8_ _1________ 0123456789 0123456789 0123456789 0123456789 _____5____ 0123456789
#             17         08        13          07         16         23         06         13         17         15
#             """,
#             Tenner,
#             Solving.tenner_techniques()):
#         return
#     assert False
