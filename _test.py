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
from techniques.RemotePair import RemotePair
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
from os import walk

EXPLICITLY = "EXPLICITLY"

skip_dict = {
    # 'almost_locked_candidates_col.sudoku': [],
    # 'almost_locked_candidates_row.sudoku': [
    #     CrossHatch(),
    #     NakedPair(),
    #     UniqueRectangleType1(),
    #     AlmostLockedCandidatesPointing(),
    #     tech.Bug(),
    # ],
    # 'almost_locked_candidates_rows_center.sudoku': [],
    # 'als_xz.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     tech.LockedCandidatesClaiming(),
    #     tech.HiddenPair(),
    #     tech.XWing(),
    #     tech.AlsXz()
    # ],
    # 'alternating_inference_chain.sudoku': [],
    # 'annoying_00.sudoku': [CrossHatch(), HiddenSingle(), NakedPair(), tech.ShashimiXWing()],
    'annoying_02.sudoku': [CrossHatch(), FinnedXWing()],
    # 'annoying_05.sudoku': [CrossHatch(),
    #         HiddenSingle(),
    #         NakedPair(),
    #         tech.LockedCandidatesPointing(),
    #         tech.LockedCandidatesClaiming(),
    #         UniqueRectangleType1(),
    #         UniqueRectangleType2(),
    #         UniqueRectangleType4(),
    #         FinnedXWing(),
    #         tech.Bug(),
    #         tech.HiddenPair(),
    #         tech.NakedTriple(),
    #         tech.XWing(),
    #         tech.XyWing(),],
    # 'annoying_06.sudoku': [CrossHatch(),
    #         HiddenSingle(),
    #         NakedPair(),
    #         tech.LockedCandidatesPointing(),
    #         tech.LockedCandidatesClaiming(),
    #         UniqueRectangleType1(),
    #         UniqueRectangleType2(),
    #         UniqueRectangleType4(),
    #         FinnedXWing(),
    #         tech.Bug(),
    #         tech.HiddenPair(),
    #         tech.NakedTriple(),
    #         tech.XWing(),
    #         tech.XyWing(),],
    # 'annoying_07.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     FinnedXWing()
    # ],
    # 'annoying_11.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     NakedPair(),
    #     tech.NakedTriple(),
    #     tech.HiddenPair(),
    #     tech.XWing(),
    #     FinnedXWing()
    # ],
    # 'annoying_13.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     NakedPair(),
    #     UniqueRectangleType1(),
    #     FinnedXWing(),
    # ],
    # 'annoying_17.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     tech.ShashimiXWing(),
    #
    # ],
    # 'annoying_22.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     UniqueRectangleType2(),
    #     FinnedXWing(),
    #
    # ],
    # 'annoying_23.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #                        ],
    # 'annoying_25.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     tech.LockedCandidatesClaiming(),
    #     tech.HiddenPair(),
    #     FinnedXWing()
    #       Corners: {41, 61, 44, 64}
    #       fin: {43, 45}
    #       candidate: 1
    #       North east
    # ],
    # 'annoying_26.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     tech.HiddenPair(),
    #     tech.ShashimiXWing()
    # ],
    # 'annoying_27.sudoku': []
    # 'annoying_28.sudoku': [
    #     CrossHatch(),
    #         HiddenSingle(),
    #         tech.LockedCandidatesPointing(),
    #         tech.NakedTriple(),
    #         UniqueRectangleType4(),
    #         FinnedXWing(),
    # ],
    # 'annoying_29.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     NakedPair(),
    #     FinnedXWing(),
    # ],
    # 'annoying_30.sudoku': [],
    # 'annoying_32.sudoku': [],
    # 'annoying_33.sudoku': [],
    # 'annoying_35.sudoku': [],
    # 'avoidable_rectangle_type1_0.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     NakedPair(),
    #     tech.LockedCandidatesPointing(),
    #     tech.LockedCandidatesClaiming(),
    #     UniqueRectangleType1(),
    #     AvoidableRectangleType1(),
    # ],
    # 'avoidable_rectangle_type1_north_east_in_cols.sudoku': [CrossHatch(), HiddenSingle(), NakedPair(), tech.LockedCandidatesPointing(), AvoidableRectangleType1()],
    # 'avoidable_rectangle_type1_north_east_in_rows.sudoku': [],
    # 'avoidable_rectangle_type1_north_west_in_cols.sudoku': [],
    # 'avoidable_rectangle_type1_north_west_in_rows.sudoku': [],
    # 'avoidable_rectangle_type1_south_east_in_cols.sudoku': [],
    # 'avoidable_rectangle_type1_south_east_in_rows.sudoku': [],
    # 'avoidable_rectangle_type1_south_west_in_rows.sudoku': [],
    # 'avoidable_rectangle_type2_1.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     NakedPair(),
    #     UniqueRectangleType1(),
    #     tech.HiddenPair(),
    #     tech.ShashimiXWing(),
    #     AvoidableRectangleType2(),
    #     tech.Bug()
    # ],
    # 'avoidable_rectangle_type2_2.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     UniqueRectangleType1(),
    #     NakedPair(),
    #     AvoidableRectangleType2(),
    #     tech.ShashimiXWing(),
    #     tech.Bug()
    # ],
    # 'avoidable_rectangle_type2_3.sudoku': [notes],
    # 'avoidable_rectangle_type2_4.sudoku': [notes],
    'avoidable_rectangle_type2_5.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        tech.LockedCandidatesPointing(),
        tech.LockedCandidatesClaiming(),
        UniqueRectangleType1(),
        AvoidableRectangleType2()
    ],
    # 'avoidable_rectangle_type2_6.sudoku': [notes],
    'avoidable_rectangle_type2_north.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        tech.LockedCandidatesPointing(),
        NakedPair(),
        UniqueRectangleType1(),
        AvoidableRectangleType2()
    ],
    # 'avoidable_rectangle_type2_south.sudoku': [],
    # 'avoidable_rectangle_type2_west.sudoku': [],
    # 'devious_1.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     tech.LockedCandidatesClaiming(),
    #     UniqueRectangleType4(),
    #     tech.NakedTriple(),
    #     FinnedXWing(),
    #     tech.HiddenPair(),
    #     tech.XyzWing(),
    #
    # ],
    # 'devious_2.sudoku': [],
    # 'devious_3.sudoku': [],
    # 'devious_4.sudoku': [],
    # 'devious_5.sudoku': [],
    # 'devious_6.sudoku': [],
    # 'devious_7.sudoku': [],
    # 'devious_8.sudoku': [],
    # 'diabolical_0.sudoku': [],
    'difficult_01.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        UniqueRectangleType4(),
        tech.XWing(),
        tech.Bug()
    ],
    'difficult_04.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        tech.LockedCandidatesPointing(),
        tech.LockedCandidatesClaiming(),
        NakedPair(),
        RemotePair(),
    ],
    'difficult_05.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        tech.Bug()
    ],
    'difficult_08.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        UniqueRectangleType1(),
        tech.Bug()
    ],
    'difficult_15.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        UniqueRectangleType1(),

    ],
    'difficult_20.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        UniqueRectangleType4(),
        tech.Bug()
    ],
    'difficult_21.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        tech.LockedCandidatesPointing(),
        UniqueRectangleType4(),
    ],
    'difficult_31.sudoku': [
        CrossHatch(),
        RemotePair()
    ],
    # 'fiendish_0.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     tech.HiddenPair(),
    #     tech.LockedCandidatesClaiming(),
    #     FinnedXWing(),
    #     WxyzWing(),
    #     tech.XyChain(),
    #     tech.XyWing(),
    #
    # ],
    # 'finned_jellyfish_0.sudoku': [],
    # 'finned_jellyfish_1.sudoku': [],
    # 'finned_jellyfish_2.sudoku': [],
    # 'finned_jellyfish_3.sudoku': [],
    # 'finned_swordfish_0.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesClaiming(),
    #     # tech.LockedCandidatesPointing(),
    #     tech.NakedTriple(),
    #     tech.FinnedSwordFish(),
    #     FinnedXWing(),
    #     tech.ShashimiXWing(),
    # ],
    # 'finned_swordfish_1.sudoku': [],
    # 'finned_swordfish_2.sudoku': [],
    # 'finned_swordfish_3.sudoku': [],
    # 'finned_x_wing_00.sudoku': [CrossHatch(),
    #         HiddenSingle(),
    #         NakedPair(),
    #         tech.LockedCandidatesPointing(),
    #         tech.LockedCandidatesClaiming(),
    #         UniqueRectangleType1(),
    #         # UniqueRectangleType2(),
    #         UniqueRectangleType4(),
    #         FinnedXWing(),
    #         # tech.Bug(),
    #         # tech.HiddenPair(),
    #         # tech.NakedTriple(),
    #         # tech.XWing(),
    #         # tech.XyWing(),
    #                             ],

    # 'finned_x_wing_04.sudoku': [],
    # 'finned_x_wing_05.sudoku': [],
    # 'finned_x_wing_06.sudoku': [],
    # 'finned_x_wing_07.sudoku': [],
    # 'finned_x_wing_08.sudoku': [],
    # 'finned_x_wing_09.sudoku': [],
    # 'finned_x_wing_10.sudoku': [],
    # 'finned_x_wing_11.sudoku': [],
    # 'finned_x_wing_12.sudoku': [],
    # 'finned_x_wing_13.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     UniqueRectangleType4(),
    #     FinnedXWing()
    # ],
    # 'finned_x_wing_14.sudoku': [],
    # 'finned_x_wing_15.sudoku': [],
    # 'finned_x_wing_16.sudoku': [],
    # 'finned_x_wing_17.sudoku': [],
    # 'finned_x_wing_cols_1_fin.sudoku': [],
    # 'finned_x_wing_rows_1_fin.sudoku': [],
    # 'fishy_cycle.sudoku': [],
    # 'fishy_cycle_0.sudoku': [],
    # 'fishy_cycle_1.sudoku': [],
    # 'hidden_pair_1.sudoku': [],
    # 'hidden_pair_col.sudoku': [],
    # 'hidden_pair_fence.sudoku': [],
    # 'hidden_pair_row.sudoku': [],
    # 'hidden_quad_5.sudoku': [],
    # 'hidden_quad_6.sudoku': [],
    # 'hidden_quad_7.sudoku': [],
    # 'hidden_unique_rectangle_0.sudoku': [],
    # 'hidden_unique_rectangle_1.sudoku': [],
    # 'hidden_unique_rectangle_2.sudoku': [],
    # 'hidden_unique_rectangle_3.sudoku': [],
    # 'hidden_unique_rectangle_4.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesClaiming(),
    #     UniqueRectangleType4(),
    #     tech.NakedTriple(),
    #     tech.ShashimiXWing(),
    #     tech.HiddenUniqueRectangle(),
    #     RemotePair(),
    #     tech.SwordFish(),
    #     tech.Bug()
    # ],
    'hidden_unique_rectangle_5.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        RemotePair(),
        tech.XWing(),
        tech.HiddenUniqueRectangle(),
        tech.Bug()
    ],
    # 'hidden_unique_rectangle_nec.sudoku': [],
    # 'hidden_unique_rectangle_nwc.sudoku': [],
    # 'hidden_unique_rectangle_sec.sudoku': [],
    # 'hidden_unique_rectangle_ser.sudoku': [],
    # 'hidden_unique_rectangle_swc.sudoku': [],
    # 'hidden_unique_rectangle_swr.sudoku': [],
    'jellyfish_0.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        tech.LockedCandidatesPointing(),
        tech.LockedCandidatesClaiming(),
        tech.NakedTriple(),
        tech.HiddenPair(),
        tech.JellyFish()
    ],
    # 'jellyfish_1.sudoku': [],
    # 'jellyfish_2.sudoku': [],
    # 'jellyfish_of_1_in_rows.sudoku': [],
    # 'jellyfish_of_3_in_cols.sudoku': [],
    'locked_candidates_claiming_col.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        NakedPair(),
        tech.LockedCandidatesPointing(),
        tech.LockedCandidatesClaiming(),
        UniqueRectangleType1()
    ],
    'locked_candidates_claiming_row.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        NakedPair(),
        tech.LockedCandidatesPointing(),
        tech.LockedCandidatesClaiming(),
        UniqueRectangleType1()
    ],
    'locked_candidates_pointing_col.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        NakedPair(),
        tech.LockedCandidatesPointing(),
        tech.LockedCandidatesClaiming(),
        UniqueRectangleType1()
    ],
    'locked_candidates_pointing_row.sudoku': [
        CrossHatch(),
        HiddenSingle(),
        NakedPair(),
        tech.LockedCandidatesPointing(),
        tech.LockedCandidatesClaiming(),
        UniqueRectangleType1()
    ],
    # 'maelstrom_0.sudoku': [],
    # 'medusa_coloring_3d.sudoku': [],
    # 'medusa_coloring_3d_0.sudoku': [],
    'naked_pair_col.sudoku': [CrossHatch(), HiddenSingle(), NakedPair()],
    'naked_pair_fence.sudoku': [CrossHatch(), HiddenSingle(), NakedPair()],
    # 'naked_pair_row.sudoku': [],
    # 'naked_quad_4.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     tech.HiddenPair(),
    #     FinnedXWing(),
    #     tech.NakedQuad(),
    #     tech.XWing(),
    #     tech.LockedCandidatesClaiming(),
    #     NakedPair(),
    #
    # ],
    # 'naked_quad_5.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     tech.LockedCandidatesClaiming(),
    #     FinnedXWing(),
    #     tech.NakedQuad(),
    #     tech.ShashimiXWing()
    # ],
    # 'naked_quad_6.sudoku': [],
    # 'naked_quad_7.sudoku': [],
    # 'naked_quad_col.sudoku': [],
    # 'naked_quad_fence.sudoku': [],
    # 'naked_quad_row.sudoku': [],
    # 'naked_triple_col.sudoku': [],
    # 'naked_triple_fence.sudoku': [],
    # 'naked_triple_row.sudoku': [],
    # 'nightmare_0.sudoku': [],
    # 'remote_pair_0.sudoku': [],
    # 'remote_pair_1.sudoku': [],
    # 'remote_pair_2.sudoku': [],
    # 'remote_pair_row.sudoku': [],
    # 'shashimi_jellyfish_0.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     NakedPair(),
    #     tech.ShashimiJellyFish()
    # ],
    # 'shashimi_jellyfish_1.sudoku': [],
    # 'shashimi_jellyfish_2.sudoku': [],
    # 'shashimi_jellyfish_3.sudoku': [],
    # 'shashimi_swordfish_0.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     NakedPair(),
    #     tech.LockedCandidatesPointing(),
    #     tech.LockedCandidatesClaiming(),
    #     tech.NakedTriple(),
    #     tech.ShashimiXWing(),
    #     tech.ShashimiSwordFish()
    # ],
    # 'shashimi_swordfish_1.sudoku': [],
    # 'shashimi_swordfish_2.sudoku': [],
    # 'shashimi_swordfish_3.sudoku': [],
    # 'shashimi_swordfish_4.sudoku': [],
    # 'shashimi_swordfish_5.sudoku': [],
    # 'shashimi_sword_fish_cols_1_fin.sudoku': [],
    # 'shashimi_sword_fish_cols_2_fins.sudoku': [],
    # 'shashimi_sword_fish_rows_1_fin.sudoku': [],
    # 'shashimi_sword_fish_rows_2_fins.sudoku': [],
    # 'shashimi_x_wing_00.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     tech.ShashimiXWing(),
    # ],
    # 'shashimi_x_wing_01.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.ShashimiXWing()
    # ],
    # 'shashimi_x_wing_02.sudoku': [],
    # 'shashimi_x_wing_03.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     tech.ShashimiXWing()
    # ],
    # 'shashimi_x_wing_04.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     tech.ShashimiXWing()
    #
    # ],
    # 'shashimi_x_wing_05.sudoku': [],
    # 'shashimi_x_wing_06.sudoku': [],
    # 'shashimi_x_wing_07.sudoku': [],
    # 'shashimi_x_wing_08.sudoku': [],
    # 'shashimi_x_wing_09.sudoku': [],
    # 'shashimi_x_wing_col_1_fin.sudoku': [],
    # 'shashimi_x_wing_col_2_fins.sudoku': [],
    # 'shashimi_x_wing_row_1_fin.sudoku': [],
    # 'shashimi_x_wing_row_2_fins.sudoku': [],
    # 'simple_coloring_0.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     NakedPair(),
    #     UniqueRectangleType4(),
    #     RemotePair(),
    #     tech.SimpleColoring(),
    # ],
    # 'simple_coloring_1.sudoku': [],
    # 'simple_coloring_trap_0.sudoku': [],
    # 'sue_de_coq_0.sudoku': [],
    # 'sue_de_coq_1.sudoku': [],
    # 'sue_de_coq_2.sudoku': [],
    # 'sue_de_coq_col.sudoku': [],
    # 'sue_de_coq_row.sudoku': [],
    # 'swordfish_0.sudoku': [
    #     CrossHatch(),
    #     HiddenSingle(),
    #     tech.LockedCandidatesPointing(),
    #     NakedPair(),
    #     UniqueRectangleType2(),
    #     tech.SwordFish()
    # ],
    # 'swordfish_1.sudoku': [],
    # 'swordfish_2.sudoku': [],
    # 'swordfish_3.sudoku': [],
    # 'swordfish_4.sudoku': [],
    # 'swordfish_5.sudoku': [],
    # 'swordfish_6.sudoku': [],
    # 'swordfish_of_5_in_rows.sudoku': [],
    # 'swordfish_of_8_in_cols.sudoku': [],
    # 'unique_rectangle_type3_00.sudoku': [
    #     CrossHatch(),
    #         HiddenSingle(),
    #         # NakedPair(),
    #         # tech.LockedCandidatesPointing(),
    #         # tech.LockedCandidatesClaiming(),
    # ],
    # 'unique_rectangle_type3_01.sudoku': [],
    # 'unique_rectangle_type3_02.sudoku': [],
    # 'unique_rectangle_type3_03.sudoku': [],
    # 'unique_rectangle_type3_04.sudoku': [],
    # 'unique_rectangle_type3_05.sudoku': [],
    # 'unique_rectangle_type3_06.sudoku': [],
    # 'unique_rectangle_type3_07.sudoku': [],
    # 'unique_rectangle_type3_east_col.sudoku': [],
    # 'unique_rectangle_type3_east_fence.sudoku': [],
    # 'unique_rectangle_type3_north_row.sudoku': [],
    # 'unique_rectangle_type3_south_row.sudoku': [],
    # 'unique_rectangle_type3_west_fence.sudoku': [],
    # 'wxyz_wing_0.sudoku': [],
    # 'wxyz_wing_19.sudoku': [],
    # 'wxyz_wing_4.sudoku': [],
    # 'wxyz_wing_5.sudoku': [],
    # 'wxyz_wing_6.sudoku': [],
    # 'wxyz_wing_cols_2_fences.sudoku': [],
    # 'wxyz_wing_cols_3_fences.sudoku': [],
    # 'wxyz_wing_rows_2_fences.sudoku': [],
    # 'wxyz_wing_rows_3_fences.sudoku': [],
    # 'w_wing_type_d_0.sudoku': [],
    # 'w_wing_type_d_6.sudoku': [],
    # 'xy_chain.sudoku': [],
    # 'xy_chain_0.sudoku': [],
    # 'xy_chain_1.sudoku': [],
    # 'xy_chain_2.sudoku': [],
    # 'xy_wing_00.sudoku': [],
    # 'xy_wing_cols_2_fences.sudoku': [],
    # 'xy_wing_north_east_3_fences.sudoku': [
    #     CrossHatch(),
    #     NakedPair(),
    #     FinnedXWing(),
    #     tech.XyWing()
    # ],
    # 'xy_wing_north_west_3_fences.sudoku': [],
    # 'xy_wing_rows_2_fences.sudoku': [],
    # 'xy_wing_south_east_3_fences.sudoku': [],
    # 'xy_wing_south_west_3_fences.sudoku': [],
    # 'x_chain.sudoku': [],
    # 'x_chain_0.sudoku': [],

}


@pytest.mark.parametrize('data',
                         [filename for filename in next(walk('C:\\repos\\logics0\\solve_files'), (None, None, []))[2]])
def test_file_puzzle1(data):

    if data not in skip_dict:
        pytest.skip(f'explicitly skipped: "{data}"')
    techniques = skip_dict[data]
    if len(techniques) == 0:
        techniques = Solving.sudoku_techniques()
    f = open(f'C:\\repos\\logics0\\solve_files\\{data}', 'r')
    string = f.read()
    f.close()
    string = f'{data}\n{string}'
    puzzle = Sudoku(string)
    edits = 0
    edit_dict = {}
    while True:
        original_edits = edits
        for tech1 in techniques:
            _edits = tech1.solve0(puzzle)
            if tech1.__class__.__name__ not in edit_dict:
                edit_dict[tech1.__class__.__name__] = 0
            edit_dict[tech1.__class__.__name__] += _edits
            edits = edits + _edits
        if original_edits == edits:
            break
    if puzzle.is_solved():
        return
    for tech1 in edit_dict:
        if edit_dict[tech1] == 0:
            continue
        print(f'{tech1}: {edit_dict[tech1]}')
    print(f'Total edits: {edits}')
    print(puzzle.to_string())
    assert False
