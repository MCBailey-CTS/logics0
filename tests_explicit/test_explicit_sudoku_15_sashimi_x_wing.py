# def test_():
#     actual = \
#         f"""
#
#         """
#
#     expected = \
#         f"""
#
#         """
#     if solve(9, actual, expected, UniqueRectangleType4()):
#         return
#     assert False
#
#
#
# sudoku_explicit_shashimi_x_wing_1_fin_cols_actual
# ____5____a 123456789a 123456789a    123456789b _____6___b 123456789b    123456789c 123456789c 123456789c
# __3______a 123456789a 123456789a    123456789b ____5____b 123456789b    123456789c 123456789c 123456789c
# _____678_a 123456789a 123456789a    123456789b ______78_b 123456789b    123456789c 123456789c 123456789c
#
# 1________d _2_______d __3___78_d    ___4__78_e ___4__78_e ____5_78_e    123456789f 123456789f 123456789f
# ______78_d __3____8_d _____6___d    _2____78_e ________9e _2__5_78_e    123456789f 123456789f 123456789f
# ___4_____d ____5____d ________9d    _____6___e __3______e 1________e    123456789f 123456789f 123456789f
#
# _____6_8_g 123456789g 123456789g    123456789h ___4___8_h 123456789h    123456789i 123456789i 123456789i
# _2_______g 123456789g 123456789g    123456789h 1________h 123456789h    123456789i 123456789i 123456789i
# ________9g 123456789g 123456789g    123456789h _2_______h 123456789h    123456789i 123456789i 123456789i
#
#
#
#
#
# sudoku_explicit_shashimi_x_wing_1_fin_cols_expected
# ____5____a 123456789a 123456789a    123456789b _____6___b 123456789b    123456789c 123456789c 123456789c
# __3______a 123456789a 123456789a    123456789b ____5____b 123456789b    123456789c 123456789c 123456789c
# _____678_a 123456789a 123456789a    123456789b ______78_b 123456789b    123456789c 123456789c 123456789c
#
# 1________d _2_______d __3____8_d    ___4__78_e ___4__78_e ____5_78_e    123456789f 123456789f 123456789f
# ______78_d __3____8_d _____6___d    _2_____8_e ________9e _2__5__8_e    123456789f 123456789f 123456789f
# ___4_____d ____5____d ________9d    _____6___e __3______e 1________e    123456789f 123456789f 123456789f
#
# _____6_8_g 123456789g 123456789g    123456789h ___4___8_h 123456789h    123456789i 123456789i 123456789i
# _2_______g 123456789g 123456789g    123456789h 1________h 123456789h    123456789i 123456789i 123456789i
# ________9g 123456789g 123456789g    123456789h _2_______h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_shashimi_x_wing_1_fin_rows_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _23456789a _23456789a 123456789a    _23456789b _23456789b _23456789b    _23456789c 123456789c _23456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# _23456789g _23456789g 123456789g    _23456789h _23456789h _23456789h    123456789i _23456789i _23456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
#
# sudoku_explicit_shashimi_x_wing_1_fin_rows_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    _23456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    _23456789c 123456789c 123456789c
# _23456789a _23456789a 123456789a    _23456789b _23456789b _23456789b    _23456789c 123456789c _23456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# _23456789g _23456789g 123456789g    _23456789h _23456789h _23456789h    123456789i _23456789i _23456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i _23456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i _23456789i 123456789i
#
#
# sudoku_explicit_shashimi_x_wing_2_fin_cols_actual
# 123456789a 123456789a 123456789a    _____6___b 123456789b 123456789b    ______7_9c 123456789c 123456789c
# 123456789a 123456789a 123456789a    ____5____b 123456789b 123456789b    _______8_c 123456789c 123456789c
# 123456789a 123456789a 123456789a    ________9b 123456789b 123456789b    ____5____c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    _2_4_____e 123456789e 123456789e    __34_____f 123456789f 123456789f
# 123456789d 123456789d 123456789d    ______7__e 123456789e 123456789e    1________f 123456789f 123456789f
# 123456789d 123456789d 123456789d    _______8_e 123456789e 123456789e    _2_______f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    __3______h 123456789h 123456789h    ___4__7_9i 123456789i 123456789i
# 123456789g 123456789g 123456789g    1________h 123456789h 123456789h    __34____9i 123456789i 123456789i
# 123456789g 123456789g 123456789g    _2_4_____h 123456789h 123456789h    _____6___i __34_____i 1________i
#
# sudoku_explicit_shashimi_x_wing_2_fin_cols_expected
# 123456789a 123456789a 123456789a    _____6___b 123456789b 123456789b    ______7_9c 123456789c 123456789c
# 123456789a 123456789a 123456789a    ____5____b 123456789b 123456789b    _______8_c 123456789c 123456789c
# 123456789a 123456789a 123456789a    ________9b 123456789b 123456789b    ____5____c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    _2_4_____e 123456789e 123456789e    __34_____f 123456789f 123456789f
# 123456789d 123456789d 123456789d    ______7__e 123456789e 123456789e    1________f 123456789f 123456789f
# 123456789d 123456789d 123456789d    _______8_e 123456789e 123456789e    _2_______f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    __3______h 123456789h 123456789h    ___4__7_9i 123456789i 123456789i
# 123456789g 123456789g 123456789g    1________h 123456789h 123456789h    __34____9i 123456789i 123456789i
# 123456789g 123456789g 123456789g    _2_4_____h 123456789h 123456789h    _____6___i __3______i 1________i
#
#
# sudoku_explicit_shashimi_x_wing_2_fin_rows_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _23456789a _23456789a 123456789a    _23456789b _23456789b _23456789b    _23456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# _23456789g _23456789g 123456789g    _23456789h _23456789h _23456789h    123456789i _23456789i _23456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
#
# sudoku_explicit_shashimi_x_wing_2_fin_rows_expected
#
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    _23456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    _23456789c 123456789c 123456789c
# _23456789a _23456789a 123456789a    _23456789b _23456789b _23456789b    _23456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# _23456789g _23456789g 123456789g    _23456789h _23456789h _23456789h    123456789i _23456789i _23456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
#
#
#
#
#
#
#
#
#
#
#
