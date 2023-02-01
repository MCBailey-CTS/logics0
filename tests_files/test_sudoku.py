# from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# from techniques.LockedCandidatesPointing import LockedCandidatesPointing

EXPLICITLY = "EXPLICITLY"

# @pytest.mark.parametrize("puzzle_string, constructor, techniques", [
#
#     # [Constants.sudoku_annoying_00.__name__, Sudoku, Solving.sudoku_techniques()],
#
#     ('sudoku_unique_rectangle_type1_00', Sudoku,
#      [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()]),
#     ('sudoku_unique_rectangle_type1_01', Sudoku,
#      [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()]),
#     ('sudoku_unique_rectangle_type1_02', Sudoku, [CrossHatch(), NakedPair(), UniqueRectangleType1()]),
#     ('sudoku_unique_rectangle_type1_03', Sudoku,
#      [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()]),
#     ('sudoku_unique_rectangle_type1_05', Sudoku, [CrossHatch(), NakedPair(), UniqueRectangleType1()]),
#     # ('sudoku_unique_rectangle_type4_00', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
#     # ('sudoku_unique_rectangle_type4_01', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
#     # ('sudoku_unique_rectangle_type4_02', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
#     # ('sudoku_unique_rectangle_type4_03', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
#     # ('sudoku_unique_rectangle_type4_04', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
#     # ('sudoku_unique_rectangle_type4_05', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
#     # ('sudoku_unique_rectangle_type4_east_rows', Sudoku,
#     #  [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
#     # ('sudoku_unique_rectangle_type4_west_rows', Sudoku,
#     #  [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
#     # ('sudoku_unique_rectangle_type4_west_cols', Sudoku,
#     #  [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
#     # ('sudoku_unique_rectangle_type4_east_cols', Sudoku,
#     #  [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]),
#     # ('sudoku_naked_triple_0', Sudoku,
#     #  [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), tech.NakedTriple()]),
#     # ('sudoku_naked_triple_2', Sudoku, [CrossHatch(), HiddenSingle(), tech.NakedTriple()]),
#     # ('sudoku_naked_triple_3', Sudoku, [CrossHatch(), NakedPair(), tech.NakedTriple()]),
#     # ('sudoku_naked_triple_4', Sudoku, [CrossHatch(), HiddenSingle(), tech.NakedTriple()]),
#     # ('sudoku_naked_triple_row', Sudoku, [CrossHatch(), tech.NakedTriple()]),
#     # ('sudoku_naked_triple_1', Sudoku, [CrossHatch(), tech.NakedTriple()]),
#     # ('sudoku_naked_triple_5', Sudoku, [CrossHatch(), tech.NakedTriple()]),
#     # ('sudoku_naked_triple_6', Sudoku, [CrossHatch(), tech.NakedTriple()]),
#     # (Constants.sudoku_naked_triple_9.__name__, Sudoku,
#     #  [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), tech.NakedTriple()]),
#     ('sudoku_bug', Sudoku, [CrossHatch(), Bug()]),
#     # ('sudoku_x_wing_row', Sudoku, [CrossHatch(), tech.XWing()]),
#     # ('sudoku_x_wing_col', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair(), Bug(), tech.XWing()]),
#     ('sudoku_unique_rectangle_type2_00', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
#     ("sudoku_unique_rectangle_type2_01", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
#     ("sudoku_unique_rectangle_type2_02", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
#     ("sudoku_unique_rectangle_type2_03", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
#     ("sudoku_unique_rectangle_type2_04", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
#     ("sudoku_unique_rectangle_type2_05", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
#     ("sudoku_unique_rectangle_type2_06", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
#     ("sudoku_unique_rectangle_type2_08", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
#     ("sudoku_unique_rectangle_type2_09", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
#     ("sudoku_unique_rectangle_type2_10", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
#     ("sudoku_unique_rectangle_type2_11", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
#     ("sudoku_unique_rectangle_type2_12", Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType2()]),
#     ('sudoku_intricate_0', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
#     ('sudoku_intricate_1', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
#     ('sudoku_intricate_2', Sudoku, [CrossHatch(), LockedCandidatesClaiming()]),
#     ('sudoku_intricate_3', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
#     ('sudoku_intricate_4', Sudoku, [CrossHatch(), LockedCandidatesPointing()]),
#     ('sudoku_intricate_5', Sudoku, [CrossHatch(), HiddenSingle(), LockedCandidatesPointing()]),
#     ('sudoku_intricate_6', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
#     ('sudoku_intricate_7', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
#     ('sudoku_intricate_8', Sudoku, [CrossHatch(), HiddenSingle(), NakedPair()]),
#     ('sudoku_locked_candidates_claiming_0', Sudoku,
#      [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()]),
#     ('sudoku_locked_candidates_claiming_1', Sudoku,
#      [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()]),
#     ('sudoku_locked_candidates_claiming_2', Sudoku,
#      [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming()]),
#     ('sudoku_locked_candidates_pointing_0', Sudoku,
#      [CrossHatch(), HiddenSingle(), LockedCandidatesPointing()]),
#     ('sudoku_easiest_0', Sudoku, [CrossHatch()]),
#     ('sudoku_easy_as_pie_0', Sudoku, [CrossHatch()]),
#     ('sudoku_first_lesson', Sudoku, [CrossHatch()]),
#     ('sudoku_hidden_single_0', Sudoku, [CrossHatch(), HiddenSingle()]),
#     ('sudoku_hidden_single_1', Sudoku, [CrossHatch(), HiddenSingle()]),
#     ('sudoku_hidden_single_2', Sudoku, [CrossHatch(), HiddenSingle()]),
#     ('sudoku_mild_0', Sudoku, [CrossHatch()]),
#     ('sudoku_mild_1', Sudoku, [CrossHatch()]),
#     ('sudoku_mild_2', Sudoku, [CrossHatch()]),
#     ('sudoku_mild_3', Sudoku, [CrossHatch()]),
#     ('sudoku_mild_4', Sudoku, [CrossHatch()]),
#     ('sudoku_moderate_0', Sudoku, [CrossHatch(), NakedPair()]),
#     ('sudoku_naked_pair_0', Sudoku, [CrossHatch(), NakedPair(), ]),
#     ('sudoku_naked_pair_1', Sudoku, [CrossHatch(), NakedPair()]),
#     ('sudoku_naked_pair_2', Sudoku, [CrossHatch(), NakedPair()]),
#     ('sudoku_picnic_0', Sudoku, [CrossHatch(), ]),
#     ('sudoku_picnic_1', Sudoku, [CrossHatch()]),
#     ('sudoku_picnic_2', Sudoku, [CrossHatch()]),
#     ('sudoku_second_lesson_0', Sudoku, [CrossHatch(), ]),
#     ('sudoku_simple_0', Sudoku, [CrossHatch()]),
#
#     ['sudoku_difficult_00', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
#     ['sudoku_difficult_03', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
#     ['sudoku_difficult_06', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
#     ['sudoku_difficult_10', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
#     # ['sudoku_difficult_12', Sudoku,
#     #  [CrossHatch(), HiddenSingle(), LockedCandidatesPointing(), tech.NakedTriple()]],
#     ['sudoku_difficult_13', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
#     ['sudoku_difficult_18', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
#     ['sudoku_difficult_19', Sudoku, [CrossHatch(), HiddenSingle(), tech.HiddenPair()]],
#     # ['sudoku_difficult_22', Sudoku, [CrossHatch(), HiddenSingle(), tech.XWing()]],
#     ['sudoku_difficult_23', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
#     ['sudoku_difficult_24', Sudoku,
#      [CrossHatch(), HiddenSingle(), NakedPair(), UniqueRectangleType1()]],
#     # ['sudoku_difficult_25', Sudoku, [CrossHatch(), LockedCandidatesClaiming(), tech.NakedTriple()]],
#     # ['sudoku_difficult_26', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]],
#     ['sudoku_difficult_27', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType1()]],
#     # ['sudoku_difficult_29', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()]],
#     # ['sudoku_difficult_30', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()]],
#     # ['sudoku_difficult_32', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()]],
#     # ['sudoku_difficult_33', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.XWing()]],
#     # ['sudoku_difficult_34', Sudoku,
#     #  [CrossHatch(), HiddenSingle(), LockedCandidatesClaiming(), UniqueRectangleType4(),
#     #   Bug()]],
#     # ['sudoku_difficult_36', Sudoku,
#     #  [CrossHatch(), LockedCandidatesPointing(), Bug(), tech.NakedTriple()]],
#     # ['sudoku_difficult_37', Sudoku, [CrossHatch(), HiddenSingle(), Bug(), tech.NakedTriple()]],
#     ['sudoku_difficult_38', Sudoku, [CrossHatch(), HiddenSingle(), Bug()]],
#     # ['sudoku_difficult_39', Sudoku, [CrossHatch(), HiddenSingle(), UniqueRectangleType4()]],
#
#
# ])
# def test_default_puzzle(puzzle_string, constructor, techniques):
#     if "\n" in puzzle_string:
#         pytest.skip(puzzle_string)
#     result = getattr(Constants, puzzle_string)
#     assert default_test_puzzle(result(), constructor, techniques)





# @staticmethod
# def sudoku_almost_locked_candidates_0():
#     return f"""
#     almost_locked_candidates_0.sudoku
#     9
#     .7.|...|198
#     829|713|564
#     614|985|237
#     ---+---+---
#     15.|.9.|.7.
#     .96|357|..1
#     ..7|..1|.59
#     ---+---+---
#     762|138|945
#     ...|629|713
#     931|574|...
#     """

# @staticmethod
# def sudoku_almost_locked_candidates_1():
#     return f"""
#     almost_locked_candidates_1.sudoku
#     9
#     4 0 0 0 6 0 0 2 0
#     8 6 7 4 2 5 3 9 1
#     0 0 0 8 0 7 6 4 5
#     7 0 0 2 0 0 0 8 6
#     3 2 0 0 0 6 0 1 9
#     6 9 0 0 0 4 2 0 0
#     9 7 0 3 0 2 0 0 0
#     5 0 3 0 0 8 9 0 2
#     0 8 0 0 5 0 0 0 0
#     """

# @staticmethod
# def sudoku_almost_locked_candidates_2():
#     return f"""
#     almost_locked_candidates_2.sudoku
#     9
#     .7.|..6|3..
#     .5.|2..|.89
#     ..1|...|2..
#     ---+---+---
#     4.8|..2|...
#     ...|1.5|...
#     ...|6..|8.1
#     ---+---+---
#     ..4|...|1..
#     18.|..4|.5.
#     ..3|8..|.7.
#     shashimi xwing
#     """

# @staticmethod
# def sudoku_almost_locked_candidates_3():
#     return f"""
#     almost_locked_candidates_3.sudoku
#     9
#     987|..2|.4.
#     132|4..|.9.
#     .4.|7.9|28.
#     ---+---+---
#     .98|...|175
#     .1.|975|86.
#     75.|..1|93.
#     ---+---+---
#     .69|12.|.5.
#     .71|..3|629
#     .2.|697|418
#     """

# @staticmethod
# def sudoku_almost_locked_candidates_4():
#     return f"""
#     almost_locked_candidates_4.sudoku
#     9
#     ..9|..5|.43
#     ...|...|...
#     .5.|..3|.28
#     ---+---+---
#     .8.|.2.|.5.
#     ..6|...|9..
#     .9.|.4.|.3.
#     ---+---+---
#     32.|9..|.1.
#     ...|...|...
#     41.|5..|6..
#     """

# @staticmethod
# def sudoku_almost_locked_candidates_5():
#     return f"""
#     almost_locked_candidates_5.sudoku
#     9
#     0 0 0 1 0 0 0 0 4
#     2 0 7 0 0 0 0 0 5
#     0 1 0 5 0 0 3 6 0
#     0 0 5 9 1 0 0 0 6
#     0 0 0 0 0 0 0 0 0
#     8 0 0 0 2 6 9 0 0
#     0 8 3 0 0 5 0 1 0
#     5 0 0 0 0 0 7 0 2
#     1 0 0 0 0 8 0 0 0
#     """

# @staticmethod
# def sudoku_almost_locked_candidates_6():
#     return f"""
#     almost_locked_candidates_6.sudoku
#     9
#     2 6 1 0 0 8 9 0 5
#     3 9 8 6 0 5 4 0 2
#     4 5 7 0 9 0 8 0 6
#     9 1 4 0 6 0 5 8 3
#     8 2 5 0 0 0 6 9 7
#     7 3 6 8 5 9 1 2 4
#     6 7 2 5 8 1 3 4 9
#     1 4 3 9 2 6 7 5 8
#     5 8 9 3 0 0 2 6 1
#     """

# @staticmethod
# def sudoku_annoying_01():
#     return f"""
#     annoying_01.sudoku
#     9
#     9 4 2 5 6 1 7 8 3
#     . 8 . 7 . 4 . . 1
#     1 . 7 . 8 . 5 4 .
#     8 . . 1 . 9 . 7 .
#     . . . 6 . 7 . . 8
#     7 9 . 3 . 8 . . 4
#     . . 9 4 . . 8 . 7
#     . 7 . 8 . 5 4 3 .
#     4 . 8 . 7 . . 1 .
#     """

# @staticmethod
# def sudoku_annoying_03():
#     return f"""
#     annoying_03.sudoku
#     9
#     2 4 9 5 3 7 1 6 8
#     7 1 . . 2 8 . 3 4
#     . . . . 4 1 2 . 7
#     . 9 2 1 7 . 8 4 3
#     4 3 7 8 9 2 6 1 5
#     . . 1 3 . 4 7 2 9
#     1 . . 4 8 . . 7 2
#     . 7 4 2 1 . . 8 6
#     . 2 . 7 . 3 4 . 1
#     """

# @staticmethod
# def sudoku_annoying_04():
#     return f"""
#     annoying_04.sudoku
#     9
#     . 5 4 . . 6 7 . .
#     3 . . . . . . 6 .
#     6 . 7 2 . . . . .
#     . 6 . . 8 9 1 . 5
#     8 . 9 5 . 2 6 . 7
#     4 . 5 6 3 . 8 2 9
#     . . . . 6 4 9 . .
#     . . . . 2 . . . 6
#     . . 6 9 . . 2 8 .
#     """

# @staticmethod
# def sudoku_annoying_08():
#     return f"""
#     annoying_08.sudoku
#     9
#     . 5 2 8 . . . 4 .
#     . 3 4 2 . . . 7 9
#     . 7 6 1 . . . 2 5
#     . 1 9 . 8 . . 5 .
#     . 2 7 9 3 . 4 1 8
#     . 4 8 . 1 . 9 6 .
#     2 8 . . . 1 . 9 4
#     4 9 1 . 2 8 5 3 .
#     7 6 . . . 9 2 8 1
#     """

# @staticmethod
# def sudoku_annoying_09():
#     return f"""
#     annoying_09.sudoku
#     9
#     . 5 . 8 3 . 7 . 6
#     8 . 7 4 . 1 3 . .
#     3 . 2 7 5 . . 8 .
#     . . . . . . 8 . .
#     . 3 . 9 . 5 . 7 .
#     . . 5 . . . . . .
#     . . . . 9 . 5 3 7
#     5 . 3 1 . 7 2 . 8
#     7 . . 5 . 3 . 4 .
#     """

# @staticmethod
# def sudoku_annoying_10():
#     return f"""
#     annoying_10.sudoku
#     9
#     3 4 . . 2 . 1 7 .
#     2 . 9 1 . 4 3 5 8
#     . . 1 . . 3 2 4 .
#     . . . 6 3 5 4 1 2
#     1 2 3 4 9 7 6 8 5
#     4 . . 8 1 2 9 3 7
#     . 3 . 2 . 1 . . 4
#     6 . 4 3 . . 5 2 1
#     . 1 2 . 4 . . . 3
#     """

# @staticmethod
# def sudoku_annoying_12():
#     return f"""
#     annoying_12.sudoku
#     9
#     5 . 2 . 6 9 3 7 8
#     9 3 8 . . 5 6 4 1
#     6 . 7 3 8 . 2 5 9
#     1 8 4 6 5 . . . 2
#     2 6 5 . . . 4 8 .
#     3 7 9 . . 8 1 6 5
#     4 5 1 . . 2 8 . 6
#     7 9 3 8 1 6 5 2 4
#     8 2 6 5 . . . 1 .
#     """

# @staticmethod
# def sudoku_annoying_14():
#     return f"""
#     annoying_14.sudoku
#     9
#     9 . . 2 . 7 . 6 .
#     . . . . . . 9 . .
#     . . 7 9 4 6 . . 1
#     8 2 . 4 . . . 9 .
#     5 7 9 8 1 . 4 . 6
#     . 3 4 . . 9 . 8 .
#     4 . . 7 9 8 2 . .
#     . . 8 . . . . 4 9
#     . 9 . 3 . 4 . . .
#     """

# @staticmethod
# def sudoku_annoying_15():
#     return f"""
#     annoying_15.sudoku
#     9
#     4 3 5 1 8 9 . . .
#     6 9 7 2 4 5 3 8 1
#     1 2 8 6 3 7 4 5 9
#     3 8 . . . 1 . 9 .
#     9 . 1 . 2 3 8 . 4
#     7 . . . . 8 1 3 .
#     2 1 3 . . 6 7 4 8
#     5 7 6 8 1 4 9 2 3
#     8 4 9 3 7 2 5 1 6
#     """

# @staticmethod
# def sudoku_annoying_16():
#     return f"""
#     annoying_16.sudoku
#     9
#     4 1 7 9 8 2 5 6 3
#     8 5 2 6 . . 9 7 1
#     3 6 9 1 5 7 4 8 2
#     5 7 1 4 6 . 3 2 .
#     6 . 4 5 . . . . 7
#     . 3 8 . . 1 6 5 4
#     . 8 5 . 1 . 7 . 6
#     1 4 6 . . 5 . . .
#     7 . 3 8 . 6 . . 5
#     """

# @staticmethod
# def sudoku_annoying_18():
#     return f"""
#     annoying_18.sudoku
#     9
#     . . 7 . . . . . .
#     4 . 9 1 7 . 5 . .
#     2 . 8 . 6 . 9 . 7
#     . . . 4 . 6 . . .
#     6 . 5 2 . 8 7 . 9
#     . . . 7 . 5 . . .
#     1 . 3 6 5 . 8 . 2
#     . . 6 . . 7 3 . 1
#     . . . . . 1 6 . .
#     """

# @staticmethod
# def sudoku_annoying_19():
#     return f"""
#     annoying_19.sudoku
#     9
#     . . . . 3 . . 7 .
#     7 . 8 1 . 6 . . .
#     3 . 1 . . . 8 . .
#     9 . . 3 . 2 . . .
#     . 3 . . . . . 4 .
#     . . . 6 . 5 . . 9
#     . . 4 . . . 9 . 3
#     . . 3 2 . 4 7 . 5
#     . 8 . . 5 3 . . .
#     """

# @staticmethod
# def sudoku_annoying_20():
#     return f"""
#     annoying_20.sudoku
#     9
#     4..|9..|.7.
#     .76|.85|...
#     ..5|...|...
#     ---+---+---
#     1.4|2..|...
#     .8.|1.9|.5.
#     ...|..3|4.1
#     ---+---+---
#     ...|...|7..
#     ...|36.|59.
#     .2.|..7|..8
#     """

# @staticmethod
# def sudoku_annoying_21():
#     return f"""
#     annoying_21.sudoku
#     9
#     .4.|2.5|.3.
#     8..|97.|4..
#     ...|...|.92
#     ---+---+---
#     ..4|...|.78
#     ...|...|...
#     71.|...|3..
#     ---+---+---
#     58.|...|...
#     ..2|.13|..5
#     .9.|8.6|.2.
#     """

# @staticmethod
# def sudoku_annoying_24():
#     return f"""
#     annoying_24.sudoku
#     9
#     6..|5..|2..
#     7..|..6|.49
#     .9.|4.7|3..
#     ---+---+---
#     .3.|...|62.
#     4..|...|..7
#     .26|...|.3.
#     ---+---+---
#     ..1|3.5|.8.
#     37.|1..|..6
#     ..2|..9|..3
#     """

# @staticmethod
# def sudoku_annoying_31():
#     return f"""
#     annoying_31.sudoku
#     9
#     ..5|8.4|.31
#     3..|.5.|...
#     ..9|.6.|.5.
#     ---+---+---
#     9..|..7|..8
#     5..|...|..2
#     2..|5..|..9
#     ---+---+---
#     .9.|.1.|8..
#     ...|.8.|..7
#     86.|9.3|4..
#     """

# @staticmethod
# def sudoku_annoying_36():
#     return f"""
#     annoying_36.sudoku
#     9
#     ...|...|..3
#     .4.|..3|1.5
#     .1.|4..|69.
#     ---+---+---
#     8..|9.4|...
#     .57|...|46.
#     ...|7.6|..2
#     ---+---+---
#     .89|..1|.5.
#     5.1|3..|.8.
#     7..|...|...
#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type1_00():
#     return f"""
#     avoidable_rectangle_type1_00.sudoku
#     9
# 123456789a 123456789a _______8_a 123456789b __3______b 123456789b 123456789c ___4_____c 123456789c
# 123456789a 123456789a 123456789a 1________b ______7__b _____6___b 123456789c 123456789c 123456789c
# _____6___a 123456789a 123456789a 123456789b _______8_b 123456789b 123456789c 123456789c 123456789c
# ______7__d ________9d 123456789d 123456789e 123456789e 123456789e _______8_f 123456789f __3______f
# 123456789d 123456789d ___4_____d 123456789e 123456789e 123456789e ________9f 123456789f 123456789f
# 1________d 123456789d _2_______d 123456789e 123456789e 123456789e 123456789f ____5____f ______7__f
# 123456789g 123456789g 123456789g 123456789h _____6___h 123456789h 123456789i 123456789i _2_______i
# 123456789g 123456789g 123456789g ____5____h _2_______h ________9h 123456789i 123456789i 123456789i
# 123456789g _______8_g 123456789g 123456789h ___4_____h 123456789h __3______i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type1_01():
#     return f"""
#     avoidable_rectangle_type1_01.sudoku
#     9
# 123456789a ________9a __3______a _2_______b 123456789b 123456789b ____5____c 123456789c 123456789c
# 123456789a 123456789a 123456789a 123456789b 123456789b ___4_____b ________9c 123456789c 123456789c
# ___4_____a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c _______8_c 123456789c
# 123456789d ___4_____d ________9d __3______e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d ______7__d 123456789d ________9e 123456789e 1________e 123456789f ____5____f 123456789f
# 123456789d 123456789d 123456789d 123456789e 123456789e ______7__e _2_______f __3______f 123456789f
# 123456789g _______8_g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i _____6___i
# 123456789g 123456789g 1________g _______8_h 123456789h 123456789h 123456789i 123456789i 123456789i
# 123456789g 123456789g _2_______g 123456789h 123456789h ____5____h __3______i 1________i 123456789i
#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type1_02():
#     return f"""
#     avoidable_rectangle_type1_02.sudoku
#     9
# 123456789a 123456789a 123456789a _______8_b 123456789b 123456789b 123456789c 123456789c _2_______c
# 123456789a 123456789a 123456789a 123456789b 123456789b _____6___b ___4_____c 123456789c ____5____c
# 1________a 123456789a 123456789a _2_______b ________9b ___4_____b 123456789c 123456789c ______7__c
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e _2_______f 123456789f ________9f
# 123456789d ____5____d __3______d 123456789e 123456789e 123456789e ______7__f _______8_f 123456789f
# _______8_d 123456789d ___4_____d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# ___4_____g 123456789g 123456789g __3______h ____5____h ______7__h 123456789i 123456789i _____6___i
# ____5____g 123456789g _____6___g ________9h 123456789h 123456789h 123456789i 123456789i 123456789i
# _2_______g 123456789g 123456789g 123456789h 123456789h _______8_h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type1_03():
#     return f"""
#     avoidable_rectangle_type1_03.sudoku
#     9
# 123456789a 123456789a 123456789a 123456789b ______7__b __3______b 123456789c ____5____c 123456789c
# _2_______a 123456789a 123456789a _______8_b 123456789b 123456789b 123456789c 123456789c __3______c
# 123456789a 123456789a 123456789a 123456789b _2_______b 123456789b 123456789c _______8_c 123456789c
# 123456789d 1________d ____5____d ______7__e 123456789e 123456789e 123456789f 123456789f _____6___f
# __3______d _2_______d 123456789d 123456789e 123456789e 123456789e 123456789f 1________f _______8_f
# _______8_d 123456789d 123456789d 123456789e 123456789e _2_______e ________9f __3______f 123456789f
# 123456789g ________9g 123456789g 123456789h 1________h 123456789h 123456789i 123456789i 123456789i
# 1________g 123456789g 123456789g 123456789h 123456789h _____6___h 123456789i 123456789i ________9i
# 123456789g _____6___g 123456789g ____5____h ___4_____h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type1_04():
#     return f"""
#     avoidable_rectangle_type1_04.sudoku
#     9
#     _____6___a 123456789a 123456789a ________9b 123456789b 123456789b ____5____c 1________c ___4_____c
#     ____5____a ________9a 1________a _____6___b ___4_____b __3______b _______8_c _2_______c ______7__c
#     ______7__a _2_______a ___4_____a _______8_b ____5____b 1________b ________9c __3______c _____6___c
#     _______8_d ____5____d _2_______d ______7__e _____6___e ___4_____e 1________f ________9f __3______f
#     ___4_____d 123456789d ________9d 1________e 123456789e 123456789e ______7__f 123456789f ____5____f
#     1________d ______7__d 123456789d ____5____e 123456789e 123456789e ___4_____f 123456789f _2_______f
#     _2_______g 123456789g 123456789g ___4_____h 123456789h 123456789h __3______i ____5____i _______8_i
#     __3______g 123456789g 123456789g _2_______h 123456789h 123456789h _____6___i ___4_____i ________9i
#     ________9g ___4_____g 123456789g __3______h _______8_h 123456789h _2_______i ______7__i 1________i
#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type1_05():
#     return f"""
#     avoidable_rectangle_type1_05.sudoku
#     9
# 123456789a 123456789a _____6___a 123456789b _2_______b _______8_b 123456789c ____5____c 123456789c
# 123456789a _______8_a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# 123456789a 123456789a 1________a 123456789b 123456789b _____6___b ______7__c 123456789c ________9c
# _______8_d 123456789d 123456789d _2_______e ________9e 123456789e ___4_____f 123456789f 123456789f
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d 123456789d ______7__d 123456789e _____6___e 1________e 123456789f 123456789f ____5____f
# _____6___g 123456789g ___4_____g ______7__h 123456789h 123456789h 1________i 123456789i 123456789i
# 123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i __3______i 123456789i
# 123456789g ____5____g 123456789g 1________h ___4_____h 123456789h ________9i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type1_07():
#     return f"""
#     avoidable_rectangle_type1_07.sudoku
#     9
# ___4_____a 123456789a 123456789a 123456789b 123456789b _____6___b 123456789c ______7__c 123456789c
# 1________a _______8_a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# __3______a 123456789a 123456789a 123456789b 1________b 123456789b 123456789c _______8_c _____6___c
# 123456789d 123456789d ______7__d _____6___e 123456789e 123456789e 123456789f 123456789f _______8_f
# 123456789d _____6___d 123456789d 123456789e ____5____e 123456789e 123456789f ________9f 123456789f
# _______8_d 123456789d 123456789d 123456789e 123456789e ________9e _2_______f 123456789f 123456789f
# _____6___g 1________g 123456789g 123456789h __3______h 123456789h 123456789i 123456789i ________9i
# 123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i _2_______i ___4_____i
# 123456789g ___4_____g 123456789g ______7__h 123456789h 123456789h 123456789i 123456789i 1________i
#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type1_08():
#     return f"""
#     avoidable_rectangle_type1_08.sudoku
#     9
# 123456789a 123456789a _______8_a _2_______b 123456789b ___4_____b 123456789c 123456789c 123456789c
# 123456789a _2_______a 123456789a 123456789b 1________b ____5____b 123456789c 123456789c 123456789c
# 123456789a ___4_____a 123456789a 123456789b 123456789b 123456789b _____6___c ____5____c 123456789c
# 123456789d 123456789d ___4_____d ______7__e 123456789e 123456789e 123456789f 123456789f _______8_f
# ________9d 123456789d 123456789d 123456789e _______8_e 123456789e 123456789f 123456789f _____6___f
# ______7__d 123456789d 123456789d 123456789e 123456789e _2_______e ________9f 123456789f 123456789f
# 123456789g 1________g __3______g 123456789h 123456789h 123456789h 123456789i ______7__i 123456789i
# 123456789g 123456789g 123456789g 1________h ________9h 123456789h 123456789i ___4_____i 123456789i
# 123456789g 123456789g 123456789g _______8_h 123456789h ______7__h __3______i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type1_09():
#     return f"""
#     avoidable_rectangle_type1_09.sudoku
#     9
# 123456789a 123456789a 123456789a 123456789b 123456789b ___4_____b 123456789c 123456789c 123456789c
# ___4_____a ______7__a 1________a 123456789b 123456789b 123456789b _2_______c ________9c 123456789c
# 123456789a 123456789a ________9a ______7__b 123456789b 123456789b 1________c 123456789c _______8_c
# 123456789d 123456789d 123456789d _2_______e 123456789e _______8_e 123456789f 123456789f ________9f
# 123456789d 123456789d 123456789d 123456789e _____6___e 123456789e 123456789f 123456789f 123456789f
# __3______d 123456789d 123456789d ____5____e 123456789e ______7__e 123456789f 123456789f 123456789f
# ______7__g 123456789g ____5____g 123456789h 123456789h _2_______h ___4_____i 123456789i 123456789i
# 123456789g __3______g _____6___g 123456789h 123456789h 123456789h _______8_i _2_______i ______7__i
# 123456789g 123456789g 123456789g __3______h 123456789h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type1_10():
#     return f"""
#     avoidable_rectangle_type1_10.sudoku
#     9
# ________9a ______7__a ___4_____a 123456789b 123456789b ____5____b 123456789c 123456789c 123456789c
# 123456789a 123456789a _______8_a 123456789b 123456789b 1________b _2_______c 123456789c 123456789c
# 123456789a 123456789a 123456789a 123456789b 123456789b ______7__b ___4_____c 123456789c 123456789c
# 123456789d _2_______d 123456789d 1________e 123456789e 123456789e 123456789f _______8_f 123456789f
# 123456789d 123456789d 123456789d 123456789e _______8_e 123456789e 123456789f 123456789f 123456789f
# 123456789d 1________d 123456789d 123456789e 123456789e ________9e 123456789f _2_______f 123456789f
# 123456789g 123456789g ______7__g ________9h 123456789h 123456789h 123456789i 123456789i 123456789i
# 123456789g 123456789g _____6___g ____5____h 123456789h 123456789h __3______i 123456789i 123456789i
# 123456789g 123456789g 123456789g ___4_____h 123456789h 123456789h ______7__i _____6___i 1________i
#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type1_11():
#     return f"""
#     avoidable_rectangle_type1_11.sudoku
#     9
# 1________a ___4_____a ________9a 123456789b __3______b 123456789b 123456789c 123456789c 123456789c
# 123456789a _2_______a 123456789a 123456789b 123456789b 123456789b 1________c 123456789c 123456789c
# 123456789a _____6___a ______7__a 1________b 123456789b _2_______b 123456789c __3______c 123456789c
# 123456789d 123456789d 123456789d _2_______e 123456789e ___4_____e 123456789f 123456789f 123456789f
# 123456789d _______8_d 123456789d 123456789e 123456789e 123456789e 123456789f ______7__f 123456789f
# 123456789d 123456789d 123456789d _____6___e 123456789e _______8_e 123456789f 123456789f 123456789f
# 123456789g ____5____g 123456789g ___4_____h 123456789h __3______h _______8_i 1________i 123456789i
# 123456789g 123456789g ___4_____g 123456789h 123456789h 123456789h 123456789i _____6___i 123456789i
# 123456789g 123456789g 123456789g 123456789h 1________h 123456789h ___4_____i _2_______i ______7__i

#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type1_12():
#     return f"""
#     avoidable_rectangle_type1_12.sudoku
#     9
# 123456789a 123456789a __3______a 123456789b 123456789b ___4_____b 123456789c ______7__c 123456789c
# 123456789a ___4_____a _2_______a 123456789b 123456789b 123456789b 123456789c 123456789c _______8_c
# 1________a _____6___a 123456789a 123456789b _______8_b 123456789b 123456789c 123456789c 123456789c
# _2_______d 123456789d _____6___d __3______e 123456789e 123456789e 123456789f _______8_f 123456789f
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d ______7__d 123456789d 123456789e 123456789e 1________e _2_______f 123456789f ________9f
# 123456789g 123456789g 123456789g 123456789h 1________h 123456789h 123456789i _2_______i __3______i
# ________9g 123456789g 123456789g 123456789h 123456789h 123456789h ___4_____i ____5____i 123456789i
# 123456789g 1________g 123456789g _2_______h 123456789h 123456789h ______7__i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type1_13():
#     return f"""
#     avoidable_rectangle_type1_13.sudoku
#     9
# 123456789a _2_______a ____5____a 123456789b ______7__b _____6___b 123456789c ___4_____c 123456789c
# ______7__a 1________a ________9a 123456789b 123456789b 123456789b _______8_c _____6___c 123456789c
# 123456789a _____6___a ___4_____a 1________b 123456789b 123456789b _2_______c 123456789c ______7__c
# 123456789d __3______d _______8_d ______7__e 123456789e _2_______e 123456789f 123456789f _____6___f
# 123456789d ________9d _____6___d 123456789e _______8_e 123456789e ______7__f 123456789f 123456789f
# ____5____d ______7__d _2_______d ________9e _____6___e 1________e ___4_____f 123456789f 123456789f
# ________9g ___4_____g __3______g _____6___h 1________h ______7__h ____5____i 123456789i 123456789i
# _____6___g ____5____g 1________g 123456789h 123456789h 123456789h __3______i ______7__i ___4_____i
# _2_______g _______8_g ______7__g ___4_____h __3______h ____5____h _____6___i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_avoidable_rectangle_type2_0():
#     return f"""
#     avoidable_rectangle_type2_0.sudoku
#     9
#     123456789a 123456789a ____5____a 123456789b 123456789b 123456789b _____6___c _______8_c __3______c
#     123456789a _____6___a ___4_____a ____5____b __3______b _______8_b ________9c 123456789c _2_______c
#     _______8_a _2_______a __3______a ________9b _____6___b 123456789b 123456789c ____5____c 123456789c
#     _2_______d 123456789d 123456789d 123456789e 123456789e _____6___e ____5____f 123456789f 123456789f
#     __3______d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f _2_______f _____6___f
#     _____6___d 123456789d 1________d _2_______e 123456789e 123456789e 123456789f 123456789f ________9f
#     ___4_____g __3______g _2_______g _____6___h ____5____h 1________h ______7__i ________9i _______8_i
#     123456789g 123456789g ______7__g _______8_h 123456789h 123456789h __3______i _____6___i ____5____i
#     ____5____g _______8_g _____6___g 123456789h 123456789h 123456789h _2_______i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_finned_x_wing_02():
#     return f"""
#     finned_x_wing_02.sudoku
#     9
#     ___4_____a _2_______a 1________a _______8_b 123456789b ________9b 123456789c ______7__c 123456789c
# _____6___a ____5____a 123456789a 1________b _2_______b 123456789b ________9c 123456789c 123456789c
# __3______a ________9a 123456789a 123456789b ____5____b 123456789b 123456789c 123456789c 1________c
# 123456789d _______8_d 123456789d 123456789e 123456789e 1________e ______7__f 123456789f 123456789f
# ______7__d ___4_____d __3______d 123456789e ________9e 123456789e _______8_f 1________f _____6___f
# 123456789d 1________d _____6___d ______7__e _______8_e 123456789e 123456789f ____5____f 123456789f
# _______8_g __3______g 123456789g ________9h ___4_____h 123456789h 1________i _____6___i ______7__i
# 1________g _____6___g ________9g 123456789h ______7__h _______8_h 123456789i ___4_____i 123456789i
# 123456789g ______7__g ___4_____g __3______h 1________h _____6___h 123456789i ________9i _______8_i
#     """

# @staticmethod
# def sudoku_finned_x_wing_03():
#     return f"""
#     finned_x_wing_03.sudoku
#     9
#     123456789a ______7__a _____6___a 123456789b _______8_b ________9b 123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a 123456789b 123456789b __3______b 123456789c _______8_c _____6___c
# ____5____a _______8_a __3______a 123456789b 123456789b ___4_____b 123456789c 123456789c 123456789c
# __3______d 123456789d ______7__d _______8_e ___4_____e 123456789e 1________f 123456789f 123456789f
# 123456789d _2_______d 123456789d 123456789e ________9e 123456789e 123456789f ___4_____f 123456789f
# 123456789d 123456789d ___4_____d 123456789e __3______e 123456789e _______8_f 123456789f ____5____f
# 123456789g 123456789g 123456789g ________9h 123456789h 123456789h _2_______i __3______i _______8_i
# _____6___g 123456789g _2_______g __3______h 123456789h _______8_h 123456789i 123456789i 123456789i
# 123456789g __3______g 123456789g ___4_____h _2_______h 123456789h _____6___i 1________i 123456789i
#     """

# @staticmethod
# def sudoku_hidden_quad_0():
#     return f"""
#     hidden_quad_0.sudoku
#     9
# _______8_a 123456789a 123456789a 1________b 123456789b ________9b 123456789c ___4_____c 123456789c
# 123456789a 123456789a 123456789a 123456789b ____5____b 123456789b 123456789c _____6___c _______8_c
# 123456789a 123456789a 123456789a ______7__b 123456789b 123456789b 1________c ________9c __3______c
# 1________d 123456789d _2_______d 123456789e 123456789e 123456789e 123456789f ____5____f 123456789f
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d ______7__d 123456789d 123456789e 123456789e 123456789e __3______f 123456789f ___4_____f
# ________9g 1________g ____5____g 123456789h 123456789h __3______h 123456789i 123456789i 123456789i
# ______7__g _2_______g 123456789g 123456789h _____6___h 123456789h 123456789i 123456789i 123456789i
# 123456789g _______8_g 123456789g ____5____h 123456789h 1________h 123456789i 123456789i _2_______i

#     """

# @staticmethod
# def sudoku_hidden_quad_1():
#     return f"""
#     hidden_quad_1.sudoku
#     9
# __3______a _____6___a ___4_____a 123456789b 123456789b ________9b 123456789c 123456789c 123456789c
# ____5____a 123456789a 123456789a __3______b 123456789b _____6___b 1________c 123456789c 123456789c
# _______8_a 123456789a 1________a 123456789b ______7__b 123456789b 123456789c 123456789c 123456789c
# ______7__d 123456789d 123456789d 123456789e 123456789e 123456789e _____6___f _2_______f 123456789f
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d ___4_____d ____5____d 123456789e 123456789e 123456789e 123456789f 123456789f ________9f
# 123456789g 123456789g 123456789g 123456789h _______8_h 123456789h ________9i 123456789i _2_______i
# 123456789g 123456789g _2_______g _____6___h 123456789h ______7__h 123456789i 123456789i 1________i
# 123456789g 123456789g 123456789g ___4_____h 123456789h 123456789h __3______i ______7__i _____6___i

#     """

# @staticmethod
# def sudoku_hidden_quad_2():
#     return f"""
#     hidden_quad_2.sudoku
#     9
# 123456789a 123456789a 123456789a 123456789b 123456789b ______7__b 123456789c ____5____c 123456789c
# 123456789a 123456789a 123456789a 123456789b 123456789b __3______b 123456789c ___4_____c 123456789c
# 123456789a 123456789a 123456789a _____6___b ___4_____b 123456789b 123456789c 123456789c _______8_c
# 123456789d ___4_____d 1________d 123456789e 123456789e 123456789e _2_______f ________9f 123456789f
# _____6___d 123456789d __3______d 123456789e ________9e 123456789e 1________f 123456789f ____5____f
# 123456789d ________9d _2_______d 123456789e 123456789e 123456789e _____6___f _______8_f 123456789f
# __3______g 123456789g 123456789g 123456789h 1________h ________9h 123456789i 123456789i 123456789i
# 123456789g _____6___g 123456789g ______7__h 123456789h 123456789h 123456789i 123456789i 123456789i
# 123456789g 1________g 123456789g __3______h 123456789h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_hidden_quad_3():
#     return f"""
#     hidden_quad_3.sudoku
#     9
# 123456789a 123456789a 123456789a _____6___b 123456789b 123456789b _______8_c 123456789c 123456789c
# 123456789a 123456789a 123456789a 123456789b ________9b 1________b 123456789c ___4_____c 123456789c
# 123456789a 123456789a 123456789a __3______b 123456789b 123456789b ________9c 123456789c 123456789c
# ____5____d 123456789d _2_______d 123456789e 123456789e 123456789e ___4_____f 123456789f 1________f
# __3______d 1________d 123456789d 123456789e _2_______e 123456789e 123456789f _______8_f ______7__f
# ______7__d 123456789d ________9d 123456789e 123456789e 123456789e _2_______f 123456789f ____5____f
# 123456789g 123456789g 1________g 123456789h 123456789h _____6___h 123456789i 123456789i 123456789i
# 123456789g __3______g 123456789g _2_______h ______7__h 123456789h 123456789i 123456789i 123456789i
# 123456789g 123456789g ______7__g 123456789h 123456789h __3______h 123456789i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_hidden_quad_4():
#     return f"""
#     hidden_quad_4.sudoku
#     9
#     __3______a 1________a 123456789a ___4_____b 123456789b ________9b 123456789c 123456789c 123456789c
#     123456789a 123456789a 123456789a 1________b ______7__b ____5____b 123456789c 123456789c 123456789c
#     123456789a 123456789a ______7__a 123456789b __3______b 123456789b 123456789c 123456789c 123456789c
#     123456789d 123456789d ________9d 123456789e 123456789e 123456789e 123456789f _______8_f ______7__f
#     123456789d 123456789d 1________d 123456789e ________9e 123456789e ___4_____f 123456789f 123456789f
#     _______8_d ______7__d 123456789d 123456789e 123456789e 123456789e __3______f 123456789f 123456789f
#     123456789g 123456789g 123456789g 123456789h _____6___h 123456789h _2_______i 123456789i 123456789i
#     123456789g 123456789g 123456789g ____5____h 1________h __3______h 123456789i 123456789i 123456789i
#     123456789g 123456789g 123456789g ________9h 123456789h _2_______h 123456789i _____6___i ___4_____i
#     """

# @staticmethod
# def sudoku_hidden_quad_8():
#     return f"""
#     hidden_quad_8.sudoku
#     9
# 123456789a 123456789a 123456789a ____5____b ___4_____b 1________b 123456789c ________9c 123456789c
# 123456789a 123456789a 123456789a ______7__b ________9b __3______b ____5____c 123456789c 123456789c
# 123456789a 123456789a 123456789a _2_______b _______8_b _____6___b __3______c 123456789c ___4_____c
# 123456789d ___4_____d 123456789d 1________e 123456789e _______8_e ________9f 123456789f ____5____f
# 123456789d _____6___d 123456789d ________9e _2_______e ____5____e ___4_____f __3______f 123456789f
# ________9d 123456789d ____5____d __3______e 123456789e ___4_____e 123456789f _2_______f 123456789f
# _____6___g __3______g 1________g _______8_h ____5____h _2_______h ______7__i ___4_____i ________9i
# 123456789g 123456789g 123456789g ___4_____h __3______h ______7__h 123456789i 123456789i 123456789i
# 123456789g _______8_g 123456789g _____6___h 1________h ________9h _2_______i ____5____i __3______i
#     """

# @staticmethod
# def sudoku_hidden_quad_9():
#     return f"""
#     hidden_quad_9.sudoku
#     9
# _2_______a ___4_____a ______7__a _____6___b __3______b 1________b ________9c _______8_c ____5____c
# _______8_a __3______a _____6___a ____5____b ___4_____b ________9b 1________c _2_______c ______7__c
# ____5____a ________9a 1________a _______8_b _2_______b ______7__b ___4_____c __3______c _____6___c
# _____6___d 123456789d 123456789d 123456789e 123456789e 123456789e __3______f ______7__f 123456789f
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d 1________d ________9d 123456789e 123456789e 123456789e 123456789f 123456789f _______8_f
# ________9g _2_______g __3______g 1________h _______8_h ____5____h ______7__i _____6___i ___4_____i
# 1________g ______7__g ____5____g ___4_____h _____6___h _2_______h _______8_i ________9i __3______i
# ___4_____g _____6___g _______8_g ______7__h ________9h __3______h ____5____i 1________i _2_______i

#     """

# @staticmethod
# def sudoku_hidden_triple_0():
#     return f"""
#     hidden_triple_0.sudoku
#     9
#     123456789a 123456789a 123456789a ____5____b 123456789b 123456789b 123456789c ______7__c ________9c
#     123456789a 1________a 123456789a 123456789b 123456789b 123456789b 123456789c ____5____c ___4_____c
#     123456789a 123456789a ___4_____a 123456789b _______8_b 123456789b 123456789c 123456789c 123456789c
#     _2_______d 123456789d 123456789d ________9e 123456789e __3______e 123456789f 123456789f _______8_f
#     123456789d 123456789d ______7__d 123456789e 123456789e 123456789e ________9f 123456789f 123456789f
#     _____6___d 123456789d 123456789d _2_______e 123456789e ______7__e 123456789f 123456789f __3______f
#     123456789g 123456789g 123456789g 123456789h ______7__h 123456789h 1________i 123456789i 123456789i
#     1________g _____6___g 123456789g 123456789h 123456789h 123456789h 123456789i _______8_i 123456789i
#     ___4_____g ______7__g 123456789g 123456789h 123456789h ____5____h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_hidden_triple_2():
#     return f"""
#     hidden_triple_2.sudoku
#     9
#     123456789a __3______a 123456789a 123456789b _______8_b 123456789b 123456789c 1________c 123456789c
#     123456789a 123456789a 123456789a 123456789b __3______b 123456789b _______8_c 123456789c 123456789c
#     123456789a 123456789a 123456789a _____6___b ______7__b 123456789b 123456789c __3______c ____5____c
#     ______7__d ________9d _2_______d 1________e _____6___e __3______e ____5____f _______8_f ___4_____f
#     ____5____d ___4_____d _______8_d _2_______e ________9e ______7__e __3______f _____6___f 1________f
#     __3______d 123456789d 123456789d ____5____e ___4_____e _______8_e ______7__f 123456789f 123456789f
#     _____6___g 123456789g 123456789g 123456789h 1________h ___4_____h 123456789i 123456789i 123456789i
#     ___4_____g 123456789g ________9g 123456789h _2_______h _____6___h 1________i 123456789i 123456789i
#     123456789g ______7__g 123456789g 123456789h ____5____h ________9h 123456789i ___4_____i 123456789i
#     """

# @staticmethod
# def sudoku_hidden_triple_3():
#     return f"""
#     hidden_triple_3.sudoku
#     9
# 123456789a ________9a 123456789a _2_______b __3______b _____6___b 123456789c 1________c 123456789c
# ____5____a 123456789a 123456789a 1________b ______7__b 123456789b __3______c 123456789c ________9c
# 123456789a 123456789a 123456789a ____5____b ________9b 123456789b _2_______c 123456789c 123456789c
# 123456789d 123456789d 123456789d ________9e ___4_____e _2_______e ______7__f 123456789f 123456789f
# _2_______d ___4_____d ________9d ______7__e _______8_e ____5____e _____6___f __3______f 1________f
# _______8_d ______7__d ____5____d __3______e _____6___e 1________e 123456789f 123456789f 123456789f
# 123456789g ____5____g ______7__g _____6___h _2_______h __3______h 123456789i 123456789i 123456789i
# _____6___g 123456789g 123456789g _______8_h ____5____h 123456789h 123456789i 123456789i __3______i
# 123456789g _______8_g 123456789g ___4_____h 1________h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_hidden_triple_4():
#     return f"""
#     hidden_triple_4.sudoku
#     9
# 123456789a 123456789a 123456789a ________9b 123456789b 123456789b ______7__c 123456789c 123456789c
# 123456789a ____5____a 123456789a _____6___b 123456789b __3______b 123456789c ___4_____c _2_______c
# 123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 1________c
# _______8_d __3______d 123456789d 123456789e ____5____e 123456789e ________9f _2_______f 123456789f
# ______7__d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f __3______f
# 123456789d _2_______d ____5____d 123456789e ___4_____e 123456789e 123456789f _______8_f ______7__f
# ____5____g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
# __3______g _____6___g 123456789g _______8_h 123456789h ______7__h 123456789i 1________i 123456789i
# 123456789g 123456789g 1________g 123456789h 123456789h ___4_____h 123456789i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_hidden_triple_5():
#     return f"""
#     hidden_triple_5.sudoku
#     9
# 123456789a 123456789a 123456789a 123456789b ______7__b 123456789b 123456789c 123456789c 123456789c
# ________9a 123456789a 123456789a ___4_____b _2_______b ____5____b 1________c 123456789c 123456789c
# ___4_____a 123456789a 123456789a 123456789b 123456789b __3______b 123456789c _2_______c ____5____c
# 123456789d ____5____d 123456789d 123456789e 123456789e 123456789e ______7__f 123456789f _______8_f
# 123456789d _____6___d 123456789d 123456789e 123456789e 123456789e 123456789f __3______f 123456789f
# _______8_d 123456789d __3______d 123456789e 123456789e 123456789e 123456789f _____6___f 123456789f
# _____6___g 1________g 123456789g ______7__h 123456789h 123456789h 123456789i 123456789i ________9i
# 123456789g 123456789g ____5____g 1________h _______8_h _____6___h 123456789i 123456789i ______7__i
# 123456789g 123456789g 123456789g 123456789h __3______h 123456789h 123456789i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_hidden_triple_6():
#     return f"""
#     hidden_triple_6.sudoku
#     9
# 123456789a ________9a 123456789a 123456789b 123456789b 123456789b 123456789c ____5____c ___4_____c
# 123456789a 123456789a 123456789a 123456789b 123456789b ____5____b 123456789c _____6___c ______7__c
# 123456789a 123456789a ___4_____a 123456789b _2_______b 123456789b 123456789c 123456789c 123456789c
# __3______d 123456789d 123456789d _____6___e 123456789e 1________e 123456789f 123456789f _______8_f
# 123456789d 123456789d _____6___d 123456789e 123456789e 123456789e ______7__f 123456789f 123456789f
# 1________d 123456789d ________9d _______8_e 123456789e ______7__e _____6___f 123456789f _2_______f
# 123456789g 123456789g 123456789g 123456789h _____6___h 123456789h ________9i 123456789i 123456789i
# ___4_____g _____6___g 123456789g ____5____h 123456789h 123456789h 123456789i 123456789i 123456789i
# ________9g __3______g 123456789g 123456789h 123456789h 123456789h 123456789i _2_______i _____6___i

#     """

# @staticmethod
# def sudoku_naked_quad_0():
#     return f"""
#     naked_quad_0.sudoku
#     9
#     123456789a ______7__a __3______a 6b 123456789b ___4_____b 123456789c 123456789c 123456789c
#     123456789a ___4_____a _2_______a 123456789b 123456789b 1________b 123456789c 123456789c 123456789c
#     ____5____a 123456789a ________9a __3______b 123456789b 123456789b 123456789c ___4_____c 123456789c
#     __3______d 123456789d ______7__d 123456789e 123456789e 123456789e _______8_f 123456789f 123456789f
#     123456789d ________9d 123456789d _______8_e 123456789e 123456789e 123456789f ______7__f 123456789f
#     123456789d 123456789d 6d 123456789e 123456789e 123456789e __3______f 123456789f ___4_____f
#     123456789g _2_______g 123456789g 123456789h 123456789h _______8_h 1________i 123456789i 6i
#     123456789g 123456789g 123456789g _2_______h 123456789h 123456789h ___4_____i ____5____i 123456789i
#     123456789g 123456789g 123456789g 1________h 123456789h ________9h ______7__i _2_______i 123456789i
#     """

# @staticmethod
# def sudoku_naked_quad_1():
#     return f"""
#     naked_quad_1.sudoku
#     9
#     ____5____a 123456789a 123456789a ______7__b 123456789b ___4_____b _2_______c 123456789c 123456789c
#     123456789a ______7__a 123456789a 1________b 123456789b 123456789b ________9c 123456789c ___4_____c
#     123456789a 123456789a 123456789a _______8_b 123456789b 123456789b 123456789c 123456789c 123456789c
#     ______7__d 123456789d 123456789d 123456789e 123456789e 123456789e __3______f 123456789f 123456789f
#     _2_______d 123456789d 1________d 123456789e 123456789e 123456789e ______7__f 123456789f ____5____f
#     123456789d 123456789d ___4_____d 123456789e 123456789e 123456789e 123456789f 123456789f _____6___f
#     123456789g 123456789g 123456789g 123456789h 123456789h _____6___h 123456789i 123456789i 123456789i
#     ___4_____g 123456789g _____6___g 123456789h 123456789h _______8_h 123456789i 1________i 123456789i
#     123456789g 123456789g ____5____g ________9h 123456789h 1________h 123456789i 123456789i __3______i
#     """

# @staticmethod
# def sudoku_naked_quad_2():
#     return f"""
#     naked_quad_2.sudoku
#     9
#     ____5____a 123456789a 123456789a 1________b ___4_____b 123456789b 123456789c ______7__c _2_______c
#     123456789a ______7__a 123456789a 123456789b 123456789b _____6___b 123456789c 123456789c ____5____c
#     123456789a 123456789a 123456789a 123456789b ____5____b 123456789b 123456789c 1________c _____6___c
#     123456789d 123456789d 123456789d ____5____e 123456789e 123456789e 123456789f 123456789f 123456789f
#     _______8_d __3______d 123456789d 123456789e 123456789e 123456789e 123456789f ___4_____f ______7__f
#     123456789d 123456789d 123456789d 123456789e 123456789e _2_______e 123456789f 123456789f 123456789f
#     _____6___g _______8_g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     ______7__g 123456789g 123456789g __3______h 123456789h 123456789h 123456789i ________9i 123456789i
#     ________9g ___4_____g 123456789g 123456789h _______8_h ____5____h 123456789i 123456789i 1________i
#     """

# @staticmethod
# def sudoku_naked_quad_3():
#     return f"""
#     naked_quad_3.sudoku
#     9
#     ________9a 123456789a 123456789a 123456789b __3______b 123456789b _____6___c 123456789c 123456789c
#     123456789a 123456789a 123456789a _____6___b 123456789b ____5____b 123456789c ________9c __3______c
#     123456789a __3______a 123456789a ________9b 123456789b ______7__b 123456789c 123456789c 123456789c
#     ______7__d _____6___d __3______d 123456789e ________9e _______8_e 123456789f 123456789f ___4_____f
#     ____5____d ___4_____d _______8_d ______7__e _____6___e 123456789e __3______f 123456789f ________9f
#     1________d ________9d _2_______d 123456789e ____5____e 123456789e _______8_f ______7__f _____6___f
#     123456789g 123456789g 123456789g _______8_h 123456789h 123456789h 123456789i 123456789i 123456789i
#     _______8_g _2_______g 123456789g ____5____h 123456789h 123456789h 123456789i 123456789i 123456789i
#     123456789g 123456789g ________9g 123456789h ___4_____h 123456789h 123456789i 123456789i _______8_i
#     """

# @staticmethod
# def sudoku_wxyz_wing_1():
#     return f"""
#     wxyz_wing_1.sudoku
#     9
# 123456789a ___4_____a 1________a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# _______8_a ______7__a 123456789a _2_______b ___4_____b 123456789b 123456789c 123456789c 123456789c
# _2_______a 123456789a _____6___a 123456789b 123456789b ________9b 123456789c 123456789c 123456789c
# ___4_____d 123456789d 123456789d ______7__e ________9e ____5____e __3______f 123456789f 123456789f
# 123456789d 123456789d 123456789d __3______e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d 123456789d ____5____d _____6___e _______8_e ___4_____e 123456789f 123456789f ________9f
# 123456789g 123456789g ___4_____g ________9h 123456789h 123456789h 1________i 123456789i _2_______i
# 123456789g 123456789g 123456789g 1________h _____6___h __3______h ___4_____i ____5____i _______8_i
# 123456789g 123456789g 123456789g ___4_____h 123456789h 123456789h ________9i ______7__i 123456789i
#     """

# @staticmethod
# def sudoku_wxyz_wing_2():
#     return f"""
#     wxyz_wing_2.sudoku
#     9
# 123456789a ___4_____a 1________a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# _______8_a ______7__a 123456789a _2_______b ___4_____b 123456789b 123456789c 123456789c 123456789c
# _2_______a 123456789a _____6___a 123456789b 123456789b ________9b 123456789c 123456789c 123456789c
# ___4_____d 123456789d 123456789d ______7__e ________9e ____5____e __3______f 123456789f 123456789f
# 123456789d 123456789d 123456789d __3______e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d 123456789d ____5____d _____6___e _______8_e ___4_____e 123456789f 123456789f ________9f
# 123456789g 123456789g ___4_____g ________9h 123456789h 123456789h 1________i 123456789i _2_______i
# 123456789g 123456789g 123456789g 1________h _____6___h __3______h ___4_____i ____5____i _______8_i
# 123456789g 123456789g 123456789g ___4_____h 123456789h 123456789h ________9i ______7__i 123456789i
#     """

# @staticmethod
# def sudoku_wxyz_wing_3():
#     return f"""
#     wxyz_wing_3.sudoku
#     9
# 123456789a ___4_____a 1________a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# _______8_a ______7__a 123456789a _2_______b ___4_____b 123456789b 123456789c 123456789c 123456789c
# _2_______a 123456789a _____6___a 123456789b 123456789b ________9b 123456789c 123456789c 123456789c
# ___4_____d 123456789d 123456789d ______7__e ________9e ____5____e __3______f 123456789f 123456789f
# 123456789d 123456789d 123456789d __3______e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d 123456789d ____5____d _____6___e _______8_e ___4_____e 123456789f 123456789f ________9f
# 123456789g 123456789g ___4_____g ________9h 123456789h 123456789h 1________i 123456789i _2_______i
# 123456789g 123456789g 123456789g 1________h _____6___h __3______h ___4_____i ____5____i _______8_i
# 123456789g 123456789g 123456789g ___4_____h 123456789h 123456789h ________9i ______7__i 123456789i
#     """

# @staticmethod
# def sudoku_wxyz_wing_7():
#     return f"""
#     wxyz_wing_7.sudoku
#     9
# __3______a _____6___a ______7__a ____5____b ________9b _2_______b 1________c ___4_____c _______8_c
# _2_______a ____5____a ___4_____a _______8_b 1________b 123456789b ________9c 123456789c ______7__c
# ________9a 1________a _______8_a 123456789b 123456789b ___4_____b 123456789c 123456789c 123456789c
# 1________d ________9d 123456789d 123456789e 123456789e 123456789e _______8_f 123456789f 123456789f
# ___4_____d ______7__d 123456789d ________9e 123456789e 123456789e 123456789f 123456789f 1________f
# _______8_d __3______d _____6___d 123456789e 123456789e 123456789e 123456789f ______7__f ________9f
# ____5____g 123456789g ________9g __3______h 123456789h ______7__h _____6___i 1________i 123456789i
# ______7__g 123456789g __3______g 123456789h _____6___h 123456789h 123456789i ________9i ____5____i
# _____6___g _2_______g 1________g ___4_____h ____5____h ________9h ______7__i _______8_i __3______i
#     """

# @staticmethod
# def sudoku_wxyz_wing_8():
#     return f"""
#     wxyz_wing_8.sudoku
#     9
# ___4_____a 123456789a ______7__a 123456789b 123456789b 123456789b 123456789c ________9c _______8_c
# 123456789a _____6___a __3______a _______8_b 123456789b ___4_____b ____5____c ______7__c _2_______c
# ____5____a 123456789a _______8_a 123456789b 123456789b 123456789b 123456789c 1________c ___4_____c
# _______8_d ______7__d 1________d ____5____e __3______e ________9e _2_______f ___4_____f _____6___f
# 123456789d 123456789d ___4_____d _2_______e 123456789e 1________e ________9f 123456789f ______7__f
# _2_______d 123456789d 123456789d ___4_____e ______7__e 123456789e 1________f 123456789f __3______f
# 123456789g _______8_g 123456789g 123456789h 123456789h 123456789h ___4_____i 123456789i ____5____i
# 123456789g ___4_____g 123456789g __3______h 123456789h 123456789h ______7__i _2_______i 1________i
# ______7__g 123456789g 123456789g 123456789h ___4_____h 123456789h _______8_i 123456789i ________9i
#     """

# @staticmethod
# def sudoku_wxyz_wing_9():
#     return f"""
#     wxyz_wing_9.sudoku
#     9
# 123456789a 123456789a 123456789a 123456789b 123456789b ______7__b ____5____c _2_______c 123456789c
# 123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c ________9c ___4_____c
# 123456789a 123456789a 123456789a _______8_b 123456789b 123456789b 1________c _____6___c ______7__c
# 123456789d 123456789d ______7__d ________9e 123456789e _____6___e 123456789f _______8_f 123456789f
# 123456789d _____6___d 123456789d ______7__e 123456789e _2_______e 123456789f __3______f 123456789f
# 123456789d ____5____d 123456789d ___4_____e _______8_e __3______e ______7__f 1________f _____6___f
# 1________g 123456789g __3______g 123456789h 123456789h ________9h _____6___i 123456789i 123456789i
# _____6___g ___4_____g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
# 123456789g _2_______g ____5____g _____6___h 123456789h 123456789h 123456789i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_w_wing_type_d_1():
#     return f"""
#     w_wing_type_d_1.sudoku
#     9
# ______7__a 123456789a 123456789a ________9b 123456789b ____5____b _2_______c 123456789c 123456789c
# _2_______a ____5____a ___4_____a 123456789b _______8_b ______7__b 123456789c ________9c _____6___c
# ________9a 123456789a 123456789a _2_______b 123456789b 123456789b 123456789c ____5____c ______7__c
# ____5____d ______7__d ________9d 123456789e 123456789e __3______e _____6___f 123456789f _2_______f
# _______8_d _2_______d 123456789d ____5____e ________9e _____6___e 123456789f ______7__f 123456789f
# _____6___d ___4_____d 123456789d ______7__e _2_______e 123456789e ____5____f 123456789f ________9f
# 123456789g _______8_g ______7__g 123456789h 123456789h _2_______h ________9i _____6___i ____5____i
# __3______g ________9g _2_______g _____6___h ____5____h 123456789h ______7__i 123456789i 123456789i
# 123456789g _____6___g ____5____g 123456789h ______7__h ________9h 123456789i _2_______i __3______i

#     """

# @staticmethod
# def sudoku_w_wing_type_d_2():
#     return f"""
#     w_wing_type_d_2.sudoku
#     9
# ___4_____a 123456789a _______8_a 1________b _____6___b 123456789b __3______c _2_______c 123456789c
# 123456789a 123456789a 1________a 123456789b 123456789b 123456789b _______8_c ___4_____c 123456789c
# 123456789a 123456789a _2_______a _______8_b ______7__b ___4_____b ____5____c 1________c 123456789c
# _____6___d 1________d ___4_____d _2_______e ________9e _______8_e ______7__f ____5____f __3______f
# _______8_d 123456789d ____5____d 123456789e ___4_____e 1________e _____6___f ________9f _2_______f
# 123456789d _2_______d ________9d _____6___e ____5____e 123456789e ___4_____f _______8_f 1________f
# _2_______g _______8_g ______7__g ____5____h 1________h 123456789h ________9i 123456789i ___4_____i
# ____5____g ___4_____g _____6___g 123456789h 123456789h 123456789h 1________i 123456789i _______8_i
# 1________g ________9g __3______g ___4_____h _______8_h 123456789h _2_______i 123456789i ____5____i

#     """

# @staticmethod
# def sudoku_w_wing_type_d_3():
#     return f"""
#     w_wing_type_d_3.sudoku
#     9
# 123456789a 123456789a _______8_a 123456789b _2_______b 123456789b 123456789c _____6___c 123456789c
# 123456789a 123456789a _____6___a ___4_____b 1________b 123456789b 123456789c 123456789c _2_______c
# 123456789a ____5____a 123456789a _______8_b 123456789b 123456789b 123456789c ________9c 123456789c
# ____5____d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# ________9d 123456789d ______7__d 123456789e 123456789e 123456789e __3______f 123456789f _____6___f
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f ______7__f
# 123456789g __3______g 123456789g 123456789h 123456789h ________9h 123456789i _2_______i 123456789i
# 1________g 123456789g 123456789g 123456789h _______8_h _2_______h _____6___i 123456789i 123456789i
# 123456789g ______7__g 123456789g 123456789h _____6___h 123456789h 1________i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_w_wing_type_d_4():
#     return f"""
#     w_wing_type_d_4.sudoku
#     9
# 123456789a ____5____a 123456789a 123456789b 123456789b 123456789b ________9c __3______c 123456789c
# ________9a 123456789a 1________a 123456789b _______8_b 123456789b 123456789c 123456789c 123456789c
# _____6___a 123456789a __3______a 123456789b ________9b ___4_____b _______8_c 1________c ____5____c
# 123456789d 1________d _____6___d 123456789e ____5____e 123456789e __3______f ______7__f _2_______f
# ______7__d 123456789d ________9d 123456789e 123456789e 123456789e ____5____f 123456789f 1________f
# ____5____d __3______d 123456789d 123456789e 123456789e 123456789e 123456789f ________9f 123456789f
# 1________g ________9g ______7__g _____6___h __3______h 123456789h 123456789i ____5____i 123456789i
# __3______g _____6___g ____5____g 123456789h ___4_____h 123456789h ______7__i 123456789i ________9i
# _2_______g _______8_g ___4_____g 123456789h ______7__h 123456789h 1________i _____6___i __3______i

#     """

# @staticmethod
# def sudoku_w_wing_type_d_5():
#     return f"""
#     w_wing_type_d_5.sudoku
#     9
# ______7__a ____5____a _2_______a __3______b 123456789b 123456789b ___4_____c 1________c 123456789c
# _______8_a 123456789a 123456789a 123456789b 123456789b ________9b 123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a 123456789b ___4_____b 123456789b 123456789c 123456789c 123456789c
# 123456789d _____6___d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d ________9d 123456789d _____6___e _______8_e __3______e 123456789f ____5____f 123456789f
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f _______8_f 123456789f
# 123456789g 123456789g 123456789g 123456789h 1________h 123456789h 123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g ___4_____h 123456789h 123456789h 123456789i 123456789i _______8_i
# 123456789g __3______g 1________g 123456789h 123456789h ____5____h _2_______i _____6___i ___4_____i

#     """

# @staticmethod
# def sudoku_xyz_wing_0():
#     return f"""
#     xyz_wing_0.sudoku
#     9
# 123456789a 123456789a 123456789a 123456789b 123456789b __3______b ___4_____c 123456789c ____5____c
# 123456789a ________9a _____6___a 123456789b 123456789b 123456789b ______7__c _______8_c 123456789c
# 123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c _2_______c 123456789c
# 123456789d 1________d 123456789d 123456789e _______8_e ________9e _____6___f 123456789f 123456789f
# 123456789d 123456789d 123456789d ___4_____e 123456789e ____5____e 123456789f 123456789f 123456789f
# 123456789d 123456789d ____5____d 1________e _2_______e 123456789e 123456789f ___4_____f 123456789f
# 123456789g __3______g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
# 123456789g ___4_____g ________9g 123456789h 123456789h 123456789h __3______i 1________i 123456789i
# _2_______g 123456789g ______7__g _____6___h 123456789h 123456789h 123456789i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_xyz_wing_1():
#     return f"""
#     xyz_wing_1.sudoku
#     9
# ________9a __3______a 123456789a 123456789b 123456789b _______8_b 123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a __3______b 123456789b 123456789b 123456789c _______8_c ____5____c
# _____6___a 123456789a 123456789a 123456789b 1________b 123456789b 123456789c ________9c ___4_____c
# 123456789d ____5____d 123456789d 123456789e 123456789e 123456789e 123456789f 1________f ________9f
# 123456789d 123456789d _____6___d 123456789e 123456789e 123456789e ___4_____f 123456789f 123456789f
# 1________d ______7__d 123456789d 123456789e 123456789e 123456789e 123456789f _2_______f 123456789f
# ______7__g _____6___g 123456789g 123456789h ________9h 123456789h 123456789i 123456789i 1________i
# ____5____g _______8_g 123456789g 123456789h 123456789h __3______h 123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g 1________h 123456789h 123456789h 123456789i __3______i _______8_i
#     """

# @staticmethod
# def sudoku_xyz_wing_2():
#     return f"""
#     xyz_wing_2.sudoku
#     9
# ________9a __3______a 123456789a 123456789b 123456789b _______8_b 123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a __3______b 123456789b 123456789b 123456789c _______8_c ____5____c
# _____6___a 123456789a 123456789a 123456789b 1________b 123456789b 123456789c ________9c ___4_____c
# 123456789d ____5____d 123456789d 123456789e 123456789e 123456789e 123456789f 1________f ________9f
# 123456789d 123456789d _____6___d 123456789e 123456789e 123456789e ___4_____f 123456789f 123456789f
# 1________d ______7__d 123456789d 123456789e 123456789e 123456789e 123456789f _2_______f 123456789f
# ______7__g _____6___g 123456789g 123456789h ________9h 123456789h 123456789i 123456789i 1________i
# ____5____g _______8_g 123456789g 123456789h 123456789h __3______h 123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g 1________h 123456789h 123456789h 123456789i __3______i _______8_i
#     """

# @staticmethod
# def sudoku_xyz_wing_3():
#     return f"""
#     xyz_wing_3.sudoku
#     9
# ________9a __3______a 123456789a 123456789b 123456789b _______8_b 123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a __3______b 123456789b 123456789b 123456789c _______8_c ____5____c
# _____6___a 123456789a 123456789a 123456789b 1________b 123456789b 123456789c ________9c ___4_____c
# 123456789d ____5____d 123456789d 123456789e 123456789e 123456789e 123456789f 1________f ________9f
# 123456789d 123456789d _____6___d 123456789e 123456789e 123456789e ___4_____f 123456789f 123456789f
# 1________d ______7__d 123456789d 123456789e 123456789e 123456789e 123456789f _2_______f 123456789f
# ______7__g _____6___g 123456789g 123456789h ________9h 123456789h 123456789i 123456789i 1________i
# ____5____g _______8_g 123456789g 123456789h 123456789h __3______h 123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g 1________h 123456789h 123456789h 123456789i __3______i _______8_i

#     """

# @staticmethod
# def sudoku_xyz_wing_4():
#     return f"""
#     xyz_wing_4.sudoku
#     9
# _______8_a 123456789a __3______a ______7__b _____6___b 123456789b 123456789c _2_______c 1________c
# 1________a ______7__a _2_______a 123456789b 123456789b 123456789b 123456789c ________9c _____6___c
# ___4_____a 123456789a _____6___a _2_______b 1________b 123456789b 123456789c ______7__c _______8_c
# ______7__d __3______d ___4_____d _______8_e _2_______e ____5____e _____6___f 1________f ________9f
# _____6___d 1________d ____5____d 123456789e 123456789e 123456789e _______8_f ___4_____f _2_______f
# _2_______d _______8_d ________9d _____6___e ___4_____e 1________e ______7__f ____5____f __3______f
# ____5____g ___4_____g 123456789g 123456789h 123456789h _____6___h _2_______i __3______i ______7__i
# __3______g _2_______g 123456789g 123456789h 123456789h 123456789h ________9i _____6___i ___4_____i
# ________9g _____6___g ______7__g ___4_____h __3______h _2_______h 1________i _______8_i ____5____i

#     """

# @staticmethod
# def sudoku_xyz_wing_5():
#     return f"""
#     xyz_wing_5.sudoku
#     9
#     9
# ________9a ______7__a 123456789a ___4_____b 123456789b 123456789b 123456789c ____5____c 123456789c
# 1________a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# 123456789a __3______a _______8_a 123456789b 123456789b _2_______b 123456789c ______7__c 123456789c
# ____5____d 123456789d 123456789d _2_______e __3______e 123456789e 123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d 1________e 123456789e _____6___e 123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d 123456789e ___4_____e ______7__e 123456789f 123456789f _______8_f
# 123456789g _2_______g 123456789g __3______h 123456789h 123456789h 1________i _____6___i 123456789i
# 123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i ___4_____i
# 123456789g _______8_g 123456789g 123456789h 123456789h ____5____h 123456789i ________9i __3______i
#     """

# @staticmethod
# def sudoku_xyz_wing_6():
#     return f"""
#     xyz_wing_6.sudoku
#     9
# ______7__a 1________a __3______a _______8_b ________9b ___4_____b ____5____c _____6___c _2_______c
# _____6___a ________9a _2_______a __3______b 1________b ____5____b _______8_c ___4_____c ______7__c
# 123456789a 123456789a ____5____a ______7__b _____6___b _2_______b __3______c 1________c ________9c
# 123456789d 123456789d _______8_d 1________e ____5____e ________9e 123456789f 123456789f 123456789f
# 123456789d 123456789d 1________d ___4_____e _______8_e ______7__e 123456789f 123456789f 123456789f
# 123456789d 123456789d ________9d _2_______e __3______e _____6___e 1________f 123456789f _______8_f
# 123456789g 123456789g ______7__g _____6___h _2_______h 1________h 123456789i 123456789i 123456789i
# 1________g ____5____g ___4_____g ________9h ______7__h _______8_h _____6___i _2_______i __3______i
# ________9g _2_______g _____6___g ____5____h ___4_____h __3______h ______7__i _______8_i 1________i
#     """

# @staticmethod
# def sudoku_xyz_wing_7():
#     return f"""
#     xyz_wing_7.sudoku
#     9
#     9
# 123456789a _2_______a ________9a __3______b ____5____b 123456789b 1________c _______8_c _____6___c
# _____6___a ____5____a _______8_a 123456789b 123456789b 123456789b __3______c 123456789c _2_______c
# 123456789a 123456789a __3______a _2_______b _____6___b _______8_b 123456789c ________9c 123456789c
# _______8_d _____6___d ____5____d 1________e ___4_____e __3______e 123456789f 123456789f 123456789f
# ________9d ______7__d 1________d _______8_e _2_______e ____5____e 123456789f 123456789f __3______f
# 123456789d 123456789d _2_______d ________9e ______7__e _____6___e _______8_f ____5____f 1________f
# 123456789g _______8_g _____6___g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
# _2_______g 123456789g ______7__g ____5____h _______8_h 123456789h 123456789i 123456789i ___4_____i
# ____5____g ________9g ___4_____g _____6___h __3______h _2_______h ______7__i 1________i _______8_i
#     """

# @staticmethod
# def sudoku_xyz_wing_8():
#     return f"""
#     xyz_wing_8.sudoku
#     9
# 123456789a 123456789a _____6___a __3______b ____5____b _______8_b 123456789c ___4_____c 123456789c
# ____5____a 123456789a _______8_a ___4_____b _2_______b 1________b 123456789c 123456789c __3______c
# __3______a ___4_____a _2_______a ________9b _____6___b ______7__b 1________c ____5____c _______8_c
# _______8_d 123456789d ________9d ______7__e 123456789e ____5____e 123456789f _2_______f 123456789f
# ___4_____d ____5____d ______7__d _2_______e ________9e _____6___e _______8_f __3______f 1________f
# _2_______d _____6___d 123456789d _______8_e 123456789e ___4_____e 123456789f 123456789f ____5____f
# 123456789g _2_______g 123456789g _____6___h 123456789h __3______h ____5____i 123456789i 123456789i
# _____6___g 123456789g ____5____g 1________h 123456789h _2_______h 123456789i 123456789i ______7__i
# 123456789g _______8_g 123456789g ____5____h 123456789h ________9h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_xyz_wing_9():
#     return f"""
#     xyz_wing_9.sudoku
#     9
# ____5____a ___4_____a __3______a _______8_b _____6___b 1________b ______7__c ________9c _2_______c
# ______7__a ________9a _2_______a ____5____b __3______b ___4_____b 123456789c _______8_c 123456789c
# _______8_a 1________a _____6___a ________9b ______7__b _2_______b 123456789c 123456789c ___4_____c
# ________9d _2_______d 1________d 123456789e 123456789e 123456789e _______8_f ______7__f __3______f
# ___4_____d ____5____d _______8_d ______7__e _2_______e __3______e 123456789f _____6___f 123456789f
# _____6___d __3______d ______7__d 1________e ________9e _______8_e ___4_____f _2_______f ____5____f
# 1________g 123456789g ________9g __3______h 123456789h 123456789h _2_______i 123456789i ______7__i
# __3______g 123456789g ___4_____g _2_______h 123456789h ______7__h 123456789i 1________i 123456789i
# _2_______g ______7__g ____5____g 123456789h 1________h ________9h 123456789i 123456789i _______8_i

#     """

# @staticmethod
# def sudoku_xy_wing_01():
#     return f"""
#     9
# _____6___a ________9a 123456789a 123456789b ______7__b _______8_b ____5____c __3______c _2_______c
# 123456789a ______7__a __3______a ________9b _2_______b 123456789b _____6___c _______8_c ___4_____c
# _2_______a _______8_a 123456789a 123456789b 123456789b 123456789b ______7__c 1________c ________9c
# _______8_d 123456789d 123456789d 123456789e __3______e 123456789e ________9f 123456789f ______7__f
# ___4_____d __3______d 123456789d ______7__e _____6___e ________9e 123456789f ____5____f _______8_f
# ________9d 123456789d ______7__d 123456789e _______8_e 123456789e 123456789f 123456789f __3______f
# 123456789g ___4_____g ________9g _______8_h 123456789h 123456789h __3______i _2_______i _____6___i
# 123456789g 123456789g 123456789g 123456789h 123456789h 123456789h _______8_i ________9i ____5____i
# 123456789g 123456789g _______8_g _2_______h ________9h 123456789h ___4_____i ______7__i 1________i
#     """

# @staticmethod
# def sudoku_xy_wing_02():
#     return f"""
#     xy_wing_02.sudoku
#     9
# __3______a 1________a ___4_____a ________9b _2_______b ____5____b _______8_c ______7__c _____6___c
# 123456789a ________9a ______7__a 1________b _______8_b _____6___b 123456789c 123456789c 123456789c
# _____6___a _______8_a 123456789a ___4_____b ______7__b __3______b 123456789c 123456789c 1________c
# _______8_d ____5____d _____6___d ______7__e __3______e _2_______e 123456789f 123456789f ________9f
# 123456789d __3______d ________9d ____5____e ___4_____e 123456789e ______7__f _____6___f 123456789f
# ___4_____d ______7__d 123456789d _____6___e ________9e 123456789e ____5____f 123456789f __3______f
# ______7__g _____6___g 123456789g _2_______h 1________h ___4_____h 123456789i 123456789i 123456789i
# 123456789g ___4_____g 123456789g _______8_h _____6___h ________9h 123456789i 123456789i ______7__i
# ________9g _2_______g 123456789g __3______h ____5____h ______7__h _____6___i 123456789i ___4_____i
#     """

# @staticmethod
# def sudoku_xy_wing_03():
#     return f"""
#     xy_wing_03.sudoku
#     9
# __3______a 1________a ___4_____a ________9b _2_______b ____5____b _______8_c ______7__c _____6___c
# 123456789a ________9a ______7__a 1________b _______8_b _____6___b 123456789c 123456789c 123456789c
# _____6___a _______8_a 123456789a ___4_____b ______7__b __3______b 123456789c 123456789c 1________c
# _______8_d ____5____d _____6___d ______7__e __3______e _2_______e 123456789f 123456789f ________9f
# 123456789d __3______d ________9d ____5____e ___4_____e 123456789e ______7__f _____6___f 123456789f
# ___4_____d ______7__d 123456789d _____6___e ________9e 123456789e ____5____f 123456789f __3______f
# ______7__g _____6___g 123456789g _2_______h 1________h ___4_____h 123456789i 123456789i 123456789i
# 123456789g ___4_____g 123456789g _______8_h _____6___h ________9h 123456789i 123456789i ______7__i
# ________9g _2_______g 123456789g __3______h ____5____h ______7__h _____6___i 123456789i ___4_____i

#     """

# @staticmethod
# def sudoku_xy_wing_04():
#     return f"""
#     xy_wing_04.sudoku
#     9
# 123456789a _____6___a __3______a 123456789b ___4_____b ____5____b _2_______c _______8_c 123456789c
# 123456789a 123456789a 123456789a 123456789b 123456789b __3______b _____6___c ______7__c ___4_____c
# ___4_____a 123456789a 123456789a 123456789b 123456789b _____6___b 123456789c ____5____c __3______c
# _______8_d ___4_____d 123456789d 123456789e 123456789e 123456789e ______7__f 123456789f _____6___f
# 123456789d __3______d 1________d ___4_____e _____6___e ______7__e _______8_f 123456789f 123456789f
# ________9d ______7__d _____6___d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# _____6___g ____5____g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i _2_______i
# 123456789g 1________g 123456789g _____6___h 123456789h 123456789h ____5____i 123456789i _______8_i
# __3______g ________9g _______8_g ____5____h _2_______h 123456789h 123456789i _____6___i ______7__i

#     """

# @staticmethod
# def sudoku_xy_wing_05():
#     return f"""
#     xy_wing_05.sudoku
#     9
# 123456789a 123456789a _____6___a 123456789b _______8_b 123456789b 1________c 123456789c ______7__c
# 123456789a 123456789a _______8_a 123456789b 123456789b 123456789b ________9c 123456789c ____5____c
# ______7__a 123456789a ____5____a __3______b 123456789b _2_______b _____6___c _______8_c ___4_____c
# __3______d ______7__d ________9d 123456789e 123456789e ___4_____e _2_______f ____5____f _______8_f
# ____5____d _____6___d 1________d _______8_e _2_______e __3______e ___4_____f ______7__f ________9f
# _______8_d ___4_____d _2_______d ________9e 123456789e 123456789e __3______f _____6___f 1________f
# 123456789g _2_______g __3______g 123456789h 123456789h _______8_h ______7__i ___4_____i _____6___i
# _____6___g _______8_g ___4_____g 123456789h __3______h 123456789h ____5____i 123456789i _2_______i
# 123456789g ____5____g ______7__g _2_______h ___4_____h _____6___h _______8_i 123456789i __3______i

#     """

# @staticmethod
# def sudoku_xy_wing_06():
#     return f"""
#     xy_wing_06.sudoku
#     9
# __3______a 123456789a 1________a _______8_b 123456789b 123456789b ______7__c ____5____c _2_______c
# 123456789a 123456789a 123456789a 123456789b 123456789b 1________b _____6___c _______8_c ________9c
# 123456789a _______8_a 123456789a ______7__b 123456789b 123456789b __3______c 1________c ___4_____c
# 123456789d 123456789d 123456789d 123456789e 123456789e _______8_e ____5____f 123456789f 1________f
# 1________d 123456789d 123456789d ____5____e _2_______e 123456789e _______8_f 123456789f __3______f
# _______8_d ____5____d __3______d ________9e 1________e ______7__e ___4_____f _2_______f _____6___f
# ______7__g ___4_____g _______8_g 1________h ________9h __3______h _2_______i _____6___i ____5____i
# _2_______g __3______g ________9g _____6___h _______8_h ____5____h 1________i ___4_____i ______7__i
# _____6___g 1________g ____5____g 123456789h ______7__h 123456789h ________9i __3______i _______8_i

#     """

# @staticmethod
# def sudoku_xy_wing_07():
#     return f"""
#     xy_wing_07.sudoku
#     9
# _____6___a _2_______a 1________a __3______b ______7__b ________9b ____5____c ___4_____c _______8_c
# ________9a ___4_____a ____5____a 1________b _______8_b _2_______b _____6___c __3______c ______7__c
# ______7__a __3______a _______8_a 123456789b ____5____b 123456789b _2_______c ________9c 1________c
# 1________d 123456789d ________9d _______8_e 123456789e 123456789e 123456789f 123456789f 123456789f
# _______8_d 123456789d __3______d 123456789e _____6___e 1________e ________9f 123456789f 123456789f
# ___4_____d _____6___d _2_______d ____5____e ________9e ______7__e _______8_f 1________f __3______f
# ____5____g 1________g _____6___g 123456789h 123456789h _______8_h __3______i 123456789i ________9i
# _2_______g _______8_g ______7__g ________9h 123456789h 123456789h 123456789i 123456789i 123456789i
# __3______g ________9g ___4_____g 123456789h 123456789h ____5____h 123456789i _______8_i 123456789i

#     """

# @staticmethod
# def sudoku_xy_wing_08():
#     return f"""
#     xy_wing_08.sudoku
#     9
# _____6___a _______8_a ________9a ______7__b _2_______b 1________b ___4_____c ____5____c __3______c
# 1________a ____5____a _2_______a ___4_____b _______8_b __3______b ________9c _____6___c ______7__c
# 123456789a ______7__a 123456789a ________9b _____6___b ____5____b 123456789c _______8_c 123456789c
# 123456789d ___4_____d 123456789d _______8_e __3______e 123456789e 123456789f ______7__f ____5____f
# ______7__d 123456789d 123456789d 123456789e ___4_____e 123456789e __3______f 123456789f _______8_f
# 123456789d __3______d 123456789d 123456789e ______7__e _2_______e 123456789f 123456789f ___4_____f
# 123456789g 123456789g 123456789g _____6___h ____5____h _______8_h ______7__i ___4_____i ________9i
# ____5____g ________9g ______7__g _2_______h 1________h ___4_____h _______8_i __3______i _____6___i
# 123456789g _____6___g 123456789g __3______h ________9h ______7__h ____5____i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_xy_wing_09():
#     return f"""
#     xy_wing_09.sudoku
#     9
#     1________a ________9a __3______a _____6___b 123456789b 123456789b ______7__c 123456789c _______8_c
#     ___4_____a _2_______a _______8_a 1________b ______7__b 123456789b _____6___c 123456789c 123456789c
#     ______7__a ____5____a _____6___a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
#     123456789d ___4_____d ______7__d 123456789e __3______e 123456789e 123456789f _____6___f 123456789f
#     ____5____d _____6___d 123456789d ___4_____e ________9e ______7__e 123456789f _______8_f __3______f
#     123456789d __3______d 123456789d 123456789e _____6___e 123456789e ___4_____f ______7__f 123456789f
#     _____6___g _______8_g ________9g ______7__h 1________h 123456789h __3______i 123456789i ___4_____i
#     __3______g 1________g ____5____g 123456789h ___4_____h _____6___h 123456789i ________9i ______7__i
#     _2_______g ______7__g ___4_____g 123456789h 123456789h 123456789h 123456789i 1________i _____6___i
#     """

# @staticmethod
# def sudoku_xy_wing_10():
#     return f"""
#     xy_wing_10.sudoku
#     9
# 123456789a _____6___a 123456789a ___4_____b 123456789b 1________b 123456789c _______8_c 123456789c
# ________9a _______8_a ___4_____a ____5____b ______7__b _____6___b _2_______c __3______c 1________c
# 1________a 123456789a 123456789a 123456789b 123456789b ________9b _____6___c ______7__c ___4_____c
# _____6___d 123456789d _2_______d 123456789e 123456789e __3______e ___4_____f 123456789f ______7__f
# __3______d ___4_____d 1________d ______7__e ________9e 123456789e _______8_f _____6___f 123456789f
# _______8_d ______7__d 123456789d _____6___e ___4_____e 123456789e 1________f 123456789f __3______f
# ___4_____g 123456789g _______8_g 123456789h 123456789h ______7__h 123456789i 123456789i _____6___i
# ____5____g __3______g 123456789g _2_______h _____6___h ___4_____h 123456789i 1________i _______8_i
# 123456789g 1________g _____6___g 123456789h 123456789h _______8_h 123456789i ___4_____i 123456789i

#     """

# @staticmethod
# def sudoku_xy_wing_11():
#     return f"""
#     xy_wing_11.sudoku
#     9
# ________9a __3______a _2_______a 123456789b 1________b 123456789b _____6___c ______7__c ____5____c
# _____6___a ____5____a ___4_____a __3______b _2_______b ______7__b ________9c _______8_c 1________c
# 1________a _______8_a ______7__a _____6___b ________9b ____5____b _2_______c __3______c ___4_____c
# ______7__d 123456789d _____6___d ________9e 123456789e 123456789e 123456789f 123456789f 123456789f
# __3______d 123456789d ________9d 123456789e ___4_____e _____6___e 123456789f 123456789f ______7__f
# ____5____d ___4_____d _______8_d 1________e ______7__e _2_______e __3______f _____6___f ________9f
# _2_______g ________9g ____5____g ______7__h 123456789h 123456789h 123456789i 123456789i 123456789i
# _______8_g ______7__g __3______g 123456789h 123456789h 1________h 123456789i ________9i 123456789i
# ___4_____g _____6___g 1________g 123456789h 123456789h ________9h ______7__i 123456789i __3______i

#     """

# @staticmethod
# def sudoku_x_wing_0():
#     return f"""
#     x_wing_0.sudoku
#     9
#     123456789a 123456789a 123456789a 123456789b 123456789b 123456789b ______7__c 123456789c ___4_____c
#     __3______a 123456789a 123456789a 123456789b ______7__b 123456789b 123456789c 123456789c ____5____c
#     123456789a 123456789a 123456789a 123456789b 1________b _______8_b 123456789c 123456789c _2_______c
#     1________d ____5____d 123456789d ________9e _2_______e 123456789e _______8_f 123456789f __3______f
#     123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
#     _____6___d 123456789d _______8_d 123456789e __3______e 1________e 123456789f ___4_____f ______7__f
#     _2_______g 123456789g 123456789g _______8_h ___4_____h 123456789h 123456789i 123456789i 123456789i
#     ____5____g 123456789g 123456789g 123456789h ________9h 123456789h 123456789i 123456789i 1________i
#     ___4_____g 123456789g ______7__g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_x_wing_1():
#     return f"""
#     x_wing_1.sudoku
#     9
#     _______8_a 7a 9a _________b 5b _________b 4c _________c _________c
#     2a 5a _________a 7b _________b 4b _________c 9c _______8_c
#     _________a 1a 4a 9b _______8_b 2b 7c 5c _________c
#     9d 4d 7d 5e _________e _________e _________f _________f _________f
#     1d _______8_d 5d 6e 2e 7e 3f 4f 9f
#     _________d _________d 2d 4e 9e _______8_e 5f 1f 7f
#     4g 2g 1g _______8_h 7h _________h _________i _________i 5i
#     7g 9g _________g 2h _________h 5h _________i _________i 4i
#     5g _________g _________g _________h 4h _________h _________i 7i _________i
#     """

# @staticmethod
# def sudoku_x_wing_2():
#     return f"""
#     x_wing_2.sudoku
#     9
# ________9a _______8_a ______7__a _2_______b ____5____b _____6___b 1________c ___4_____c __3______c
# ___4_____a __3______a _____6___a _______8_b 1________b ______7__b ________9c _2_______c ____5____c
# ____5____a _2_______a 1________a ________9b __3______b ___4_____b 123456789c ______7__c 123456789c
# ______7__d ____5____d 123456789d _____6___e _2_______e 1________e 123456789f ________9f 123456789f
# 123456789d ___4_____d ________9d ____5____e ______7__e _______8_e 123456789f 1________f 123456789f
# 1________d _____6___d 123456789d ___4_____e ________9e __3______e 123456789f ____5____f ______7__f
# 123456789g 1________g 123456789g ______7__h _______8_h ________9h ____5____i _____6___i 123456789i
# _____6___g ________9g ____5____g __3______h ___4_____h _2_______h ______7__i _______8_i 1________i
# _______8_g ______7__g 123456789g 1________h _____6___h ____5____h 123456789i __3______i ________9i

#     """

# @staticmethod
# def sudoku_x_wing_3():
#     return f"""
#     x_wing_3.sudoku
#     9
#     5a 0a 7a 9b 0b 0b 1c 0c 6c
#     6a 3a 4a 1b 7b 5b 8c 9c 2c
#     0a 1a 9a 0b 0b 0b 5c 0c 7c
#     7d 9d 6d 2e 1e 3e 4f 5f 8f
#     3d 4d 2d 5e 9e 8e 7f 6f 1f
#     1d 5d 8d 6e 4e 7e 9f 2f 3f
#     0g 0g 1g 0h 5h 0h 3i 7i 9i
#     9g 7g 5g 3h 2h 1h 6i 8i 4i
#     4g 0g 3g 7h 0h 9h 2i 1i 5i
#     """









# @staticmethod
# def sudoku_unique_rectangle_type1_south_east_in_rows():
#     return f"""
#         unique_rectangle_type1_south_east_in_rows.sudoku
#         9
#         _____6___a ______7__a _2_______a ____5____b ________9b __3______b 1________c ___4_____c _______8_c
# 1________a __3______a _______8_a 123456789b 123456789b ___4_____b ____5____c ______7__c ________9c
# ___4_____a ________9a ____5____a 1________b ______7__b _______8_b __3______c _2_______c _____6___c
# ________9d _2_______d 123456789d 123456789e ____5____e 1________e _______8_f __3______f 123456789f
# __3______d 1________d 123456789d _______8_e 123456789e ________9e 123456789f ____5____f 123456789f
# ____5____d _______8_d ___4_____d ______7__e __3______e _2_______e ________9f _____6___f 1________f
# 123456789g ___4_____g 1________g __3______h 123456789h _____6___h ______7__i ________9i ____5____i
# 123456789g ____5____g __3______g ________9h 123456789h ______7__h _____6___i 1________i 123456789i
# ______7__g _____6___g ________9g 123456789h 1________h ____5____h 123456789i _______8_i __3______i
#         """

# @staticmethod
# def sudoku_unique_rectangle_type1_south_west_in_cols():
#     return f"""
#         unique_rectangle_type1_south_west_in_cols.sudoku
#         9
# _2_______a _____6___a 123456789a ________9b __3______b 123456789b 123456789c 123456789c 123456789c
# 123456789a _______8_a __3______a _____6___b ___4_____b 123456789b 123456789c 123456789c _2_______c
# ___4_____a ________9a ______7__a ____5____b _2_______b _______8_b _____6___c __3______c 1________c
# ______7__d ___4_____d _____6___d _2_______e _______8_e ________9e __3______f 1________f ____5____f
# _______8_d ____5____d ________9d __3______e 1________e _____6___e _2_______f ___4_____f ______7__f
# 123456789d 123456789d _2_______d ______7__e ____5____e ___4_____e _______8_f _____6___f ________9f
# _____6___g _2_______g _______8_g ___4_____h ________9h ____5____h 1________i ______7__i __3______i
# ________9g ______7__g 123456789g 123456789h _____6___h __3______h ____5____i _2_______i 123456789i
# 123456789g 123456789g 123456789g 123456789h ______7__h _2_______h 123456789i 123456789i _____6___i

#         """

# @staticmethod
# def sudoku_unique_rectangle_type1_north_east_in_cols():
#     return f"""
#         unique_rectangle_type1_north_east_in_cols.sudoku
#         9
# ________9a 1________a _2_______a ____5____b ___4_____b _______8_b ______7__c __3______c _____6___c
# ____5____a ___4_____a 123456789a 1________b ______7__b 123456789b _______8_c ________9c _2_______c
# _______8_a ______7__a 123456789a 123456789b ________9b _2_______b 1________c ____5____c ___4_____c
# 123456789d _____6___d ___4_____d 123456789e 1________e 123456789e ____5____f _______8_f 123456789f
# 123456789d ____5____d ________9d ___4_____e _______8_e 123456789e _____6___f _2_______f 123456789f
# 123456789d __3______d _______8_d 123456789e 123456789e 123456789e ___4_____f ______7__f 123456789f
# _____6___g ________9g ______7__g _______8_h _2_______h ___4_____h __3______i 1________i ____5____i
# ___4_____g _______8_g ____5____g ________9h __3______h 1________h _2_______i _____6___i ______7__i
# __3______g _2_______g 1________g ______7__h 123456789h 123456789h ________9i ___4_____i _______8_i
#         """

# @staticmethod
# def sudoku_unique_rectangle_type1_south_east_in_cols():
#     return f"""
#         unique_rectangle_type1_south_east_in_cols.sudoku
#         9
# _______8_a __3______a ______7__a ___4_____b 123456789b 123456789b ____5____c _____6___c 1________c
# 123456789a 123456789a ________9a ____5____b __3______b _____6___b _2_______c ______7__c _______8_c
# ____5____a _2_______a _____6___a 1________b ______7__b _______8_b ________9c 123456789c 123456789c
# _2_______d 123456789d _______8_d ________9e ___4_____e __3______e 123456789f 1________f ____5____f
# __3______d 123456789d ____5____d _______8_e _____6___e 1________e 123456789f _2_______f ________9f
# 123456789d ________9d 1________d _2_______e ____5____e ______7__e _______8_f 123456789f 123456789f
# 123456789g 123456789g ___4_____g ______7__h 123456789h ____5____h __3______i _______8_i 123456789i
# ______7__g ____5____g __3______g _____6___h _______8_h 123456789h 1________i ________9i 123456789i
# 123456789g _______8_g _2_______g __3______h 123456789h 123456789h 123456789i ____5____i ______7__i
#         """

# @staticmethod
# def sudoku_unique_rectangle_type1_north_west_in_rows():
#     return f"""
#         unique_rectangle_type1_north_west_in_rows.sudoku
#         9
# ________9a 1________a _2_______a 123456789b 123456789b 123456789b _____6___c 123456789c _______8_c
# _______8_a ___4_____a _____6___a ________9b 123456789b _2_______b 123456789c 123456789c ____5____c
# __3______a ______7__a ____5____a _______8_b _____6___b 1________b ________9c ___4_____c _2_______c
# _____6___d ____5____d ________9d ______7__e _______8_e ___4_____e __3______f _2_______f 1________f
# 1________d _______8_d __3______d ____5____e _2_______e ________9e ___4_____f _____6___f ______7__f
# ___4_____d _2_______d ______7__d _____6___e 1________e __3______e ____5____f _______8_f ________9f
# _2_______g _____6___g _______8_g 123456789h 123456789h 123456789h 123456789i 123456789i __3______i
# ____5____g 123456789g ___4_____g 123456789h 123456789h _______8_h _2_______i 123456789i _____6___i
# ______7__g 123456789g 1________g _2_______h 123456789h _____6___h _______8_i ____5____i ___4_____i

#         """

# @staticmethod
# def sudoku_unique_rectangle_type1_north_east_in_rows():
#     return f"""
#         unique_rectangle_type1_north_east_in_rows.sudoku
#         9
# _2_______a __3______a ______7__a _____6___b ____5____b ________9b _______8_c ___4_____c 1________c
# _______8_a ________9a _____6___a __3______b 123456789b 123456789b ______7__c _2_______c ____5____c
# ____5____a ___4_____a 1________a _______8_b _2_______b ______7__b ________9c _____6___c __3______c
# _____6___d ______7__d __3______d 1________e _______8_e ____5____e _2_______f ________9f ___4_____f
# ________9d _______8_d 123456789d _2_______e 123456789e _____6___e 123456789f 123456789f ______7__f
# 1________d _2_______d 123456789d ________9e ______7__e 123456789e _____6___f 123456789f _______8_f
# ___4_____g ____5____g _2_______g ______7__h ________9h 123456789h 123456789i _______8_i _____6___i
# ______7__g 123456789g _______8_g ____5____h 123456789h _2_______h ___4_____i 123456789i ________9i
# __3______g 123456789g ________9g ___4_____h 123456789h _______8_h ____5____i ______7__i _2_______i
#         """

# @staticmethod
# def sudoku_unique_rectangle_type1_north_west_in_cols():
#     return f"""
#         unique_rectangle_type1_north_west_in_cols.sudoku
#         9
# 123456789a ________9a ______7__a _2_______b 123456789b 123456789b 123456789c __3______c 123456789c
# 123456789a __3______a ___4_____a 123456789b 123456789b ______7__b 123456789c _2_______c 123456789c
# _2_______a ____5____a _______8_a 123456789b _____6___b 123456789b 123456789c 1________c ______7__c
# ______7__d _2_______d ____5____d 123456789e 123456789e 123456789e __3______f _____6___f ________9f
# ___4_____d 1________d _____6___d 123456789e ______7__e 123456789e _2_______f ____5____f _______8_f
# __3______d _______8_d ________9d ____5____e _2_______e _____6___e ______7__f ___4_____f 1________f
# ________9g ___4_____g 1________g ______7__h __3______h ____5____h _____6___i _______8_i _2_______i
# ____5____g _____6___g __3______g _______8_h ________9h _2_______h 1________i ______7__i ___4_____i
# _______8_g ______7__g _2_______g _____6___h 1________h ___4_____h ____5____i ________9i __3______i

#         """

# @staticmethod
# def sudoku_unique_rectangle_type1_south_west_in_rows():
#     return f"""   
#         unique_rectangle_type1_south_west_in_rows.sudoku
#         9
# ___4_____a 123456789a __3______a ______7__b 123456789b 123456789b 123456789c 123456789c ____5____c
# _______8_a 123456789a _2_______a ____5____b 123456789b 123456789b 123456789c 123456789c __3______c
# ________9a ____5____a ______7__a 123456789b __3______b _____6___b 123456789c ___4_____c 1________c
# 1________d ___4_____d ____5____d __3______e _2_______e 123456789e _____6___f _______8_f 123456789f
# __3______d _2_______d _____6___d 123456789e 123456789e 123456789e ___4_____f ____5____f 123456789f
# ______7__d ________9d _______8_d ___4_____e _____6___e ____5____e __3______f 1________f _2_______f
# _____6___g __3______g 123456789g 123456789h ____5____h 123456789h 1________i 123456789i _______8_i
# ____5____g _______8_g 123456789g 123456789h 123456789h __3______h 123456789i 123456789i _____6___i
# _2_______g ______7__g 123456789g _____6___h 123456789h _______8_h ____5____i __3______i ___4_____i

#         """

# @staticmethod
# def sudoku_unique_rectangle_type2_east():
#     return f"""
#         unique_rectangle_type2_east.sudoku
#         9
# ______7__a _2_______a __3______a 123456789b ____5____b ___4_____b ________9c _______8_c 123456789c
# 123456789a _______8_a ___4_____a 123456789b ________9b _2_______b 123456789c 123456789c __3______c
# 123456789a ________9a 1________a _______8_b 123456789b __3______b 123456789c _2_______c ___4_____c
# __3______d ___4_____d ____5____d 123456789e 1________e _______8_e 123456789f ________9f _2_______f
# _______8_d 123456789d _____6___d __3______e _2_______e ________9e ___4_____f 123456789f ____5____f
# ________9d 123456789d _2_______d ___4_____e 123456789e ____5____e _______8_f __3______f 123456789f
# _2_______g __3______g ______7__g ________9h ___4_____h _____6___h 1________i ____5____i _______8_i
# ___4_____g ____5____g ________9g _2_______h _______8_h 1________h __3______i _____6___i ______7__i
# 1________g _____6___g _______8_g ____5____h __3______h ______7__h _2_______i ___4_____i ________9i
#         """

# @staticmethod
# def sudoku_unique_rectangle_type2_south():
#     return f"""
#         unique_rectangle_type2_south.sudoku
#         9
# 123456789a _______8_a 123456789a 123456789b __3______b 123456789b _2_______c ______7__c ___4_____c
# 123456789a ___4_____a _2_______a 123456789b 123456789b ______7__b 123456789c ____5____c __3______c
# __3______a ______7__a 123456789a 123456789b _2_______b 123456789b ________9c 1________c 123456789c
# ___4_____d 1________d __3______d ______7__e ________9e _______8_e ____5____f _____6___f _2_______f
# _____6___d ____5____d ______7__d 123456789e ___4_____e 123456789e __3______f _______8_f ________9f
# _2_______d ________9d _______8_d _____6___e ____5____e __3______e ______7__f ___4_____f 1________f
# _______8_g _____6___g ________9g 123456789h ______7__h 123456789h 123456789i __3______i ____5____i
# ______7__g _2_______g ___4_____g __3______h 123456789h ____5____h 123456789i ________9i 123456789i
# ____5____g __3______g 1________g 123456789h _______8_h 123456789h 123456789i _2_______i ______7__i
#         """

# @staticmethod
# def sudoku_unique_rectangle_type2_west():
#     return f"""
#         unique_rectangle_type2_west.sudoku
#         9
# _2_______a 123456789a 123456789a _____6___b 123456789b 1________b __3______c ____5____c ______7__c
# 1________a ____5____a _____6___a ______7__b _2_______b __3______b ________9c _______8_c ___4_____c
# 123456789a ______7__a __3______a ________9b ____5____b 123456789b _2_______c _____6___c 1________c
# ________9d __3______d _2_______d ___4_____e _____6___e ____5____e ______7__f 1________f _______8_f
# ____5____d ___4_____d _______8_d 1________e ______7__e ________9e _____6___f __3______f _2_______f
# ______7__d _____6___d 1________d _______8_e __3______e _2_______e ___4_____f ________9f ____5____f
# __3______g 123456789g ____5____g _2_______h 123456789h 123456789h 123456789i 123456789i _____6___i
# 123456789g 123456789g ______7__g __3______h 123456789h _____6___h ____5____i _2_______i ________9i
# _____6___g _2_______g 123456789g ____5____h 123456789h 123456789h 123456789i 123456789i __3______i
#         """

# @staticmethod
# def sudoku_unique_rectangle_type4_south_rows():
#     return f"""
#         unique_rectangle_type4_south_rows.sudoku
#         9
# __3______a 123456789a ____5____a _______8_b _2_______b 123456789b 1________c ______7__c ________9c
# 123456789a 123456789a 123456789a 123456789b 1________b 123456789b ___4_____c 123456789c _____6___c
# 123456789a 123456789a 1________a 123456789b ________9b 123456789b _2_______c 123456789c 123456789c
# ____5____d 1________d _____6___d ___4_____e _______8_e ________9e ______7__f _2_______f __3______f
# ______7__d _______8_d ___4_____d 123456789e __3______e 123456789e _____6___f ________9f 1________f
# _2_______d ________9d __3______d _____6___e ______7__e 1________e _______8_f 123456789f 123456789f
# 123456789g ____5____g 123456789g 123456789h _____6___h 123456789h __3______i 123456789i ______7__i
# 1________g 123456789g ______7__g 123456789h ____5____h 123456789h ________9i _____6___i 123456789i
# _____6___g __3______g 123456789g 123456789h ___4_____h 123456789h ____5____i 123456789i _2_______i

#         """

# @staticmethod
# def sudoku_unique_rectangle_type4_south_cols():
#     return f"""
#         unique_rectangle_type4_south_cols.sudoku
#         9
# 123456789a _____6___a 123456789a _______8_b _2_______b ____5____b ______7__c 1________c ________9c
# ______7__a 123456789a 123456789a ___4_____b 1________b _____6___b __3______c ____5____c 123456789c
# 123456789a ____5____a 123456789a __3______b ______7__b ________9b _____6___c 123456789c ___4_____c
# ____5____d 1________d ______7__d _____6___e 123456789e 123456789e 123456789f __3______f 123456789f
# 123456789d 123456789d 123456789d ______7__e 123456789e 123456789e 1________f 123456789f ____5____f
# 123456789d _______8_d 123456789d 1________e ____5____e __3______e 123456789f ______7__f _____6___f
# _______8_g __3______g ____5____g 123456789h _____6___h 1________h 123456789i ___4_____i ______7__i
# 123456789g ______7__g 123456789g 123456789h ___4_____h _______8_h ____5____i 123456789i __3______i
# ________9g ___4_____g _2_______g ____5____h __3______h ______7__h _______8_i _____6___i 1________i

#         """

# @staticmethod
# def sudoku_unique_rectangle_type4_east_rows():
#     return f"""
#         unique_rectangle_type4_east_rows.sudoku
#         9
# ________9a ___4_____a _2_______a 123456789b 123456789b __3______b ______7__c 1________c 123456789c
# _______8_a 1________a 123456789a _2_______b ___4_____b 123456789b ________9c ____5____c 123456789c
# ____5____a _____6___a 123456789a 123456789b 123456789b 1________b ___4_____c _2_______c 123456789c
# _2_______d _______8_d _____6___d __3______e 123456789e 123456789e 123456789f ________9f ___4_____f
# 123456789d ______7__d ________9d 123456789e _______8_e _2_______e __3______f _____6___f 123456789f
# 123456789d __3______d ____5____d 123456789e 123456789e 123456789e _______8_f ______7__f _2_______f
# _____6___g ____5____g 1________g ______7__h __3______h ___4_____h _2_______i _______8_i ________9i
# ______7__g ________9g ___4_____g 123456789h _2_______h _______8_h _____6___i __3______i 123456789i
# __3______g _2_______g _______8_g _____6___h 123456789h 123456789h 123456789i ___4_____i ______7__i

#         """

# @staticmethod
# def sudoku_unique_rectangle_type4_west_rows():
#     return f"""
#         unique_rectangle_type4_west_rows.sudoku
#         9        
#         _____6___a ________9a 1________a 123456789b ___4_____b _______8_b _2_______c ______7__c 123456789c
# 123456789a 123456789a ______7__a 123456789b 123456789b 123456789b 123456789c ________9c 123456789c
# 123456789a 123456789a 123456789a 123456789b ________9b ______7__b 123456789c ___4_____c 123456789c
# ______7__d _______8_d _____6___d ________9e 1________e _2_______e __3______f ____5____f ___4_____f
# ________9d 123456789d 123456789d 123456789e __3______e 123456789e ______7__f _______8_f 1________f
# ____5____d 1________d __3______d ______7__e _______8_e ___4_____e ________9f _2_______f _____6___f
# 1________g __3______g 123456789g 123456789h 123456789h 123456789h _______8_i _____6___i ______7__i
# 123456789g ______7__g 123456789g 123456789h _____6___h 123456789h ____5____i 1________i _2_______i
# _2_______g _____6___g ____5____g _______8_h ______7__h 1________h ___4_____i __3______i ________9i
#         """

# @staticmethod
# def sudoku_unique_rectangle_type4_west_cols():
#     return f"""
#         unique_rectangle_type4_west_cols.sudoku
#         9
# _____6___a 1________a 123456789a ____5____b ______7__b ___4_____b 123456789c 123456789c _2_______c
# _2_______a 123456789a ____5____a 1________b ________9b _______8_b 123456789c 123456789c 123456789c
# 123456789a ______7__a 123456789a _____6___b __3______b _2_______b 1________c 123456789c ____5____c
# 123456789d 123456789d 123456789d __3______e 123456789e _____6___e 123456789f 123456789f ________9f
# __3______d ____5____d _____6___d ________9e _2_______e ______7__e _______8_f 1________f ___4_____f
# 123456789d 123456789d 123456789d _______8_e 123456789e 1________e 123456789f 123456789f 123456789f
# ____5____g _______8_g _2_______g ______7__h _____6___h ________9h ___4_____i __3______i 1________i
# 123456789g _____6___g 123456789g ___4_____h _______8_h 123456789h 123456789i 123456789i ______7__i
# ___4_____g 123456789g ______7__g _2_______h 1________h 123456789h 123456789i _____6___i _______8_i
#         """

# @staticmethod
# def sudoku_unique_rectangle_type4_east_cols():
#     return f"""
#         unique_rectangle_type4_east_cols.sudoku
#         9
# _2_______a 123456789a 123456789a 123456789b 123456789b 123456789b ______7__c ________9c ____5____c
# 123456789a ____5____a ______7__a ________9b 123456789b 123456789b _____6___c 1________c ___4_____c
# ________9a 1________a _____6___a ______7__b ___4_____b ____5____b __3______c _______8_c _2_______c
# ______7__d _____6___d 1________d _2_______e _______8_e ___4_____e ____5____f __3______f ________9f
# 123456789d 123456789d 123456789d ____5____e ________9e 1________e _______8_f _____6___f ______7__f
# ____5____d ________9d _______8_d __3______e ______7__e _____6___e _2_______f ___4_____f 1________f
# 1________g __3______g 123456789g _______8_h ____5____h ______7__h 123456789i _2_______i _____6___i
# 123456789g 123456789g ____5____g 123456789h 123456789h ________9h 123456789i ______7__i __3______i
# _____6___g ______7__g 123456789g ___4_____h 123456789h 123456789h 123456789i ____5____i _______8_i
#         """

# @staticmethod
# def sudoku_bug():
#     return f"""
#         bug.sudoku
#         9
# ___4_____a _____6___a ____5____a 1________b __3______b _2_______b ________9c ______7__c _______8_c
# 123456789a 123456789a 123456789a _______8_b _____6___b ___4_____b __3______c 1________c ____5____c
# 1________a __3______a _______8_a ____5____b ________9b ______7__b ___4_____c _2_______c _____6___c
# _____6___d _______8_d 123456789d __3______e ___4_____e 123456789e 123456789f ____5____f 123456789f
# ____5____d 123456789d __3______d _2_______e ______7__e 123456789e _____6___f _______8_f ___4_____f
# 123456789d 123456789d ___4_____d _____6___e ____5____e _______8_e 123456789f __3______f 123456789f
# _______8_g ______7__g 1________g ________9h _2_______h _____6___h ____5____i ___4_____i __3______i
# _2_______g ____5____g ________9g ___4_____h 1________h __3______h _______8_i _____6___i ______7__i
# __3______g ___4_____g _____6___g ______7__h _______8_h ____5____h _2_______i ________9i 1________i

#         """

# @staticmethod
# def sudoku_hidden_triple_row():
#     return f"""
#         hidden_triple_row.sudoku
#         9
# 123456789a __3______a ____5____a ______7__b _2_______b 1________b _______8_c ___4_____c 123456789c
# ______7__a 123456789a 123456789a __3______b ___4_____b _____6___b _2_______c 123456789c ____5____c
# 123456789a ___4_____a _2_______a _______8_b ____5____b ________9b 123456789c __3______c 123456789c
# 123456789d ____5____d _____6___d ________9e 123456789e _2_______e __3______f 123456789f ___4_____f
# 123456789d 123456789d 123456789d 123456789e __3______e 123456789e ____5____f 123456789f 123456789f
# __3______d 123456789d ___4_____d _____6___e 123456789e ____5____e 1________f 123456789f 123456789f
# 123456789g ________9g 123456789g 123456789h 123456789h 123456789h 123456789i ____5____i 123456789i
# ____5____g 123456789g 1________g _2_______h ________9h __3______h ___4_____i 123456789i _______8_i
# ___4_____g 123456789g 123456789g ____5____h 123456789h _______8_h ________9i 123456789i 123456789i

#         """

# @staticmethod
# def sudoku_hidden_quad_fence():
#     return f"""
#         hidden_quad_fence.sudoku
#         9
# _____6___a 1________a ______7__a 123456789b _______8_b 123456789b ____5____c 123456789c 123456789c
# ________9a _______8_a ___4_____a ____5____b 123456789b _____6___b 123456789c 123456789c 123456789c
# ____5____a _2_______a __3______a 1________b ________9b ______7__b _____6___c _______8_c ___4_____c
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e ___4_____f ____5____f 123456789f
# 1________d 123456789d _____6___d 123456789e 123456789e 123456789e _2_______f 123456789f _______8_f
# 123456789d ___4_____d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# _2_______g ______7__g 123456789g __3______h 123456789h 1________h _______8_i ___4_____i 123456789i
# ___4_____g 123456789g 123456789g ________9h 123456789h _______8_h 123456789i _2_______i __3______i
# 123456789g 123456789g 123456789g 123456789h ___4_____h _2_______h 123456789i 123456789i ____5____i
#         """

# @staticmethod
# def sudoku_hidden_triple_col():
#     return f"""
#         hidden_triple_col.sudoku
#         9
# __3______a 123456789a ____5____a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# _____6___a 1________a _2_______a _______8_b 123456789b ___4_____b ________9c __3______c 123456789c
# 123456789a ______7__a _______8_a 123456789b __3______b 1________b _____6___c 123456789c 123456789c
# _______8_d _2_______d 123456789d 123456789e 123456789e ________9e 123456789f 123456789f _____6___f
# 1________d _____6___d 123456789d 123456789e 123456789e 123456789e 123456789f ______7__f 123456789f
# ______7__d ____5____d 123456789d ___4_____e 123456789e 123456789e 123456789f 123456789f _2_______f
# 123456789g __3______g ______7__g _____6___h 123456789h _______8_h 123456789i ____5____i 123456789i
# 123456789g _______8_g 1________g __3______h 123456789h _2_______h ______7__i _____6___i 123456789i
# 123456789g 123456789g _____6___g 123456789h 123456789h 123456789h _______8_i 123456789i __3______i

#         """

# @staticmethod
# def sudoku_hidden_triple_fence():
#     return f"""
#         hidden_triple_fence.sudoku
#         9
# 123456789a 123456789a 1________a 123456789b ______7__b _____6___b 123456789c 123456789c 123456789c
# 123456789a ________9a 123456789a 123456789b __3______b 1________b 123456789c ___4_____c 123456789c
# _______8_a 123456789a __3______a ___4_____b ____5____b ________9b 123456789c 123456789c 123456789c
# __3______d 1________d _______8_d ______7__e ________9e ___4_____e 123456789f 123456789f 123456789f
# _2_______d ____5____d _____6___d __3______e 1________e _______8_e ___4_____f ______7__f ________9f
# 123456789d 123456789d 123456789d ____5____e _____6___e _2_______e 123456789f 123456789f _______8_f
# 123456789g 123456789g 123456789g 123456789h _2_______h __3______h 123456789i 123456789i ____5____i
# 123456789g __3______g 123456789g 123456789h _______8_h ______7__h 123456789i _2_______i ___4_____i
# 123456789g 123456789g _2_______g ________9h ___4_____h ____5____h ______7__i 123456789i 123456789i

#         """

# @staticmethod
# def sudoku_hidden_quad_row():
#     return f"""
#         hidden_quad_row.sudoku
#         9
# 123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# 1________a _____6___a 123456789a 123456789b ________9b _2_______b 123456789c _______8_c __3______c
# ____5____a ________9a 123456789a 123456789b _____6___b 123456789b 123456789c 123456789c ______7__c
# 123456789d __3______d 123456789d 123456789e _2_______e 1________e 123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d ___4_____e ____5____e 123456789e 123456789f _2_______f 123456789f
# ______7__g 123456789g 123456789g 123456789h __3______h 123456789h 123456789i _____6___i ___4_____i
# _______8_g ___4_____g 123456789g _____6___h 1________h ____5____h 123456789i ______7__i ________9i
# 123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i

#         """

# @staticmethod
# def sudoku_hidden_quad_col():
#     return f"""
#         hidden_quad_col.sudoku
#         9
# ______7__a ________9a _____6___a 123456789b 123456789b _2_______b _______8_c ___4_____c __3______c
# _______8_a 1________a __3______a 123456789b 123456789b ________9b ____5____c _2_______c _____6___c
# ____5____a ___4_____a _2_______a _____6___b 123456789b 123456789b ________9c 1________c ______7__c
# ________9d _______8_d ___4_____d 123456789e 123456789e 123456789e ______7__f _____6___f 1________f
# __3______d _____6___d 1________d 123456789e 123456789e 123456789e ___4_____f ____5____f _2_______f
# _2_______d ______7__d ____5____d 123456789e 123456789e 123456789e __3______f ________9f _______8_f
# ___4_____g __3______g _______8_g 123456789h 123456789h 1________h _____6___i ______7__i ____5____i
# 1________g ____5____g ________9g _______8_h 123456789h 123456789h _2_______i __3______i ___4_____i
# _____6___g _2_______g ______7__g __3______h 123456789h 123456789h 1________i _______8_i ________9i
#         """

# @staticmethod
# def sudoku_x_wing_row():
#     return f"""
#         x_wing_row.sudoku
#         9
# 123456789a ______7__a ________9a 1________b 123456789b _______8_b _2_______c ___4_____c 123456789c
# ___4_____a ____5____a 123456789a ________9b _2_______b 123456789b 123456789c _______8_c 123456789c
# _______8_a 123456789a _2_______a ___4_____b 123456789b 123456789b 123456789c 123456789c 123456789c
# _2_______d ___4_____d ____5____d __3______e ______7__e 1________e ________9f _____6___f _______8_f
# ______7__d __3______d _____6___d _______8_e ___4_____e ________9e 1________f ____5____f _2_______f
# 1________d ________9d _______8_d ____5____e _____6___e _2_______e ___4_____f __3______f ______7__f
# ________9g _2_______g ___4_____g 123456789h _______8_h ____5____h 123456789i 1________i __3______i
# ____5____g 123456789g 123456789g 123456789h ________9h __3______h _______8_i _2_______i ___4_____i
# 123456789g _______8_g 123456789g _2_______h 1________h ___4_____h ____5____i 123456789i 123456789i
#         """

# @staticmethod
# def sudoku_x_wing_col():
#     return f"""
#         x_wing_col.sudoku
#         9
# 123456789a ________9a _____6___a 123456789b 123456789b ____5____b ___4_____c _2_______c ______7__c
# ______7__a 123456789a ___4_____a _2_______b 123456789b _____6___b ____5____c 1________c ________9c
# _2_______a 1________a ____5____a ______7__b ___4_____b ________9b _____6___c _______8_c __3______c
# ________9d ___4_____d ______7__d ____5____e _____6___e 1________e _______8_f __3______f _2_______f
# ____5____d 123456789d 123456789d ___4_____e 123456789e __3______e 123456789f ______7__f _____6___f
# 123456789d _____6___d __3______d 123456789e ______7__e _2_______e 123456789f ____5____f ___4_____f
# 123456789g 123456789g 123456789g 123456789h ____5____h ___4_____h ______7__i _____6___i _______8_i
# ___4_____g ____5____g _______8_g _____6___h _2_______h ______7__h __3______i ________9i 1________i
# _____6___g ______7__g 123456789g __3______h 123456789h _______8_h _2_______i ___4_____i ____5____i
#         """

# @staticmethod
# def sudoku_w_wing_row():
#     return f"""
#         w_wing_row.sudoku
#         9
# __3______a 1________a ____5____a ___4_____b ________9b _______8_b _2_______c _____6___c ______7__c
# _______8_a 123456789a 123456789a 123456789b 123456789b 123456789b ___4_____c __3______c 1________c
# 123456789a ______7__a 123456789a __3______b 1________b _2_______b ________9c _______8_c ____5____c
# 123456789d _______8_d ______7__d _2_______e 123456789e __3______e 123456789f 1________f ________9f
# ________9d __3______d 123456789d 123456789e _______8_e 123456789e 123456789f _2_______f 123456789f
# ____5____d 123456789d 123456789d 123456789e 123456789e ________9e _______8_f 123456789f __3______f
# ______7__g _____6___g 123456789g ________9h _2_______h 1________h __3______i ____5____i 123456789i
# 1________g ____5____g __3______g _______8_h 123456789h 123456789h 123456789i ________9i _2_______i
# _2_______g 123456789g 123456789g 123456789h __3______h ____5____h 1________i 123456789i 123456789i

#         """

# @staticmethod
# def sudoku_w_wing_col():
#     return f"""
#         w_wing_col.sudoku
#         9
# 123456789a ___4_____a ____5____a 123456789b _____6___b ________9b ______7__c __3______c _2_______c
# 123456789a __3______a 123456789a 123456789b ____5____b 123456789b ___4_____c _______8_c ________9c
# 123456789a 123456789a _2_______a __3______b ___4_____b 123456789b ____5____c 1________c _____6___c
# ___4_____d 123456789d 123456789d 123456789e ______7__e 1________e __3______f 123456789f ____5____f
# ____5____d _2_______d 123456789d _____6___e __3______e ___4_____e ________9f ______7__f 123456789f
# 123456789d 123456789d __3______d ____5____e ________9e 123456789e 123456789f 123456789f ___4_____f
# __3______g _____6___g 123456789g 123456789h _______8_h ____5____h _2_______i ___4_____i 123456789i
# 123456789g 123456789g ___4_____g 123456789h _2_______h _____6___h 123456789i ____5____i __3______i
# _2_______g ____5____g 123456789g ___4_____h 1________h __3______h _____6___i ________9i 123456789i

#         """

# @staticmethod
# def sudoku_xyz_wing_rows():
#     return f"""
#         xyz_wing_rows.sudoku
#         9
# ________9a _____6___a 1________a __3______b ____5____b _______8_b _2_______c ___4_____c ______7__c
# __3______a ______7__a _2_______a 123456789b ___4_____b 1________b ____5____c 123456789c 123456789c
# ___4_____a _______8_a ____5____a 123456789b ______7__b _2_______b 123456789c 123456789c 123456789c
# 1________d __3______d ______7__d _2_______e _______8_e ____5____e 123456789f 123456789f ___4_____f
# _2_______d ________9d _______8_d ______7__e _____6___e ___4_____e 1________f ____5____f __3______f
# ____5____d ___4_____d _____6___d 1________e 123456789e 123456789e _______8_f ______7__f _2_______f
# 123456789g ____5____g ________9g ___4_____h 123456789h _____6___h 123456789i _2_______i 123456789i
# 123456789g 1________g ___4_____g ____5____h _2_______h 123456789h 123456789i 123456789i _____6___i
# _____6___g _2_______g __3______g _______8_h 123456789h ______7__h ___4_____i 123456789i ____5____i
#         """

# @staticmethod
# def sudoku_xyz_wing_cols():
#     return f"""
#         xyz_wing_cols.sudoku
#         9
# 1________a _______8_a _2_______a 123456789b 123456789b 123456789b ________9c 123456789c ______7__c
# ____5____a ________9a 123456789a ______7__b _______8_b 123456789b _2_______c 1________c __3______c
# ______7__a 123456789a 123456789a ________9b _2_______b 1________b 123456789c ____5____c 123456789c
# _______8_d _2_______d 1________d __3______e ___4_____e ______7__e 123456789f 123456789f 123456789f
# __3______d _____6___d ____5____d 1________e ________9e _______8_e ______7__f 123456789f 123456789f
# ________9d 123456789d 123456789d ____5____e _____6___e _2_______e __3______f _______8_f 1________f
# _2_______g 1________g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
# ___4_____g ____5____g _______8_g _2_______h ______7__h ________9h 1________i __3______i _____6___i
# _____6___g 123456789g ________9g _______8_h 1________h 123456789h ___4_____i 123456789i 123456789i
#         """

# @staticmethod
# def sudoku_w_wing_center_col():
#     return f"""   
#         w_wing_center_col.sudoku
#         9
# ________9a _______8_a 1________a 123456789b 123456789b ____5____b _2_______c __3______c ______7__c
# ____5____a ______7__a __3______a _______8_b 1________b _2_______b ___4_____c ________9c _____6___c
# _2_______a ___4_____a _____6___a 123456789b 123456789b ________9b 1________c _______8_c ____5____c
# _____6___d ____5____d ______7__d ________9e _2_______e _______8_e __3______f 1________f ___4_____f
# _______8_d __3______d ___4_____d 1________e 123456789e 123456789e ____5____f _2_______f ________9f
# 1________d _2_______d ________9d 123456789e ____5____e 123456789e ______7__f _____6___f _______8_f
# 123456789g _____6___g ____5____g _2_______h ________9h 123456789h _______8_i ___4_____i 1________i
# 123456789g 1________g _2_______g 123456789h _______8_h 123456789h ________9i ____5____i __3______i
# 123456789g ________9g _______8_g ____5____h 123456789h 1________h _____6___i ______7__i _2_______i

#         """

# @staticmethod
# def sudoku_w_wing_left_col():
#     return f"""   
#         w_wing_left_col.sudoku
#         9
# _2_______a 123456789a _____6___a __3______b 1________b 123456789b ____5____c ______7__c ___4_____c
# 123456789a 123456789a ______7__a 123456789b _2_______b ___4_____b _____6___c 1________c ________9c
# ___4_____a 123456789a 123456789a 123456789b _____6___b 123456789b _2_______c __3______c _______8_c
# 123456789d _2_______d 123456789d ________9e ____5____e 123456789e ___4_____f _____6___f 123456789f
# ______7__d _____6___d 123456789d _2_______e ___4_____e 1________e __3______f 123456789f ____5____f
# 123456789d 123456789d ___4_____d 123456789e __3______e _____6___e 123456789f _2_______f 123456789f
# 123456789g 123456789g _2_______g 1________h ______7__h 123456789h 123456789i ___4_____i _____6___i
# 1________g ___4_____g 123456789g _____6___h _______8_h 123456789h ______7__i 123456789i _2_______i
# _____6___g ______7__g 123456789g ___4_____h ________9h _2_______h 1________i 123456789i __3______i

#         """

# @staticmethod
# def sudoku_001_4x4():
#     return f"""
#     001_4x4.sudoku
#     4
#     1234a 1234a 1234c __3_c
#     1234a 1___a 1234c ___4c
#     ___4b _2__b __3_d 1___d
#     1___b __3_b ___4d _2__d
#     """

# @staticmethod
# def sudoku_bug_0():
#     return f"""
#     bug_0.sudoku
#     9
#     123456789a 123456789a 123456789a ________9b 123456789b _______8_b _2_______c 123456789c 123456789c
#     123456789a 123456789a 123456789a 123456789b 1________b 123456789b 123456789c ______7__c 123456789c
#     _____6___a 123456789a _2_______a 123456789b 123456789b 123456789b ___4_____c 123456789c 123456789c
#     123456789d _2_______d 123456789d 123456789e 123456789e ________9e _______8_f 123456789f 123456789f
#     123456789d 123456789d 1________d ___4_____e 123456789e ____5____e __3______f 123456789f 123456789f
#     123456789d 123456789d _____6___d _______8_e 123456789e 123456789e 123456789f 1________f 123456789f
#     123456789g 123456789g ________9g 123456789h 123456789h 123456789h 1________i 123456789i _______8_i
#     123456789g ___4_____g 123456789g 123456789h _______8_h 123456789h 123456789i 123456789i 123456789i
#     123456789g 123456789g __3______g ____5____h 123456789h ______7__h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_00():
#     return f"""
#     difficult_00.sudoku
#     9
#     ______7__a 123456789a 123456789a _____6___b 123456789b 123456789b 123456789c ________9c 123456789c
# 123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# ____5____a 123456789a _____6___a _______8_b 123456789b 1________b ___4_____c 123456789c 123456789c
# 123456789d 123456789d __3______d ________9e 123456789e 123456789e _______8_f ______7__f ___4_____f
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# ________9d _2_______d ___4_____d 123456789e 123456789e __3______e ____5____f 123456789f 123456789f
# 123456789g 123456789g _2_______g ___4_____h 123456789h ________9h __3______i 123456789i _____6___i
# 123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
# 123456789g _______8_g 123456789g 123456789h 123456789h ______7__h 123456789i 123456789i ________9i
#     """

# @staticmethod
# def sudoku_difficult_02():
#     return f"""
#     difficult_02.sudoku
#     9
#     123456789a 123456789a ________9a 123456789b 123456789b 123456789b _____6___c 123456789c 123456789c
# 123456789a ______7__a ___4_____a 123456789b 123456789b 1________b 123456789c 123456789c 123456789c
# 1________a 123456789a 123456789a ___4_____b 123456789b 123456789b 123456789c 123456789c 123456789c
# 123456789d 123456789d __3______d _______8_e ______7__e 123456789e ________9f 123456789f _2_______f
# ______7__d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f _______8_f
# ___4_____d 123456789d _2_______d 123456789e _____6___e __3______e ______7__f 123456789f 123456789f
# 123456789g 123456789g 123456789g 123456789h 123456789h ________9h 123456789i 123456789i ____5____i
# 123456789g 123456789g 123456789g ______7__h 123456789h 123456789h __3______i _______8_i 123456789i
# 123456789g 123456789g 1________g 123456789h 123456789h 123456789h _2_______i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_03():
#     return f"""
#     difficult_03.sudoku
#     9
#     123456789a 123456789a 123456789a 123456789b 123456789b ____5____b ________9c 123456789c __3______c
# 123456789a 1________a 123456789a ______7__b _2_______b 123456789b 123456789c 123456789c ____5____c
# _______8_a 123456789a 123456789a 123456789b ________9b __3______b 123456789c 1________c 123456789c
# 123456789d __3______d 123456789d ________9e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d 123456789d ___4_____d 123456789e 123456789e 123456789e __3______f 123456789f 123456789f
# 123456789d 123456789d 123456789d 123456789e 123456789e _______8_e 123456789f ________9f 123456789f
# 123456789g ________9g 123456789g _2_______h ___4_____h 123456789h 123456789i 123456789i ______7__i
# ____5____g 123456789g 123456789g 123456789h ______7__h ________9h 123456789i _____6___i 123456789i
# _2_______g 123456789g __3______g ____5____h 123456789h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_06():
#     return f"""
#     difficult_06.sudoku
#     9
#     1________a _______8_a ____5____a __3______b ___4_____b ______7__b ________9c _____6___c _2_______c
#     123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c __3______c
#     __3______a ________9a 123456789a 1________b 123456789b 123456789b 123456789c 123456789c _______8_c
#     123456789d _2_______d 123456789d 123456789e ______7__e 123456789e 123456789f 123456789f 1________f
#     123456789d 123456789d 123456789d ___4_____e 123456789e __3______e 123456789f _______8_f ____5____f
#     ____5____d __3______d 123456789d 123456789e 1________e 123456789e 123456789f ________9f ______7__f
#     ______7__g 123456789g 123456789g 123456789h 123456789h _____6___h 123456789i _2_______i ___4_____i
#     123456789g 123456789g 123456789g ______7__h 123456789h 123456789h 123456789i 123456789i ________9i
#     123456789g 123456789g __3______g _2_______h _______8_h 123456789h ____5____i ______7__i _____6___i
#     """

# @staticmethod
# def sudoku_difficult_07():
#     return f"""
#     difficult_07.sudoku
#     9
#     _______8_a ______7__a ___4_____a _2_______b __3______b ________9b _____6___c ____5____c 1________c
#     __3______a ____5____a _2_______a 1________b _____6___b ______7__b ________9c ___4_____c _______8_c
#     1________a ________9a _____6___a 123456789b 123456789b 123456789b _2_______c ______7__c __3______c
#     _____6___d 123456789d __3______d ___4_____e ______7__e _2_______e 123456789f ________9f ____5____f
#     ______7__d _2_______d ____5____d ________9e 1________e _______8_e ___4_____f __3______f _____6___f
#     ________9d ___4_____d 123456789d __3______e ____5____e _____6___e ______7__f 123456789f _2_______f
#     ____5____g _____6___g 123456789g ______7__h 123456789h 123456789h __3______i _2_______i ________9i
#     ___4_____g 123456789g ________9g 123456789h _2_______h __3______h ____5____i 123456789i ______7__i
#     _2_______g __3______g ______7__g 123456789h ________9h 123456789h 123456789i 123456789i ___4_____i
#     requires a remote pair
#     """

# @staticmethod
# def sudoku_difficult_09():
#     return f"""
#     difficult_09.sudoku
#     9
#     123456789a 1________a 123456789a ______7__b _______8_b 123456789b _____6___c 123456789c 123456789c
#     _____6___a ____5____a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c _______8_c
#     123456789a _______8_a ______7__a 123456789b ________9b _____6___b 123456789c 123456789c ___4_____c
#     ___4_____d __3______d 1________d 123456789e 123456789e 123456789e ____5____f _______8_f 123456789f
#     ______7__d _2_______d _______8_d 123456789e ___4_____e 123456789e 123456789f 123456789f __3______f
#     ________9d _____6___d ____5____d _______8_e 123456789e __3______e ___4_____f _2_______f 123456789f
#     123456789g ______7__g _2_______g ___4_____h _____6___h _______8_h __3______i ________9i 123456789i
#     _______8_g ___4_____g __3______g 123456789h ____5____h 123456789h 123456789i 123456789i 123456789i
#     123456789g ________9g _____6___g 123456789h __3______h ______7__h _______8_i ___4_____i 123456789i
#     unique rectangle type 1
#     """

# @staticmethod
# def sudoku_difficult_10():
#     return f"""
#     difficult_10.sudoku
#     9
#     123456789a _2_______a 123456789a 1________b 123456789b ___4_____b 123456789c ______7__c 123456789c
#     123456789a 123456789a 123456789a 123456789b 123456789b ______7__b 123456789c 123456789c _2_______c
#     1________a 123456789a 123456789a _2_______b 123456789b 123456789b ___4_____c 123456789c _____6___c
#     _______8_d 1________d _2_______d ________9e 123456789e 123456789e ______7__f 123456789f ___4_____f
#     ________9d ____5____d 123456789d 123456789e 123456789e 123456789e 123456789f _2_______f 123456789f
#     __3______d 123456789d _____6___d 123456789e 123456789e _2_______e ________9f 123456789f 123456789f
#     _2_______g _____6___g __3______g 123456789h 123456789h 1________h ____5____i ___4_____i ________9i
#     ______7__g _______8_g ____5____g ___4_____h 123456789h 123456789h 123456789i 123456789i 123456789i
#     ___4_____g ________9g 1________g ____5____h 123456789h _____6___h 123456789i 123456789i ______7__i
#     """

# @staticmethod
# def sudoku_difficult_11():
#     return f"""
#     difficult_11.sudoku
#     9
#     123456789a 123456789a _____6___a ________9b _2_______b 123456789b ___4_____c _______8_c ____5____c
#     123456789a _______8_a 123456789a ___4_____b 123456789b ______7__b ________9c _2_______c _____6___c
#     123456789a ___4_____a 123456789a ____5____b _______8_b _____6___b ______7__c __3______c 1________c
#     123456789d _____6___d 123456789d 1________e ______7__e _2_______e 123456789f ___4_____f 123456789f
#     _______8_d _2_______d ______7__d __3______e ___4_____e ____5____e _____6___f 1________f ________9f
#     1________d __3______d ___4_____d _______8_e _____6___e ________9e _2_______f ____5____f ______7__f
#     123456789g ________9g __3______g 123456789h 123456789h _______8_h 123456789i _____6___i ___4_____i
#     ___4_____g ____5____g 123456789g _____6___h ________9h 123456789h 123456789i ______7__i 123456789i
#     _____6___g 123456789g _______8_g 123456789h 123456789h ___4_____h 123456789i ________9i 123456789i
#     Unique Rectangle Type 3
#     """

# @staticmethod
# def sudoku_difficult_12():
#     return f"""
#     difficult_12.sudoku
#     9
#     ______7__a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
#     123456789a 1________a 123456789a ___4_____b 123456789b _____6___b 123456789c 123456789c 123456789c
#     ____5____a _2_______a 123456789a 123456789b 123456789b __3______b 123456789c _____6___c 123456789c
#     __3______d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 1________f _____6___f
#     123456789d 123456789d ____5____d ________9e 123456789e 1________e __3______f 123456789f 123456789f
#     _______8_d _____6___d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f _2_______f
#     123456789g ____5____g 123456789g _______8_h 123456789h 123456789h 123456789i _2_______i 1________i
#     123456789g 123456789g 123456789g 1________h 123456789h _2_______h 123456789i _______8_i 123456789i
#     123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i ____5____i
#     """

# @staticmethod
# def sudoku_difficult_13():
#     return f"""
#     difficult_13.sudoku
#     9
#     ___4_____a ______7__a _2_______a 1________b ____5____b __3______b 123456789c 123456789c ________9c
#     123456789a 123456789a 123456789a ______7__b _______8_b _____6___b __3______c _2_______c ___4_____c
#     _______8_a _____6___a __3______a ___4_____b ________9b _2_______b ______7__c 1________c ____5____c
#     123456789d _2_______d 123456789d 123456789e 123456789e 123456789e 123456789f ___4_____f _______8_f
#     123456789d 123456789d _____6___d ________9e ___4_____e _______8_e _2_______f 123456789f 123456789f
#     123456789d _______8_d ___4_____d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
#     123456789g ___4_____g _______8_g 123456789h 123456789h 1________h ____5____i ________9i 123456789i
#     123456789g ________9g 1________g ____5____h ______7__h ___4_____h 123456789i 123456789i _2_______i
#     _2_______g 123456789g 123456789g _______8_h _____6___h ________9h ___4_____i 123456789i 1________i
#     """

# @staticmethod
# def sudoku_difficult_14():
#     return f"""
#     difficult_14.sudoku
#     9
#     123456789a 123456789a 123456789a ______7__b ___4_____b 1________b __3______c _____6___c _______8_c
#     ______7__a _______8_a 1________a _2_______b _____6___b __3______b ___4_____c ____5____c ________9c
#     __3______a ___4_____a _____6___a ________9b _______8_b ____5____b ______7__c _2_______c 1________c
#     123456789d ____5____d 123456789d 123456789e 1________e _____6___e 123456789f 123456789f 123456789f
#     123456789d 123456789d 123456789d 123456789e __3______e _2_______e 123456789f 1________f 123456789f
#     1________d 123456789d 123456789d ____5____e ________9e ______7__e 123456789f ___4_____f 123456789f
#     _____6___g ______7__g ___4_____g __3______h ____5____h _______8_h 1________i ________9i _2_______i
#     123456789g __3______g 123456789g 1________h _2_______h ________9h _____6___i ______7__i ___4_____i
#     _2_______g 1________g ________9g _____6___h ______7__h ___4_____h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_16():
#     return f"""
#     difficult_16.sudoku
#     9
#     123456789a ________9a ___4_____a _____6___b _2_______b 123456789b 123456789c _______8_c 1________c
#     1________a __3______a _2_______a 123456789b ____5____b 123456789b _____6___c ________9c ______7__c
#     _______8_a 123456789a _____6___a 123456789b 1________b 123456789b ___4_____c _2_______c 123456789c
#     ________9d _____6___d __3______d ____5____e _______8_e 1________e _2_______f ______7__f ___4_____f
#     _2_______d _______8_d ____5____d 123456789e ___4_____e 123456789e 1________f __3______f _____6___f
#     ___4_____d 1________d ______7__d _2_______e __3______e _____6___e ________9f ____5____f _______8_f
#     123456789g ___4_____g 1________g 123456789h ________9h 123456789h 123456789i _____6___i _2_______i
#     __3______g 123456789g _______8_g 1________h _____6___h _2_______h 123456789i ___4_____i ________9i
#     _____6___g _2_______g ________9g 123456789h ______7__h 123456789h _______8_i 1________i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_17():
#     return f"""
#     difficult_17.sudoku
#     9
#     _______8_a 123456789a 1________a 123456789b 123456789b ________9b ______7__c __3______c 123456789c
#     _____6___a ____5____a __3______a _______8_b ______7__b 1________b ________9c _2_______c ___4_____c
#     ______7__a ________9a 123456789a 123456789b __3______b 123456789b 1________c _______8_c 123456789c
#     123456789d ______7__d _______8_d 123456789e 123456789e 123456789e _2_______f ________9f 1________f
#     123456789d _____6___d ____5____d 1________e ________9e 123456789e _______8_f ___4_____f 123456789f
#     ________9d 1________d 123456789d 123456789e _______8_e 123456789e _____6___f ____5____f 123456789f
#     1________g _______8_g ______7__g ________9h ____5____h __3______h ___4_____i _____6___i _2_______i
#     ____5____g 123456789g _____6___g 123456789h 1________h _______8_h __3______i ______7__i ________9i
#     123456789g __3______g ________9g ______7__h 123456789h 123456789h ____5____i 1________i _______8_i
#     uniqe rec3
#     remote pair
#     """

# @staticmethod
# def sudoku_difficult_18():
#     return f"""
#     difficult_18.sudoku
#     9
#     __3______a 123456789a ___4_____a ________9b ____5____b 123456789b 123456789c 123456789c 123456789c
# 123456789a ________9a 123456789a 123456789b 123456789b 123456789b 123456789c _____6___c ____5____c
# 123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# ________9d __3______d 123456789d _2_______e 123456789e 123456789e 123456789f 123456789f ___4_____f
# ___4_____d 123456789d _______8_d __3______e 123456789e _____6___e 1________f 123456789f ________9f
# _____6___d 123456789d 123456789d 123456789e 123456789e ________9e 123456789f _2_______f ______7__f
# 123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
# 1________g ______7__g 123456789g 123456789h 123456789h 123456789h 123456789i ___4_____i 123456789i
# 123456789g 123456789g 123456789g 123456789h __3______h ______7__h _2_______i 123456789i _____6___i

#     """

# @staticmethod
# def sudoku_difficult_19():
#     return f"""
#     difficult_19.sudoku
#     9
#     123456789a 123456789a 123456789a 123456789b 123456789b 123456789b _______8_c ____5____c _2_______c
# _____6___a 123456789a 123456789a ___4_____b 123456789b 123456789b __3______c 123456789c 123456789c
# ____5____a 123456789a 123456789a 123456789b ________9b 123456789b 123456789c 123456789c 123456789c
# 123456789d 123456789d ________9d 123456789e 123456789e _____6___e ___4_____f 123456789f 123456789f
# 123456789d ____5____d 123456789d 123456789e __3______e 123456789e 123456789f 1________f 123456789f
# 123456789d 123456789d ______7__d 1________e 123456789e 123456789e _____6___f 123456789f 123456789f
# 123456789g 123456789g 123456789g 123456789h ______7__h 123456789h 123456789i 123456789i _______8_i
# 123456789g 123456789g ____5____g 123456789h 123456789h _______8_h 123456789i 123456789i __3______i
# 1________g ___4_____g _______8_g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_22():
#     return f"""
#     difficult_22.sudoku
#     9
#     123456789a 123456789a __3______a _2_______b 123456789b _______8_b 123456789c 123456789c ___4_____c
# _____6___a ___4_____a 123456789a 123456789b 123456789b ______7__b 123456789c _2_______c 123456789c
# 123456789a 123456789a 123456789a 123456789b 123456789b ___4_____b _______8_c 123456789c ________9c
# 123456789d _2_______d 123456789d 123456789e 123456789e 123456789e 123456789f ___4_____f 123456789f
# ________9d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f __3______f
# 123456789d __3______d 123456789d 123456789e 123456789e 123456789e 123456789f _______8_f 123456789f
# __3______g 123456789g ____5____g _______8_h 123456789h 123456789h 123456789i 123456789i 123456789i
# 123456789g _____6___g 123456789g ______7__h 123456789h 123456789h 123456789i ____5____i _2_______i
# _2_______g 123456789g 123456789g _____6___h 123456789h ____5____h 1________i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_23():
#     return f"""
#     difficult_23.sudoku
#     9
#     ____5____a ______7__a 123456789a 123456789b 123456789b _2_______b _______8_c 123456789c 123456789c
# 123456789a 123456789a 123456789a 123456789b __3______b 123456789b ______7__c 123456789c 123456789c
# 123456789a 1________a 123456789a 123456789b 123456789b _____6___b 123456789c __3______c 123456789c
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e ________9f ____5____f 1________f
# ________9d 123456789d 123456789d ___4_____e 123456789e 1________e 123456789f 123456789f _____6___f
# 1________d _______8_d ____5____d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789g ________9g 123456789g _2_______h 123456789h 123456789h 123456789i ___4_____i 123456789i
# 123456789g 123456789g _______8_g 123456789h 1________h 123456789h 123456789i 123456789i 123456789i
# 123456789g 123456789g _2_______g ____5____h 123456789h 123456789h 123456789i ________9i __3______i
#     """

# @staticmethod
# def sudoku_difficult_24():
#     return f"""
#     difficult_24.sudoku
#     9
#     123456789a 123456789a 123456789a ____5____b 123456789b 1________b 123456789c ______7__c 123456789c
# 123456789a 123456789a _2_______a ________9b 123456789b 123456789b _______8_c 123456789c 123456789c
# ______7__a 123456789a _____6___a _2_______b 123456789b 123456789b ___4_____c 123456789c 123456789c
# ____5____d 123456789d __3______d 123456789e 123456789e 123456789e 123456789f 1________f 123456789f
# 123456789d 123456789d 123456789d __3______e 123456789e ____5____e 123456789f 123456789f 123456789f
# 123456789d ________9d 123456789d 123456789e 123456789e 123456789e __3______f 123456789f _2_______f
# 123456789g 123456789g ____5____g 123456789h 123456789h ______7__h _____6___i 123456789i ________9i
# 123456789g 123456789g ___4_____g 123456789h 123456789h _2_______h ____5____i 123456789i 123456789i
# 123456789g _____6___g 123456789g ___4_____h 123456789h _______8_h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_25():
#     return f"""
#     difficult_25.sudoku
#     9
#     123456789a _______8_a 123456789a _____6___b 123456789b 123456789b 123456789c 123456789c 1________c
# ___4_____a ______7__a 123456789a ____5____b 123456789b 123456789b 123456789c _____6___c 123456789c
# 123456789a 123456789a __3______a 123456789b 123456789b ________9b 123456789c 123456789c 123456789c
# 123456789d _2_______d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f _____6___f
# 123456789d _____6___d 123456789d ________9e 123456789e ___4_____e 123456789f _______8_f 123456789f
# ____5____d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f __3______f 123456789f
# 123456789g 123456789g 123456789g ______7__h 123456789h 123456789h _2_______i 123456789i 123456789i
# 123456789g ____5____g 123456789g 123456789h 123456789h __3______h 123456789i ______7__i ________9i
# _______8_g 123456789g 123456789g 123456789h 123456789h _2_______h 123456789i ___4_____i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_26():
#     return f"""
#     difficult_26.sudoku
#     9
#     __3______a 123456789a 123456789a ______7__b 123456789b 123456789b ___4_____c 123456789c _____6___c
# 123456789a _____6___a 123456789a ________9b 123456789b _______8_b 123456789c 123456789c 123456789c
# _______8_a 123456789a 123456789a 1________b 123456789b 123456789b 123456789c 123456789c __3______c
# _2_______d 123456789d __3______d 123456789e 123456789e 123456789e 123456789f ____5____f 123456789f
# 123456789d 123456789d 123456789d __3______e 123456789e _2_______e 123456789f 123456789f 123456789f
# 123456789d ___4_____d 123456789d 123456789e 123456789e 123456789e 1________f 123456789f _2_______f
# 1________g 123456789g 123456789g 123456789h 123456789h ___4_____h 123456789i 123456789i ________9i
# 123456789g 123456789g 123456789g ____5____h 123456789h __3______h 123456789i ______7__i 123456789i
# _____6___g 123456789g ______7__g 123456789h 123456789h 1________h 123456789i 123456789i _______8_i
#     """

# @staticmethod
# def sudoku_difficult_27():
#     return f"""
#     difficult_27.sudoku
#     9
#     123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c _____6___c 123456789c
# 123456789a __3______a 123456789a 123456789b ____5____b 123456789b ______7__c 123456789c _2_______c
# 123456789a 123456789a 1________a ______7__b 123456789b _______8_b 123456789c 123456789c __3______c
# 123456789d ________9d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f ______7__f
# 123456789d 123456789d ____5____d __3______e 123456789e ________9e _______8_f 123456789f 123456789f
# _______8_d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f ___4_____f 123456789f
# ________9g 123456789g 123456789g ___4_____h 123456789h 1________h _____6___i 123456789i 123456789i
# ____5____g 123456789g _2_______g 123456789h __3______h 123456789h 123456789i 1________i 123456789i
# 123456789g _____6___g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_28():
#     return f"""
#     difficult_28.sudoku
#     9
#     123456789a ______7__a 123456789a ________9b 123456789b 123456789b 123456789c _____6___c 123456789c
# 123456789a 123456789a 123456789a 123456789b 123456789b ____5____b ___4_____c 123456789c 123456789c
# ________9a 123456789a ___4_____a 1________b ______7__b 123456789b 123456789c 123456789c 123456789c
# 1________d 123456789d _2_______d 123456789e 123456789e 123456789e ________9f ___4_____f 123456789f
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d ____5____d _____6___d 123456789e 123456789e 123456789e ______7__f 123456789f _______8_f
# 123456789g 123456789g 123456789g 123456789h _____6___h _2_______h 1________i 123456789i ____5____i
# 123456789g 123456789g ________9g ______7__h 123456789h 123456789h 123456789i 123456789i 123456789i
# 123456789g _____6___g 123456789g 123456789h 123456789h __3______h 123456789i _______8_i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_29():
#     return f"""
#     difficult_29.sudoku
#     9
#     ______7__a __3______a ___4_____a 123456789b _2_______b 123456789b 1________c ____5____c _____6___c
#     ____5____a _____6___a _2_______a 123456789b 1________b 123456789b _______8_c ________9c ______7__c
#     ________9a _______8_a 1________a _____6___b ____5____b ______7__b _2_______c __3______c ___4_____c
#     ___4_____d 1________d _____6___d 123456789e __3______e ____5____e 123456789f _2_______f 123456789f
#     __3______d ________9d ____5____d 123456789e 123456789e 123456789e ___4_____f 123456789f 1________f
#     _______8_d _2_______d ______7__d 123456789e ___4_____e 123456789e ____5____f _____6___f __3______f
#     _____6___g ___4_____g ________9g ____5____h ______7__h 123456789h __3______i 1________i 123456789i
#     1________g ____5____g __3______g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     _2_______g ______7__g _______8_g 123456789h ________9h 123456789h _____6___i ___4_____i ____5____i
#     """

# @staticmethod
# def sudoku_difficult_30():
#     return f"""
#     difficult_30.sudoku
#     9
#     ________9a _______8_a 1________a 123456789b 123456789b ______7__b ___4_____c _2_______c 123456789c
#     ___4_____a ______7__a _____6___a 123456789b _2_______b _______8_b 123456789c ____5____c 123456789c
#     __3______a _2_______a ____5____a 123456789b 123456789b 123456789b 123456789c _______8_c ______7__c
#     123456789d ___4_____d ________9d 123456789e 123456789e __3______e _2_______f ______7__f 123456789f
#     ______7__d 1________d _2_______d 123456789e 123456789e 123456789e 123456789f __3______f ________9f
#     123456789d _____6___d __3______d _2_______e ______7__e ________9e 123456789f ___4_____f 123456789f
#     _2_______g ________9g _______8_g ______7__h 123456789h 123456789h __3______i _____6___i ___4_____i
#     1________g ____5____g ___4_____g _____6___h __3______h _2_______h ______7__i ________9i _______8_i
#     _____6___g __3______g ______7__g _______8_h ________9h ___4_____h ____5____i 1________i _2_______i
#     """

# @staticmethod
# def sudoku_difficult_32():
#     return f"""
#     difficult_32.sudoku
#     9
#     ______7__a __3______a ___4_____a 123456789b _2_______b 123456789b 1________c ____5____c _____6___c
#     ____5____a _____6___a _2_______a 123456789b 1________b 123456789b _______8_c ________9c ______7__c
#     ________9a _______8_a 1________a _____6___b ____5____b ______7__b _2_______c __3______c ___4_____c
#     ___4_____d 1________d _____6___d 123456789e __3______e ____5____e 123456789f _2_______f 123456789f
#     __3______d ________9d ____5____d 123456789e 123456789e 123456789e ___4_____f 123456789f 1________f
#     _______8_d _2_______d ______7__d 123456789e ___4_____e 123456789e ____5____f _____6___f __3______f
#     _____6___g ___4_____g ________9g ____5____h ______7__h 123456789h __3______i 1________i 123456789i
#     1________g ____5____g __3______g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     _2_______g ______7__g _______8_g 123456789h ________9h 123456789h _____6___i ___4_____i ____5____i
#     """

# @staticmethod
# def sudoku_difficult_33():
#     return f"""
#     difficult_33.sudoku
#     9
#     ________9a _______8_a 1________a 123456789b 123456789b ______7__b ___4_____c _2_______c 123456789c
#     ___4_____a ______7__a _____6___a 123456789b _2_______b _______8_b 123456789c ____5____c 123456789c
#     __3______a _2_______a ____5____a 123456789b 123456789b 123456789b 123456789c _______8_c ______7__c
#     123456789d ___4_____d ________9d 123456789e 123456789e __3______e _2_______f ______7__f 123456789f
#     ______7__d 1________d _2_______d 123456789e 123456789e 123456789e 123456789f __3______f ________9f
#     123456789d _____6___d __3______d _2_______e ______7__e ________9e 123456789f ___4_____f 123456789f
#     _2_______g ________9g _______8_g ______7__h 123456789h 123456789h __3______i _____6___i ___4_____i
#     1________g ____5____g ___4_____g _____6___h __3______h _2_______h ______7__i ________9i _______8_i
#     _____6___g __3______g ______7__g _______8_h ________9h ___4_____h ____5____i 1________i _2_______i
#     """

# @staticmethod
# def sudoku_difficult_34():
#     return f"""
#     difficult_34.sudoku
#     9
#     123456789a 123456789a 123456789a _____6___b 123456789b ______7__b 123456789c ____5____c ___4_____c
# 123456789a 123456789a 123456789a 123456789b _______8_b 123456789b ________9c 123456789c 123456789c
# ____5____a 123456789a 123456789a ___4_____b 123456789b 123456789b _____6___c ______7__c 123456789c
# ________9d __3______d 123456789d 1________e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d 123456789e 123456789e ________9e 123456789f _2_______f _____6___f
# 123456789g ____5____g ______7__g 123456789h 123456789h 1________h 123456789i 123456789i _______8_i
# 123456789g 123456789g __3______g 123456789h ___4_____h 123456789h 123456789i 123456789i 123456789i
# _2_______g _______8_g 123456789g ________9h 123456789h __3______h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_35():
#     return f"""
#     difficult_35.sudoku
#     9
#     123456789a 123456789a _2_______a 123456789b 123456789b ________9b 123456789c 123456789c 123456789c
# 123456789a 123456789a ____5____a __3______b ___4_____b 123456789b 123456789c 1________c 123456789c
# 123456789a 123456789a 123456789a ______7__b 123456789b 123456789b 123456789c 123456789c _______8_c
# 123456789d ___4_____d ______7__d 123456789e 123456789e 123456789e 123456789f 123456789f __3______f
# __3______d 123456789d ________9d 1________e 123456789e ___4_____e _____6___f 123456789f ____5____f
# _2_______d 123456789d 123456789d 123456789e 123456789e 123456789e ________9f ___4_____f 123456789f
# ______7__g 123456789g 123456789g 123456789h 123456789h _____6___h 123456789i 123456789i 123456789i
# 123456789g ____5____g 123456789g 123456789h 1________h ______7__h __3______i 123456789i 123456789i
# 123456789g 123456789g 123456789g _2_______h 123456789h 123456789h ___4_____i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_36():
#     return f"""
#     difficult_36.sudoku
#     9
#     123456789a 123456789a 123456789a ______7__b 123456789b 123456789b 123456789c 123456789c ________9c
# 123456789a 1________a 123456789a 123456789b __3______b 123456789b 123456789c _____6___c 123456789c
# __3______a 123456789a 123456789a 123456789b ________9b 123456789b ___4_____c 123456789c 123456789c
# 123456789d 123456789d __3______d _____6___e 123456789e 123456789e _2_______f ___4_____f 123456789f
# 123456789d _______8_d 123456789d 123456789e 123456789e 123456789e 123456789f 1________f 123456789f
# 123456789d ____5____d ___4_____d 123456789e 123456789e __3______e _______8_f 123456789f 123456789f
# 123456789g 123456789g 1________g 123456789h _2_______h 123456789h 123456789i 123456789i ____5____i
# 123456789g __3______g 123456789g 123456789h _______8_h 123456789h 123456789i ______7__i 123456789i
# _____6___g 123456789g 123456789g 123456789h 123456789h ___4_____h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_37():
#     return f"""
#     difficult_37.sudoku
#     9
#     123456789a 123456789a ____5____a 123456789b 123456789b _______8_b 123456789c ______7__c __3______c
# 123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# 123456789a ______7__a _2_______a ___4_____b 123456789b 123456789b 1________c 123456789c 123456789c
# 123456789d _2_______d ___4_____d 123456789e ______7__e 123456789e 123456789f 123456789f _____6___f
# 123456789d _______8_d 123456789d _2_______e 123456789e ____5____e 123456789f __3______f 123456789f
# ____5____d 123456789d 123456789d 123456789e ___4_____e 123456789e ______7__f 1________f 123456789f
# 123456789g 123456789g _______8_g 123456789h 123456789h 1________h ________9i _____6___i 123456789i
# 123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
# ___4_____g 1________g 123456789g ________9h 123456789h 123456789h _______8_i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_difficult_38():
#     return f"""
#     difficult_38.sudoku
#     9
#     123456789a ___4_____a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# _2_______a 123456789a ________9a _______8_b 123456789b 123456789b ______7__c 123456789c 123456789c
# 123456789a 123456789a 123456789a ______7__b 123456789b _2_______b 123456789c 1________c 123456789c
# 123456789d _2_______d ___4_____d ____5____e 123456789e 123456789e 123456789f __3______f 123456789f
# 1________d _______8_d 123456789d _2_______e 123456789e ________9e 123456789f _____6___f ______7__f
# 123456789d __3______d 123456789d 123456789e 123456789e 1________e ____5____f _______8_f 123456789f
# 123456789g ____5____g 123456789g __3______h 123456789h ______7__h 123456789i 123456789i 123456789i
# 123456789g 123456789g _2_______g 123456789h 123456789h ___4_____h _______8_i 123456789i __3______i
# 123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i ____5____i 123456789i

#     """

# @staticmethod
# def sudoku_difficult_39():
#     return f"""
#     difficult_39.sudoku
#     9
#     123456789a __3______a 123456789a 123456789b ________9b 123456789b _______8_c 123456789c ______7__c
# _______8_a 123456789a 123456789a 1________b 123456789b 123456789b _____6___c 123456789c __3______c
# _2_______a 123456789a 123456789a 123456789b 123456789b _______8_b 123456789c 123456789c 123456789c
# 123456789d 123456789d __3______d 123456789e 123456789e 123456789e ____5____f 123456789f 123456789f
# _____6___d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 1________f
# 123456789d 123456789d _2_______d 123456789e 123456789e 123456789e ______7__f 123456789f 123456789f
# 123456789g 123456789g 123456789g _______8_h 123456789h 123456789h 123456789i 123456789i ___4_____i
# ______7__g 123456789g 1________g 123456789h 123456789h __3______h 123456789i 123456789i _______8_i
# ________9g 123456789g ____5____g 123456789h ______7__h 123456789h 123456789i 1________i 123456789i
#     """

# @staticmethod
# def sudoku_easiest_0():
#     return f"""
#     easiest_0.sudoku
#     9
#     123456789a __3______a 1________a _______8_b 123456789b _2_______b ____5____c ________9c ___4_____c
#     _____6___a 123456789a _______8_a ________9b 123456789b ___4_____b 123456789c _2_______c ______7__c
#     _2_______a ________9a ___4_____a ______7__b 1________b ____5____b 123456789c _____6___c __3______c

#     _______8_d ___4_____d _____6___d 123456789e 123456789e ________9e 123456789f ____5____f 1________f
#     __3______d 123456789d ________9d _2_______e ____5____e 1________e ___4_____f 123456789f _____6___f
#     1________d _2_______d 123456789d ___4_____e 123456789e 123456789e __3______f ______7__f ________9f

#     ________9g _______8_g 123456789g 1________h _2_______h __3______h _____6___i ___4_____i ____5____i
#     ____5____g 1________g 123456789g _____6___h 123456789h ______7__h ________9i 123456789i _______8_i
#     ___4_____g _____6___g __3______g ____5____h 123456789h _______8_h ______7__i 1________i 123456789i
#     """

# @staticmethod
# def sudoku_easy_as_pie_0():
#     return f"""
#     easy_as_pie_0.sudoku
#     9
#     123456789a ___4_____a _____6___a _______8_b 123456789b 1________b _2_______c 123456789c ______7__c
#     123456789a ________9a 1________a ___4_____b 123456789b ______7__b _______8_c 123456789c ____5____c
#     123456789a 123456789a __3______a ____5____b _2_______b ________9b ___4_____c 1________c _____6___c
#     ___4_____d 123456789d 123456789d _2_______e 123456789e 123456789e 123456789f ______7__f _______8_f
#     123456789d _____6___d 123456789d __3______e 1________e _______8_e 123456789f ___4_____f 123456789f
#     ________9d __3______d 123456789d 123456789e 123456789e ____5____e 123456789f 123456789f _2_______f
#     _____6___g _______8_g ___4_____g 1________h ______7__h _2_______h ________9i 123456789i 123456789i
#     1________g 123456789g ______7__g ________9h 123456789h __3______h _____6___i _______8_i 123456789i
#     __3______g 123456789g ________9g _____6___h 123456789h ___4_____h ______7__i _2_______i 123456789i
#     """

# @staticmethod
# def sudoku_first_lesson():
#     return f"""
#     first_lesson.sudoku
#     9
#     ______7__a ____5____a 1________a _2_______b _______8_b ________9b __3______c _____6___c ____4____c
#     _____6___a _2_______a __3______a 1________b ____4____b ______7__b ____5____c ________9c _______8_c
#     ________9a ____4____a _______8_a __3______b ____5____b _____6___b 1________c _2_______c ______7__c
#     __3______d _______8_d ______7__d ____4____e ________9e ____5____e _____6___f 1________f _2_______f
#     _2_______d 1________d ____4____d _____6___e __3______e _______8_e ______7__f ____5____f ________9f
#     ____5____d ________9d _____6___d ______7__e _2_______e 1________e ____4____f _______8_f __3______f
#     _______8_g ______7__g ________9g ____5____h 1________h __3______h _2_______i ____4____i _____6___i
#     1________g __3______g _2_______g 123456789h _____6___h ____4____h _______8_i ______7__i ____5____i
#     ____4____g _____6___g ____5____g _______8_h ______7__h _2_______h ________9i __3______i 1________i
#     """

# @staticmethod
# def sudoku_hidden_pair_0():
#     return f"""
#     hidden_pair_0.sudoku
#     9
#     _____6___a ____5____a 1________a _______8_b ________9b ______7__b ___4_____c __3______c _2_______c
#     ________9a 123456789a _2_______a 123456789b 1________b __3______b ______7__c 123456789c 123456789c
#     __3______a ______7__a 123456789a 123456789b _2_______b _____6___b 1________c 123456789c ________9c
#     ______7__d 123456789d ____5____d __3______e ___4_____e _2_______e ________9f 123456789f 1________f
#     1________d __3______d 123456789d ______7__e _____6___e ________9e 123456789f 123456789f 123456789f
#     _2_______d 123456789d ________9d 1________e _______8_e ____5____e __3______f ______7__f 123456789f
#     ____5____g ________9g __3______g _____6___h ______7__h 1________h 123456789i 123456789i 123456789i
#     ___4_____g _2_______g ______7__g ________9h ____5____h _______8_h _____6___i 1________i __3______i
#     _______8_g 1________g _____6___g _2_______h __3______h ___4_____h ____5____i ________9i ______7__i
#     """

# @staticmethod
# def sudoku_hidden_single_0():
#     return f"""
#     hidden_single_0.sudoku
#     9
#     ______7__a ___4_____a 1________a 123456789b _2_______b 123456789b ____5____c __3______c _______8_c
#     __3______a _____6___a _______8_a 123456789b 123456789b 1________b ___4_____c ________9c _2_______c
#     ____5____a ________9a _2_______a ___4_____b __3______b _______8_b 1________c _____6___c ______7__c
#     _______8_d ______7__d ____5____d 123456789e 123456789e __3______e _____6___f _2_______f ___4_____f
#     _2_______d 1________d ________9d 123456789e 123456789e ___4_____e _______8_f ____5____f __3______f
#     _____6___d __3______d ___4_____d _2_______e _______8_e ____5____e ________9f ______7__f 1________f
#     ________9g _______8_g _____6___g __3______h ___4_____h _2_______h ______7__i 1________i ____5____i
#     1________g ____5____g __3______g _______8_h 123456789h 123456789h _2_______i ___4_____i ________9i
#     ___4_____g _2_______g ______7__g 123456789h 123456789h 123456789h __3______i _______8_i _____6___i
#     """

# @staticmethod
# def sudoku_hidden_single_1():
#     return f"""
#     hidden_single_1.sudoku
#     9
#     123456789a ___4_____a 123456789a 123456789b 123456789b __3______b 123456789c _2_______c _____6___c
#     1________a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
#     123456789a _2_______a 123456789a 123456789b _____6___b ______7__b ____5____c 123456789c ___4_____c
#     123456789d 123456789d _____6___d 123456789e 123456789e 1________e 123456789f 123456789f ____5____f
#     ___4_____d 1________d 123456789d 123456789e 123456789e 123456789e 123456789f ______7__f ________9f
#     ____5____d 123456789d 123456789d ______7__e 123456789e 123456789e _______8_f 123456789f 123456789f
#     _2_______g 123456789g 1________g __3______h ______7__h 123456789h 123456789i ____5____i 123456789i
#     123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i ______7__i
#     _______8_g ______7__g 123456789g ___4_____h 123456789h 123456789h 123456789i 1________i 123456789i
#     """

# @staticmethod
# def sudoku_hidden_single_2():
#     return f"""
#     hidden_single_2.sudoku
#     9
#     _2_______a 123456789a ______7__a 123456789b 123456789b 123456789b _______8_c ________9c 123456789c
#     123456789a ________9a 123456789a ______7__b ___4_____b ____5____b __3______c _____6___c _2_______c
#     123456789a 123456789a __3______a ________9b _2_______b _______8_b ______7__c 123456789c 123456789c
#     ________9d 123456789d 123456789d __3______e 123456789e ___4_____e ____5____f 123456789f 123456789f
#     ___4_____d 123456789d 123456789d ____5____e 123456789e _2_______e ________9f 123456789f __3______f
#     ______7__d __3______d ____5____d 123456789e 123456789e ________9e ___4_____f _2_______f 123456789f
#     123456789g 123456789g 123456789g ___4_____h 123456789h 123456789h _____6___i 123456789i ________9i
#     __3______g ______7__g ________9g _2_______h 123456789h _____6___h 1________i ___4_____i 123456789i
#     _____6___g 1________g ___4_____g 123456789h ________9h 123456789h _2_______i 123456789i ______7__i
#     """

# @staticmethod
# def sudoku_intricate_0():
#     return f"""
#     intricate_0.sudoku
#     9
#     123456789a 123456789a 1________a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
#     123456789a 123456789a _______8_a ____5____b 123456789b __3______b 123456789c 123456789c ________9c
#     123456789a 123456789a ________9a 123456789b 123456789b 123456789b _2_______c ____5____c 123456789c
#     123456789d 123456789d 123456789d _____6___e 123456789e 123456789e 123456789f 123456789f 1________f
#     1________d 123456789d _____6___d ________9e 123456789e _______8_e ____5____f 123456789f __3______f
#     __3______d 123456789d 123456789d 123456789e 123456789e ___4_____e 123456789f 123456789f 123456789f
#     123456789g ___4_____g __3______g 123456789h 123456789h 123456789h 1________i 123456789i 123456789i
#     _2_______g 123456789g 123456789g 1________h 123456789h ______7__h __3______i 123456789i 123456789i
#     123456789g 123456789g 123456789g 123456789h 123456789h 123456789h ________9i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_intricate_1():
#     return f"""
#     intricate_1.sudoku
#     9
#     1________a ______7__a 123456789a 123456789b 123456789b ________9b __3______c _______8_c ____5____c
#     ____5____a _____6___a 123456789a 123456789b __3______b 123456789b 123456789c 123456789c 123456789c
#     _______8_a __3______a ________9a 123456789b ______7__b 123456789b _____6___c 123456789c 123456789c
#     123456789d _2_______d 123456789d 123456789e ____5____e __3______e ___4_____f 123456789f _______8_f
#     123456789d ____5____d 123456789d _2_______e _______8_e ___4_____e 123456789f __3______f 123456789f
#     __3______d ___4_____d _______8_d 123456789e ________9e 123456789e ____5____f _2_______f 123456789f
#     ___4_____g _______8_g ____5____g ________9h 1________h ______7__h _2_______i _____6___i __3______i
#     _2_______g 1________g __3______g 123456789h 123456789h 123456789h ______7__i 123456789i ________9i
#     _____6___g ________9g ______7__g __3______h 123456789h 123456789h _______8_i 123456789i 1________i
#     """

# @staticmethod
# def sudoku_intricate_2():
#     return f"""
#     intricate_2.sudoku
#     9
#     123456789a ________9a 123456789a _____6___b 123456789b 123456789b 123456789c ______7__c __3______c
#     123456789a 123456789a ______7__a __3______b 123456789b 123456789b ________9c 123456789c _______8_c
#     123456789a 123456789a 123456789a _______8_b ______7__b ________9b _2_______c 123456789c _____6___c
#     ______7__d ____5____d 123456789d ___4_____e _2_______e _______8_e 123456789f _____6___f 123456789f
#     _2_______d 123456789d 123456789d ______7__e 123456789e 123456789e 123456789f _______8_f ___4_____f
#     ___4_____d _______8_d 123456789d 1________e 123456789e 123456789e 123456789f _2_______f 123456789f
#     123456789g 123456789g ____5____g 123456789h 123456789h __3______h 123456789i 123456789i 123456789i
#     123456789g 123456789g ___4_____g 123456789h 123456789h ______7__h _______8_i 123456789i 123456789i
#     1________g ______7__g 123456789g 123456789h 123456789h ___4_____h 123456789i __3______i 123456789i
#     """

# @staticmethod
# def sudoku_intricate_3():
#     return f"""
#     intricate_3.sudoku
#     9
#     123456789a ___4_____a ________9a 123456789b ______7__b __3______b ____5____c 123456789c 123456789c
#     ____5____a ______7__a _______8_a 123456789b 1________b _____6___b 123456789c __3______c 123456789c
#     123456789a __3______a 1________a 123456789b 123456789b ____5____b 123456789c 123456789c ______7__c
#     ___4_____d 1________d _2_______d ____5____e __3______e _______8_e 123456789f ______7__f 123456789f
#     ________9d ____5____d __3______d ______7__e _____6___e _2_______e 123456789f 123456789f ___4_____f
#     ______7__d _______8_d _____6___d 1________e ________9e ___4_____e _2_______f ____5____f __3______f
#     _______8_g 123456789g ____5____g __3______h ___4_____h 123456789h ______7__i _____6___i 123456789i
#     __3______g 123456789g ______7__g _____6___h ____5____h 123456789h 123456789i 123456789i 123456789i
#     1________g _____6___g ___4_____g 123456789h 123456789h ______7__h __3______i 123456789i ____5____i
#     """

# @staticmethod
# def sudoku_intricate_4():
#     return f"""
#     intricate_4.sudoku
#     9
#     123456789a __3______a 1________a 123456789b ______7__b 123456789b ________9c 123456789c _2_______c
#     ______7__a ________9a ____5____a 123456789b 123456789b 123456789b 1________c 123456789c _______8_c
#     123456789a 123456789a _____6___a 123456789b 1________b ________9b 123456789c 123456789c ______7__c
#     ________9d ______7__d _2_______d 123456789e 123456789e _____6___e ___4_____f _______8_f 1________f
#     _____6___d ___4_____d __3______d ______7__e _______8_e 1________e 123456789f 123456789f ________9f
#     ____5____d 1________d _______8_d ___4_____e ________9e _2_______e _____6___f ______7__f __3______f
#     123456789g 123456789g ________9g 1________h 123456789h ______7__h 123456789i 123456789i 123456789i
#     __3______g 123456789g ___4_____g ________9h 123456789h _______8_h ______7__i 1________i 123456789i
#     1________g 123456789g ______7__g 123456789h _____6___h 123456789h _______8_i ________9i 123456789i
#     """

# @staticmethod
# def sudoku_intricate_5():
#     return f"""
#     intricate_5.sudoku
#     9
#     _____6___a 123456789a 123456789a ________9b 123456789b ______7__b 123456789c 123456789c 123456789c
#     123456789a 123456789a ______7__a 123456789b _2_______b 123456789b 123456789c 123456789c 123456789c
#     _2_______a ____5____a 123456789a __3______b 123456789b 1________b 123456789c 123456789c 123456789c
#     1________d 123456789d 123456789d 123456789e 123456789e 123456789e ________9f _______8_f 123456789f
#     123456789d _______8_d _____6___d 123456789e 123456789e 123456789e ____5____f _2_______f 123456789f
#     123456789d _2_______d ___4_____d 123456789e 123456789e 123456789e 123456789f 123456789f __3______f
#     123456789g 123456789g 123456789g ___4_____h 123456789h ____5____h 123456789i ______7__i _______8_i
#     123456789g 123456789g 123456789g 123456789h _______8_h 123456789h 1________i 123456789i 123456789i
#     123456789g 123456789g 123456789g _____6___h 123456789h __3______h 123456789i 123456789i ________9i
#     """

# @staticmethod
# def sudoku_intricate_6():
#     return f"""
#     intricate_6.sudoku
#     9
#     _____6___a 123456789a ____5____a _______8_b 123456789b __3______b 1________c 123456789c ___4_____c
#     _______8_a 123456789a 123456789a ___4_____b 123456789b _2_______b __3______c _____6___c 123456789c
#     123456789a __3______a ___4_____a 123456789b _____6___b 1________b _______8_c ________9c 123456789c
#     123456789d ___4_____d _______8_d 123456789e 123456789e ________9e _____6___f __3______f 123456789f
#     123456789d _____6___d _2_______d __3______e 123456789e ___4_____e ____5____f 123456789f 123456789f
#     123456789d 123456789d __3______d _____6___e 123456789e 123456789e ___4_____f 123456789f 123456789f
#     ___4_____g ____5____g ________9g _2_______h __3______h _____6___h ______7__i 1________i _______8_i
#     123456789g 123456789g _____6___g 1________h ___4_____h 123456789h ________9i ____5____i __3______i
#     __3______g 123456789g 123456789g ________9h 123456789h ____5____h _2_______i ___4_____i _____6___i
#     """

# @staticmethod
# def sudoku_intricate_7():
#     return f"""
#     intricate_7.sudoku
#     9
#     ________9a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
#     123456789a _______8_a 123456789a ______7__b __3______b 123456789b 123456789c _____6___c ________9c
#     123456789a 123456789a 123456789a 123456789b 123456789b _2_______b 123456789c ______7__c 1________c
#     123456789d 123456789d 123456789d _____6___e 123456789e 123456789e 123456789f __3______f ____5____f
#     123456789d 123456789d 123456789d ___4_____e 123456789e ____5____e 123456789f 123456789f 123456789f
#     _2_______d _____6___d 123456789d 123456789e 123456789e _______8_e 123456789f 123456789f 123456789f
#     ___4_____g ____5____g 123456789g _2_______h 123456789h 123456789h 123456789i 123456789i 123456789i
#     _____6___g __3______g 123456789g 123456789h ________9h ______7__h 123456789i _______8_i 123456789i
#     123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i _2_______i
#     """

# @staticmethod
# def sudoku_intricate_8():
#     return f"""
#     intricate_8.sudoku
#     9
#     123456789a ____5____a 123456789a 123456789b _______8_b 123456789b 123456789c 123456789c ______7__c
#     1________a __3______a ______7__a 123456789b 123456789b ________9b 123456789c 123456789c 123456789c
#     ________9a _______8_a 123456789a ______7__b 123456789b 123456789b 123456789c 123456789c 123456789c
#     123456789d ___4_____d 123456789d _2_______e 1________e _______8_e 123456789f ____5____f 123456789f
#     123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
#     123456789d ______7__d 123456789d ___4_____e ________9e ____5____e 123456789f _2_______f 123456789f
#     123456789g 123456789g 123456789g 123456789h 123456789h ______7__h 123456789i ________9i ____5____i
#     123456789g 123456789g 123456789g _____6___h 123456789h 123456789h _2_______i ___4_____i __3______i
#     ____5____g 123456789g 123456789g 123456789h __3______h 123456789h 123456789i ______7__i 123456789i
#     """

# @staticmethod
# def sudoku_locked_candidates_claiming_0():
#     return f"""
#     locked_candidates_claiming_0.sudoku
#     9
#     123456789a 123456789a 123456789a ________9b 123456789b 123456789b 123456789c 123456789c ___4_____c
# ___4_____a 123456789a _____6___a 123456789b 123456789b _______8_b ______7__c 123456789c __3______c
# 123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c _2_______c 123456789c
# 123456789d _______8_d ________9d 1________e 123456789e 123456789e 123456789f 123456789f 123456789f
# _____6___d 123456789d ______7__d 123456789e 123456789e 123456789e ________9f 123456789f ____5____f
# 123456789d 123456789d 123456789d 123456789e 123456789e ________9e _______8_f __3______f 123456789f
# 123456789g _____6___g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
# __3______g 123456789g _2_______g ____5____h 123456789h 123456789h 1________i 123456789i ______7__i
# 1________g 123456789g 123456789g 123456789h 123456789h __3______h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_locked_candidates_claiming_1():
#     return f"""
#     locked_candidates_claiming_1.sudoku
#     9
#     123456789a 123456789a 123456789a 123456789b 123456789b 123456789b __3______c 123456789c ___4_____c
# _______8_a ____5____a 123456789a _____6___b 123456789b 123456789b 123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a 1________b _2_______b 123456789b 123456789c _____6___c ________9c
# 123456789d 123456789d _______8_d 123456789e 123456789e 123456789e _2_______f ______7__f 123456789f
# ________9d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f _____6___f
# 123456789d _____6___d _2_______d 123456789e 123456789e 123456789e ___4_____f 123456789f 123456789f
# 1________g ________9g 123456789g 123456789h ______7__h __3______h 123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g 123456789h 123456789h _2_______h 123456789i 1________i __3______i
# __3______g 123456789g ____5____g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_locked_candidates_claiming_2():
#     return f"""
#     locked_candidates_claiming_2.sudoku
#     9
#     123456789a _______8_a 123456789a 123456789b 123456789b _2_______b 123456789c 123456789c 123456789c
# _2_______a 123456789a 123456789a 123456789b _____6___b 123456789b _______8_c __3______c 123456789c
# 123456789a 123456789a 123456789a ______7__b 123456789b __3______b 123456789c 123456789c 123456789c
# ___4_____d 123456789d 123456789d 123456789e 123456789e ______7__e _____6___f 1________f 123456789f
# 123456789d 123456789d _______8_d 123456789e 123456789e 123456789e ________9f 123456789f 123456789f
# 123456789d 1________d _____6___d ___4_____e 123456789e 123456789e 123456789f 123456789f _2_______f
# 123456789g 123456789g 123456789g _____6___h 123456789h ___4_____h 123456789i 123456789i 123456789i
# 123456789g ___4_____g ______7__g 123456789h ________9h 123456789h 123456789i 123456789i 1________i
# 123456789g 123456789g 123456789g ____5____h 123456789h 123456789h 123456789i _2_______i 123456789i
#     """

# @staticmethod
# def sudoku_locked_candidates_pointing_0():
#     return f"""
#     locked_candidates_pointing_0.sudoku
#     9
#     123456789a __3______a 123456789a 123456789b 123456789b 123456789b 123456789c _____6___c 123456789c
#     123456789a 123456789a 123456789a 123456789b 123456789b __3______b ________9c 123456789c 123456789c
#     123456789a ___4_____a _2_______a _____6___b 123456789b 123456789b 123456789c _______8_c 123456789c
#     123456789d 123456789d 123456789d 123456789e __3______e _2_______e _______8_f 123456789f 123456789f
#     123456789d ______7__d 123456789d ___4_____e 123456789e _____6___e 123456789f ____5____f 123456789f
#     123456789d 123456789d ____5____d 1________e ______7__e 123456789e 123456789f 123456789f 123456789f
#     123456789g ________9g 123456789g 123456789h 123456789h _______8_h _2_______i ___4_____i 123456789i
#     123456789g 123456789g _____6___g _2_______h 123456789h 123456789h 123456789i 123456789i 123456789i
#     123456789g _______8_g 123456789g 123456789h 123456789h 123456789h 123456789i ________9i 123456789i
#     """

# @staticmethod
# def sudoku_mild_0():
#     return f"""
#     mild_0.sudoku
#     9
#     123456789a ___4_____a __3______a _______8_b 123456789b 123456789b 123456789c 123456789c 123456789c
#     ____5____a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
#     _2_______a 1________a 123456789a 123456789b 123456789b _____6___b 123456789c ________9c ___4_____c
#     ___4_____d _2_______d 123456789d ________9e 123456789e 123456789e _____6___f __3______f 123456789f
#     __3______d 123456789d ____5____d 123456789e 123456789e 123456789e ___4_____f 123456789f 1________f
#     123456789d _______8_d 1________d 123456789e 123456789e ___4_____e 123456789f _2_______f ________9f
#     _______8_g ______7__g 123456789g ___4_____h 123456789h 123456789h 123456789i _____6___i ____5____i
#     123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i _2_______i
#     123456789g 123456789g 123456789g 123456789h 123456789h _2_______h __3______i ___4_____i 123456789i
#     """

# @staticmethod
# def sudoku_mild_1():
#     return f"""
#     mild_1.sudoku
#     9
#     ___4_____a __3______a 123456789a 123456789b _____6___b _2_______b ____5____c 123456789c _______8_c
#     123456789a 123456789a _2_______a ___4_____b ______7__b 123456789b 123456789c _____6___c 123456789c
#     123456789a 123456789a 123456789a 123456789b 123456789b 123456789b ___4_____c 123456789c 123456789c
#     123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f ___4_____f
#     _______8_d 123456789d 123456789d ______7__e 1________e ____5____e 123456789f 123456789f _2_______f
#     1________d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
#     123456789g 123456789g ________9g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     123456789g _____6___g 123456789g 123456789h _2_______h ________9h __3______i 123456789i 123456789i
#     _2_______g 123456789g ___4_____g 1________h _______8_h 123456789h 123456789i ________9i _____6___i
#     """

# @staticmethod
# def sudoku_mild_2():
#     return f"""
#     mild_2.sudoku
#     9
#     _______8_a _____6___a 123456789a 123456789b ____5____b 123456789b 123456789c 123456789c 123456789c
#     123456789a 123456789a 123456789a 123456789b 123456789b __3______b _______8_c 1________c _____6___c
#     123456789a 123456789a 123456789a 123456789b 1________b 123456789b 123456789c 123456789c 123456789c
#     123456789d ___4_____d 123456789d 123456789e 123456789e 123456789e 123456789f _____6___f _2_______f
#     123456789d 123456789d ______7__d _2_______e 123456789e ________9e __3______f 123456789f 123456789f
#     _2_______d _______8_d 123456789d 123456789e 123456789e 123456789e 123456789f ____5____f 123456789f
#     123456789g 123456789g 123456789g 123456789h _2_______h 123456789h 123456789i 123456789i 123456789i
#     ______7__g 1________g __3______g _____6___h 123456789h 123456789h 123456789i 123456789i 123456789i
#     123456789g 123456789g 123456789g 123456789h ________9h 123456789h 123456789i __3______i ___4_____i
#     """

# @staticmethod
# def sudoku_mild_3():
#     return f"""
#     mild_3.sudoku
#     9
#     ____5____a ________9a 123456789a ___4_____b _____6___b 123456789b 123456789c 123456789c 1________c
#     123456789a __3______a _____6___a _______8_b 123456789b ______7__b 123456789c 123456789c ____5____c
#     123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
#     123456789d 123456789d 123456789d 123456789e 123456789e 123456789e __3______f _2_______f 123456789f
#     123456789d 123456789d 123456789d ______7__e ___4_____e ________9e 123456789f 123456789f 123456789f
#     123456789d 1________d ______7__d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
#     123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     _2_______g 123456789g 123456789g _____6___h 123456789h _______8_h 1________i ______7__i 123456789i
#     __3______g 123456789g 123456789g 123456789h _2_______h 1________h 123456789i ____5____i _______8_i
#     """

# @staticmethod
# def sudoku_mild_4():
#     return f"""
#     mild_4.sudoku
#     9
#     ___4_____a 123456789a 123456789a 123456789b ____5____b ______7__b 2c _______8_c 123456789c
#     123456789a 1________a 123456789a 123456789b 2b 123456789b ___4_____c 123456789c 123456789c
#     123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c ________9c
#     ________9d _____6___d 123456789d 123456789e ______7__e 123456789e 123456789f ___4_____f 1________f
#     123456789d ______7__d 123456789d 123456789e 123456789e 123456789e 123456789f __3______f 123456789f
#     _______8_d __3______d 123456789d 123456789e 1________e 123456789e 123456789f ____5____f ______7__f
#     __3______g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     123456789g 123456789g _______8_g 123456789h _____6___h 123456789h 123456789i 2i 123456789i
#     123456789g ____5____g _____6___g __3______h _______8_h 123456789h 123456789i 123456789i ___4_____i
#     """

# @staticmethod
# def sudoku_moderate_0():
#     return f"""
#     moderate_0.sudoku
#     9
#     1________a 123456789a _2_______a 123456789b 123456789b 123456789b ___4_____c 123456789c 123456789c
#     123456789a __3______a ________9a 123456789b _______8_b 123456789b 123456789c ______7__c 123456789c
#     123456789a ______7__a _______8_a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
#     ______7__d 123456789d 123456789d _______8_e 123456789e _____6___e 123456789f 123456789f 1________f
#     123456789d ____5____d 123456789d 123456789e 123456789e 123456789e 123456789f _______8_f 123456789f
#     _______8_d 123456789d 123456789d ____5____e 123456789e _2_______e 123456789f 123456789f ________9f
#     123456789g 123456789g 123456789g 123456789h 123456789h 123456789h _______8_i _____6___i 123456789i
#     123456789g 1________g 123456789g 123456789h _____6___h 123456789h __3______i ____5____i 123456789i
#     123456789g 123456789g ______7__g 123456789h 123456789h 123456789h ________9i 123456789i ___4_____i
#     """

# @staticmethod
# def sudoku_naked_pair_0():
#     return f"""
#     naked_pair_0.sudoku
#     9
#     123456789a 1________a ________9a __3______b 123456789b _______8_b 123456789c 123456789c 123456789c
#     123456789a _2_______a _____6___a ________9b 123456789b ______7__b __3______c _______8_c 123456789c
#     _______8_a __3______a ______7__a 123456789b 123456789b ____5____b 123456789c 123456789c 123456789c
#     _____6___d ______7__d _2_______d ____5____e 123456789e ________9e _______8_f ___4_____f 123456789f
#     123456789d ____5____d _______8_d 123456789e 123456789e _____6___e 123456789f 123456789f 123456789f
#     123456789d ___4_____d 1________d _______8_e 123456789e _2_______e ____5____f 123456789f _____6___f
#     1________g _______8_g __3______g _____6___h ________9h ___4_____h ______7__i ____5____i _2_______i
#     ______7__g ________9g ___4_____g _2_______h ____5____h __3______h 1________i _____6___i _______8_i
#     _2_______g _____6___g ____5____g ______7__h _______8_h 1________h ___4_____i __3______i ________9i
#     """

# @staticmethod
# def sudoku_naked_pair_1():
#     return f"""
#     naked_pair_1.sudoku
#     9
#     _____6___a 1________a 123456789a _______8_b ____5____b __3______b 123456789c 123456789c ________9c
#     ________9a 123456789a _______8_a 123456789b ___4_____b 123456789b _____6___c __3______c ____5____c
#     ____5____a 123456789a 123456789a ________9b 123456789b _____6___b 123456789c 1________c _______8_c
#     __3______d _______8_d ________9d 123456789e 123456789e ___4_____e 1________f 123456789f _____6___f
#     _2_______d _____6___d 1________d 123456789e __3______e _______8_e 123456789f ________9f ___4_____f
#     ______7__d ___4_____d ____5____d _____6___e 123456789e 123456789e __3______f _______8_f _2_______f
#     _______8_g ____5____g 123456789g ___4_____h 123456789h _2_______h ________9i _____6___i 123456789i
#     ___4_____g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     1________g 123456789g 123456789g __3______h 123456789h ____5____h 123456789i 123456789i ______7__i
#     """

# @staticmethod
# def sudoku_naked_pair_2():
#     return f"""
#     naked_pair_2.sudoku
#     9
#     123456789a 123456789a 1________a _2_______b 123456789b ________9b 123456789c ______7__c 123456789c
#     _____6___a 123456789a 123456789a ___4_____b ____5____b ______7__b _______8_c __3______c 1________c
#     123456789a 123456789a ______7__a _______8_b 1________b 123456789b ________9c _2_______c 123456789c
#     _2_______d 123456789d ____5____d ______7__e 123456789e 123456789e 1________f 123456789f _______8_f
#     123456789d 123456789d 123456789d 123456789e _2_______e 123456789e 123456789f ____5____f __3______f
#     __3______d 123456789d ___4_____d 123456789e _______8_e ____5____e ______7__f 123456789f _2_______f
#     123456789g 123456789g __3______g ____5____h ______7__h _______8_h 123456789i 123456789i ________9i
#     ________9g ____5____g _______8_g _____6___h ___4_____h _2_______h __3______i 1________i ______7__i
#     123456789g 123456789g 123456789g __3______h ________9h 1________h 123456789i _______8_i 123456789i
#     """

# @staticmethod
# def sudoku_naked_triple_0():
#     return f"""
#     naked_triple_0.sudoku
#     9
#     123456789a ___4_____a 123456789a 123456789b 123456789b 123456789b __3______c 123456789c 123456789c
# _2_______a 123456789a 123456789a ______7__b 123456789b 123456789b 123456789c _____6___c 123456789c
# 123456789a 123456789a ________9a _______8_b 123456789b 123456789b 123456789c 123456789c 123456789c
# 123456789d 123456789d _______8_d 123456789e 123456789e 123456789e 123456789f ________9f _____6___f
# ________9d 123456789d 123456789d _2_______e 123456789e ___4_____e 123456789f 123456789f 1________f
# ______7__d _2_______d 123456789d 123456789e 123456789e 123456789e ____5____f 123456789f 123456789f
# 123456789g 123456789g 123456789g 123456789h 123456789h ____5____h _______8_i 123456789i 123456789i
# 123456789g 1________g 123456789g 123456789h 123456789h ______7__h 123456789i 123456789i _2_______i
# 123456789g 123456789g __3______g 123456789h 123456789h 123456789h 123456789i ______7__i 123456789i
#     """

# @staticmethod
# def sudoku_naked_triple_1():
#     return f"""
#     naked_triple_1.sudoku
#     9
#     123456789a 123456789a 123456789a ________9b 123456789b 123456789b 123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a 123456789b __3______b _____6___b 123456789c ___4_____c ________9c
# __3______a ____5____a 123456789a 123456789b 123456789b 1________b 123456789c 123456789c 123456789c
# 123456789d 123456789d 123456789d _2_______e 123456789e 123456789e _______8_f 123456789f _____6___f
# ____5____d _____6___d 123456789d 123456789e 123456789e 123456789e 123456789f ______7__f ___4_____f
# ________9d 123456789d __3______d 123456789e 123456789e ___4_____e 123456789f 123456789f 123456789f
# 123456789g 123456789g 123456789g ___4_____h 123456789h 123456789h 123456789i _______8_i 1________i
# _2_______g ________9g 123456789g _____6___h 1________h 123456789h 123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g 123456789h 123456789h ______7__h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_naked_triple_2():
#     return f"""
#     naked_triple_2.sudoku
#     9
#     123456789a 123456789a 123456789a 123456789b _2_______b 123456789b 123456789c 123456789c 123456789c
# 123456789a __3______a ____5____a _____6___b 123456789b 123456789b _2_______c 123456789c 123456789c
# ___4_____a 123456789a 123456789a ____5____b 123456789b 123456789b 123456789c 123456789c _______8_c
# 123456789d 123456789d _______8_d 123456789e ________9e ______7__e 123456789f 123456789f 123456789f
# 123456789d 123456789d _2_______d _______8_e 123456789e _____6___e 1________f 123456789f 123456789f
# 123456789d 123456789d 123456789d ___4_____e 1________e 123456789e ____5____f 123456789f 123456789f
# __3______g 123456789g 123456789g 123456789h 123456789h ____5____h 123456789i 123456789i ______7__i
# 123456789g 123456789g ___4_____g 123456789h 123456789h _______8_h ________9i _____6___i 123456789i
# 123456789g 123456789g 123456789g 123456789h ___4_____h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_naked_triple_3():
#     return f"""
#     naked_triple_3.sudoku
#     9
#     _____6___a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c ______7__c
# 123456789a 123456789a ____5____a 123456789b _____6___b 123456789b 123456789c ________9c 123456789c
# _______8_a 123456789a 123456789a ___4_____b 123456789b 123456789b _2_______c 123456789c 123456789c
# 123456789d __3______d 123456789d 123456789e 123456789e 123456789e ______7__f 123456789f 123456789f
# 123456789d 1________d 123456789d ________9e 123456789e ______7__e 123456789f __3______f 123456789f
# 123456789d 123456789d _______8_d 123456789e 123456789e 123456789e 123456789f 1________f 123456789f
# 123456789g 123456789g ______7__g 123456789h 123456789h ____5____h 123456789i 123456789i _______8_i
# 123456789g _2_______g 123456789g 123456789h _______8_h 123456789h 1________i 123456789i 123456789i
# ___4_____g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i __3______i
#     """

# @staticmethod
# def sudoku_naked_triple_4():
#     return f"""
#     naked_triple_4.sudoku
#     9
#     123456789a 123456789a 123456789a 123456789b 123456789b 123456789b _____6___c ________9c _______8_c
#     123456789a 123456789a 123456789a 123456789b _2_______b _____6___b 123456789c 123456789c 123456789c
#     1________a 123456789a 123456789a ________9b 123456789b 123456789b 123456789c 123456789c ____5____c
#     123456789d 123456789d ______7__d 123456789e ___4_____e 123456789e 123456789f __3______f _2_______f
#     123456789d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 123456789f
#     __3______d _____6___d 123456789d 123456789e ____5____e 123456789e _______8_f 123456789f 123456789f
#     ____5____g 123456789g 123456789g 123456789h 123456789h ___4_____h 123456789i 123456789i 1________i
#     123456789g 123456789g 123456789g ____5____h ______7__h 123456789h 123456789i 123456789i 123456789i
#     ________9g _2_______g _______8_g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_naked_triple_5():
#     return f"""
#     naked_triple_5.sudoku
#     9
#     ___4_____a ______7__a _______8_a 123456789b 1________b 123456789b _____6___c ____5____c 123456789c
#     123456789a __3______a 123456789a 123456789b 123456789b ______7__b _______8_c 1________c 123456789c
#     123456789a 1________a 123456789a 123456789b 123456789b _______8_b 123456789c 123456789c 123456789c
#     123456789d 123456789d ______7__d ____5____e _______8_e 123456789e 123456789f __3______f _____6___f
#     _____6___d ____5____d ___4_____d ______7__e __3______e _2_______e 1________f ________9f _______8_f
#     __3______d _______8_d 123456789d 123456789e ________9e _____6___e ____5____f 123456789f 123456789f
#     _______8_g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i _____6___i 123456789i
#     123456789g _____6___g 123456789g _______8_h 123456789h 123456789h 123456789i ___4_____i 123456789i
#     ______7__g 123456789g __3______g 123456789h _____6___h ____5____h ________9i _______8_i 1________i
#     """

# @staticmethod
# def sudoku_naked_triple_6():
#     return f"""
#     naked_triple_6.sudoku
#     9
#     ____5____a _______8_a 123456789a ______7__b __3______b ________9b _2_______c 1________c 123456789c
#     ________9a __3______a 123456789a 1________b _2_______b _____6___b 123456789c 123456789c _______8_c
#     1________a _2_______a 123456789a ____5____b _______8_b ___4_____b 123456789c ________9c __3______c
#     123456789d ________9d ____5____d _______8_e ___4_____e _2_______e 123456789f 123456789f 123456789f
#     _____6___d ___4_____d _______8_d ________9e 1________e 123456789e 123456789f _2_______f ____5____f
#     123456789d 1________d _2_______d _____6___e 123456789e 123456789e ___4_____f _______8_f ________9f
#     _______8_g ______7__g ________9g ___4_____h 123456789h 1________h 123456789i __3______i _2_______i
#     ___4_____g _____6___g __3______g _2_______h 123456789h 123456789h 123456789i 123456789i 123456789i
#     _2_______g ____5____g 1________g __3______h 123456789h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_naked_triple_7():
#     return f"""
#     naked_triple_7.sudoku
#     9
#     1________a _____6___a 123456789a 123456789b ______7__b ____5____b ___4_____c 123456789c 123456789c
#     123456789a ____5____a ___4_____a _2_______b 1________b 123456789b 123456789c 123456789c ______7__c
#     _2_______a __3______a ______7__a ________9b ___4_____b _____6___b _______8_c 1________c ____5____c
#     ____5____d ________9d __3______d ______7__e _______8_e _2_______e 1________f ___4_____f _____6___f
#     ______7__d _______8_d _2_______d 1________e _____6___e ___4_____e ____5____f __3______f ________9f
#     ___4_____d 1________d _____6___d 123456789e 123456789e 123456789e _2_______f ______7__f _______8_f
#     123456789g _2_______g ____5____g ___4_____h __3______h ______7__h 123456789i 123456789i 1________i
#     123456789g ___4_____g 123456789g 123456789h 123456789h 1________h ______7__i 123456789i 123456789i
#     123456789g ______7__g 1________g _____6___h _2_______h 123456789h 123456789i ____5____i ___4_____i
#     """

# @staticmethod
# def sudoku_naked_triple_8():
#     return f"""
#     naked_triple_8.sudoku
#     9
#     123456789a ___4_____a 123456789a 123456789b 123456789b 123456789b ________9c __3______c 123456789c
# __3______a ______7__a 123456789a _2_______b 123456789b _______8_b _____6___c ___4_____c 1________c
# 123456789a _____6___a 123456789a 123456789b ___4_____b 123456789b ____5____c 123456789c ______7__c
# ____5____d 123456789d ___4_____d 123456789e 1________e ______7__e __3______f ________9f 123456789f
# _____6___d 123456789d 1________d 123456789e 123456789e 123456789e 123456789f ______7__f ____5____f
# ________9d 123456789d ______7__d ____5____e 123456789e 123456789e 1________f 123456789f ___4_____f
# ___4_____g 1________g _____6___g 123456789h _2_______h ________9h 123456789i ____5____i __3______i
# ______7__g ____5____g _2_______g 1________h 123456789h 123456789h 123456789i 123456789i ________9i
# _______8_g ________9g __3______g 123456789h 123456789h 123456789h 123456789i 1________i 123456789i
#     """

# @staticmethod
# def sudoku_naked_triple_9():
#     return f"""
#     naked_triple_9.sudoku
#     9
#     123456789a ___4_____a _2_______a ______7__b 123456789b 123456789b 123456789c 123456789c 123456789c
# 123456789a 123456789a __3______a ________9b 123456789b 123456789b ______7__c 123456789c ___4_____c
# ____5____a ______7__a 123456789a 123456789b ___4_____b 123456789b 123456789c 123456789c 123456789c
# ______7__d 123456789d ____5____d 123456789e _____6___e _2_______e ___4_____f 123456789f 123456789f
# 123456789d 123456789d 123456789d 123456789e ________9e 123456789e 123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d ___4_____e ______7__e 123456789e _2_______f 123456789f __3______f
# 123456789g 123456789g 123456789g 123456789h 123456789h ______7__h 123456789i _______8_i _____6___i
# _____6___g 123456789g 1________g 123456789h 123456789h ___4_____h ____5____i 123456789i 123456789i
# 123456789g 123456789g ______7__g _____6___h 123456789h ________9h __3______i ___4_____i 123456789i
#     """

# @staticmethod
# def sudoku_naked_triple_row():
#     return f"""
#     naked_triple_row.sudoku
#     9
#     ______7__a _______8_a _2_______a __3______b ____5____b ___4_____b 1________c ________9c _____6___c
# 123456789a 123456789a 123456789a _2_______b _____6___b ______7__b ___4_____c ____5____c _______8_c
# ___4_____a ____5____a _____6___a _______8_b ________9b 1________b __3______c _2_______c ______7__c
# 123456789d 123456789d 1________d ____5____e 123456789e 123456789e _____6___f 123456789f 123456789f
# ____5____d ______7__d 123456789d _____6___e 123456789e ________9e _2_______f 123456789f 1________f
# 123456789d _____6___d 123456789d 123456789e 123456789e _______8_e ____5____f 123456789f 123456789f
# _____6___g __3______g ______7__g ___4_____h _______8_h ____5____h ________9i 1________i _2_______i
# 123456789g ___4_____g 123456789g 123456789h 123456789h _____6___h 123456789i __3______i ____5____i
# 123456789g 123456789g ____5____g ________9h 123456789h 123456789h 123456789i _____6___i ___4_____i
#     """

# @staticmethod
# def sudoku_picnic_0():
#     return f"""
#     picnic_0.sudoku
#     9
#     ___4_____a 123456789a _2_______a 123456789b _______8_b ________9b 123456789c ______7__c __3______c
#     ______7__a ________9a 1________a ___4_____b 123456789b _____6___b 123456789c ____5____c 123456789c
#     123456789a 123456789a 123456789a 123456789b 123456789b 123456789b ___4_____c 123456789c ________9c
#     _______8_d 1________d ______7__d 123456789e 123456789e ____5____e 123456789f 123456789f 123456789f
#     123456789d _____6___d 123456789d _______8_e ________9e ______7__e 123456789f _2_______f 123456789f
#     123456789d 123456789d 123456789d _____6___e 123456789e 123456789e ____5____f _______8_f ______7__f
#     __3______g 123456789g ____5____g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     123456789g _______8_g 123456789g ______7__h 123456789h __3______h 1________i ________9i ___4_____i
#     1________g ______7__g 123456789g _2_______h _____6___h 123456789h _______8_i 123456789i ____5____i
#     """

# @staticmethod
# def sudoku_picnic_1():
#     return f"""
#     picnic_1.sudoku
#     9
#     123456789a 123456789a _____6___a __3______b _2_______b ______7__b 123456789c _______8_c 123456789c
#     ___4_____a 123456789a 123456789a 123456789b ____5____b 1________b 123456789c ______7__c _____6___c
#     123456789a _2_______a 123456789a ___4_____b _______8_b 123456789b 123456789c __3______c 1________c
#     123456789d __3______d 1________d 123456789e 123456789e 123456789e _______8_f _2_______f ______7__f
#     123456789d 123456789d 123456789d 123456789e __3______e 123456789e 123456789f 123456789f 123456789f
#     _______8_d ______7__d ___4_____d 123456789e 123456789e 123456789e __3______f ________9f 123456789f
#     ________9g ___4_____g 123456789g 123456789h ______7__h ____5____h 123456789i _____6___i 123456789i
#     __3______g _____6___g 123456789g _2_______h 1________h 123456789h 123456789i 123456789i _______8_i
#     123456789g ____5____g 123456789g _____6___h ________9h __3______h ______7__i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_picnic_2():
#     return f"""
#     picnic_2.sudoku
#     9
#     123456789a ______7__a 123456789a ____5____b 1________b __3______b 123456789c _2_______c ________9c
#     __3______a 123456789a ________9a 123456789b _____6___b _2_______b 123456789c 123456789c 1________c
#     ____5____a _2_______a 123456789a 123456789b 123456789b 123456789b 123456789c __3______c _____6___c
#     123456789d 123456789d 123456789d 123456789e __3______e 123456789e 1________f ___4_____f _______8_f
#     ___4_____d 123456789d 123456789d 123456789e _2_______e 123456789e 123456789f 123456789f ______7__f
#     1________d _____6___d __3______d 123456789e ______7__e 123456789e 123456789f 123456789f 123456789f
#     ________9g 1________g 123456789g 123456789h 123456789h 123456789h 123456789i _______8_i ___4_____i
#     _______8_g 123456789g 123456789g ___4_____h ________9h 123456789h ____5____i 123456789i _2_______i
#     ______7__g ____5____g 123456789g _2_______h _______8_h _____6___h 123456789i 1________i 123456789i
#     """

# @staticmethod
# def sudoku_second_lesson_0():
#     return f"""
#     second_lesson_0.sudoku
#     9
#     __3______a ____5____a _______8_a _2_______b 123456789b 1________b ___4_____c _____6___c ______7__c
#     _2_______a 1________a _____6___a ___4_____b 123456789b ______7__b ________9c _______8_c ____5____c
#     ___4_____a ________9a ______7__a _______8_b 123456789b ____5____b _2_______c 1________c __3______c
#     _____6___d ___4_____d __3______d ____5____e 123456789e _2_______e ______7__f ________9f 1________f
#     ________9d ______7__d ____5____d __3______e 123456789e ___4_____e _____6___f _2_______f _______8_f
#     1________d _______8_d _2_______d ________9e 123456789e _____6___e ____5____f __3______f ___4_____f
#     ______7__g _2_______g ________9g 1________h 123456789h __3______h _______8_i ___4_____i _____6___i
#     _______8_g _____6___g 1________g ______7__h 123456789h ________9h __3______i ____5____i _2_______i
#     ____5____g __3______g ___4_____g _____6___h 123456789h _______8_h 1________i ______7__i ________9i
#     """

# @staticmethod
# def sudoku_simple_0():
#     return f"""
#     simple_0.sudoku
#     9
#     123456789a ___4_____a 123456789a ______7__b _______8_b 123456789b 123456789c 123456789c 123456789c
#     _____6___a 123456789a 1________a 123456789b 123456789b ___4_____b _2_______c 123456789c 123456789c
#     ____5____a ______7__a 123456789a _2_______b _____6___b 123456789b 123456789c 123456789c 123456789c
#     123456789d __3______d 123456789d ____5____e 123456789e _______8_e 123456789f 123456789f _____6___f
#     1________d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f ______7__f
#     ______7__d 123456789d 123456789d ___4_____e 123456789e __3______e 123456789f _______8_f 123456789f
#     123456789g 123456789g 123456789g 123456789h ___4_____h ________9h 123456789i ____5____i _______8_i
#     123456789g 123456789g _____6___g _______8_h 123456789h 123456789h __3______i 123456789i _2_______i
#     123456789g 123456789g 123456789g 123456789h __3______h _2_______h 123456789i 1________i 123456789i
#     """

# @staticmethod
# def sudoku_unique_rectangle_type1_00():
#     return f"""
#     unique_rectangle_type1_00.sudoku
#     9
# 123456789a _____6___a ___4_____a 123456789b __3______b ______7__b 123456789c 123456789c 123456789c
# 1________a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# ____5____a 123456789a 123456789a ___4_____b 123456789b 123456789b __3______c 123456789c ________9c
# 123456789d 123456789d 123456789d ________9e ____5____e 123456789e _2_______f 123456789f 123456789f
# 123456789d ________9d 123456789d 123456789e 123456789e 123456789e 123456789f _______8_f 123456789f
# 123456789d 123456789d _______8_d 123456789e ___4_____e 1________e 123456789f 123456789f 123456789f
# ______7__g 123456789g 1________g 123456789h 123456789h _2_______h 123456789i 123456789i _______8_i
# 123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i ___4_____i
# 123456789g 123456789g 123456789g ______7__h ________9h 123456789h _____6___i __3______i 123456789i
#     """

# @staticmethod
# def sudoku_unique_rectangle_type1_01():
#     return f"""
#     unique_rectangle_type1_01.sudoku
#     9
# __3______a 123456789a _2_______a ___4_____b 123456789b 123456789b 123456789c 123456789c ______7__c
# 123456789a _____6___a ___4_____a 123456789b ______7__b 123456789b __3______c ____5____c 123456789c
# 123456789a ______7__a 123456789a 123456789b 123456789b 123456789b 123456789c _2_______c 123456789c
# 123456789d ____5____d ______7__d 123456789e 123456789e 123456789e 123456789f _____6___f 1________f
# 123456789d 123456789d 123456789d _____6___e 123456789e _______8_e 123456789f 123456789f 123456789f
# _____6___d ___4_____d 123456789d 123456789e 123456789e 123456789e _______8_f ________9f 123456789f
# 123456789g __3______g 123456789g 123456789h 123456789h 123456789h 123456789i ___4_____i 123456789i
# 123456789g 1________g _____6___g 123456789h _______8_h 123456789h ____5____i __3______i 123456789i
# ___4_____g 123456789g 123456789g 123456789h 123456789h _____6___h 1________i 123456789i _2_______i
#     """

# @staticmethod
# def sudoku_unique_rectangle_type1_02():
#     return f"""
#     unique_rectangle_type1_02.sudoku
#     9
# 123456789a __3______a 123456789a _______8_b 123456789b ____5____b ___4_____c _____6___c 123456789c
# 123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c __3______c 123456789c
# 123456789a 123456789a 123456789a _____6___b ___4_____b 123456789b 1________c 123456789c _2_______c
# _____6___d 123456789d ________9d 123456789e 123456789e 123456789e 123456789f _2_______f 123456789f
# 123456789d 1________d ___4_____d 123456789e 123456789e 123456789e ________9f _______8_f 123456789f
# 123456789d _2_______d 123456789d 123456789e 123456789e 123456789e _____6___f 123456789f 1________f
# 1________g 123456789g _2_______g 123456789h ____5____h ______7__h 123456789i 123456789i 123456789i
# 123456789g ________9g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
# 123456789g ___4_____g ______7__g 1________h 123456789h _____6___h 123456789i ____5____i 123456789i
#     """

# @staticmethod
# def sudoku_unique_rectangle_type1_03():
#     return f"""
#     unique_rectangle_type1_03.sudoku
#     9
#     123456789a 123456789a 123456789a _______8_b 123456789b 123456789b ______7__c _2_______c 123456789c
# 123456789a 123456789a _______8_a 123456789b ___4_____b 123456789b 123456789c 123456789c 123456789c
# 123456789a 123456789a __3______a 1________b ______7__b _2_______b ________9c 123456789c 123456789c
# 123456789d __3______d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f _______8_f
# 123456789d 123456789d ___4_____d 123456789e 123456789e 123456789e 1________f 123456789f 123456789f
# _2_______d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f ______7__f 123456789f
# 123456789g 123456789g _2_______g _____6___h _______8_h ________9h __3______i 123456789i 123456789i
# 123456789g 123456789g 123456789g 123456789h __3______h 123456789h ___4_____i 123456789i 123456789i
# 123456789g 1________g _____6___g 123456789h 123456789h ___4_____h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_unique_rectangle_type1_04():
#     return f"""
#     unique_rectangle_type1_04.sudoku
#     9
#     _____6___a _2_______a 123456789a 123456789b 123456789b ___4_____b ____5____c 123456789c 123456789c
#     _______8_a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c ___4_____c 123456789c
#     123456789a 123456789a ___4_____a __3______b 123456789b 123456789b 123456789c 123456789c _______8_c
#     _2_______d ________9d 123456789d 1________e 123456789e 123456789e __3______f 123456789f 123456789f
#     123456789d 123456789d 123456789d 123456789e _______8_e 123456789e 123456789f 123456789f 123456789f
#     123456789d 123456789d _______8_d 123456789e 123456789e ________9e 123456789f _2_______f _____6___f
#     ___4_____g 123456789g 123456789g 123456789h 123456789h _2_______h _____6___i 123456789i 123456789i
#     123456789g _____6___g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 1________i
#     123456789g 123456789g 1________g ____5____h 123456789h 123456789h 123456789i __3______i ___4_____i
#     """

# #
# @staticmethod
# def sudoku_unique_rectangle_type1_05():
#     return f"""
#     unique_rectangle_type1_05.sudoku
#     9
# 123456789a ___4_____a 123456789a 123456789b ______7__b ____5____b 1________c _2_______c 123456789c
# ____5____a 123456789a _2_______a ________9b ___4_____b 123456789b ______7__c __3______c 123456789c
# 123456789a 123456789a ______7__a _2_______b 123456789b 123456789b ___4_____c ________9c ____5____c
# ______7__d ____5____d 1________d 123456789e 123456789e 123456789e ________9f 123456789f _2_______f
# _2_______d __3______d _______8_d 1________e ________9e 123456789e ____5____f 123456789f ______7__f
# ___4_____d ________9d _____6___d ____5____e _2_______e ______7__e _______8_f 1________f __3______f
# _______8_g _2_______g ___4_____g _____6___h ____5____h ________9h __3______i ______7__i 1________i
# 1________g ______7__g ____5____g ___4_____h __3______h _2_______h _____6___i _______8_i ________9i
# 123456789g _____6___g 123456789g ______7__h 1________h _______8_h _2_______i ____5____i ___4_____i
#     """

# @staticmethod
# def sudoku_unique_rectangle_type2_00():
#     return f"""
#     unique_rectangle_type2_00.sudoku
#     9
#     123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# ________9a 123456789a _2_______a ______7__b 123456789b 123456789b 123456789c 123456789c 123456789c
# 1________a __3______a 123456789a 123456789b 123456789b 123456789b ________9c ____5____c 123456789c
# 123456789d 123456789d 123456789d ___4_____e ____5____e 123456789e ______7__f _______8_f 123456789f
# ___4_____d ____5____d 123456789d ________9e 123456789e ______7__e 123456789f 1________f _____6___f
# 123456789d _____6___d _______8_d 123456789e 1________e _2_______e 123456789f 123456789f 123456789f
# 123456789g 1________g ______7__g 123456789h 123456789h 123456789h 123456789i _2_______i ________9i
# 123456789g 123456789g 123456789g 123456789h 123456789h _______8_h ___4_____i 123456789i ____5____i
# 123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_unique_rectangle_type2_01():
#     return f"""
#     unique_rectangle_type2_01.sudoku
#     9
#     123456789a 123456789a 123456789a 123456789b 123456789b 123456789b _2_______c 123456789c 123456789c
# ______7__a ____5____a 123456789a 123456789b __3______b ___4_____b 123456789c 123456789c 123456789c
# __3______a 123456789a _______8_a ________9b 123456789b 123456789b 123456789c 123456789c 123456789c
# 123456789d 123456789d _____6___d 123456789e ______7__e 123456789e 123456789f _______8_f 123456789f
# ___4_____d ______7__d 123456789d 123456789e _______8_e 123456789e 123456789f 1________f _____6___f
# 123456789d _______8_d 123456789d 123456789e ___4_____e 123456789e ________9f 123456789f 123456789f
# 123456789g 123456789g 123456789g 123456789h 123456789h _____6___h __3______i 123456789i _2_______i
# 123456789g 123456789g 123456789g ______7__h _2_______h 123456789h 123456789i ___4_____i _______8_i
# 123456789g 123456789g 1________g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_unique_rectangle_type2_02():
#     return f"""
#     unique_rectangle_type2_02.sudoku
#     9
# __3______a 123456789a 123456789a 123456789b 123456789b ____5____b 123456789c 123456789c _2_______c
# 123456789a 123456789a ______7__a 123456789b 1________b _______8_b 123456789c 123456789c 123456789c
# 123456789a ________9a ____5____a ___4_____b 123456789b _____6___b __3______c 123456789c 123456789c
# ________9d 123456789d 123456789d 123456789e 123456789e ______7__e 123456789f 123456789f 123456789f
# 123456789d ___4_____d 123456789d 123456789e 123456789e 123456789e 123456789f _2_______f 123456789f
# 123456789d 123456789d 123456789d 1________e 123456789e 123456789e 123456789f 123456789f ___4_____f
# 123456789g 123456789g _______8_g ________9h 123456789h 1________h ___4_____i __3______i 123456789i
# 123456789g 123456789g 123456789g ____5____h __3______h 123456789h 1________i 123456789i 123456789i
# ______7__g 123456789g 123456789g _____6___h 123456789h 123456789h 123456789i 123456789i ________9i

#     """

# @staticmethod
# def sudoku_unique_rectangle_type2_03():
#     return f"""
#     unique_rectangle_type2_03.sudoku
#     9
# 123456789a 123456789a 123456789a _2_______b 123456789b 123456789b ________9c 123456789c 123456789c
# _______8_a 123456789a 123456789a 123456789b _____6___b 123456789b ____5____c 123456789c _2_______c
# ______7__a 123456789a 123456789a 123456789b 123456789b _______8_b 123456789c 123456789c 123456789c
# _2_______d 123456789d 1________d ____5____e 123456789e 123456789e 123456789f 123456789f 123456789f
# _____6___d 123456789d 123456789d _______8_e 123456789e ________9e 123456789f 123456789f __3______f
# 123456789d 123456789d 123456789d 123456789e 123456789e 1________e ______7__f 123456789f _______8_f
# 123456789g 123456789g 123456789g ______7__h 123456789h 123456789h 123456789i 123456789i ____5____i
# 1________g 123456789g ________9g 123456789h ____5____h 123456789h 123456789i 123456789i _____6___i
# 123456789g 123456789g _______8_g 123456789h 123456789h _____6___h 123456789i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_unique_rectangle_type2_04():
#     return f"""
#     unique_rectangle_type2_04.sudoku
#     9
# 123456789a 123456789a ________9a 123456789b ____5____b 123456789b 123456789c 123456789c 123456789c
# 123456789a ___4_____a __3______a 123456789b 123456789b 123456789b _______8_c 123456789c 123456789c
# _____6___a 123456789a 123456789a 123456789b 123456789b ________9b 123456789c 123456789c ___4_____c
# __3______d _______8_d ______7__d 123456789e 123456789e ___4_____e _2_______f 123456789f 123456789f
# 123456789d _2_______d 123456789d 123456789e 123456789e 123456789e 123456789f _____6___f 123456789f
# 123456789d 123456789d ____5____d _2_______e 123456789e 123456789e ________9f __3______f ______7__f
# 1________g 123456789g 123456789g ____5____h 123456789h 123456789h 123456789i 123456789i ________9i
# 123456789g 123456789g _____6___g 123456789h 123456789h 123456789h ____5____i _2_______i 123456789i
# 123456789g 123456789g 123456789g 123456789h 1________h 123456789h _____6___i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_unique_rectangle_type2_05():
#     return f"""
#     unique_rectangle_type2_05.sudoku
#     9
    
# 123456789a 123456789a 123456789a 123456789b ___4_____b 123456789b __3______c ____5____c 123456789c
# 123456789a 123456789a _______8_a 123456789b 123456789b 1________b 123456789c _____6___c 123456789c
# 123456789a 123456789a __3______a 123456789b _2_______b ________9b ______7__c 123456789c 123456789c
# 123456789d 123456789d 123456789d ___4_____e ____5____e 123456789e 123456789f _______8_f 123456789f
# 123456789d 123456789d 123456789d _2_______e 123456789e __3______e 123456789f 123456789f 123456789f
# 123456789d 1________d 123456789d 123456789e _______8_e _____6___e 123456789f 123456789f 123456789f
# 123456789g 123456789g _____6___g 1________h __3______h 123456789h _2_______i 123456789i 123456789i
# 123456789g ___4_____g 123456789g _______8_h 123456789h 123456789h ____5____i 123456789i 123456789i
# 123456789g _2_______g ____5____g 123456789h ________9h 123456789h 123456789i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_unique_rectangle_type2_06():
#     return f"""
#     unique_rectangle_type2_06.sudoku
#     9
# ________9a _______8_a 123456789a 123456789b 123456789b ___4_____b 123456789c ______7__c 123456789c
# 123456789a __3______a 1________a _______8_b ________9b 123456789b 123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# 123456789d ____5____d 123456789d 123456789e ______7__e 1________e ________9f 123456789f _____6___f
# ___4_____d 123456789d 123456789d ____5____e 123456789e ________9e 123456789f 123456789f 1________f
# 1________d 123456789d _______8_d __3______e _____6___e 123456789e 123456789f ___4_____f 123456789f
# 123456789g 123456789g 123456789g 123456789h 123456789h 123456789h 123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g 123456789h __3______h _____6___h _2_______i 1________i 123456789i
# 123456789g 1________g 123456789g ________9h 123456789h 123456789h 123456789i _____6___i ____5____i

#     """

# @staticmethod
# def sudoku_unique_rectangle_type2_07():
#     return f"""
#     unique_rectangle_type2_07.sudoku
#     9
# 123456789a 123456789a 123456789a ___4_____b 123456789b 123456789b 123456789c 123456789c _2_______c
# 123456789a 123456789a 123456789a 123456789b ______7__b _______8_b 123456789c 123456789c ___4_____c
# _____6___a 123456789a 123456789a __3______b 123456789b 123456789b 123456789c ________9c 123456789c
# ___4_____d _2_______d 123456789d 123456789e 123456789e 123456789e 123456789f _______8_f 123456789f
# 123456789d 123456789d ______7__d 123456789e _2_______e 123456789e ___4_____f 123456789f 123456789f
# 123456789d 1________d 123456789d 123456789e 123456789e 123456789e 123456789f ____5____f _____6___f
# 123456789g __3______g 123456789g 123456789h 123456789h ______7__h 123456789i 123456789i 1________i
# _______8_g 123456789g 123456789g _2_______h 1________h 123456789h 123456789i 123456789i 123456789i
# _2_______g 123456789g 123456789g 123456789h 123456789h __3______h 123456789i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_unique_rectangle_type2_08():
#     return f"""
#     unique_rectangle_type2_08.sudoku
#     9
# 123456789a __3______a ___4_____a 123456789b ______7__b _______8_b _2_______c ____5____c _____6___c
# _____6___a 123456789a ____5____a _2_______b ___4_____b 123456789b 123456789c __3______c ______7__c
# 123456789a _2_______a 123456789a ____5____b _____6___b __3______b 123456789c 1________c ___4_____c
# 123456789d ______7__d 123456789d 123456789e ____5____e 123456789e ___4_____f _2_______f __3______f
# ____5____d 123456789d _2_______d 123456789e __3______e ___4_____e ______7__f _____6___f ________9f
# __3______d ___4_____d 123456789d 123456789e _2_______e ______7__e ____5____f _______8_f 1________f
# ___4_____g ________9g 1________g __3______h _______8_h _2_______h _____6___i ______7__i ____5____i
# 123456789g _____6___g 123456789g ___4_____h 1________h ____5____h __3______i ________9i _2_______i
# _2_______g ____5____g __3______g ______7__h ________9h _____6___h 1________i ___4_____i _______8_i

#     """

# @staticmethod
# def sudoku_unique_rectangle_type2_09():
#     return f"""
#     unique_rectangle_type2_09.sudoku
#     9
# ____5____a ___4_____a 123456789a 123456789b ________9b 123456789b 123456789c 123456789c 123456789c
# 123456789a ________9a 123456789a __3______b 123456789b 123456789b 123456789c 123456789c _____6___c
# 123456789a 123456789a 123456789a ____5____b 123456789b 123456789b 123456789c 1________c ________9c
# ________9d 123456789d __3______d _____6___e 123456789e 123456789e ____5____f 123456789f 123456789f
# ___4_____d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 1________f
# 123456789d 123456789d ______7__d 123456789e 123456789e 1________e _____6___f 123456789f __3______f
# 1________g _2_______g 123456789g 123456789h 123456789h ____5____h 123456789i 123456789i 123456789i
# ______7__g 123456789g 123456789g 123456789h 123456789h ________9h 123456789i _2_______i 123456789i
# 123456789g 123456789g 123456789g 123456789h __3______h 123456789h 123456789i ______7__i _______8_i
#     """

# @staticmethod
# def sudoku_unique_rectangle_type2_10():
#     return f"""
#     unique_rectangle_type2_10.sudoku
#     9
# 123456789a 123456789a 123456789a 123456789b _2_______b 123456789b 123456789c ________9c _______8_c
# _2_______a ______7__a 123456789a 123456789b 123456789b _______8_b 123456789c 123456789c 123456789c
# ____5____a 123456789a 123456789a 123456789b 123456789b 1________b 123456789c _2_______c 123456789c
# 1________d 123456789d ____5____d ______7__e 123456789e 123456789e __3______f 123456789f 123456789f
# ______7__d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f ________9f
# 123456789d 123456789d _______8_d 123456789e 123456789e ____5____e 1________f 123456789f _2_______f
# 123456789g _____6___g 123456789g _2_______h 123456789h 123456789h 123456789i 123456789i __3______i
# 123456789g 123456789g 123456789g _______8_h 123456789h 123456789h 123456789i _____6___i ______7__i
# ___4_____g __3______g 123456789g 123456789h 1________h 123456789h 123456789i 123456789i 123456789i
#     """

# @staticmethod
# def sudoku_unique_rectangle_type2_11():
#     return f"""
#     unique_rectangle_type2_11.sudoku
#     9
# ___4_____a _2_______a __3______a ________9b _______8_b _____6___b 123456789c 123456789c 1________c
# _____6___a ____5____a ________9a ______7__b _2_______b 1________b __3______c _______8_c ___4_____c
# ______7__a _______8_a 1________a ____5____b __3______b ___4_____b 123456789c 123456789c _2_______c
# __3______d 123456789d ____5____d 1________e ___4_____e _2_______e 123456789f 123456789f _______8_f
# _2_______d 1________d 123456789d _______8_e ________9e __3______e 123456789f 123456789f 123456789f
# ________9d ___4_____d _______8_d _____6___e ____5____e ______7__e 1________f _2_______f __3______f
# 1________g ________9g 123456789g __3______h _____6___h _______8_h _2_______i 123456789i 123456789i
# ____5____g 123456789g _2_______g ___4_____h 1________h ________9h _______8_i __3______i 123456789i
# _______8_g __3______g 123456789g _2_______h ______7__h ____5____h 123456789i 1________i ________9i
#     """

# @staticmethod
# def sudoku_unique_rectangle_type2_12():
#     return f"""
#     unique_rectangle_type2_12.sudoku
#     9
# __3______a 1________a 123456789a 123456789b 123456789b 123456789b ____5____c _____6___c ________9c
# ______7__a _____6___a 123456789a 123456789b 123456789b 123456789b _______8_c ___4_____c __3______c
# ___4_____a ________9a 123456789a __3______b _____6___b 123456789b ______7__c 1________c _2_______c
# _____6___d _______8_d ______7__d _2_______e 123456789e 123456789e ___4_____f ________9f 1________f
# 1________d _2_______d ___4_____d ________9e _______8_e _____6___e __3______f ____5____f ______7__f
# ________9d ____5____d __3______d ___4_____e 1________e ______7__e _____6___f _2_______f _______8_f
# _______8_g ___4_____g _____6___g 123456789h 123456789h _2_______h 123456789i __3______i ____5____i
# 123456789g __3______g ________9g 123456789h 123456789h 123456789h 123456789i ______7__i _____6___i
# 123456789g ______7__g 1________g _____6___h 123456789h 123456789h 123456789i _______8_i ___4_____i

#     """

# @staticmethod
# def sudoku_unique_rectangle_type4_00():
#     return f"""
#     unique_rectangle_type4_00.sudoku
#     9
# _2_______a 123456789a 123456789a _____6___b 123456789b ________9b ______7__c 123456789c 123456789c
# 123456789a ___4_____a 123456789a 1________b 123456789b 123456789b 123456789c 123456789c ________9c
# 123456789a _____6___a 1________a 123456789b 123456789b 123456789b 123456789c 123456789c 123456789c
# 123456789d 123456789d 123456789d ________9e 123456789e 123456789e __3______f _____6___f 123456789f
# __3______d 123456789d _____6___d 123456789e 123456789e 123456789e 1________f 123456789f ______7__f
# 123456789d _______8_d ________9d 123456789e 123456789e 1________e 123456789f 123456789f 123456789f
# 123456789g 123456789g 123456789g 123456789h 123456789h 123456789h _2_______i ____5____i 123456789i
# _____6___g 123456789g 123456789g 123456789h 123456789h _2_______h 123456789i ___4_____i 123456789i
# 123456789g 123456789g _2_______g _______8_h 123456789h __3______h 123456789i 123456789i _____6___i

#     """

# @staticmethod
# def sudoku_unique_rectangle_type4_01():
#     return f"""
#     unique_rectangle_type4_01.sudoku
#     9
# 123456789a 123456789a ______7__a 123456789b _2_______b 123456789b 123456789c _____6___c 123456789c
# 123456789a ___4_____a 123456789a 123456789b 1________b 123456789b 123456789c 123456789c _______8_c
# 123456789a _____6___a __3______a ______7__b 123456789b 123456789b ___4_____c 1________c 123456789c
# 123456789d _2_______d 123456789d 123456789e 123456789e 123456789e 123456789f _______8_f 123456789f
# 123456789d 123456789d 1________d 123456789e ____5____e 123456789e _2_______f 123456789f 123456789f
# 123456789d ____5____d 123456789d 123456789e 123456789e 123456789e 123456789f ___4_____f 123456789f
# 123456789g 1________g ___4_____g 123456789h 123456789h _2_______h _____6___i ______7__i 123456789i
# _____6___g 123456789g 123456789g 123456789h __3______h 123456789h 123456789i ____5____i 123456789i
# 123456789g ______7__g 123456789g 123456789h ___4_____h 123456789h _______8_i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_unique_rectangle_type4_02():
#     return f"""
#     unique_rectangle_type4_02.sudoku
#     9
# 123456789a ___4_____a 123456789a 123456789b 123456789b ____5____b _____6___c ______7__c 123456789c
# 123456789a 1________a 123456789a _______8_b 123456789b ______7__b 123456789c 123456789c 123456789c
# 123456789a 123456789a _____6___a 123456789b ___4_____b 123456789b 123456789c 123456789c 1________c
# 123456789d __3______d 123456789d _2_______e 123456789e 123456789e 123456789f 123456789f 123456789f
# _______8_d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f ______7__f
# 123456789d 123456789d 123456789d 123456789e 123456789e ___4_____e 123456789f _2_______f 123456789f
# ________9g 123456789g 123456789g 123456789h _2_______h 123456789h __3______i 123456789i 123456789i
# 123456789g 123456789g 123456789g ___4_____h 123456789h __3______h 123456789i ________9i 123456789i
# 123456789g ____5____g 1________g _____6___h 123456789h 123456789h 123456789i _______8_i 123456789i

#     """

# @staticmethod
# def sudoku_unique_rectangle_type4_03():
#     return f"""
#     unique_rectangle_type4_03.sudoku
#     9
# 123456789a 123456789a ______7__a ___4_____b 1________b 123456789b 123456789c 123456789c ____5____c
# 123456789a 123456789a 123456789a 123456789b 123456789b ______7__b ________9c 123456789c 123456789c
# _______8_a 123456789a 123456789a 123456789b 123456789b 123456789b ___4_____c 123456789c 123456789c
# _____6___d 123456789d 123456789d 123456789e 123456789e 1________e _2_______f ___4_____f 123456789f
# ___4_____d 123456789d 1________d 123456789e _2_______e 123456789e ____5____f 123456789f __3______f
# 123456789d ______7__d _2_______d _____6___e 123456789e 123456789e 123456789f 123456789f ________9f
# 123456789g 123456789g _______8_g 123456789h 123456789h 123456789h 123456789i 123456789i _2_______i
# 123456789g 123456789g __3______g ________9h 123456789h 123456789h 123456789i 123456789i 123456789i
# ______7__g 123456789g 123456789g 123456789h __3______h _____6___h _______8_i 123456789i 123456789i

#     """

# @staticmethod
# def sudoku_unique_rectangle_type4_04():
#     return f"""
#     unique_rectangle_type4_04.sudoku
#     9
#     123456789a __3______a 123456789a 123456789b ________9b 123456789b _______8_c 123456789c ______7__c
# _______8_a 123456789a 123456789a 1________b 123456789b 123456789b _____6___c 123456789c __3______c
# _2_______a 123456789a 123456789a 123456789b 123456789b _______8_b 123456789c 123456789c 123456789c
# 123456789d 123456789d __3______d 123456789e 123456789e 123456789e ____5____f 123456789f 123456789f
# _____6___d 123456789d 123456789d 123456789e 123456789e 123456789e 123456789f 123456789f 1________f
# 123456789d 123456789d _2_______d 123456789e 123456789e 123456789e ______7__f 123456789f 123456789f
# 123456789g 123456789g 123456789g _______8_h 123456789h 123456789h 123456789i 123456789i ___4_____i
# ______7__g 123456789g 1________g 123456789h 123456789h __3______h 123456789i 123456789i _______8_i
# ________9g 123456789g ____5____g 123456789h ______7__h 123456789h 123456789i 1________i 123456789i
#     """

# @staticmethod
# def sudoku_unique_rectangle_type4_05():
#     return f"""
#     unique_rectangle_type4_05.sudoku
#     9
# _____6___a ________9a _2_______a ____5____b 123456789b 123456789b ______7__c __3______c _______8_c
# ____5____a __3______a _______8_a _2_______b ________9b ______7__b ___4_____c _____6___c 1________c
# ______7__a 123456789a 123456789a __3______b _______8_b _____6___b ____5____c ________9c _2_______c
# 123456789d _______8_d 123456789d 123456789e 123456789e 123456789e _____6___f 123456789f 123456789f
# 1________d 123456789d 123456789d 123456789e 123456789e 123456789e ________9f 123456789f ___4_____f
# 123456789d 123456789d ____5____d 123456789e 123456789e 123456789e 1________f _______8_f 123456789f
# _______8_g ____5____g ________9g ___4_____h ______7__h _2_______h __3______i 1________i _____6___i
# ___4_____g _2_______g _____6___g 1________h ____5____h __3______h _______8_i ______7__i ________9i
# __3______g 123456789g 123456789g 123456789h _____6___h 123456789h _2_______i ___4_____i ____5____i

#     """



#
# avoidable_rectangle_type1_north_east_in_cols
# 123456789a 123456789a 123456789a   _2_______b ____5____b 123456789b   _____6___c 123456789c 123456789c
# 123456789a 123456789a _____6___a   123456789b 123456789b _______8_b   123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a   ______7__b 123456789b ________9b   123456789c 123456789c 1________c
#
# 123456789d _______8_d 123456789d   123456789e 123456789e 123456789e   123456789f 1________f 123456789f
# 1________d _2_______d ____5____d   123456789e 123456789e 123456789e   __3______f ________9f _____6___f
# 123456789d ___4_____d 123456789d   123456789e 123456789e 123456789e   123456789f ______7__f 123456789f
#
# _2_______g 123456789g 123456789g   ________9h 123456789h __3______h   123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g   ___4_____h 123456789h 123456789h   ____5____i 123456789i 123456789i
# 123456789g 123456789g __3______g   123456789h _______8_h _____6___h   123456789i 123456789i 123456789i
#
# avoidable_rectangle_type1_north_east_in_rows
# 123456789a 123456789a ______7__a   123456789b 1________b _____6___b   123456789c _2_______c 123456789c
# 123456789a 123456789a 123456789a   123456789b 123456789b 123456789b   _____6___c 123456789c 123456789c
# _______8_a ____5____a 123456789a   123456789b 123456789b _2_______b   123456789c ________9c 123456789c
#
# ______7__d 123456789d 123456789d   123456789e _2_______e ________9e   123456789f ____5____f 123456789f
# 123456789d 123456789d 123456789d   123456789e 123456789e 123456789e   123456789f 123456789f 123456789f
# 123456789d ___4_____d 123456789d   1________e _______8_e 123456789e   123456789f 123456789f _____6___f
#
# 123456789g ________9g 123456789g   ____5____h 123456789h 123456789h   123456789i ___4_____i _2_______i
# 123456789g 123456789g __3______g   123456789h 123456789h 123456789h   123456789i 123456789i 123456789i
# 123456789g _______8_g 123456789g   ________9h ___4_____h 123456789h   ______7__i 123456789i 123456789i
#
# avoidable_rectangle_type1_north_west_in_cols
# 123456789a 123456789a ________9a   123456789b ______7__b __3______b   123456789c 123456789c 123456789c
# _2_______a 123456789a 123456789a   ___4_____b 123456789b _______8_b   123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a   _____6___b 123456789b 123456789b   ________9c 123456789c 123456789c
#
# 123456789d _______8_d 123456789d   123456789e 123456789e 123456789e   123456789f 1________f 123456789f
# ________9d ___4_____d ____5____d   123456789e 123456789e 123456789e   ______7__f __3______f _2_______f
# 123456789d _2_______d 123456789d   123456789e 123456789e 123456789e   123456789f _____6___f 123456789f
#
# 123456789g 123456789g ______7__g   123456789h 123456789h 1________h   123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g   ____5____h 123456789h ___4_____h   123456789i 123456789i __3______i
# 123456789g 123456789g 123456789g   ________9h _____6___h 123456789h   ____5____i 123456789i 123456789i
#
# avoidable_rectangle_type1_north_west_in_rows
# 123456789a _______8_a 123456789a   123456789b 123456789b 123456789b   123456789c 123456789c 123456789c
# _____6___a _2_______a 123456789a   123456789b 123456789b ___4_____b   123456789c 123456789c 123456789c
# 1________a __3______a ______7__a   123456789b 123456789b ____5____b   123456789c _______8_c 123456789c
#
# __3______d ____5____d 123456789d   _2_______e 123456789e 123456789e   123456789f 1________f 123456789f
# 123456789d 123456789d _____6___d   123456789e 123456789e 123456789e   __3______f 123456789f 123456789f
# 123456789d ________9d 123456789d   123456789e 123456789e ______7__e   123456789f ___4_____f _____6___f
#
# 123456789g 1________g 123456789g   ______7__h 123456789h 123456789h   ___4_____i ________9i _2_______i
# 123456789g 123456789g 123456789g   1________h 123456789h 123456789h   123456789i _____6___i ______7__i
# 123456789g 123456789g 123456789g   123456789h 123456789h 123456789h   123456789i ____5____i 123456789i
#
#
# avoidable_rectangle_type1_south_east_in_cols
# 123456789a ____5____a _2_______a   123456789b 123456789b 123456789b   123456789c 123456789c 1________c
# _____6___a ________9a 1________a   123456789b __3______b 123456789b   _______8_c 123456789c 123456789c
# 123456789a __3______a 123456789a   123456789b 123456789b 123456789b   123456789c 123456789c 123456789c
#
# 123456789d 123456789d _______8_d   _2_______e 123456789e ____5____e   ________9f 123456789f 123456789f
# 123456789d 1________d 123456789d   123456789e 123456789e 123456789e   123456789f _______8_f 123456789f
# 123456789d 123456789d ____5____d   _____6___e 123456789e ________9e   1________f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g   123456789h 123456789h 123456789h   123456789i 1________i 123456789i
# 123456789g 123456789g ___4_____g   123456789h _2_______h 123456789h   _____6___i ____5____i ________9i
# ____5____g 123456789g 123456789g   123456789h 123456789h 123456789h   __3______i ______7__i 123456789i
#
#
# avoidable_rectangle_type1_south_east_in_rows
# 123456789a 123456789a 123456789a   __3______b 123456789b _2_______b   123456789c 1________c 123456789c
# 123456789a 123456789a 123456789a   123456789b ________9b ___4_____b   123456789c 123456789c __3______c
# ___4_____a ______7__a 123456789a   123456789b 123456789b 123456789b   123456789c 123456789c _2_______c
#
# 123456789d 123456789d 1________d   ____5____e 123456789e 123456789e   123456789f _2_______f 123456789f
# 123456789d 123456789d ______7__d   123456789e 1________e 123456789e   _______8_f 123456789f 123456789f
# 123456789d _______8_d 123456789d   123456789e 123456789e __3______e   ____5____f 123456789f 123456789f
#
# ____5____g 123456789g 123456789g   123456789h 123456789h 123456789h   123456789i _____6___i ________9i
# _2_______g 123456789g 123456789g   ________9h _______8_h 123456789h   123456789i 123456789i 123456789i
# 123456789g _____6___g 123456789g   1________h 123456789h ____5____h   123456789i 123456789i 123456789i
#
# avoidable_rectangle_type1_south_west_in_rows
# _______8_a ___4_____a 123456789a   123456789b 123456789b ______7__b   123456789c 123456789c 123456789c
# 123456789a 123456789a __3______a   123456789b 123456789b ____5____b   123456789c 123456789c _____6___c
# 1________a 123456789a ______7__a   _____6___b 123456789b 123456789b   123456789c ___4_____c 123456789c
#
# 123456789d 123456789d 123456789d   123456789e 123456789e ________9e   123456789f _______8_f 123456789f
# 123456789d 123456789d ________9d   123456789e 123456789e 123456789e   _____6___f 123456789f 123456789f
# 123456789d ______7__d 123456789d   __3______e 123456789e 123456789e   123456789f 123456789f 123456789f
#
# 123456789g ________9g 123456789g   123456789h 123456789h ___4_____h   _2_______i 123456789i _______8_i
# ____5____g 123456789g 123456789g   ______7__h 123456789h 123456789h   ________9i 123456789i 123456789i
# 123456789g 123456789g 123456789g   _2_______h 123456789h 123456789h   123456789i __3______i ______7__i
#
# avoidable_rectangle_type1_0
# 123456789a _____6___a 123456789a   123456789b 123456789b 123456789b   123456789c __3______c ________9c
# 123456789a _______8_a 123456789a   __3______b _2_______b 123456789b   123456789c 123456789c 123456789c
# ________9a 123456789a 123456789a   ____5____b 123456789b _____6___b   123456789c 123456789c 123456789c
#
# _2_______d 123456789d 123456789d   123456789e 123456789e ___4_____e   _____6___f 123456789f 123456789f
# 123456789d 123456789d ______7__d   123456789e ____5____e 123456789e   _2_______f 123456789f 123456789f
# 123456789d 123456789d ____5____d   _____6___e 123456789e 123456789e   123456789f 123456789f _______8_f
#
# 123456789g 123456789g 123456789g   ___4_____h 123456789h _______8_h   123456789i 123456789i ____5____i
# 123456789g 123456789g 123456789g   123456789h __3______h 1________h   123456789i ___4_____i 123456789i
# ______7__g 1________g 123456789g   123456789h 123456789h 123456789h   123456789i _______8_i 123456789i












