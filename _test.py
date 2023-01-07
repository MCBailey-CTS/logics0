import puzzles
import pytest

from Constants import Constants
from _defaults import default_test_puzzle, default_test_explicit_actual_expected
from _puzzles import Sudoku, Parks1, Tenner, Sumscrapers, AbstractPainting, \
    PowerGrid
from techniques0 import KropkiBlack, KropkiWhite, KropkiEmpty, NakedPair, LockedCandidatesPointing, \
    LockedCandidatesClaiming
from puzzles import RobotFences
from techniques0.kropki.KropkiBb import KropkiBb
from techniques0.kropki.KropkiBw import KropkiBw
from techniques0.kropki.KropkiDiamondWwwe import KropkiDiamondWwwe
from techniques0.kropki.KropkiDominatingEmpty import KropkiDominatingEmpty
from techniques0.solver_groups import Solving
from techniques0.sudoku.AvoidableRectangleType1 import AvoidableRectangleType1
from techniques0.sudoku.CrossHatch import CrossHatch
from techniques0.sudoku.HiddenPair import HiddenPair
from techniques0.sudoku.HiddenSingle import HiddenSingle
from techniques0.sudoku.HiddenUniqueRectangle import HiddenUniqueRectangle
from techniques0.sudoku.JellyFish import JellyFish
from techniques0.sudoku.NakedTriple import NakedTriple
from techniques0.sudoku.SwordFish import SwordFish
from techniques0.sudoku.UniqueRectangleType1 import UniqueRectangleType1
from techniques0.sudoku.UniqueRectangleType2 import UniqueRectangleType2
from techniques0.sudoku.UniqueRectangleType4 import UniqueRectangleType4
from techniques0.sudoku.WWing import WWing
from techniques0.sudoku.XWing import XWing
from techniques0.sudoku.FinnedXWing import FinnedXWing
from techniques0.sudoku.XyWing import XyWing
from techniques0.sudoku.Bug import Bug
from techniques0.sudoku.ShashimiXWing import ShashimiXWing
from puzzles import Skyscrapers
from puzzles import Kropki

EXPLICITLY = "EXPLICITLY"


@pytest.mark.parametrize("puzzle_string, constructor, techniques", [
    ("sumscrapers_008", Sumscrapers, Solving.sumscrapers_techniques()),
    ("sumscrapers_001", Sumscrapers, Solving.sumscrapers_techniques()),
    ("sumscrapers_002", Sumscrapers, Solving.sumscrapers_techniques()),
    ("sumscrapers_003", Sumscrapers, Solving.sumscrapers_techniques()),
    ("sumscrapers_004", Sumscrapers, Solving.sumscrapers_techniques()),
    ("sumscrapers_005", Sumscrapers, Solving.sumscrapers_techniques()),
    ('tenner_easier_002', Tenner, Solving.tenner_techniques()),
    ('tenner_easier_003', Tenner, Solving.tenner_techniques()),
    ('tenner_easier_004', Tenner, Solving.tenner_techniques()),
    ('sudoku_easiest_0', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_easy_as_pie_0', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_first_lesson', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_hidden_single_0', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_hidden_single_1', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_hidden_single_2', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_intricate_0', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_intricate_1', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_intricate_2', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_intricate_3', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_intricate_4', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_intricate_5', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_intricate_6', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_intricate_7', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_intricate_8', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_mild_0', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_mild_1', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_mild_2', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_mild_3', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_mild_4', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_moderate_0', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_naked_pair_0', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_naked_pair_1', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_naked_pair_2', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_picnic_0', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_picnic_1', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_picnic_2', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_second_lesson_0', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_simple_0', Sudoku, Solving.sudoku_techniques()),
    ('parks1_001', Parks1, Solving.parks1_techniques()),
    ('parks1_002', Parks1, Solving.parks1_techniques()),
    ('parks1_003', Parks1, Solving.parks1_techniques()),
    ('parks1_004', Parks1, Solving.parks1_techniques()),

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
    ('tenner_001', Tenner, Solving.tenner_techniques()),
    ('tenner_002', Tenner, Solving.tenner_techniques()),
    ('tenner_003', Tenner, Solving.tenner_techniques()),
    ('tenner_004', Tenner, Solving.tenner_techniques()),
    ('tenner_005', Tenner, Solving.tenner_techniques()),
    ('tenner_006', Tenner, Solving.tenner_techniques()),
    ('tenner_008', Tenner, Solving.tenner_techniques()),
    ('tenner_009', Tenner, Solving.tenner_techniques()),
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
    ['sudoku_difficult_00', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_03', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_06', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_10', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_11', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_12', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_13', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_14', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_16', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_18', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_19', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_22', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_23', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_24', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_25', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_26', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_27', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_29', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_30', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_32', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_33', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_34', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_36', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_37', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_38', Sudoku, Solving.sudoku_techniques()],
    ['sudoku_difficult_39', Sudoku, Solving.sudoku_techniques()],
    ('sudoku_locked_candidates_claiming_0', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_locked_candidates_claiming_1', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_locked_candidates_claiming_2', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_locked_candidates_pointing_0', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_naked_triple_0', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_naked_triple_1', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_naked_triple_2', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_naked_triple_3', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_naked_triple_4', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_naked_triple_5', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_naked_triple_6', Sudoku, Solving.sudoku_techniques()),
    # ('sudoku_naked_triple_8', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_naked_triple_9', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_naked_triple_row', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type1_00', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type1_01', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type1_02', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type1_03', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type1_04', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type1_05', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type4_00', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type4_01', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type4_02', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type4_03', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type4_04', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type4_05', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type4_east_rows', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type4_west_rows', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type4_west_cols', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type4_east_cols', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_bug', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_x_wing_row', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_x_wing_col', Sudoku, Solving.sudoku_techniques()),
    ('sudoku_unique_rectangle_type2_00', Sudoku, Solving.sudoku_techniques()),
    ("sudoku_unique_rectangle_type2_01", Sudoku, Solving.sudoku_techniques()),
    ("sudoku_unique_rectangle_type2_02", Sudoku, Solving.sudoku_techniques()),
    ("sudoku_unique_rectangle_type2_03", Sudoku, Solving.sudoku_techniques()),
    ("sudoku_unique_rectangle_type2_04", Sudoku, Solving.sudoku_techniques()),
    ("sudoku_unique_rectangle_type2_05", Sudoku, Solving.sudoku_techniques()),
    ("sudoku_unique_rectangle_type2_06", Sudoku, Solving.sudoku_techniques()),
    ("sudoku_unique_rectangle_type2_08", Sudoku, Solving.sudoku_techniques()),
    ("sudoku_unique_rectangle_type2_09", Sudoku, Solving.sudoku_techniques()),
    ("sudoku_unique_rectangle_type2_10", Sudoku, Solving.sudoku_techniques()),
    ("sudoku_unique_rectangle_type2_11", Sudoku, Solving.sudoku_techniques()),
    ("sudoku_unique_rectangle_type2_12", Sudoku, Solving.sudoku_techniques()),
("parks1_009", Parks1, Solving.parks1_techniques()),
("parks1_010", Parks1, Solving.parks1_techniques()),
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
("parks1_spring_016", Parks1, Solving.parks1_techniques()),
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
("parks1_spring_027", Parks1, Solving.parks1_techniques()),
("parks1_spring_028", Parks1, Solving.parks1_techniques()),
("parks1_spring_029", Parks1, Solving.parks1_techniques()),
("parks1_spring_030", Parks1, Solving.parks1_techniques()),
("parks1_spring_031", Parks1, Solving.parks1_techniques()),
("parks1_spring_032", Parks1, Solving.parks1_techniques()),
("parks1_spring_033", Parks1, Solving.parks1_techniques()),
("parks1_spring_034", Parks1, Solving.parks1_techniques()),
("parks1_spring_039", Parks1, Solving.parks1_techniques()),
("parks1_spring_045", Parks1, Solving.parks1_techniques()),
("parks1_spring_046", Parks1, Solving.parks1_techniques()),
("parks1_spring_047", Parks1, Solving.parks1_techniques()),
("parks1_spring_051", Parks1, Solving.parks1_techniques()),
("parks1_spring_062", Parks1, Solving.parks1_techniques()),
("parks1_winter_037", Parks1, Solving.parks1_techniques()),
("parks1_winter_038", Parks1, Solving.parks1_techniques()),
("parks1_winter_039", Parks1, Solving.parks1_techniques()),
("parks1_winter_040", Parks1, Solving.parks1_techniques()),
("parks1_winter_041", Parks1, Solving.parks1_techniques()),
("parks1_winter_042", Parks1, Solving.parks1_techniques()),
("parks1_winter_044", Parks1, Solving.parks1_techniques()),
("parks1_winter_045", Parks1, Solving.parks1_techniques()),
("parks1_winter_046", Parks1, Solving.parks1_techniques()),
("parks1_winter_047", Parks1, Solving.parks1_techniques()),
("parks1_winter_048", Parks1, Solving.parks1_techniques()),
("parks1_winter_049", Parks1, Solving.parks1_techniques()),
# ("parks1_winter_050", Parks1, Solving.parks1_techniques()),
# ("parks1_winter_051", Parks1, Solving.parks1_techniques()),
    ###########################
    ###########################
    ###########################
    ###########################
    ###########################
    ('parks1_005', Parks1, Solving.parks1_techniques()),

    # ('sudoku_avoidable_rectangle_type1_00", Sudoku, Solving.sudoku_techniques()),
    # ('sudoku_naked_triple_7", Sudoku, Solving.sudoku_techniques()),
    # ('sudoku_remote_pair_row", Sudoku, Solving.sudoku_techniques()),
    # ('sudoku_xy_wing_00", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_avoidable_rectangle_type1_01", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_avoidable_rectangle_type1_02", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_avoidable_rectangle_type1_03", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_avoidable_rectangle_type1_04", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_avoidable_rectangle_type1_05", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_avoidable_rectangle_type1_07", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_avoidable_rectangle_type1_08", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_avoidable_rectangle_type1_09", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_avoidable_rectangle_type1_10", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_avoidable_rectangle_type1_11", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_avoidable_rectangle_type1_12", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_avoidable_rectangle_type1_13", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_xy_wing_01", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_xy_wing_02", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_xy_wing_03", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_xy_wing_04", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_xy_wing_05", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_xy_wing_06", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_xy_wing_07", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_xy_wing_08", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_xy_wing_09", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_xy_wing_10", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_xy_wing_11", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_hidden_pair_row", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_hidden_pair_col", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_hidden_pair_fence", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_hidden_triple_row", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_hidden_triple_col", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_hidden_triple_fence", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_hidden_quad_row", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_hidden_quad_col", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_hidden_quad_fence", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_swordfish_of_5_in_rows", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_swordfish_of_8_in_cols", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_jellyfish_of_1_in_rows", Sudoku, Solving.sudoku_techniques()),
    # ("sudoku_jellyfish_of_3_in_cols", Sudoku, Solving.sudoku_techniques()),
    # ["sudoku_difficult_01", Sudoku, Solving.sudoku_techniques()],
    # ["sudoku_difficult_02", Sudoku, Solving.sudoku_techniques()],
    # ["sudoku_difficult_04", Sudoku, Solving.sudoku_techniques()],
    # ["sudoku_difficult_05", Sudoku, Solving.sudoku_techniques()],
    # ["sudoku_difficult_07", Sudoku, Solving.sudoku_techniques()],
    # ["sudoku_difficult_08", Sudoku, Solving.sudoku_techniques()],
    # ["sudoku_difficult_09", Sudoku, Solving.sudoku_techniques()],
    # ["sudoku_difficult_15", Sudoku, Solving.sudoku_techniques()],
    # ["sudoku_difficult_17", Sudoku, Solving.sudoku_techniques()],
    # ["sudoku_difficult_20", Sudoku, Solving.sudoku_techniques()],
    # ["sudoku_difficult_21", Sudoku, Solving.sudoku_techniques()],
    # ["sudoku_difficult_28", Sudoku, Solving.sudoku_techniques()],
    # ["sudoku_difficult_31", Sudoku, Solving.sudoku_techniques()],
    # ["sudoku_difficult_35", Sudoku, Solving.sudoku_techniques()],
    # ("sudoku_unique_rectangle_type4_south_cols", Sudoku, Solving.sudoku_techniques()),

    # ("sudoku_unique_rectangle_type2_07", Sudoku, Solving.sudoku_techniques()),

])
def test_default_puzzle(puzzle_string, constructor, techniques):
    if "\n" in puzzle_string:
        # assert default_test_puzzle(puzzle_string, constructor, techniques)
        pytest.skip(puzzle_string)

    result = getattr(Constants, puzzle_string)

    assert default_test_puzzle(result(), constructor, techniques)

    # print(result())

    # assert False

    # pytest.skip(puzzle_string)


@pytest.mark.parametrize("constructor, technique, actual, expected", [
    # (Sudoku,
    #  ShashimiXWing(),
    #  Constants.sudoku_explicit_shashimi_x_wing_1_fin_cols_actual(),
    #  Constants.sudoku_explicit_shashimi_x_wing_1_fin_cols_expected()),
    # (Sudoku,
    #  ShashimiXWing(),
    #  Constants.sudoku_explicit_shashimi_x_wing_1_fin_rows_actual(),
    #  Constants.sudoku_explicit_shashimi_x_wing_1_fin_rows_expected()),
    # (Sudoku,
    #  ShashimiXWing(),
    #  Constants.sudoku_explicit_shashimi_x_wing_2_fin_rows_actual(),
    #  Constants.sudoku_explicit_shashimi_x_wing_2_fin_rows_expected()),
    #
    # (Sudoku,
    #  ShashimiXWing(),
    #  Constants.sudoku_explicit_shashimi_x_wing_2_fin_cols_actual(),
    #  Constants.sudoku_explicit_shashimi_x_wing_2_fin_cols_expected()),
    (Sudoku,
     XWing(),
     Constants.sudoku_explicit_x_wing_row_actual(),
     Constants.sudoku_explicit_x_wing_row_expected()),
    # (Sudoku,
    #  FinnedXWing(),
    #  Constants.sudoku_explicit_finned_x_wing_2_fin_cols_actual(),
    #  Constants.sudoku_explicit_finned_x_wing_2_fin_cols_expected()),
    # (Sudoku,
    #  FinnedXWing(),
    #  Constants.sudoku_explicit_finned_x_wing_2_fin_rows_actual(),
    #  Constants.sudoku_explicit_finned_x_wing_2_fin_rows_expected()),
    #
    #
    # (Sudoku,
    #  FinnedXWing(),
    #  Constants.sudoku_explicit_finned_x_wing_1_fin_rows_actual(),
    #  Constants.sudoku_explicit_finned_x_wing_1_fin_rows_expected()),
    (Sudoku,
     XWing(),
     Constants.sudoku_explicit_x_wing_col_actual(),
     Constants.sudoku_explicit_x_wing_col_expected()),

    (Sudoku,
     UniqueRectangleType2(),
     Constants.sudoku_explicit_unique_rectangle_type2_normal_north_actual(),
     Constants.sudoku_explicit_unique_rectangle_type2_normal_north_expected()),
    (Sudoku,
     HiddenUniqueRectangle(),
     Constants.sudoku_explicit_hidden_unique_rectangle_type1_north_east_row_chute_actual(),
     Constants.sudoku_explicit_hidden_unique_rectangle_type1_north_east_row_chute_expected()),
    (Sudoku,
     HiddenUniqueRectangle(),
     Constants.sudoku_explicit_hidden_unique_rectangle_north_west_row_chute_actual(),
     Constants.sudoku_explicit_hidden_unique_rectangle_north_west_row_chute_expected()),
    (Sudoku,
     HiddenUniqueRectangle(),
     Constants.sudoku_explicit_hidden_unique_rectangle_north_west_col_chute_actual(),
     Constants.sudoku_explicit_hidden_unique_rectangle_north_west_col_chute_expected()),
    (Sudoku,
     HiddenUniqueRectangle(),
     Constants.sudoku_explicit_hidden_unique_rectangle_north_east_col_chute_actual(),
     Constants.sudoku_explicit_hidden_unique_rectangle_north_east_col_chute_expected()),
    (Sudoku,
     HiddenUniqueRectangle(),
     Constants.sudoku_explicit_hidden_unique_rectangle_south_east_col_chute_actual(),
     Constants.sudoku_explicit_hidden_unique_rectangle_south_east_col_chute_expected()),
    (Sudoku,
     HiddenUniqueRectangle(),
     Constants.sudoku_explicit_hidden_unique_rectangle_south_west_col_chute_actual(),
     Constants.sudoku_explicit_hidden_unique_rectangle_south_west_col_chute_expected()),
    (Sudoku,
     HiddenUniqueRectangle(),
     Constants.sudoku_explicit_hidden_unique_rectangle_south_east_row_chute_actual(),
     Constants.sudoku_explicit_hidden_unique_rectangle_south_east_row_chute_expected()),
    (Sudoku,
     HiddenUniqueRectangle(),
     Constants.hidden_unique_rectangle_default_actual(),
     Constants.hidden_unique_rectangle_default_expected()),
    (Sudoku,
     UniqueRectangleType4(),
     Constants.sudoku_explicit_unique_rectangle_type4_north_actual(),
     Constants.sudoku_explicit_unique_rectangle_type4_north_expected()),
    (Sudoku,
     UniqueRectangleType4(),
     Constants.sudoku_explicit_unique_rectangle_type4_normal_east_actual(),
     Constants.sudoku_explicit_unique_rectangle_type4_normal_east_expected()),
    (Sudoku,
     UniqueRectangleType4(),
     Constants.sudoku_explicit_unique_rectangle_type4_normal_south_actual(),
     Constants.sudoku_explicit_unique_rectangle_type4_normal_south_expected()),
    (Sudoku,
     UniqueRectangleType4(),
     Constants.sudoku_explicit_unique_rectangle_type4_normal_west_actual(),
     Constants.sudoku_explicit_unique_rectangle_type4_normal_west_expected()),
    (Sudoku,
     UniqueRectangleType4(),
     Constants.sudoku_explicit_unique_rectangle_type4_goofy_west_actual(),
     Constants.sudoku_explicit_unique_rectangle_type4_goofy_west_expected()),
    (Sudoku,
     UniqueRectangleType4(),
     Constants.sudoku_explicit_unique_rectangle_type4_goofy_north_actual(),
     Constants.sudoku_explicit_unique_rectangle_type4_goofy_north_expected()),
    (Sudoku,
     UniqueRectangleType4(),
     Constants.sudoku_explicit_unique_rectangle_type4_goofy_east_actual(),
     Constants.sudoku_explicit_unique_rectangle_type4_goofy_east_expected()),
    (Sudoku,
     UniqueRectangleType4(),
     Constants.sudoku_explicit_unique_rectangle_type4_goofy_south_actual(),
     Constants.sudoku_explicit_unique_rectangle_type4_goofy_south_expected()),
    (Sudoku,
     UniqueRectangleType2(),
     Constants.sudoku_explicit_unique_rectangle_type2_goofy_east_actual(),
     Constants.sudoku_explicit_unique_rectangle_type2_goofy_east_expected()),
    (Sudoku,
     UniqueRectangleType2(),
     Constants.sudoku_explicit_unique_rectangle_type2_goofy_north_actual(),
     Constants.sudoku_explicit_unique_rectangle_type2_goofy_north_expected()),
    (Sudoku,
     UniqueRectangleType2(),
     Constants.sudoku_explicit_unique_rectangle_type2_normal_west_actual(),
     Constants.sudoku_explicit_unique_rectangle_type2_normal_west_expected()),
    (Sudoku,
     UniqueRectangleType2(),
     Constants.sudoku_explicit_unique_rectangle_type2_goofy_west_actual(),
     Constants.sudoku_explicit_unique_rectangle_type2_goofy_west_expected()),
    (Sudoku,
     UniqueRectangleType2(),
     Constants.sudoku_explicit_unique_rectangle_type2_normal_east_actual(),
     Constants.sudoku_explicit_unique_rectangle_type2_normal_east_expected()),
    (Sudoku,
     UniqueRectangleType2(),
     Constants.sudoku_explicit_unique_rectangle_type2_goofy_south_actual(),
     Constants.sudoku_explicit_unique_rectangle_type2_goofy_south_expected()),
    (Sudoku,
     UniqueRectangleType2(),
     Constants.sudoku_explicit_unique_rectangle_type2_normal_south_actual(),
     Constants.sudoku_explicit_unique_rectangle_type2_normal_south_expected()),
    (Sudoku,
     HiddenPair(),
     Constants.sudoku_explicit_hidden_pair_fences_actual(),
     Constants.sudoku_explicit_hidden_pair_fences_expected()),
    (Sudoku,
     HiddenPair(),
     Constants.sudoku_explicit_hidden_pair_rows_actual(),
     Constants.sudoku_explicit_hidden_pair_rows_expected()),
    (Sudoku,
     HiddenPair(),
     Constants.sudoku_explicit_hidden_pair_cols_actual(),
     Constants.sudoku_explicit_hidden_pair_cols_expected()),
    (Sudoku,
     LockedCandidatesPointing(),
     Constants.sudoku_explicit_locked_candidates_pointing_2_fins_cols_actual(),
     Constants.sudoku_explicit_locked_candidates_pointing_2_fins_cols_expected()),
    (Sudoku,
     LockedCandidatesClaiming(),
     Constants.sudoku_explicit_locked_candidates_claiming_3_fins_rows_actual(),
     Constants.sudoku_explicit_locked_candidates_claiming_3_fins_rows_expected()),
    (Sudoku,
     LockedCandidatesClaiming(),
     Constants.sudoku_explicit_locked_candidates_claiming_2_fins_rows_actual(),
     Constants.sudoku_explicit_locked_candidates_claiming_2_fins_rows_expected()),
    (Sudoku,
     LockedCandidatesClaiming(),
     Constants.sudoku_explicit_locked_candidates_claiming_2_fins_cols_actual(),
     Constants.sudoku_explicit_locked_candidates_claiming_2_fins_cols_expected()),
    (Sudoku,
     LockedCandidatesClaiming(),
     Constants.sudoku_explicit_locked_candidates_claiming_3_fins_cols_actual(),
     Constants.sudoku_explicit_locked_candidates_claiming_3_fins_cols_expected()),
    (Sudoku,
     JellyFish(),
     Constants.sudoku_explicit_jelly_fish_cols_actual(),
     Constants.sudoku_explicit_jelly_fish_cols_expected()),
    (Sudoku,
     JellyFish(),
     Constants.sudoku_explicit_jelly_fish_rows_actual(),
     Constants.sudoku_explicit_jelly_fish_rows_expected()),
    (Sudoku,
     UniqueRectangleType1(),
     Constants.sudoku_explicit_unique_rectangle_type1_north_west_row_chute_actual(),
     Constants.sudoku_explicit_unique_rectangle_type1_north_west_row_chute_expected()),
    (Sudoku,
     UniqueRectangleType1(),
     Constants.sudoku_explicit_unique_rectangle_type1_south_east_row_chute_actual(),
     Constants.sudoku_explicit_unique_rectangle_type1_south_east_row_chute_expected()),
    (Sudoku,
     UniqueRectangleType1(),
     Constants.sudoku_explicit_unique_rectangle_type1_south_west_row_chute_actual(),
     Constants.sudoku_explicit_unique_rectangle_type1_south_west_row_chute_expected()),
    (Sudoku,
     UniqueRectangleType1(),
     Constants.sudoku_explicit_unique_rectangle_type1_north_east_col_chute_actual(),
     Constants.sudoku_explicit_unique_rectangle_type1_north_east_col_chute_expected()),
    (Sudoku,
     UniqueRectangleType1(),
     Constants.sudoku_explicit_unique_rectangle_type1_north_west_col_chute_actual(),
     Constants.sudoku_explicit_unique_rectangle_type1_north_west_col_chute_expected()),
    (Sudoku,
     UniqueRectangleType1(),
     Constants.sudoku_explicit_unique_rectangle_type1_south_east_col_chute_actual(),
     Constants.sudoku_explicit_unique_rectangle_type1_south_east_col_chute_expected()),
    (Sudoku,
     UniqueRectangleType1(),
     Constants.sudoku_explicit_unique_rectangle_type1_south_west_col_chute_actual(),
     Constants.sudoku_explicit_unique_rectangle_type1_south_west_col_chute_expected()),
    (Sudoku,
     SwordFish(),
     Constants.sudoku_explicit_sword_fish_rows_actual(),
     Constants.sudoku_explicit_sword_fish_rows_expected()),
    (Sudoku,
     SwordFish(),
     Constants.sudoku_explicit_sword_fish_cols_actual(),
     Constants.sudoku_explicit_sword_fish_cols_expected()),
    (Sudoku,
     XyWing(),
     Constants.sudoku_explicit_xy_wing_north_east_actual(),
     Constants.sudoku_explicit_xy_wing_north_east_expected()),
    (Sudoku,
     XyWing(),
     Constants.sudoku_explicit_xy_wing_south_west_actual(),
     Constants.sudoku_explicit_xy_wing_south_west_expected()),
    (Kropki,
     KropkiBw(),
     Constants.kropki_explicit_bw_actual(),
     Constants.kropki_explicit_bw_expected()),
    (Kropki,
     KropkiBlack(),
     Constants.kropki_explicit_black_actual(),
     Constants.kropki_explicit_black_expected()),
    (Kropki,
     KropkiWhite(),
     Constants.kropki_explicit_white_actual(),
     Constants.kropki_explicit_white_expected()),
    (Kropki,
     KropkiEmpty(),
     Constants.kropki_explicit_empty_actual(),
     Constants.kropki_explicit_empty_expected()),
    (Kropki,
     KropkiBb(),
     Constants.kropki_explicit_bb_actual(),
     Constants.kropki_explicit_bb_expected()),
    (Kropki,
     KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty1_actual(),
     Constants.kropki_explicit_dominating_empty1_expected()),
    (Kropki,
     KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty3_actual(),
     Constants.kropki_explicit_dominating_empty3_expected()),
    (Kropki,
     KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty4_actual(),
     Constants.kropki_explicit_dominating_empty4_expected()),
    (Kropki,
     KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty5_actual(),
     Constants.kropki_explicit_dominating_empty5_expected()),
    (Kropki,
     KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty6_actual(),
     Constants.kropki_explicit_dominating_empty6_expected()),
    (Kropki,
     KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty7_actual(),
     Constants.kropki_explicit_dominating_empty7_expected()),
    (Kropki,
     KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty8_actual(),
     Constants.kropki_explicit_dominating_empty8_expected()),
    (Kropki,
     KropkiDominatingEmpty(),
     Constants.kropki_explicit_dominating_empty9_actual(),
     Constants.kropki_explicit_dominating_empty9_expected()),
    (Kropki,
     KropkiDiamondWwwe(),
     Constants.kropki_explicit_diamond_wwwe_actual(),
     Constants.kropki_explicit_diamond_wwwe_expected()),
    (Sudoku,
     NakedPair(),
     Constants.sudoku_explicit_naked_pair_rows_actual(),
     Constants.sudoku_explicit_naked_pair_rows_expected()),
    (Sudoku,
     NakedPair(),
     Constants.sudoku_explicit_naked_pair_cols_actual(),
     Constants.sudoku_explicit_naked_pair_cols_expected()),
    (Sudoku,
     NakedPair(),
     Constants.sudoku_explicit_naked_pair_fences_actual(),
     Constants.sudoku_explicit_naked_pair_fences_expected()),
    (Sudoku,
     AvoidableRectangleType1(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_south_east_col_chute_actual(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_south_east_col_chute_expected()),
    (Sudoku,
     AvoidableRectangleType1(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_north_west_col_chute_actual(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_north_west_col_chute_expected()),
    (Sudoku,
     AvoidableRectangleType1(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_south_west_row_chute_actual(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_south_west_row_chute_expected()),
    (Sudoku,
     AvoidableRectangleType1(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_north_east_col_chute_actual(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_north_east_col_chute_expected()),
    (Sudoku,
     AvoidableRectangleType1(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_north_west_row_chute_actual(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_north_west_row_chute_expected()),
    (Sudoku,
     AvoidableRectangleType1(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_north_east_row_chute_actual(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_north_east_row_chute_expected()),
    (Sudoku,
     AvoidableRectangleType1(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_south_east_row_chute_actual(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_south_east_row_chute_expected()),
    (Sudoku,
     NakedTriple(),
     Constants.sudoku_explicit_naked_triple_cols_actual(),
     Constants.sudoku_explicit_naked_triple_cols_expected()),
    (Sudoku,
     NakedTriple(),
     Constants.sudoku_explicit_naked_triple_rows_actual(),
     Constants.sudoku_explicit_naked_triple_rows_expected()),
    (Sudoku,
     NakedTriple(),
     Constants.sudoku_explicit_naked_triple_fences_actual(),
     Constants.sudoku_explicit_naked_triple_fences_expected()),
    (Sudoku,
     AvoidableRectangleType1(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_south_west_col_chute_actual(),
     Constants.sudoku_explicit_avoidable_rectangle_type1_south_west_col_chute_expected()),
    (Sudoku,
     CrossHatch(),
     Constants.sudoku_explicit_cross_hatch_actual(),
     Constants.sudoku_explicit_cross_hatch_expected()),

    (Sudoku,
     HiddenSingle(),
     Constants.sudoku_explicit_hidden_single_rows_actual(),
     Constants.sudoku_explicit_hidden_single_rows_expected()),
    (Sudoku,
     HiddenSingle(),
     Constants.sudoku_explicit_hidden_single_cols_actual(),
     Constants.sudoku_explicit_hidden_single_cols_expected()),
    (Sudoku,
     HiddenSingle(),
     Constants.sudoku_explicit_hidden_single_fences_actual(),
     Constants.sudoku_explicit_hidden_single_fences_expected()),
    (Sudoku,
     LockedCandidatesPointing(),
     Constants.sudoku_explicit_locked_candidates_pointing_3_fins_rows_actual(),
     Constants.sudoku_explicit_locked_candidates_pointing_3_fins_rows_expected()),
    (Sudoku,
     LockedCandidatesPointing(),
     Constants.sudoku_explicit_locked_candidates_pointing_3_fins_cols_actual(),
     Constants.sudoku_explicit_locked_candidates_pointing_3_fins_cols_expected()),
    (Sudoku,
     LockedCandidatesPointing(),
     Constants.sudoku_explicit_locked_candidates_pointing_2_fins_rows_actual(),
     Constants.sudoku_explicit_locked_candidates_pointing_2_fins_rows_expected()),

    (Sudoku,
     WWing(),
     Constants.sudoku_explicit_w_wing_rows_actual(),
     Constants.sudoku_explicit_w_wing_rows_expected()),
    (Sudoku,
     WWing(),
     Constants.sudoku_explicit_w_wing_cols_actual(),
     Constants.sudoku_explicit_w_wing_cols_expected()),
    (Sudoku,
     XyWing(),
     Constants.sudoku_explicit_xy_wing_north_west_actual(),
     Constants.sudoku_explicit_xy_wing_north_west_expected()),
    (Sudoku,
     XyWing(),
     Constants.sudoku_explicit_xy_wing_south_east_actual(),
     Constants.sudoku_explicit_xy_wing_south_east_expected()),

])
def test_default_actual_expected(constructor, technique, actual, expected):
    assert default_test_explicit_actual_expected(constructor, technique, actual, expected)
