# sudoku_explicit_naked_quad_cols_actual
# _2_456_8_a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _2__56_8_a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _2_4_6___a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 1_3_5_7__d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 1_3_5____d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# __3_5_7__d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# __3___7__g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# ________9g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# __34_6___g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
# sudoku_explicit_naked_quad_cols_expected
# _2_4_6_8_a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _2___6_8_a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# _2_4_6___a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 1_3_5_7__d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 1_3_5____d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# __3_5_7__d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# __3___7__g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# ________9g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# ___4_6___g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_naked_quad_fences_actual
#
# __3__678_a ______7_9a _2_______a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# ___4__78_a ___4__7_9a ___4___8_a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 1_345678_a 1__45_7__a __3456_8_a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_naked_quad_fences_expected
# __3__6___a ______7_9a _2_______a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# ___4__78_a ___4__7_9a ___4___8_a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 1_3_56___a 1___5____a __3_56___a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
# sudoku_explicit_naked_quad_rows_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 1__4__7_9g 123456789g 123456789g    1__4__7_9h 123456789h 1__4__7_9h    123456789i 123456789i 1__4__7_9i
#
# sudoku_explicit_naked_quad_rows_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 1__4__7_9g _23_56_8_g _23_56_8_g    1__4__7_9h _23_56_8_h 1__4__7_9h    _23_56_8_i _23_56_8_i 1__4__7_9i
#
#
#
