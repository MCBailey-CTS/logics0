
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

    # [Constants.sudoku_annoying_00.__name__, Sudoku, Solving.sudoku_techniques()],

    ('sudoku_unique_rectangle_type1_00', Sudoku,
     [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()]),
    ('sudoku_unique_rectangle_type1_01', Sudoku,
     [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()]),
    ('sudoku_unique_rectangle_type1_02', Sudoku, [CrossHatch(), NakedPair(), UniqueRectangleType1()]),
    ('sudoku_unique_rectangle_type1_03', Sudoku,
     [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()]),
    ('sudoku_unique_rectangle_type1_05', Sudoku, [CrossHatch(), NakedPair(), UniqueRectangleType1()]),
    # ('sudoku_unique_rectangle_type4_00', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    # ('sudoku_unique_rectangle_type4_01', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    # ('sudoku_unique_rectangle_type4_02', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    # ('sudoku_unique_rectangle_type4_03', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    # ('sudoku_unique_rectangle_type4_04', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    # ('sudoku_unique_rectangle_type4_05', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    # ('sudoku_unique_rectangle_type4_east_rows', Sudoku,
    #  [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    # ('sudoku_unique_rectangle_type4_west_rows', Sudoku,
    #  [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    # ('sudoku_unique_rectangle_type4_west_cols', Sudoku,
    #  [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    # ('sudoku_unique_rectangle_type4_east_cols', Sudoku,
    #  [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    # ('sudoku_naked_triple_0', Sudoku,
    #  [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), tech.NakedTriple()]),
    # ('sudoku_naked_triple_2', Sudoku, [CrossHatch(), HiddenSingle(), tech.NakedTriple()]),
    # ('sudoku_naked_triple_3', Sudoku, [CrossHatch(), NakedPair(), tech.NakedTriple()]),
    # ('sudoku_naked_triple_4', Sudoku, [CrossHatch(), HiddenSingle(), tech.NakedTriple()]),
    # ('sudoku_naked_triple_row', Sudoku, [CrossHatch(), tech.NakedTriple()]),
    # ('sudoku_naked_triple_1', Sudoku, [CrossHatch(), tech.NakedTriple()]),
    # ('sudoku_naked_triple_5', Sudoku, [CrossHatch(), tech.NakedTriple()]),
    # ('sudoku_naked_triple_6', Sudoku, [CrossHatch(), tech.NakedTriple()]),
    # (Constants.sudoku_naked_triple_9.__name__, Sudoku,
    #  [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), tech.NakedTriple()]),
    ('sudoku_bug', Sudoku, [CrossHatch(), Bug()]),
    # ('sudoku_x_wing_row', Sudoku, [CrossHatch(), tech.XWing()]),
    # ('sudoku_x_wing_col', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair(), Bug(), tech.XWing()]),
    ('sudoku_unique_rectangle_type2_00', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
    ("sudoku_unique_rectangle_type2_01", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
    ("sudoku_unique_rectangle_type2_02", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
    ("sudoku_unique_rectangle_type2_03", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
    ("sudoku_unique_rectangle_type2_04", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
    ("sudoku_unique_rectangle_type2_05", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
    ("sudoku_unique_rectangle_type2_06", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
    ("sudoku_unique_rectangle_type2_08", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
    ("sudoku_unique_rectangle_type2_09", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
    ("sudoku_unique_rectangle_type2_10", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
    ("sudoku_unique_rectangle_type2_11", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
    ("sudoku_unique_rectangle_type2_12", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
    ('sudoku_intricate_0', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
    ('sudoku_intricate_1', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
    ('sudoku_intricate_2', Sudoku, [CrossHatch(), LockedCandidatesClaiming()]),
    ('sudoku_intricate_3', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
    ('sudoku_intricate_4', Sudoku, [CrossHatch(), LockedCandidatesPointing()]),
    ('sudoku_intricate_5', Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesPointing()]),
    ('sudoku_intricate_6', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
    ('sudoku_intricate_7', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
    ('sudoku_intricate_8', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
    ('sudoku_locked_candidates_claiming_0', Sudoku,
     [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()]),
    ('sudoku_locked_candidates_claiming_1', Sudoku,
     [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()]),
    ('sudoku_locked_candidates_claiming_2', Sudoku,
     [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()]),
    ('sudoku_locked_candidates_pointing_0', Sudoku,
     [CrossHatch(), HiddenSingle(), LockedCandidatesPointing()]),
    ('sudoku_easiest_0', Sudoku, [CrossHatch()]),
    ('sudoku_easy_as_pie_0', Sudoku, [CrossHatch()]),
    ('sudoku_first_lesson', Sudoku, [CrossHatch()]),
    ('sudoku_hidden_single_0', Sudoku, [CrossHatch(), HiddenSingle()]),
    ('sudoku_hidden_single_1', Sudoku, [CrossHatch(), HiddenSingle()]),
    ('sudoku_hidden_single_2', Sudoku, [CrossHatch(), HiddenSingle()]),
    ('sudoku_mild_0', Sudoku, [CrossHatch()]),
    ('sudoku_mild_1', Sudoku, [CrossHatch()]),
    ('sudoku_mild_2', Sudoku, [CrossHatch()]),
    ('sudoku_mild_3', Sudoku, [CrossHatch()]),
    ('sudoku_mild_4', Sudoku, [CrossHatch()]),
    ('sudoku_moderate_0', Sudoku, [CrossHatch(), NakedPair()]),
    ('sudoku_naked_pair_0', Sudoku, [CrossHatch(), NakedPair(), ]),
    ('sudoku_naked_pair_1', Sudoku, [CrossHatch(), NakedPair()]),
    ('sudoku_naked_pair_2', Sudoku, [CrossHatch(), NakedPair()]),
    ('sudoku_picnic_0', Sudoku, [CrossHatch(), ]),
    ('sudoku_picnic_1', Sudoku, [CrossHatch()]),
    ('sudoku_picnic_2', Sudoku, [CrossHatch()]),
    ('sudoku_second_lesson_0', Sudoku, [CrossHatch(), ]),
    ('sudoku_simple_0', Sudoku, [CrossHatch()]),
    
    ['sudoku_difficult_00', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
    ['sudoku_difficult_03', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
    ['sudoku_difficult_06', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
    ['sudoku_difficult_10', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
    # ['sudoku_difficult_12', Sudoku,
    #  [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), tech.NakedTriple()]],
    ['sudoku_difficult_13', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
    ['sudoku_difficult_18', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
    ['sudoku_difficult_19', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
    # ['sudoku_difficult_22', Sudoku, [CrossHatch(), HiddenSingle(), tech.XWing()]],
    ['sudoku_difficult_23', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
    ['sudoku_difficult_24', Sudoku,
     [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()]],
    # ['sudoku_difficult_25', Sudoku, [CrossHatch(), LockedCandidatesClaiming(), tech.NakedTriple()]],
    # ['sudoku_difficult_26', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]],
    ['sudoku_difficult_27', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
    # ['sudoku_difficult_29', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()]],
    # ['sudoku_difficult_30', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()]],
    # ['sudoku_difficult_32', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()]],
    # ['sudoku_difficult_33', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()]],
    # ['sudoku_difficult_34', Sudoku,
    #  [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming(), UniqueRectangleType4(),
    #   Bug()]],
    # ['sudoku_difficult_36', Sudoku,
    #  [CrossHatch(), LockedCandidatesPointing(), Bug(), tech.NakedTriple()]],
    # ['sudoku_difficult_37', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.NakedTriple()]],
    ['sudoku_difficult_38', Sudoku, [CrossHatch(), HiddenSingle(), Bug()]],
    # ['sudoku_difficult_39', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]],
  

])
def test_default_puzzle(puzzle_string, constructor, techniques):
    if "\n" in puzzle_string:
        pytest.skip(puzzle_string)
    result = getattr(Constants, puzzle_string)
    assert default_test_puzzle(result(), constructor, techniques)
