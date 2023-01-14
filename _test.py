import pytest
from techniques0 import *
from Constants import Constants
from _defaults import default_test_puzzle, default_test_explicit_actual_expected

from techniques0 import KropkiBlack, KropkiWhite, KropkiEmpty, NakedPair, LockedCandidatesPointing, \
    LockedCandidatesClaiming
from puzzles import RobotFences
from techniques0.solver_groups import Solving
from techniques0.sudoku.AvoidableRectangleType1 import AvoidableRectangleType1
from techniques0.sudoku.CrossHatch import CrossHatch
from techniques0.sudoku.HiddenPair import HiddenPair
from techniques0.sudoku.JellyFish import JellyFish
from techniques0.sudoku.NakedTriple import NakedTriple
from techniques0.sudoku.SwordFish import SwordFish
from techniques0.sudoku.XyzWing import XyzWing
from techniques0.sudoku.FinnedXWing import FinnedXWing
from techniques0.sudoku.Bug import Bug
from puzzles import *

EXPLICITLY = "EXPLICITLY"


@pytest.mark.parametrize("constructor, technique, actual, expected", [
    (Sudoku,
     XWing(),
     Constants.sudoku_explicit_x_wing_row_actual(),
     Constants.sudoku_explicit_x_wing_row_expected()),
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
    (Sudoku,
     XyzWing(),
     Constants.sudoku_explicit_xyz_wing_rows_actual(),
     Constants.sudoku_explicit_xyz_wing_rows_expected()),
    (Sudoku,
     XyzWing(),
     Constants.sudoku_explicit_xyz_wing_cols_actual(),
     Constants.sudoku_explicit_xyz_wing_cols_expected()),
    (Sudoku,
     XWing(),
     Constants.sudoku_explicit_x_wing_col_actual(),
     Constants.sudoku_explicit_x_wing_col_expected()),
    (Sudoku,
     UniqueRectangleType2(),
     Constants.sudoku_explicit_unique_rectangle_type2_normal_north_actual(),
     Constants.sudoku_explicit_unique_rectangle_type2_normal_north_expected()),
#      (Mathrax,
#  MathraxCrossHatch(),
#  Constants.mathrax_explicit_cross_hatch_actual(),
#  Constants.mathrax_explicit_cross_hatch_expected()),
# (Mathrax,
#  MathraxHiddenSingle(),
#  Constants.mathrax_explicit_hidden_single_actual(),
#  Constants.mathrax_explicit_hidden_single_expected()),
])
def test_default_actual_expected(constructor, technique, actual, expected):
    assert default_test_explicit_actual_expected(constructor, technique, actual, expected)


# [
#         CrossHatch(),
#         HiddenSingle(),
#         NakedPair(),
#         LockedCandidatesPointing(),
#         LockedCandidatesClaiming(),
#         UniqueRectangleType1(),
#         UniqueRectangleType2(),
#         UniqueRectangleType4(),
#         FinnedXWing(),
#         Bug(),
#         HiddenPair(),
#         NakedTriple(),
#         XWing(),
#         XyWing(),
#     ]

@pytest.mark.parametrize("puzzle_string, constructor, techniques", [
    ('sudoku_unique_rectangle_type1_00', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()]),
    ('sudoku_unique_rectangle_type1_01', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()]),
    ('sudoku_unique_rectangle_type1_02', Sudoku, [CrossHatch(), NakedPair(), UniqueRectangleType1()]),
    ('sudoku_unique_rectangle_type1_03', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()]),
    ('sudoku_unique_rectangle_type1_05', Sudoku, [CrossHatch(), NakedPair(), UniqueRectangleType1()]),
    ('sudoku_unique_rectangle_type4_00', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_01', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_02', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_03', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_04', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_05', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_east_rows', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_west_rows', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_west_cols', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_unique_rectangle_type4_east_cols', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
    ('sudoku_naked_triple_0', Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), NakedTriple()]),
    ('sudoku_naked_triple_2', Sudoku, [CrossHatch(), HiddenSingle(), NakedTriple()]),
    ('sudoku_naked_triple_3', Sudoku, [CrossHatch(), NakedPair(), NakedTriple()]),
    ('sudoku_naked_triple_4', Sudoku, [CrossHatch(), HiddenSingle(), NakedTriple()]),
    ('sudoku_naked_triple_row', Sudoku, [CrossHatch(), NakedTriple()]),
    ('sudoku_naked_triple_1', Sudoku, [CrossHatch(), NakedTriple()]),
    ('sudoku_naked_triple_5', Sudoku, [CrossHatch(), NakedTriple()]),
    ('sudoku_naked_triple_6', Sudoku, [CrossHatch(), NakedTriple()]),
    ('sudoku_naked_triple_9', Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), NakedTriple()]),
    ('sudoku_bug', Sudoku, [CrossHatch(), Bug()]),
    ('sudoku_x_wing_row', Sudoku, [CrossHatch(), XWing()]),
    ('sudoku_x_wing_col', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair(), Bug(), XWing()]),
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
    ('sudoku_locked_candidates_claiming_0', Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()]),
    ('sudoku_locked_candidates_claiming_1', Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()]),
    ('sudoku_locked_candidates_claiming_2', Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()]),
    ('sudoku_locked_candidates_pointing_0', Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesPointing()]),
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
    ['sudoku_difficult_03', Sudoku, [CrossHatch(), HiddenSingle(), HiddenPair()]],
    ['sudoku_difficult_06', Sudoku, [CrossHatch(), HiddenSingle(), HiddenPair()]],
    ['sudoku_difficult_10', Sudoku, [CrossHatch(), HiddenSingle(), HiddenPair()]],
    ['sudoku_difficult_12', Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), NakedTriple()]],
    ['sudoku_difficult_13', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
    ['sudoku_difficult_18', Sudoku, [CrossHatch(), HiddenSingle(), HiddenPair()]],
    ['sudoku_difficult_19', Sudoku, [CrossHatch(), HiddenSingle(), HiddenPair()]],
    ['sudoku_difficult_22', Sudoku, [CrossHatch(), HiddenSingle(), XWing()]],
    ['sudoku_difficult_23', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
    ['sudoku_difficult_24', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()]],
    ['sudoku_difficult_25', Sudoku, [CrossHatch(), LockedCandidatesClaiming(), NakedTriple()]],
    ['sudoku_difficult_26', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]],
    ['sudoku_difficult_27', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
    ['sudoku_difficult_29', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), XWing()]],
    ['sudoku_difficult_30', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), XWing()]],
    ['sudoku_difficult_32', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), XWing()]],
    ['sudoku_difficult_33', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), XWing()]],
    ['sudoku_difficult_34', Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming(), UniqueRectangleType4(), Bug()]],
    ['sudoku_difficult_36', Sudoku, [CrossHatch(), LockedCandidatesPointing(), Bug(), NakedTriple()]],
    ['sudoku_difficult_37', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), NakedTriple()]],
    ['sudoku_difficult_38', Sudoku, [CrossHatch(), HiddenSingle(), Bug()]],
    ['sudoku_difficult_39', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]],
    # ('mathrax_020', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_019', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_018', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_017', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_016', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_015', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_014', Mathrax, Solving.mathrax_techniques()),
    # ('magnets_014', Magnets, Solving.magnets_techniques()),
    # ('mathrax_013', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_012', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_011', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_010', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_009', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_008', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_007', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_006', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_005', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_004', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_003', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_002', Mathrax, Solving.mathrax_techniques()),
    # ('mathrax_001', Mathrax, Solving.mathrax_techniques()),
])
def test_default_puzzle(puzzle_string, constructor, techniques):
    if "\n" in puzzle_string:
        # assert default_test_puzzle(puzzle_string, constructor, techniques)
        pytest.skip(puzzle_string)
    result = getattr(Constants, puzzle_string)
    assert default_test_puzzle(result(), constructor, techniques)
