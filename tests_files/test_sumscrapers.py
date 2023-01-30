import pytest

from Constants import Constants
from _defaults import default_test_puzzle
from puzzles import *
from solving import Solving

# from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# from techniques.LockedCandidatesPointing import LockedCandidatesPointing

EXPLICITLY = "EXPLICITLY"


# @pytest.mark.parametrize("puzzle_string, constructor, techniques", [
#
#     ("sumscrapers_008", Sumscrapers, Solving.sumscrapers_techniques()),
#     ("sumscrapers_001", Sumscrapers, Solving.sumscrapers_techniques()),
#     ("sumscrapers_002", Sumscrapers, Solving.sumscrapers_techniques()),
#     ("sumscrapers_003", Sumscrapers, Solving.sumscrapers_techniques()),
#     ("sumscrapers_004", Sumscrapers, Solving.sumscrapers_techniques()),
#     ("sumscrapers_005", Sumscrapers, Solving.sumscrapers_techniques()),
#
# ])
# def test_default_puzzle(puzzle_string, constructor, techniques):
#     if "\n" in puzzle_string:
#         pytest.skip(puzzle_string)
#     result = getattr(Constants, puzzle_string)
#     assert default_test_puzzle(result(), constructor, techniques)


# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_001():
#     return f"""
#     001.sumscrapers
#     4
#     1234 1234 1234 1234 04 10
#     1234 1234 1234 1234 07 04
#     1234 1234 1234 1234 06 07
#     1234 1234 1234 1234 05 09
#     04   07   06   05   $$ $$
#     10   04   07   09   $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_002():
#     return f"""
#     002.sumscrapers
#     4
#     1234 1234 1234 1234 07 06
#     1234 1234 1234 1234 05 07
#     1234 1234 1234 1234 04 08
#     1234 1234 1234 1234 09 04
#     07 05 04 09 $$ $$
#     06 07 08 04 $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_003():
#     return f"""
#     003.sumscrapers
#     4
#     1234 1234 1234 1234 07 05
#     1234 1234 1234 1234 05 07
#     1234 1234 1234 1234 09 04
#     1234 1234 1234 1234 04 09
#     07 06 ?? 08  $$ $$
#     ?? 08 07 06 $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_004():
#     return f"""
#     004.sumscrapers
#     4
#     1234 1234 1234 1234 06 ??
#     1234 1234 1234 1234 04 08
#     1234 1234 1234 1234 07 04
#     1234 1234 1234 1234 08 06
#     06 04 08 07 $$ $$
#     08 07 04 ?? $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_005():
#     return f"""
#     005.sumscrapers
#     4
#     1234 1234 1234 1234 04 07
#     1234 1234 1234 1234 ?? ??
#     1234 1234 1234 1234 07 04
#     1234 1234 1234 1234 09 05
#     04 06 08 ?? $$ $$
#     09 ?? 04 05 $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_006():
#     return f"""
#     006.sumscrapers
#     4
#      1234 1234 1234 1234 04 08
#      1234 1234 1234 1234 ?? 04
#      1234 1234 1234 1234 05 07
#      1234 1234 1234 1234 ?? 06
#      04 09 07 ?? $$ $$
#      ?? ?? ?? ?? $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_007():
#     return f"""
#     007.sumscrapers
#     4
#       1234 1234
#      1234 1234 1234 1234 04 ??
#      1234 1234 1234 1234 ?? ??
#      1234 1234 1234 1234 07 ??
#      1234 1234 1234 1234 09 04
#      ?? 09 05 ?? $$ $$
#      ?? 05 ?? ?? $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_008():
#     return f"""
#     008.sumscrapers
#     4
#      1234 1234 1234 1234 ?? 06
#      1234 1234 1234 1234 ?? 07
#      1234 1234 1234 1234 ?? ??
#      1234 1234 1234 1234 ?? ??
#      07 ?? ?? ?? $$ $$
#      ?? 04 ?? 05 $$ $$
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_010():
#     return f"""
#     010.sumscrapers
#     5
#     .. 09 ?? 08 05 ?? ..
#     09 .. 01 .. .. .. ??
#     08 .. .. .. .. .. ??
#     07 .. .. .. .. .. 12
#     ?? .. .. .. .. .. ??
#     13 .. .. .. .. .. ??
#     .. ?? 12 ?? 14 05 ..
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_011():
#     return f"""
#     011.sumscrapers
#     5
#     .. 09 ?? 14 ?? 12 ..
#     ?? .. .. .. .. .. ??
#     ?? .. .. .. .. .. 09
#     ?? .. .. .. .. .. ??
#     ?? .. .. .. .. .. 11
#     ?? .. .. .. .. .. ??
#     .. 10 ?? ?? 09 ?? ..
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_012():
#     return f"""
#     012.sumscrapers
#     5
#     .. ?? ?? 05 ?? 07 ..
#     ?? .. .. .. .. .. 11
#     ?? .. .. .. .. .. ??
#     09 .. .. .. .. .. ??
#     ?? .. .. .. .. .. ??
#     ?? .. .. .. .. .. 12
#     .. ?? ?? 10 ?? ?? ..
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_017():
#     return f"""
#     017.sumscrapers
#     6
#     .. ?? ?? ?? 06 17 ?? ..
#     11 .. .. .. .. .. .. ??
#     10 .. .. .. .. .. .. ??
#     ?? .. .. .. .. .. .. ??
#     18 .. .. .. .. .. .. ??
#     13 .. .. .. .. .. .. ??
#     ?? .. .. .. .. .. .. ??
#     .. 11 14 ?? 15 ?? 12 ..
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_018():
#     return f"""
#     018.sumscrapers
#     7
#     .. 13 13 20 11 ?? 18 09 ..
#     ?? 01 .. .. .. .. .. .. 14
#     ?? .. .. .. .. .. .. .. 07
#     07 .. .. .. .. .. .. .. 13
#     ?? 03 .. .. .. .. .. .. 12
#     13 .. .. .. .. .. .. .. 17
#     ?? .. .. .. .. 02 .. .. 10
#     12 .. .. .. .. .. .. .. 17
#     .. ?? 10 07 18 13 ?? 22 ..
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_019():
#     return f"""
#     019.sumscrapers
#     7
#     .. 13 ?? 10 20 ?? 12 ?? ..
#     13 .. .. 03 .. .. .. .. 16
#     14 .. .. .. .. .. .. .. 19
#     20 .. .. .. .. .. .. .. 09
#     07 .. .. 05 .. .. .. .. ??
#     22 .. .. .. .. .. 06 .. 07
#     13 .. .. .. .. .. .. .. 18
#     ?? .. .. .. .. .. .. .. 13
#     .. 12 21 24 ?? 07 17 13 ..
#     """
#
#
# @pytest.mark.skip("EXPLICITLY")
# def sumscrapers_020():
#     return f"""
#     020.sumscrapers
#     7
#     .. ?? 13 19 07 ?? 18 ?? ..
#     15 .. .. .. .. .. .. .. 15
#     07 .. .. 02 .. .. .. .. 18
#     12 .. .. .. .. 03 .. 02 15
#     13 .. .. .. 03 .. .. .. ??
#     ?? .. 04 .. .. .. .. .. 13
#     16 .. .. .. .. .. .. .. ??
#     16 .. .. .. .. 05 .. .. ??
#     .. ?? ?? ?? ?? ?? 07 17 ..
#     """


# @staticmethod
# def sumscrapers_009():
#     return f"""
#     009.sumscrapers
#     5
#     .. 08 ?? ?? 05 14 ..
#     12 .. .. .. .. .. ??
#     05 .. .. .. .. .. 10
#     11 .. .. .. .. .. 08
#     ?? .. .. .. .. .. 09
#     09 .. .. .. .. .. 05
#     .. 09 07 ?? 12 05 ..
#     """