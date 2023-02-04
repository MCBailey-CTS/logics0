# sudoku_explicit_sue_de_coq_cols_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    1________c _2____78_c _2_45_7__c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    ________9c _2___67__c _2_4567__c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    __34_____c _23____8_c _2_4_____c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f ___4_____f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f _____67__f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f ________9f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i ____5____i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i _23__67__i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 1________i 123456789i
#
#
#
# sudoku_explicit_sue_de_coq_cols_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    1________c _2____78_c ____5_7__c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    ________9c _2___67__c ____567__c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    __34_____c _23____8_c _2_4_____c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f ___4_____f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f _____67__f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f ________9f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i ____5____i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i _23______i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 1________i 123456789i
#
# sudoku_explicit_sue_de_coq_rows_actual
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    123456789e 123456789e 123456789e    123456789f 123456789f 123456789f
# 123456789d 12_______d 123456789d    12345____e 12345____e 12345____e    123456789f 123456789f 123456789f
# 123456789d 123456789d 123456789d    123456789e 123456789e __34_____e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
#
#
#
# sudoku_explicit_sue_de_coq_rows_expected
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
# 123456789a 123456789a 123456789a    123456789b 123456789b 123456789b    123456789c 123456789c 123456789c
#
# 123456789d 123456789d 123456789d    12___6789e 12___6789e 12___6789e    123456789f 123456789f 123456789f
# __34_6789d 12_______d __34_6789d    12345____e 12345____e 12345____e    __34_6789f __34_6789f __34_6789f
# 123456789d 123456789d 123456789d    12___6789e 12___6789e __34_____e    123456789f 123456789f 123456789f
#
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
# 123456789g 123456789g 123456789g    123456789h 123456789h 123456789h    123456789i 123456789i 123456789i
