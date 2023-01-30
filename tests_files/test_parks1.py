import pytest

from Constants import Constants
from _defaults import default_test_puzzle
from puzzles import *
from solving import Solving

# from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# from techniques.LockedCandidatesPointing import LockedCandidatesPointing

EXPLICITLY = "EXPLICITLY"


# @pytest.mark.parametrize("puzzle_string, constructor, techniques", [


   
#     ('parks1_001', Parks1, Solving.parks1_techniques()),
#     ('parks1_002', Parks1, Solving.parks1_techniques()),
#     ('parks1_003', Parks1, Solving.parks1_techniques()),
#     ('parks1_006', Parks1, Solving.parks1_techniques()),
#     ('parks1_007', Parks1, Solving.parks1_techniques()),
#     ('parks1_008', Parks1, Solving.parks1_techniques()),
#     ('parks1_beach_001', Parks1, Solving.parks1_techniques()),
#     ('parks1_beach_002', Parks1, Solving.parks1_techniques()),
#     ('parks1_beach_003', Parks1, Solving.parks1_techniques()),
#     ('parks1_beach_004', Parks1, Solving.parks1_techniques()),
#     ('parks1_maui_001', Parks1, Solving.parks1_techniques()),
#     ('parks1_spring_001', Parks1, Solving.parks1_techniques()),
#     ('parks1_spring_002', Parks1, Solving.parks1_techniques()),
#     ('parks1_spring_003', Parks1, Solving.parks1_techniques()),
#     ('parks1_spring_004', Parks1, Solving.parks1_techniques()),
#     ('parks1_spring_005', Parks1, Solving.parks1_techniques()),
#     ('parks1_spring_006', Parks1, Solving.parks1_techniques()),
#     ('parks1_spring_007', Parks1, Solving.parks1_techniques()),
#     ('parks1_spring_008', Parks1, Solving.parks1_techniques()),
#
#
#     ("parks1_011", Parks1, Solving.parks1_techniques()),
#     ("parks1_012", Parks1, Solving.parks1_techniques()),
#     ("parks1_013", Parks1, Solving.parks1_techniques()),
#     ("parks1_014", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_009", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_010", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_011", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_012", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_013", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_014", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_015", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_017", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_018", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_019", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_020", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_021", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_022", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_023", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_024", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_025", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_026", Parks1, Solving.parks1_techniques()),
#     ('parks1_005', Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_028", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_029", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_030", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_031", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_032", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_033", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_034", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_039", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_045", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_047", Parks1, Solving.parks1_techniques()),
#     ("parks1_spring_062", Parks1, Solving.parks1_techniques()),
#     ("parks1_winter_049", Parks1, Solving.parks1_techniques()),
#
#
# ])
# def test_default_puzzle(puzzle_string, constructor, techniques):
#     if "\n" in puzzle_string:
#         pytest.skip(puzzle_string)
#     result = getattr(Constants, puzzle_string)
#     assert default_test_puzzle(result(), constructor, techniques)



# @staticmethod
# def parks1_001():
#     return f"""
#     001.parks1
#     5
#     10a 10a 10b 10e 10d
#     10a 10a 10b 10b 10d
#     10c 10a 10b 10d 10d
#     10c 10c 10c 10d 10d
#     10c 10c 10c 10c 10c
#     """

# @staticmethod
# def parks1_002():
#     return f"""
#     002.parks1
#     5
#     10a 10a 10a 10a 10a
#     10b 10a 10a 10a 10e
#     10a 10a 10a 10d 10e
#     10a 10c 10d 10d 10e
#     10a 10c 10d 10d 10d
#     """

# @staticmethod
# def parks1_003():
#     return f"""
#     003.parks1
#     5
#     10a 10a 10d 10d 10d
#     10a 10a 10d 10d 10d
#     10b 10d 10d 10d 10d
#     10b 10c 10c 10e 10e
#     10b 10b 10e 10e 10e
#     """

# @staticmethod
# def parks1_004():
#     return f"""
#     004.parks1
#     5
#     10a 10a 10e 10e 10e
#     10a 10a 10b 10e 10e
#     10b 10b 10b 10d 10e
#     10b 10c 10c 10d 10e
#     10b 10c 10d 10d 10e
#     """

# @staticmethod
# def parks1_005():
#     return f"""
#     005.parks1
#     5
#     10a 10a 10a 10b 10b
#     10a 10b 10b 10b 10e
#     10a 10c 10c 10e 10e
#     10c 10c 10e 10e 10d
#     10c 10d 10d 10d 10d
#     """

# @staticmethod
# def parks1_006():
#     return f"""
#     006.parks1
#     5
#     10a 10a 10a 10d 10d
#     10a 10b 10d 10d 10d
#     10b 10b 10d 10d 10d
#     10c 10c 10d 10e 10e
#     10c 10e 10e 10e 10e
#     """

# @staticmethod
# def parks1_007():
#     return f"""
#     007.parks1
#     6
#     10a 10a 10f 10f 10f 10f
#     10a 10a 10f 10f 10f 10f
#     10a 10a 10d 10d 10f 10f
#     10a 10d 10d 10d 10e 10f
#     10b 10d 10d 10d 10e 10f
#     10b 10b 10b 10c 10c 10c
#     """

# @staticmethod
# def parks1_008():
#     return f"""
#     008.parks1
#     6
#     10a 10a 10b 10d 10d 10d
#     10a 10a 10d 10d 10d 10d
#     10a 10a 10c 10c 10d 10f
#     10a 10f 10f 10f 10f 10f
#     10a 10f 10f 10f 10e 10f
#     10f 10f 10f 10f 10f 10f
#     """

# @staticmethod
# def parks1_009():
#     return f"""
#     009.parks1
#     6
#     10a 10b 10b 10b 10f 10f
#     10a 10b 10b 10b 10f 10f
#     10a 10a 10a 10f 10f 10f
#     10a 10c 10d 10f 10f 10f
#     10c 10c 10d 10f 10f 10e
#     10c 10c 10f 10f 10e 10e
#     """

# @staticmethod
# def parks1_010():
#     return f"""
#     010.parks1
#     6
#     10a 10a 10c 10c 10c 10c
#     10a 10c 10c 10f 10d 10c
#     10a 10c 10c 10f 10d 10d
#     10b 10b 10f 10f 10e 10d
#     10b 10f 10f 10e 10e 10d
#     10b 10b 10b 10e 10e 10e
#     """

# @staticmethod
# def parks1_011():
#     return f"""
#     011.parks1
#     6
#     10c 10c 10c 10e 10e 10e
#     10c 10c 10c 10e 10e 10e
#     10c 10d 10d 10f 10e 10e
#     10f 10f 10f 10f 10f 10f
#     10f 10f 10a 10a 10f 10f
#     10a 10a 10a 10b 10b 10f
#     """

# @staticmethod
# def parks1_012():
#     return f"""
#     012.parks1
#     6
#     10a 10a 10a 10a 10e 10e
#     10a 10a 10b 10e 10e 10e
#     10a 10a 10f 10f 10f 10e
#     10a 10f 10f 10c 10c 10d
#     10f 10f 10f 10f 10c 10c
#     10f 10f 10f 10c 10c 10c
#     """

# @staticmethod
# def parks1_013():
#     return f"""
#     013.parks1
#     6
#     10b 10c 10c 10c 10d 10a
#     10b 10c 10a 10c 10d 10a
#     10b 10a 10a 10a 10a 10a
#     10a 10a 10a 10a 10a 10a
#     10e 10f 10f 10a 10f 10f
#     10e 10e 10f 10f 10f 10f
#     """

# @staticmethod
# def parks1_014():
#     return f"""
#     014.parks1
#     7
#     10g 10g 10g 10g 10b 10b 10b
#     10g 10g 10e 10g 10c 10c 10b
#     10g 10f 10e 10d 10d 10c 10b
#     10g 10f 10e 10e 10d 10c 10c
#     10g 10f 10f 10e 10d 10a 10a
#     10g 10g 10a 10a 10a 10a 10a
#     10a 10a 10a 10a 10a 10a 10a
#     """

# @staticmethod
# def parks1_beach_001():
#     return f"""
#     beach_001.parks1
#     5
#     10a 10a 10a 10a 10a
#     10b 10a 10a 10a 10a
#     10b 10c 10d 10e 10e
#     10c 10c 10c 10e 10e
#     10c 10c 10c 10e 10e
#     """

# @staticmethod
# def parks1_beach_002():
#     return f"""
#     beach_002.parks1
#     5
#     10a 10a 10a 10c 10c
#     10a 10a 10c 10d 10c
#     10b 10a 10c 10c 10c
#     10b 10b 10c 10e 10e
#     10b 10b 10b 10b 10e
#     """

# @staticmethod
# def parks1_beach_003():
#     return f"""
#     beach_003.parks1
#     5
#     10a 10d 10d 10d 10e
#     10a 10d 10d 10d 10e
#     10a 10a 10d 10d 10e
#     10a 10a 10c 10c 10e
#     10b 10c 10c 10c 10c
#     """

# @staticmethod
# def parks1_beach_004():
#     return f"""
#     beach_004.parks1
#     5
#     10a 10a 10a 10a 10a
#     10a 10a 10a 10e 10e
#     10a 10c 10c 10c 10e
#     10b 10c 10c 10d 10c
#     10b 10b 10c 10c 10c
#     """

# @staticmethod
# def parks1_maui_001():
#     return f"""
#     maui_001.parks1
#     12
#     10a 10a 10a 10a 10a 10a 10a 10i 10i 10i 10i 10i
#     10a 10a 10a 10a 10a 10a 10a 10a 10a 10i 10i 10i
#     10a 10b 10b 10d 10d 10a 10a 10a 10a 10i 10i 10l
#     10c 10e 10e 10d 10d 10h 10a 10h 10i 10i 10i 10l
#     10c 10d 10e 10d 10d 10h 10h 10h 10h 10i 10i 10l
#     10c 10d 10d 10d 10d 10h 10h 10h 10h 10i 10i 10l
#     10f 10f 10f 10f 10h 10h 10h 10h 10k 10k 10k 10l
#     10f 10f 10f 10f 10g 10g 10h 10h 10k 10k 10k 10k
#     10f 10f 10f 10f 10g 10g 10j 10j 10k 10k 10k 10k
#     10f 10f 10f 10f 10j 10j 10j 10j 10k 10k 10k 10k
#     10f 10f 10f 10j 10j 10j 10j 10j 10k 10k 10k 10k
#     10f 10f 10f 10j 10j 10j 10k 10k 10k 10k 10k 10k
#     """

# @staticmethod
# def parks1_spring_001():
#     return f"""
#     spring_001.parks1
#     5
#     10a 10e 10e 10e 10e
#     10a 10a 10e 10e 10e
#     10a 10b 10c 10e 10e
#     10a 10c 10c 10c 10d
#     10c 10c 10c 10d 10d
#     """

# @staticmethod
# def parks1_spring_002():
#     return f"""
#     spring_002.parks1
#     5
#     10a 10a 10a 10a 10a
#     10b 10a 10a 10a 10a
#     10b 10b 10a 10d 10d
#     10b 10c 10c 10d 10e
#     10b 10b 10c 10c 10e
#     """

# @staticmethod
# def parks1_spring_003():
#     return f"""
#     spring_003.parks1
#     5
#     10a 10a 10b 10d 10d
#     10a 10b 10b 10c 10c
#     10b 10b 10b 10c 10c
#     10b 10b 10b 10c 10e
#     10b 10c 10c 10c 10e
#     """

# @staticmethod
# def parks1_spring_004():
#     return f"""
#     spring_004.parks1
#     5
#     10a 10a 10a 10d 10d
#     10a 10a 10a 10d 10d
#     10a 10a 10a 10d 10e
#     10b 10b 10b 10d 10e
#     10b 10b 10c 10c 10c
#     """

# @staticmethod
# def parks1_spring_005():
#     return f"""
#     spring_005.parks1
#     5
#     10a 10a 10d 10d 10e
#     10a 10a 10a 10e 10e
#     10a 10a 10a 10e 10e
#     10a 10b 10e 10e 10e
#     10b 10b 10c 10c 10e
#     """

# @staticmethod
# def parks1_spring_006():
#     return f"""
#     spring_006.parks1
#     5
#     10a 10a 10a 10a 10a
#     10b 10a 10a 10a 10e
#     10b 10c 10a 10a 10a
#     10b 10c 10c 10d 10a
#     10c 10c 10c 10d 10a
#     """

# @staticmethod
# def parks1_spring_007():
#     return f"""
#     spring_007.parks1
#     5
#     10a 10a 10a 10d 10d
#     10a 10a 10c 10d 10d
#     10a 10a 10c 10d 10d
#     10a 10a 10c 10d 10e
#     10b 10b 10b 10b 10b
#     """

# @staticmethod
# def parks1_spring_008():
#     return f"""
#     spring_008.parks1
#     5
#     10a 10a 10b 10b 10b
#     10a 10a 10b 10b 10b
#     10b 10b 10b 10d 10e
#     10b 10c 10e 10e 10e
#     10c 10c 10e 10e 10e
#     """

# @staticmethod
# def parks1_spring_009():
#     return f"""
#     spring_009.parks1
#     5
#     10a 10c 10c 10c 10c
#     10a 10c 10c 10c 10c
#     10a 10c 10d 10d 10d
#     10a 10a 10d 10e 10e
#     10b 10b 10b 10b 10e
#     """

# @staticmethod
# def parks1_spring_010():
#     return f"""
#     spring_010.parks1
#     5
#     10a 10a 10d 10d 10d
#     10b 10c 10d 10d 10d
#     10b 10c 10c 10d 10e
#     10b 10c 10e 10e 10e
#     10b 10e 10e 10e 10e
#     """

# @staticmethod
# def parks1_spring_011():
#     return f"""
#     spring_011.parks1
#     5
#     10a 10e 10e 10e 10e
#     10a 10e 10e 10e 10e
#     10a 10b 10b 10d 10e
#     10b 10b 10c 10d 10d
#     10b 10b 10c 10d 10d
#     """

# @staticmethod
# def parks1_spring_012():
#     return f"""
#     spring_012.parks1
#     5
#     10a 10a 10c 10c 10c
#     10a 10b 10c 10d 10e
#     10a 10b 10c 10d 10e
#     10a 10d 10d 10d 10e
#     10d 10d 10d 10d 10e
#     """

# @staticmethod
# def parks1_spring_013():
#     return f"""
#     spring_013.parks1
#     5
#     10a 10a 10d 10d 10e
#     10a 10a 10b 10d 10e
#     10b 10b 10b 10d 10d
#     10b 10b 10b 10b 10b
#     10c 10c 10c 10c 10b
#     """

# @staticmethod
# def parks1_spring_014():
#     return f"""
#     spring_014.parks1
#     5
#     10a 10c 10c 10c 10c
#     10a 10c 10c 10c 10c
#     10b 10b 10c 10d 10e
#     10b 10b 10d 10d 10e
#     10b 10b 10b 10b 10e
#     """

# @staticmethod
# def parks1_spring_015():
#     return f"""
#     spring_015.parks1
#     5
#     10a 10a 10d 10e 10e
#     10a 10a 10d 10e 10e
#     10a 10a 10b 10c 10c
#     10b 10b 10b 10c 10c
#     10b 10c 10c 10c 10c
#     """

# @staticmethod
# def parks1_spring_016():
#     return f"""
#     spring_016.parks1
#     5
#     10a 10a 10a 10b 10b
#     10a 10a 10a 10b 10b
#     10c 10d 10d 10d 10c
#     10c 10c 10c 10c 10c
#     10e 10c 10c 10c 10c
#     """

# @staticmethod
# def parks1_spring_017():
#     return f"""
#     spring_017.parks1
#     5
#     10a 10d 10d 10d 10d
#     10a 10d 10d 10d 10e
#     10a 10a 10b 10e 10e
#     10b 10b 10b 10e 10e
#     10c 10c 10c 10e 10e
#     """

# @staticmethod
# def parks1_spring_018():
#     return f"""
#     spring_018.parks1
#     5
#     10a 10d 10d 10d 10e
#     10a 10c 10c 10e 10e
#     10a 10a 10c 10c 10e
#     10b 10a 10b 10e 10e
#     10b 10b 10b 10b 10b
#     """

# @staticmethod
# def parks1_spring_019():
#     return f"""
#     spring_019.parks1
#     5
#     10a 10a 10a 10a 10c
#     10a 10a 10c 10c 10c
#     10a 10a 10c 10e 10e
#     10b 10c 10c 10d 10e
#     10b 10b 10d 10d 10d
#     """

# @staticmethod
# def parks1_spring_020():
#     return f"""
#     spring_020.parks1
#     5
#     10a 10a 10a 10e 10e
#     10a 10a 10e 10e 10e
#     10a 10a 10e 10d 10e
#     10b 10b 10c 10d 10d
#     10b 10b 10c 10d 10d
#     """

# @staticmethod
# def parks1_spring_021():
#     return f"""
#     spring_021.parks1
#     5
#     10a 10a 10a 10d 10e
#     10a 10b 10a 10d 10e
#     10a 10b 10a 10d 10e
#     10b 10b 10c 10e 10e
#     10b 10c 10c 10c 10c
#     """

# @staticmethod
# def parks1_spring_022():
#     return f"""
#     spring_022.parks1
#     5
#     10b 10d 10d 10e 10e
#     10b 10b 10d 10e 10e
#     10a 10b 10c 10c 10e
#     10a 10b 10c 10c 10c
#     10a 10a 10a 10a 10c
#     """

# @staticmethod
# def parks1_spring_023():
#     return f"""
#     spring_023.parks1
#     5
#     10a 10d 10d 10d 10d
#     10a 10d 10d 10d 10d
#     10a 10a 10c 10e 10e
#     10b 10c 10c 10e 10e
#     10b 10b 10c 10e 10e
#     """

# @staticmethod
# def parks1_spring_024():
#     return f"""
#     spring_024.parks1
#     5
#     10a 10a 10a 10e 10e
#     10a 10a 10a 10e 10e
#     10a 10a 10a 10d 10e
#     10b 10c 10c 10d 10e
#     10b 10b 10c 10d 10d
#     """

# @staticmethod
# def parks1_spring_025():
#     return f"""
#     spring_025.parks1
#     5
#     10c 10c 10e 10e 10e
#     10b 10c 10c 10c 10e
#     10b 10b 10d 10d 10e
#     10a 10b 10b 10d 10d
#     10a 10a 10a 10a 10d
#     """

# @staticmethod
# def parks1_spring_026():
#     return f"""
#     spring_026.parks1
#     5
#     10a 10a 10a 10a 10e
#     10a 10b 10b 10e 10e
#     10a 10b 10b 10d 10d
#     10b 10b 10b 10c 10d
#     10b 10c 10c 10c 10c
#     """

# @staticmethod
# def parks1_spring_027():
#     return f"""
#     spring_027.parks1
#     5
#     10a 10a 10a 10d 10d
#     10b 10b 10a 10d 10d
#     10c 10b 10c 10d 10e
#     10c 10b 10c 10d 10e
#     10c 10c 10c 10e 10e
#     """

# @staticmethod
# def parks1_spring_028():
#     return f"""
#     spring_028.parks1
#     5
#     10a 10a 10b 10b 10d
#     10a 10b 10b 10d 10d
#     10a 10b 10e 10e 10e
#     10c 10b 10b 10c 10e
#     10c 10c 10c 10c 10e
#     """

# @staticmethod
# def parks1_spring_029():
#     return f"""
#     spring_029.parks1
#     5
#     10a 10a 10a 10a 10d
#     10a 10c 10c 10d 10d
#     10a 10c 10d 10d 10e
#     10b 10c 10c 10d 10e
#     10b 10b 10b 10e 10e
#     """

# @staticmethod
# def parks1_spring_030():
#     return f"""
#     spring_030.parks1
#     6
#     10a 10a 10a 10a 10f 10f
#     10a 10a 10a 10d 10f 10f
#     10a 10a 10a 10e 10e 10f
#     10a 10a 10a 10e 10e 10e
#     10b 10e 10e 10e 10e 10e
#     10c 10c 10c 10c 10c 10c
#     """

# @staticmethod
# def parks1_spring_031():
#     return f"""
#     spring_031.parks1
#     6
#     10a 10a 10a 10e 10e 10e
#     10a 10a 10a 10e 10f 10e
#     10b 10b 10b 10d 10f 10f
#     10c 10b 10c 10d 10d 10d
#     10c 10c 10c 10c 10c 10d
#     10c 10c 10c 10c 10c 10d
#     """

# @staticmethod
# def parks1_spring_032():
#     return f"""
#     spring_032.parks1
#     6
#     10a 10a 10a 10a 10e 10e
#     10b 10b 10b 10a 10a 10e
#     10b 10b 10c 10c 10e 10e
#     10b 10b 10c 10c 10e 10f
#     10c 10c 10c 10d 10d 10f
#     10c 10d 10d 10d 10f 10f
#     """

# @staticmethod
# def parks1_spring_033():
#     return f"""
#     spring_033.parks1
#     6
#     10a 10a 10a 10e 10e 10e
#     10a 10b 10a 10a 10e 10e
#     10a 10b 10a 10e 10e 10f
#     10b 10b 10c 10c 10e 10f
#     10b 10c 10c 10d 10d 10f
#     10b 10d 10d 10d 10f 10f
#     """

# @staticmethod
# def parks1_spring_034():
#     return f"""
#     spring_034.parks1
#     5
#     10c 10c 10e 10e 10e
#     10b 10c 10c 10c 10e
#     10b 10b 10d 10d 10e
#     10a 10b 10b 10d 10d
#     10a 10a 10a 10a 10d
#     """

# @staticmethod
# def parks1_spring_039():
#     return f"""
#     spring_039.parks1
#     7
#     10a 10b 10b 10e 10e 10e 10e
#     10a 10b 10c 10e 10e 10e 10e
#     10c 10c 10c 10e 10e 10e 10f
#     10c 10c 10c 10d 10g 10g 10f
#     10c 10d 10c 10d 10d 10g 10f
#     10d 10d 10d 10d 10d 10d 10f
#     10d 10d 10d 10d 10f 10f 10f
#     """

# @staticmethod
# def parks1_spring_045():
#     return f"""
#     spring_045.parks1
#     7
#     10a 10a 10a 10a 10a 10f 10f
#     10a 10f 10f 10f 10f 10f 10g
#     10a 10a 10e 10e 10e 10f 10g
#     10a 10a 10e 10d 10e 10g 10g
#     10c 10c 10c 10d 10d 10g 10g
#     10b 10b 10c 10c 10c 10g 10g
#     10b 10b 10g 10g 10g 10g 10g
#     """

# @staticmethod
# def parks1_spring_046():
#     return f"""
#     spring_046.parks1
#     7
#     10a 10d 10d 10d 10d 10d 10d
#     10a 10a 10a 10d 10e 10e 10d
#     10b 10b 10d 10d 10e 10d 10d
#     10b 10d 10d 10f 10f 10d 10d
#     10d 10c 10d 10d 10g 10g 10d
#     10d 10c 10c 10d 10g 10g 10d
#     10d 10d 10d 10d 10d 10g 10g
#     """

# @staticmethod
# def parks1_spring_047():
#     return f"""
#     spring_047.parks1
#     7
#     10a 10a 10a 10a 10a 10f 10f
#     10a 10f 10f 10f 10f 10f 10g
#     10a 10a 10e 10e 10e 10f 10g
#     10a 10a 10e 10d 10e 10g 10g
#     10c 10c 10c 10d 10d 10g 10g
#     10b 10b 10c 10c 10c 10g 10g
#     10b 10b 10g 10g 10g 10g 10g
#     """

# @staticmethod
# def parks1_spring_051():
#     return f"""
#     spring_051.parks1
#     8
#     10a 10a 10a 10b 10b 10b 10e 10e
#     10a 10b 10a 10b 10b 10b 10e 10e
#     10b 10b 10b 10b 10b 10e 10e 10h
#     10b 10b 10b 10b 10b 10b 10h 10h
#     10c 10c 10c 10b 10b 10f 10h 10h
#     10c 10c 10c 10b 10f 10f 10g 10g
#     10d 10c 10c 10d 10d 10f 10f 10g
#     10d 10d 10d 10d 10f 10f 10f 10f
#     """

# @staticmethod
# def parks1_spring_062():
#     return f"""
#     spring_062.parks1
#     8
#     10a 10a 10c 10c 10h 10h 10h 10h
#     10a 10a 10a 10a 10h 10h 10h 10h
#     10a 10a 10b 10a 10h 10h 10h 10h
#     10d 10d 10e 10e 10e 10h 10h 10h
#     10d 10d 10e 10g 10g 10g 10h 10h
#     10d 10d 10e 10f 10f 10g 10f 10f
#     10d 10d 10d 10f 10f 10f 10f 10f
#     10d 10d 10d 10d 10f 10f 10f 10f
#     """

# @staticmethod
# def parks1_winter_037():
#     return f"""
#     winter_037.parks1
#     7
#     10a 10b 10c 10c 10c 10d 10d
#     10a 10b 10a 10a 10c 10d 10d
#     10a 10a 10a 10a 10a 10d 10g
#     10a 10e 10e 10e 10g 10d 10g
#     10e 10e 10g 10g 10g 10g 10g
#     10e 10e 10g 10e 10f 10f 10g
#     10e 10e 10e 10e 10e 10f 10g
#     """

# @staticmethod
# def parks1_winter_038():
#     return f"""
#     winter_038.parks1
#     7
#     10a 10a 10a 10a 10a 10a 10e
#     10a 10b 10b 10d 10d 10e 10e
#     10b 10b 10b 10f 10d 10f 10f
#     10b 10b 10b 10f 10d 10f 10g
#     10c 10c 10b 10f 10f 10f 10g
#     10c 10b 10b 10b 10b 10g 10g
#     10c 10b 10b 10b 10b 10b 10g
#     """

# @staticmethod
# def parks1_winter_039():
#     return f"""
#     winter_039.parks1
#     7
#     10a 10e 10e 10e 10f 10g 10g
#     10a 10a 10e 10e 10f 10g 10g
#     10a 10a 10c 10e 10f 10f 10g
#     10a 10a 10c 10c 10c 10d 10d
#     10a 10b 10c 10c 10c 10c 10c
#     10b 10b 10c 10c 10c 10c 10c
#     10b 10b 10c 10c 10c 10c 10c
#     """

# @staticmethod
# def parks1_winter_040():
#     return f"""
#     winter_040.parks1
#     7
#     10a 10a 10b 10b 10b 10b 10b
#     10a 10a 10a 10a 10a 10b 10a
#     10a 10a 10d 10d 10a 10a 10a
#     10a 10d 10d 10e 10g 10g 10a
#     10a 10a 10d 10e 10g 10g 10g
#     10c 10c 10e 10e 10f 10f 10g
#     10c 10c 10f 10f 10f 10g 10g
#     """

# @staticmethod
# def parks1_winter_041():
#     return f"""
#     winter_041.parks1
#     7
#     10g 10g 10g 10d 10a 10a 10a
#     10g 10c 10c 10d 10d 10d 10a
#     10b 10b 10c 10e 10d 10d 10a
#     10b 10b 10e 10e 10a 10a 10a
#     10a 10b 10a 10e 10a 10a 10h
#     10a 10a 10a 10a 10a 10h 10h
#     10a 10h 10h 10h 10h 10h 10h
#     """

# @staticmethod
# def parks1_winter_042():
#     return f"""
#     winter_042.parks1
#     7
#     10a 10d 10d 10d 10e 10e 10e
#     10a 10a 10d 10d 10d 10d 10e
#     10a 10a 10d 10d 10d 10d 10f
#     10a 10c 10c 10c 10d 10d 10f
#     10a 10c 10c 10c 10f 10f 10f
#     10b 10c 10c 10c 10f 10f 10f
#     10b 10b 10b 10c 10f 10g 10g
#     """

# @staticmethod
# def parks1_winter_044():
#     return f"""
#     winter_044.parks1
#     7
#     10a 10a 10c 10c 10e 10e 10e
#     10a 10c 10c 10c 10d 10e 10e
#     10a 10c 10c 10c 10d 10d 10d
#     10c 10c 10c 10c 10c 10g 10g
#     10b 10c 10c 10c 10c 10c 10g
#     10b 10c 10b 10c 10c 10g 10g
#     10b 10b 10b 10h 10h 10h 10h
#     """

# @staticmethod
# def parks1_winter_045():
#     return f"""
#     winter_045.parks1
#     7
#     10a 10a 10a 10e 10e 10f 10f
#     10a 10e 10e 10e 10f 10f 10f
#     10a 10b 10b 10c 10f 10g 10g
#     10b 10b 10b 10c 10f 10g 10g
#     10c 10c 10c 10c 10f 10g 10g
#     10c 10d 10d 10d 10d 10d 10g
#     10c 10d 10d 10d 10d 10d 10g
#     """

# @staticmethod
# def parks1_winter_046():
#     return f"""
#     winter_046.parks1
#     8
#     10a 10a 10a 10a 10g 10g 10g 10g
#     10b 10a 10a 10a 10g 10g 10g 10h
#     10b 10c 10c 10a 10g 10g 10g 10h
#     10c 10c 10c 10f 10f 10f 10f 10h
#     10c 10c 10d 10d 10f 10f 10f 10h
#     10e 10e 10e 10e 10f 10f 10f 10h
#     10e 10e 10e 10e 10f 10f 10f 10h
#     10e 10e 10e 10e 10e 10e 10f 10h
#     """

# @staticmethod
# def parks1_winter_047():
#     return f"""
#     winter_047.parks1
#     8
#     10a 10a 10a 10a 10e 10e 10h 10h
#     10b 10a 10a 10e 10e 10e 10g 10h
#     10b 10a 10e 10e 10e 10e 10g 10g
#     10b 10a 10e 10e 10e 10g 10g 10g
#     10a 10a 10e 10e 10e 10f 10f 10f
#     10a 10a 10e 10e 10e 10f 10f 10f
#     10c 10c 10c 10e 10e 10f 10f 10f
#     10d 10d 10d 10d 10f 10f 10f 10f
#     """

# @staticmethod
# def parks1_winter_048():
#     return f"""
#     winter_048.parks1
#     8
#     10a 10a 10a 10a 10a 10a 10c 10c
#     10a 10d 10b 10b 10a 10a 10a 10c
#     10a 10d 10d 10b 10a 10a 10a 10h
#     10d 10d 10e 10g 10g 10g 10g 10h
#     10d 10d 10e 10f 10f 10f 10g 10h
#     10e 10d 10e 10f 10f 10f 10f 10f
#     10e 10e 10e 10f 10f 10f 10f 10f
#     10e 10e 10f 10f 10f 10f 10f 10f
#     """

# @staticmethod
# def parks1_winter_049():
#     return f"""
#     winter_049.parks1
#     8
#     10a 10d 10d 10e 10e 10f 10h 10h
#     10a 10d 10d 10d 10f 10f 10h 10h
#     10a 10a 10d 10f 10f 10f 10h 10h
#     10a 10a 10f 10f 10f 10g 10h 10h
#     10a 10a 10a 10a 10f 10g 10g 10g
#     10a 10b 10c 10g 10g 10g 10g 10g
#     10a 10c 10c 10g 10g 10g 10g 10g
#     10c 10c 10c 10c 10g 10g 10g 10g
#     """

# @staticmethod
# def parks1_winter_050():
#     return f"""
#     winter_050.parks1
#     8
#     10a 10a 10d 10d 10h 10h 10h 10h
#     10a 10b 10d 10d 10h 10h 10h 10h
#     10a 10b 10d 10d 10h 10h 10h 10h
#     10a 10b 10d 10d 10h 10h 10g 10h
#     10b 10b 10b 10d 10d 10d 10g 10g
#     10c 10c 10c 10f 10f 10f 10f 10g
#     10c 10c 10c 10f 10f 10f 10f 10g
#     10e 10e 10e 10e 10f 10f 10g 10g
#     """

# @staticmethod
# def parks1_winter_051():
#     return f"""
#     winter_051.parks1
#     8
#     10a 10a 10a 10b 10b 10b 10g 10g
#     10a 10b 10a 10b 10b 10b 10g 10g
#     10b 10b 10b 10b 10b 10g 10g 10h
#     10b 10b 10b 10b 10b 10b 10h 10h
#     10c 10c 10c 10b 10b 10e 10h 10h
#     10c 10c 10c 10b 10e 10e 10f 10f
#     10d 10c 10c 10d 10d 10e 10e 10f
#     10d 10d 10d 10d 10e 10e 10e 10e
#     """


