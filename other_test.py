import numpy
import pytest

from Constants import Constants
from Loc import Loc
from _defaults import default_test_puzzle, default_test_explicit_actual_expected
from puzzles import *
from tech import tech
from techniques.AbstractPaintingTech import AbstractPaintingTech
from techniques.AvoidableRectangleType1 import AvoidableRectangleType1
from techniques.AvoidableRectangleType2 import AvoidableRectangleType2
from techniques.CrossHatch import CrossHatch
from techniques.CrossHatchRobotFences import CrossHatchRobotFences
from techniques.CrossHatchSumscrapers import CrossHatchSumscrapers
from techniques.HiddenSingle import HiddenSingle
from techniques.HiddenSingleRobotFences import HiddenSingleRobotFences
from techniques.HiddenSingleSumscrapers import HiddenSingleSumscrapers
from techniques.Parks1Shapes import Parks1Shapes
from techniques.Parks1XWing import Parks1XWing
from techniques.TennerHiddenSingle import TennerHiddenSingle
from techniques.UniqueRectangleType1 import UniqueRectangleType1
from techniques.UniqueRectangleType2 import UniqueRectangleType2
from techniques.UniqueRectangleType3 import UniqueRectangleType3
from techniques.UniqueRectangleType4 import UniqueRectangleType4
from techniques.WWing import WWing
from techniques.WxyzWing import WxyzWing
from techniques.FinnedXWing import FinnedXWing
from techniques.AlmostLockedCandidatesClaiming import AlmostLockedCandidatesClaiming
from techniques.AlmostLockedCandidatesPointing import AlmostLockedCandidatesPointing
from techniques.NakedPair import NakedPair
from solving import Solving

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
    ('sudoku_unique_rectangle_type4_00', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_01', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_02', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_03', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_04', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_05', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_east_rows', Sudoku,
     [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_west_rows', Sudoku,
     [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_west_cols', Sudoku,
     [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_east_cols', Sudoku,
     [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_naked_triple_0', Sudoku,
     [CrossHatch(), HiddenSingle(), tech.LockedCandidatesPointing(), tech.NakedTriple()]),
    ('sudoku_naked_triple_2', Sudoku, [CrossHatch(), HiddenSingle(), tech.NakedTriple()]),
    ('sudoku_naked_triple_3', Sudoku, [CrossHatch(), NakedPair(), tech.NakedTriple()]),
    ('sudoku_naked_triple_4', Sudoku, [CrossHatch(), HiddenSingle(), tech.NakedTriple()]),
    ('sudoku_naked_triple_row', Sudoku, [CrossHatch(), tech.NakedTriple()]),
    ('sudoku_naked_triple_1', Sudoku, [CrossHatch(), tech.NakedTriple()]),
    ('sudoku_naked_triple_5', Sudoku, [CrossHatch(), tech.NakedTriple()]),
    ('sudoku_naked_triple_6', Sudoku, [CrossHatch(), tech.NakedTriple()]),
    (Constants.sudoku_naked_triple_9.__name__, Sudoku,
     [CrossHatch(), HiddenSingle(), tech.LockedCandidatesPointing(), tech.NakedTriple()]),
    ('sudoku_bug', Sudoku, [CrossHatch(), tech.Bug()]),
    ('sudoku_x_wing_row', Sudoku, [CrossHatch(), tech.XWing()]),
    ('sudoku_x_wing_col', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair(), tech.Bug(), tech.XWing()]),
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
    ('sudoku_intricate_2', Sudoku, [CrossHatch(), tech.LockedCandidatesClaiming()]),
    ('sudoku_intricate_3', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
    ('sudoku_intricate_4', Sudoku, [CrossHatch(), tech.LockedCandidatesPointing()]),
    ('sudoku_intricate_5', Sudoku, [CrossHatch(), HiddenSingle(), tech.LockedCandidatesPointing()]),
    ('sudoku_intricate_6', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
    ('sudoku_intricate_7', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
    ('sudoku_intricate_8', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
    ('sudoku_locked_candidates_claiming_0', Sudoku,
     [CrossHatch(), HiddenSingle(), tech.LockedCandidatesClaiming()]),
    ('sudoku_locked_candidates_claiming_1', Sudoku,
     [CrossHatch(), HiddenSingle(), tech.LockedCandidatesClaiming()]),
    ('sudoku_locked_candidates_claiming_2', Sudoku,
     [CrossHatch(), HiddenSingle(), tech.LockedCandidatesClaiming()]),
    ('sudoku_locked_candidates_pointing_0', Sudoku,
     [CrossHatch(), HiddenSingle(), tech.LockedCandidatesPointing()]),
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
    ("sumscrapers_008", Sumscrapers, Solving.sumscrapers_techniques()),
    ("sumscrapers_001", Sumscrapers, Solving.sumscrapers_techniques()),
    ("sumscrapers_002", Sumscrapers, Solving.sumscrapers_techniques()),
    ("sumscrapers_003", Sumscrapers, Solving.sumscrapers_techniques()),
    ("sumscrapers_004", Sumscrapers, Solving.sumscrapers_techniques()),
    ("sumscrapers_005", Sumscrapers, Solving.sumscrapers_techniques()),
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
    ('skyscrapers_001', Skyscrapers, Solving.skyscrapers_techniques()),
    ('skyscrapers_002', Skyscrapers, Solving.skyscrapers_techniques()),
    ('skyscrapers_003', Skyscrapers, Solving.skyscrapers_techniques()),
    ('skyscrapers_005', Skyscrapers, Solving.skyscrapers_techniques()),
    ('skyscrapers_tc_001', Skyscrapers, Solving.skyscrapers_techniques()),
    ('skyscrapers_tc_002', Skyscrapers, Solving.skyscrapers_techniques()),
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
    ('lightenup_001', LightenUp, Solving.lightenup_techniques()),
    ('lightenup_002', LightenUp, Solving.lightenup_techniques()),
    ('lightenup_003', LightenUp, Solving.lightenup_techniques()),
    ('lightenup_004', LightenUp, Solving.lightenup_techniques()),
    ('lightenup_005', LightenUp, Solving.lightenup_techniques()),
    ('lighthouses_001', Lighthouses, Solving.lighthouses_techniques()),
    ('lighthouses_002', Lighthouses, Solving.lighthouses_techniques()),
    ('power_grid_001', PowerGrid, Solving.power_grid_techniques()),
    ('power_grid_002', PowerGrid, Solving.power_grid_techniques()),
    ('power_grid_003', PowerGrid, Solving.power_grid_techniques()),
    ('power_grid_004', PowerGrid, Solving.power_grid_techniques()),
    ('power_grid_005', PowerGrid, Solving.power_grid_techniques()),
    ('power_grid_006', PowerGrid, Solving.power_grid_techniques()),
    ('power_grid_011', PowerGrid, Solving.power_grid_techniques()),
    ('power_grid_012', PowerGrid, Solving.power_grid_techniques()),
    ('power_grid_013', PowerGrid, Solving.power_grid_techniques()),
    ('power_grid_014', PowerGrid, Solving.power_grid_techniques()),
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
    ['sudoku_difficult_00', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
    ['sudoku_difficult_03', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
    ['sudoku_difficult_06', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
    ['sudoku_difficult_10', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
    ['sudoku_difficult_12', Sudoku,
     [CrossHatch(), HiddenSingle(), tech.LockedCandidatesPointing(), tech.NakedTriple()]],
    ['sudoku_difficult_13', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
    ['sudoku_difficult_18', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
    ['sudoku_difficult_19', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
    ['sudoku_difficult_22', Sudoku, [CrossHatch(), HiddenSingle(), tech.XWing()]],
    ['sudoku_difficult_23', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
    ['sudoku_difficult_24', Sudoku,
     [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()]],
    ['sudoku_difficult_25', Sudoku, [CrossHatch(), tech.LockedCandidatesClaiming(), tech.NakedTriple()]],
    ['sudoku_difficult_26', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]],
    ['sudoku_difficult_27', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
    ['sudoku_difficult_29', Sudoku, [CrossHatch(), HiddenSingle(), tech.Bug(), tech.XWing()]],
    ['sudoku_difficult_30', Sudoku, [CrossHatch(), HiddenSingle(), tech.Bug(), tech.XWing()]],
    ['sudoku_difficult_32', Sudoku, [CrossHatch(), HiddenSingle(), tech.Bug(), tech.XWing()]],
    ['sudoku_difficult_33', Sudoku, [CrossHatch(), HiddenSingle(), tech.Bug(), tech.XWing()]],
    ['sudoku_difficult_34', Sudoku,
     [CrossHatch(), HiddenSingle(), tech.LockedCandidatesClaiming(), UniqueRectangleType4(),
      tech.Bug()]],
    # ['sudoku_difficult_36', Sudoku,
    #  [CrossHatch(), tech.LockedCandidatesPointing(), tech.Bug(), tech.NakedTriple()]],
    ['sudoku_difficult_37', Sudoku, [CrossHatch(), HiddenSingle(), tech.Bug(), tech.NakedTriple()]],
    ['sudoku_difficult_38', Sudoku, [CrossHatch(), HiddenSingle(), tech.Bug()]],
    ['sudoku_difficult_39', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]],
    # (Constants.mathrax_020.__name__, Mathrax, Solving.mathrax_techniques()),
    # (Constants.mathrax_019.__name__, Mathrax, Solving.mathrax_techniques()),
    # (Constants.mathrax_018.__name__, Mathrax, Solving.mathrax_techniques()),
    (Constants.mathrax_017.__name__, Mathrax, Solving.mathrax_techniques()),
    # (Constants.mathrax_016.__name__, Mathrax, Solving.mathrax_techniques()),
    # (Constants.mathrax_015.__name__, Mathrax, Solving.mathrax_techniques()),
    # (Constants.mathrax_014.__name__, Mathrax, Solving.mathrax_techniques()),
    # (Constants.mathrax_013.__name__, Mathrax, Solving.mathrax_techniques()),
    (Constants.mathrax_012.__name__, Mathrax, Solving.mathrax_techniques()),
    (Constants.mathrax_011.__name__, Mathrax, Solving.mathrax_techniques()),
    (Constants.mathrax_010.__name__, Mathrax, Solving.mathrax_techniques()),
    # (Constants.mathrax_009.__name__, Mathrax, Solving.mathrax_techniques()),
    # (Constants.mathrax_008.__name__, Mathrax, Solving.mathrax_techniques()),
    (Constants.mathrax_007.__name__, Mathrax, Solving.mathrax_techniques()),
    # (Constants.mathrax_006.__name__, Mathrax, Solving.mathrax_techniques()),
    (Constants.mathrax_005.__name__, Mathrax, Solving.mathrax_techniques()),
    (Constants.mathrax_004.__name__, Mathrax, Solving.mathrax_techniques()),
    (Constants.mathrax_003.__name__, Mathrax, Solving.mathrax_techniques()),
    (Constants.mathrax_002.__name__, Mathrax, Solving.mathrax_techniques()),
    (Constants.mathrax_001.__name__, Mathrax, Solving.mathrax_techniques()),
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


def all_file_leaves():
    from os import walk
    files = []
    for filename in next(walk('C:\\Repos\\logics0\\files'), (None, None, []))[2]:  # [] if no file
        if 'actual' in filename:
            files.append(filename)
    return files


def the_data():
    for _id in all_file_leaves():

        if 'hidden_single' in _id:
            yield [_id, HiddenSingle()]
        elif 'almost_locked_candidates_claiming' in _id:
            yield [_id, AlmostLockedCandidatesClaiming()]
        elif 'hidden_pair' in _id:
            yield [_id, tech.HiddenPair()]
        elif 'hidden_triple' in _id:
            yield [_id, tech.HiddenTriple()]
        elif 'hidden_quad' in _id:
            yield [_id, tech.HiddenQuad()]
        elif 'naked_pair' in _id:
            yield [_id, NakedPair()]
        elif 'naked_triple' in _id:
            yield [_id, tech.NakedTriple()]
        elif 'naked_quad' in _id:
            yield [_id, tech.NakedQuad()]
        elif 'cross_hatch' in _id:
            yield [_id, CrossHatch()]
        elif 'avoidable_rectangle_type1' in _id:
            yield [_id, AvoidableRectangleType1()]
        elif 'avoidable_rectangle_type2' in _id:
            yield [_id, AvoidableRectangleType2()]
        elif 'hidden_unique_rectangle' in _id:
            yield [_id, tech.HiddenUniqueRectangle()]
        elif 'unique_rectangle_type1' in _id:
            yield [_id, UniqueRectangleType1()]
        elif 'unique_rectangle_type2' in _id:
            yield [_id, UniqueRectangleType2()]
        elif 'unique_rectangle_type3' in _id:
            yield [_id, UniqueRectangleType3()]
        elif 'unique_rectangle_type4' in _id:
            yield [_id, UniqueRectangleType4()]
        elif 'locked_candidates_pointing' in _id:
            yield [_id, tech.LockedCandidatesPointing()]
        elif 'locked_candidates_claiming' in _id:
            yield [_id, tech.LockedCandidatesClaiming()]
        elif 'finned_jelly_fish' in _id:
            yield [_id, tech.FinnedJellyFish()]
        elif 'shashimi_jelly_fish' in _id:
            yield [_id, tech.ShashimiJellyFish()]
        elif 'jelly_fish' in _id:
            yield [_id, tech.JellyFish()]
        elif 'finned_sword_fish' in _id:
            yield [_id, tech.FinnedSwordFish()]
        elif 'shashimi_sword_fish' in _id:
            yield [_id, tech.ShashimiSwordFish()]
        elif 'sword_fish' in _id:
            yield [_id, tech.SwordFish()]
        elif 'finned_x_wing' in _id:
            yield [_id, FinnedXWing()]
        elif 'shashimi_x_wing' in _id:
            yield [_id, tech.ShashimiXWing()]
        elif 'x_wing' in _id:
            yield [_id, tech.XWing()]
        elif 'x_chain' in _id:
            yield [_id, tech.XChain()]
        elif 'xy_chain' in _id:
            yield [_id, tech.XyChain()]
        elif 'xy_wing' in _id:
            yield [_id, tech.XyWing()]
        elif 'wxyz_wing' in _id:
            yield [_id, WxyzWing()]
        elif 'xyz_wing' in _id:
            yield [_id, tech.XyzWing()]
        elif 'w_wing' in _id:
            yield [_id, WWing()]
        elif 'simple_coloring' in _id:
            yield [_id, tech.SimpleColoring()]
        elif 'sue_de_coq' in _id:
            yield [_id, tech.SueDeCoq()]
        elif 'fishy_cycle' in _id:
            yield [_id, tech.FishyCycle()]
        else:
            yield [_id, None]


def __test_file_puzzle(data) -> tuple[bool, str]:
    actual_path, technique = data

    if technique is None:
        pytest.skip(actual_path)

    actual_path = f'C:\\Repos\\logics0\\files\\{actual_path}'

    expected_path = actual_path.replace('actual', 'expected')

    actual = numpy.loadtxt(actual_path, dtype=str)
    expected = numpy.loadtxt(expected_path, dtype=str)

    actual_split = actual_path.split('\\')
    expected_split = expected_path.split('\\')

    actual_id = actual_split[-1]
    expected_id = expected_split[-1]

    length_actual = int(actual[0, 0])
    actual = numpy.delete(actual, 0, 0)

    length_expected = int(expected[0, 0])
    expected = numpy.delete(expected, 0, 0)

    if actual_id.endswith('.sudoku'):
        constructor = Sudoku
    elif actual_id.endswith('.kropki'):
        constructor = Kropki
    else:
        return False, 'Could not determine puzzle type'

    if constructor is None:
        return False, "Constructor was None"

    actual_puzzle = constructor(actual, length_actual, actual_id)
    expected_puzzle = constructor(expected, length_expected, expected_id)

    technique.solve0(actual_puzzle)

    if actual_puzzle == expected_puzzle:
        return True, ""

    if actual_id.endswith('.sudoku'):
        for r in range(len(actual_puzzle)):
            for c in range(len(actual_puzzle)):
                loc = Loc(r, c)
                actual_candidates = actual_puzzle.cell_candidates(loc)
                expected_candidates = expected_puzzle.cell_candidates(loc)

                if set(actual_candidates) == set(expected_candidates):
                    continue

                expected_puzzle.override_loc_color([loc], Fore.CYAN)

    print(actual_puzzle.to_string())
    print(expected_puzzle.to_string())

    return False, "{actual_puzzle} dit not equal {expected_puzzle}"


@pytest.mark.parametrize('data', the_data(), ids=[i[0] for i in the_data()])
def test_file_puzzle(data):
    result, message = __test_file_puzzle(data)

    assert result, message

