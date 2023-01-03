import pytest
from Constants import Constants
from Techniques import Solving
from _defaults import default_test_puzzle, default_test_explicit_actual_expected
from _puzzles import Sudoku, Magnets, Kropki, Parks1, Tenner, RobotFences, Skyscrapers, Sumscrapers, AbstractPainting, \
    PowerGrid
from techniques0 import KropkiBlack, KropkiWhite, KropkiEmpty
from techniques0.JellyFish import JellyFish
from techniques0.KropkiBb import KropkiBb
from techniques0.KropkiBw import KropkiBw
from techniques0.KropkiDiamondWwwe import KropkiDiamondWwwe
from techniques0.KropkiDominatingEmpty import KropkiDominatingEmpty
from techniques0.MagnetsFullHouse import MagnetsFullHouse
from techniques0.MagnetsPair import MagnetsPair
from techniques0.MagnetsZero import MagnetsZero
from techniques0.SwordFish import SwordFish
from techniques0.UniqueRectangleType1 import UniqueRectangleType1
from techniques0.XyWing import XyWing

EXPLICITLY = "EXPLICITLY"


@pytest.mark.parametrize("puzzle_string, constructor, techniques", [
    (Constants.sumscrapers_008(), Sumscrapers, Solving.sumscrapers_techniques()),
    (Constants.sumscrapers_001(), Sumscrapers, Solving.sumscrapers_techniques()),
    (Constants.sumscrapers_002(), Sumscrapers, Solving.sumscrapers_techniques()),
    (Constants.sumscrapers_003(), Sumscrapers, Solving.sumscrapers_techniques()),
    (Constants.sumscrapers_004(), Sumscrapers, Solving.sumscrapers_techniques()),
    (Constants.sumscrapers_005(), Sumscrapers, Solving.sumscrapers_techniques()),
    (Constants.tenner_easier_002(), Tenner, Solving.tenner_techniques()),
    (Constants.tenner_easier_003(), Tenner, Solving.tenner_techniques()),
    (Constants.tenner_easier_004(), Tenner, Solving.tenner_techniques()),
    (Constants.sudoku_easiest_0(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_easy_as_pie_0(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_first_lesson(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_hidden_single_0(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_hidden_single_1(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_hidden_single_2(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_intricate_0(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_intricate_1(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_intricate_2(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_intricate_3(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_intricate_4(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_intricate_5(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_intricate_6(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_intricate_7(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_intricate_8(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_mild_0(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_mild_1(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_mild_2(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_mild_3(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_mild_4(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_moderate_0(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_naked_pair_0(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_naked_pair_1(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_naked_pair_2(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_picnic_0(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_picnic_1(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_picnic_2(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_second_lesson_0(), Sudoku, Solving.sudoku_techniques()),
    (Constants.sudoku_simple_0(), Sudoku, Solving.sudoku_techniques()),
    (Constants.parks1_001(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_002(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_003(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_006(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_007(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_008(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_beach_001(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_beach_002(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_beach_003(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_beach_004(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_maui_001(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_spring_001(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_spring_002(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_spring_003(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_spring_004(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_spring_005(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_spring_006(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_spring_007(), Parks1, Solving.parks1_techniques()),
    (Constants.parks1_spring_008(), Parks1, Solving.parks1_techniques()),
    (Constants.robot_fences_001(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_002(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_003(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_004(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_005(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_006(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_007(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_008(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_009(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_010(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_011(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_012(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_013(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_014(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_015(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_016(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_017(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_018(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_019(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_020(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_022(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_023(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_025(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_028(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.robot_fences_030(), RobotFences, Solving.robot_fences_techniques()),
    (Constants.tenner_001(), Tenner, Solving.tenner_techniques()),
    (Constants.tenner_002(), Tenner, Solving.tenner_techniques()),
    (Constants.tenner_003(), Tenner, Solving.tenner_techniques()),
    (Constants.tenner_004(), Tenner, Solving.tenner_techniques()),
    (Constants.tenner_005(), Tenner, Solving.tenner_techniques()),
    (Constants.tenner_006(), Tenner, Solving.tenner_techniques()),
    (Constants.tenner_008(), Tenner, Solving.tenner_techniques()),
    (Constants.tenner_009(), Tenner, Solving.tenner_techniques()),
    (Constants.skyscrapers_001(), Skyscrapers, Solving.skyscrapers_techniques()),
    (Constants.skyscrapers_002(), Skyscrapers, Solving.skyscrapers_techniques()),
    (Constants.skyscrapers_003(), Skyscrapers, Solving.skyscrapers_techniques()),
    (Constants.skyscrapers_005(), Skyscrapers, Solving.skyscrapers_techniques()),
    (Constants.skyscrapers_tc_001(), Skyscrapers, Solving.skyscrapers_techniques()),
    (Constants.skyscrapers_tc_002(), Skyscrapers, Solving.skyscrapers_techniques()),
    (Constants.abstractpainting_001(), AbstractPainting, Solving.abstractpainting_techniques()),
    (Constants.abstractpainting_002(), AbstractPainting, Solving.abstractpainting_techniques()),
    (Constants.abstractpainting_003(), AbstractPainting, Solving.abstractpainting_techniques()),
    (Constants.abstractpainting_004(), AbstractPainting, Solving.abstractpainting_techniques()),
    (Constants.abstractpainting_005(), AbstractPainting, Solving.abstractpainting_techniques()),
    (Constants.abstractpainting_006(), AbstractPainting, Solving.abstractpainting_techniques()),
    (Constants.power_grid_001(), PowerGrid, Solving.power_grid_techniques()),
    (Constants.power_grid_002(), PowerGrid, Solving.power_grid_techniques()),
    (Constants.power_grid_003(), PowerGrid, Solving.power_grid_techniques()),
    (Constants.power_grid_004(), PowerGrid, Solving.power_grid_techniques()),
    (Constants.power_grid_005(), PowerGrid, Solving.power_grid_techniques()),
    (Constants.power_grid_006(), PowerGrid, Solving.power_grid_techniques()),
    (Constants.power_grid_011(), PowerGrid, Solving.power_grid_techniques()),
    (Constants.power_grid_012(), PowerGrid, Solving.power_grid_techniques()),
    (Constants.power_grid_013(), PowerGrid, Solving.power_grid_techniques()),
    (Constants.power_grid_014(), PowerGrid, Solving.power_grid_techniques()),


])
def test_default_puzzle(puzzle_string, constructor, techniques):
    assert default_test_puzzle(puzzle_string, constructor, techniques)


@pytest.mark.parametrize("constructor, technique, actual, expected", [

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
])
def test_default_actual_expected(constructor, technique, actual, expected):
    assert default_test_explicit_actual_expected(constructor, technique, actual, expected)
