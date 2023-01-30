import numpy
import pytest

from Constants import Constants
from Loc import Loc
from _defaults import default_test_puzzle, default_test_explicit_actual_expected
from puzzles import *
from solving import Solving
from tech import tech
from techniques.AlmostLockedCandidatesClaiming import AlmostLockedCandidatesClaiming
from techniques.AvoidableRectangleType1 import AvoidableRectangleType1
from techniques.AvoidableRectangleType2 import AvoidableRectangleType2
from techniques.Bug import Bug
from techniques.CrossHatch import CrossHatch
from techniques.FinnedXWing import FinnedXWing
from techniques.HiddenSingle import HiddenSingle
from techniques.HiddenUniqueRectangle import HiddenUniqueRectangle
from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
from techniques.LockedCandidatesPointing import LockedCandidatesPointing
# from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# from techniques.LockedCandidatesPointing import LockedCandidatesPointing
from techniques.NakedPair import NakedPair
from techniques.ShashimiXWing import ShashimiXWing
from techniques.UniqueRectangleType1 import UniqueRectangleType1
from techniques.UniqueRectangleType2 import UniqueRectangleType2
from techniques.UniqueRectangleType3 import UniqueRectangleType3
from techniques.UniqueRectangleType4 import UniqueRectangleType4
from techniques.WWing import WWing
from techniques.WxyzWing import WxyzWing
from techniques.XyWing import XyWing

EXPLICITLY = "EXPLICITLY"
from colorama import Fore


# @pytest.mark.parametrize("puzzle_string, constructor, techniques", [
#
#
#     ('robot_fences_001', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_002', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_003', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_004', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_005', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_006', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_007', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_008', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_009', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_010', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_011', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_012', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_013', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_014', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_015', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_016', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_017', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_018', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_019', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_020', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_022', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_023', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_025', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_028', RobotFences, Solving.robot_fences_techniques()),
#     ('robot_fences_030', RobotFences, Solving.robot_fences_techniques()),
#
#
# ])
# def test_default_puzzle(puzzle_string, constructor, techniques):
#     if "\n" in puzzle_string:
#         pytest.skip(puzzle_string)
#     result = getattr(Constants, puzzle_string)
#     assert default_test_puzzle(result(), constructor, techniques)




# @staticmethod
# def robot_fences_001():
#     return f"""
#     001.robot_fences
#     4
#     1234a 1234b __3_c 1___c
#     1234a 1___b 1234c __3_e
#     1___a 1234b 1234c 1234e
#     __3_a _2__b 1234d 1234e
#     """

# @staticmethod
# def robot_fences_002():
#     return f"""
#     002.robot_fences
#     4
#     2A 0A 0A 4H
#     4B 0C 1C 0H
#     0D 3D 0F 0H
#     3E 0D 0D 1G
#     """

# @staticmethod
# def robot_fences_003():
#     return f"""
#     003.robot_fences
#     4
#     3A 0A 0A 0A
#     1B 0C 0E 0F
#     0D 3D 0E 1F
#     2D 0E 0E 3F
#     """

# @staticmethod
# def robot_fences_004():
#     return f"""
#     004.robot_fences
#     4
#     0A 0A 3A 1B
#     0C 0C 0C 0C
#     1D 0E 0F 2F
#     0E 2E 1F 3F
#     """

# @staticmethod
# def robot_fences_005():
#     return f"""
#     005.robot_fences
#     5
#     0a 0a 0a 0a 5b
#     0c 5c 0c 2c 0c
#     3d 0d 0d 5f 0h
#     0e 4e 1d 0g 0h
#     2g 1g 0g 4g 0h
#     """

# @staticmethod
# def robot_fences_006():
#     return f"""
#     006.robot_fences
#     5
#     1A 0A 2A 0A 0A
#     0B 5B 0B 3G 0G
#     2B 0B 4C 0G 0G
#     0D 1E 0F 2F 0G
#     3E 0E 0F 0F 1F
#     """

# @staticmethod
# def robot_fences_007():
#     return f"""
#     007.robot_fences
#     5
#     4A 1A 0A 2A 5G
#     0E 0E 5E 0F 0H
#     0B 0B 0E 0F 0I
#     2B 0C 1D 0D 4I
#     5B 0B 0D 0I 3I
#     """

# @staticmethod
# def robot_fences_008():
#     return f"""
#     008.robot_fences
#     5
#     4a 0a 1a 0g 5i
#     0b 0f 2a 0h 0i
#     0b 2f 0a 4h 0j
#     0b 5e 0e 0h 1j
#     0c 0c 0c 1d 2j
#     """

# @staticmethod
# def robot_fences_009():
#     return f"""
#     009.robot_fences
#     5
#     3a 5a 0a 0e 2f
#     2b 0b 0a 5e 0f
#     4b 0c 2a 0e 0g
#     0b 0c 0d 2d 0d
#     5c 0c 0c 0d 4d
#     """

# @staticmethod
# def robot_fences_010():
#     return f"""
#     010.robot_fences
#     5
#     5a 0a 0c 4d 3d
#     1b 0a 3a 0d 0j
#     2h 1h 0h 0j 5j
#     0e 3h 0h 0i 0j
#     0e 0f 2g 0g 0j
#     """

# @staticmethod
# def robot_fences_011():
#     return f"""
#     011.robot_fences
#     5
#     0a 0d 3e 0f 4i
#     0a 0c 0e 2f 0f
#     0a 0c 0e 0f 5f
#     0a 0c 4e 0g 2h
#     5a 0b 0e 3h 0h
#     """

# @staticmethod
# def robot_fences_012():
#     return f"""
#     012.robot_fences
#     5
#     0a 0b 2g 0g 0g
#     0b 5b 0f 4g 0h
#     3b 0c 0e 0e 5h
#     0b 0c 0d 0e 0h
#     4c 1c 0e 0e 2i
#     """

# @staticmethod
# def robot_fences_013():
#     return f"""
#     013.robot_fences
#     5
#     2a 0a 5a 0a 1h
#     3b 0f 0g 2g 0h
#     0b 0b 0g 0g 2h
#     0c 0b 0b 5h 0h
#     4c 0c 3c 0d 0e
#     """

# @staticmethod
# def robot_fences_014():
#     return f"""
#     014.robot_fences
#     5
#     5A 0B 0B 2G 0G
#     0B 0B 0F 0G 4G
#     1C 0D 3H 0H 0H
#     0D 0D 0D 3D 0H
#     2E 0E 4E 0E 0H
#     """

# @staticmethod
# def robot_fences_015():
#     return f"""
#     015.robot_fences
#     5
#     0a 0b 0c 0c 3c
#     0a 2a 0a 0a 0c
#     0d 0d 0f 0f 0h
#     0d 3d 0f 0g 2h
#     2d 0e 4f 3g 5g
#     """

# @staticmethod
# def robot_fences_016():
#     return f"""
#     016.robot_fences
#     5
#     0a 5a 0d 3d 4e
#     0b 0a 0d 0d 0d
#     3b 0a 5f 0g 1h
#     4b 0c 0g 0g 0h
#     0b 0b 4g 0g 0h
#     """

# @staticmethod
# def robot_fences_017():
#     return f"""
#     017.robot_fences
#     5
#     0a 0f 1g 0g 0g
#     0a 3f 0f 5g 0g
#     3a 0a 2e 0e 0h
#     0b 2c 0d 0h 0h
#     0b 0c 3c 0h 4h
#     """

# @staticmethod
# def robot_fences_018():
#     return f"""
#     018.robot_fences
#     5
#     0a 0a 0a 0a 1b
#     0a 3d 0d 4g 0g
#     0c 1d 0e 2e 0f
#     3c 0e 1e 0f 0f
#     2c 0c 0e 0f 0f
#     """

# @staticmethod
# def robot_fences_019():
#     return f"""
#     019.robot_fences
#     5
#     0a 0a 0a 0h 3i
#     0a 5a 0g 1i 0i
#     5b 0b 3g 0g 1j
#     0c 0d 0f 0k 0k
#     1d 0d 5e 0k 4l
#     """

# @staticmethod
# def robot_fences_020():
#     return f"""
#     020.robot_fences
#     5
#     0a 4a 5g 0h 0h
#     0a 0e 0f 0f 0h
#     0a 2f 0f 0f 0i
#     1a 0c 4c 0c 5i
#     4b 0c 0d 0d 3d
#     """

# @staticmethod
# def robot_fences_021():
#     return f"""
#     021.robot_fences
#     5
#     5a 0i 0i 0j 1k
#     0a 0i 0i 0j 0j
#     0a 5f 0g 2g 0h
#     0b 0b 4e 0h 0h
#     1c 2c 0d 0d 0d
#     """

# @staticmethod
# def robot_fences_022():
#     return f"""
#     022.robot_fences
#     5
#     4a 0a 1a 0g 5g
#     0a 0b 0a 2g 0g
#     0c 0b 0f 0f 0h
#     0d 0b 0f 0h 3h
#     2b 0b 4e 0h 0h
#     """

# @staticmethod
# def robot_fences_023():
#     return f"""
#     023.robot_fences
#     5
#     0a 0a 0a 5g 3g
#     0b 0b 0a 0g 0g
#     0b 0d 3a 0e 1g
#     0b 3c 0c 1e 0f
#     0c 0c 0c 3f 0f
#     """

# @staticmethod
# def robot_fences_024():
#     return f"""
#     024.robot_fences
#     5
#     4a 0a 0g 0g 3h
#     0b 0b 0g 3g 0h
#     0b 0c 0f 0g 1h
#     2d 0d 5f 1f 0h
#     0e 0d 0f 0f 0h
#     """

# @staticmethod
# def robot_fences_025():
#     return f"""
#     025.robot_fences
#     5
#     0A 5A 0A 0G 4H
#     0A 0A 0E 0H 0H
#     0B 3B 0E 5I 0J
#     1C 0C 3E 0K 5K
#     0D 0D 0F 3K 0K
#     """

# @staticmethod
# def robot_fences_026():
#     return f"""
#     026.robot_fences
#     5
#     0a 0a 0b 0d 1d
#     0a 5c 0c 0d 3d
#     0e 0e 3e 0e 0e
#     0f 4f 0f 5f 0f
#     0g 0h 0h 0h 5i
#     """

# @staticmethod
# def robot_fences_027():
#     return f"""
#     027.robot_fences
#     5
#     5a 0a 0a 0a 0a
#     4b 0b 0b 0b 0i
#     0b 0e 0f 0h 2i
#     0c 0c 0f 1g 0j
#     3c 4c 0d 2d 0j
#     """

# @staticmethod
# def robot_fences_028():
#     return f"""
#     028.robot_fences
#     5
#     0a 0a 0f 1g 0h
#     0a 4a 0a 0g 3i
#     1b 0b 0d 0i 0i
#     3c 0c 0d 0d 0e
#     0c 0d 0d 3e 2e
#     """

# @staticmethod
# def robot_fences_029():
#     return f"""
#     029.robot_fences
#     5
#     0a 4a 1g 0g 0h
#     1b 0a 0d 0g 0g
#     0a 1a 0d 2e 0g
#     0c 0c 5d 0e 0f
#     0c 0c 0d 1e 0e
#     """

# @staticmethod
# def robot_fences_030():
#     return f"""
#     030.robot_fences
#     5
#     0a 0e 3e 0g 1h
#     0a 0e 0h 0h 4h
#     0b 0f 5f 0i 0j
#     0c 0c 0c 0j 0j
#     3d 0d 0d 1j 2j
#     """

# @staticmethod
# def robot_fences_031():
#     return f"""
#     031.robot_fences
#     6
#     6a 5a 0f 0f 4f 0f
#     0b 4a 5f 0g 0g 0p
#     0c 0d 0d 0e 3g 0p
#     0h 2h 0h 0m 0n 5p
#     2i 0j 0k 0m 0m 0o
#     4i 3i 0k 5k 0l 0l
#     """

# @staticmethod
# def robot_fences_032():
#     return f"""
#     032.robot_fences
#     6
#     4a 0a 0f 0g 5g 0h
#     0b 6e 0f 0j 0m 0o
#     0b 0f 6f 0j 2m 0o
#     0c 0f 0i 2j 0m 6o
#     6c 0d 0j 3j 0n 0o
#     3d 0d 0k 5k 0k 2l
#     """

# @staticmethod
# def robot_fences_033():
#     return f"""
#     033.robot_fences
#     6
#     6a 0b 0b 3b 0h 4h
#     0c 0c 4c 0d 0g 0h
#     0e 0e 0f 0g 0g 3h
#     4e 0e 0f 6g 0g 1i
#     0j 0j 0j 0j 1j 0k
#     1l 4l 0l 2l 0m 5k
#     """

# @staticmethod
# def robot_fences_034():
#     return f"""
#     034.robot_fences
#     6
#     6a 0f 1h 0h 2h 3i
#     0b 6f 0g 3h 0h 0i
#     0b 0b 4j 0j 6j 0k
#     3c 0d 0e 0l 0m 6p
#     0c 1d 0e 2m 0m 0p
#     5c 0e 3e 0n 0o 0o
#     """

# @staticmethod
# def robot_fences_035():
#     return f"""
#     035.robot_fences
#     6
#     4A 0A 0E 0E 0G 3G
#     5A 3A 6F 0G 0G 0H
#     0A 0D 0I 0I 0M 5L
#     0B 0D 0J 0I 4L 0L
#     0B 6D 0J 2J 0K 4K
#     6C 0N 0J 5J 0K 0K
#     """

# @staticmethod
# def robot_fences_036():
#     return f"""
#     036.robot_fences
#     6
#     0a 0a 6h 0i 1k 0k
#     0b 5a 0a 3i 0k 0l
#     5b 0e 0a 0i 0i 2m
#     0b 0f 0g 0i 5j 0m
#     1c 0c 2g 0j 6j 0n
#     6d 2c 0g 0g 0g 4n
#     """

# @staticmethod
# def robot_fences_037():
#     return f"""
#     037.robot_fences
#     6
#     5a 6a 2b 0b 4b 0b
#     4c 0d 0e 6e 0e 0e
#     0c 3c 0e 1m 0l 0n
#     1f 0g 5g 0h 0l 0l
#     0g 4g 0g 0h 0i 0l
#     0j 0j 0k 0k 0k 4l
#     """

# @staticmethod
# def robot_fences_038():
#     return f"""
#     038.robot_fences
#     6
#     6a 0f 0g 2g 4n 5n
#     0b 0f 0g 0g 0m 0m
#     2b 0e 0g 3h 0m 0m
#     5c 0c 4h 0h 6k 0l
#     0c 0d 0h 0i 0j 0l
#     0d 0d 6d 0i 2j 1l
#     """

# @staticmethod
# def robot_fences_039():
#     return f"""
#     039.robot_fences
#     6
#     6a 0i 2i 5i 0j 0m
#     3b 0o 0i 0i 0l 0m
#     0b 0l 0l 0l 0l 5m
#     5b 6f 0g 0g 0g 0m
#     4b 0e 0g 0h 2g 3m
#     2b 0c 4c 3c 0c 1d
#     """

# @staticmethod
# def robot_fences_040():
#     return f"""
#     040.robot_fences
#     6
#     0a 0a 0c 5d 0d 3d
#     0b 0a 0d 0d 6e 0n
#     6a 0a 0j 0k 0n 2n
#     0f 0k 0k 3k 0l 0l
#     2f 0i 0l 1l 0l 0m
#     0g 1g 2g 0h 4h 5h
#     """

# @staticmethod
# def robot_fences_041():
#     return f"""
#     041.robot_fences
#     6
#     0a 0b 0b 4d 0e 0e
#     2c 0c 3c 0d 4e 0e
#     0c 0d 0d 2d 0k 4l
#     4c 0f 0g 0j 0l 0l
#     0g 0g 0g 0j 2l 0m
#     0h 4h 0h 3i 0i 2i
#     """

# @staticmethod
# def robot_fences_042():
#     return f"""
#     042.robot_fences
#     6
#     6a 0e 0e 0e 0l 0o
#     1b 0e 3i 0j 2k 0o
#     0b 0e 0i 0i 0k 0o
#     5b 0d 0g 0g 6m 0o
#     0b 6c 0g 0h 5m 0n
#     0b 0c 6f 0h 0n 2n
#     """

# @staticmethod
# def robot_fences_043():
#     return f"""
#     043.robot_fences
#     6
#     0a 0b 3c 0c 0d 2l
#     0a 3a 0c 4c 0k 1l
#     0e 0e 5e 0j 0k 0k
#     5f 0h 0i 0j 0k 0k
#     0g 0h 4h 0j 0o 0o
#     3g 2g 0m 0n 0o 0o
#     """

# @staticmethod
# def robot_fences_044():
#     return f"""
#     044.robot_fences
#     6
#     3a 0a 4a 0e 5e 1f
#     0b 0c 0a 0d 0e 0f
#     0c 0c 0a 0g 0g 4g
#     0h 0h 3h 0l 0l 0l
#     0i 0h 0h 4l 6m 0l
#     0j 0j 1j 0j 2j 0k
#     """

# @staticmethod
# def robot_fences_045():
#     return f"""
#     045.robot_fences
#     6
#     3a 0a 0j 0n 4n 6n
#     5b 0a 6k 0l 0l 0n
#     0b 0b 0l 0l 0m 0n
#     0c 0b 0f 2g 0h 0h
#     0d 5d 2f 0g 1g 0h
#     2e 0d 0f 0f 0f 0i
#     """

# @staticmethod
# def robot_fences_046():
#     return f"""
#     046.robot_fences
#     6
#     0a 6a 0b 4b 0b 0b
#     4c 0f 2f 0g 3n 0o
#     2c 5h 0h 0j 0n 6o
#     0c 0h 6i 0j 0n 0o
#     0c 0h 0i 0j 0l 0m
#     6d 0h 0i 0k 0m 1m
#     """

# @staticmethod
# def robot_fences_047():
#     return f"""
#     047.robot_fences
#     6
#     1a 0b 0i 3k 2k 4k
#     0b 0b 0i 6j 0k 0k
#     0b 0c 2i 0i 0l 0m
#     0d 3d 0d 5i 0m 0m
#     0e 0e 0g 0h 3m 0n
#     0e 1f 0g 2g 0g 3g
#     """

# @staticmethod
# def robot_fences_048():
#     return f"""
#     048.robot_fences
#     6
#     0a 0a 5a 0i 4n 0n
#     0a 1j 0k 0k 0n 0m
#     0a 0b 1k 3l 0m 5m
#     1b 0b 0e 0f 2g 3h
#     0b 0d 0f 6f 0g 0h
#     0c 0c 0c 0c 0c 0h
#     """

# @staticmethod
# def robot_fences_049():
#     return f"""
#     049.robot_fences
#     6
#     0a 5a 0i 0m 0m 4m
#     0b 0c 3i 0k 0k 2m
#     5d 0d 4i 0i 0k 0l
#     2d 0d 0d 5j 0k 0k
#     3e 0e 0e 0g 0g 0h
#     0e 0e 0f 2g 0g 0g
#     """

# @staticmethod
# def robot_fences_050():
#     return f"""
#     050.robot_fences
#     6
#     2a 0a 0a 0b 0b 0n
#     0c 0d 1d 0d 4m 0n
#     5c 0e 0f 0g 0m 6n
#     0c 0f 0f 3k 0m 1m
#     0f 0f 0i 0k 0l 0m
#     1h 0i 5i 0j 0l 3l
#     """

# @staticmethod
# def robot_fences_051():
#     return f"""
#     051.robot_fences
#     6
#     0a 0a 0l 0m 0m 5m
#     0b 4b 0b 0k 2m 0m
#     6c 0j 4j 1j 0j 0j
#     4d 0h 0i 0i 0i 0i
#     0d 0d 0d 0d 0g 0i
#     5e 0e 0e 3e 0e 6f
#     """

# @staticmethod
# def robot_fences_052():
#     return f"""
#     052.robot_fences
#     6
#     5a 0a 0b 2b 0g 0g
#     0a 2f 0f 0f 0g 0h
#     0c 0c 2c 0f 6i 0i
#     6d 0d 0d 0e 0e 0e
#     0j 5k 0k 0l 0m 0m
#     3j 0j 6k 0m 0m 4m
#     """

# @staticmethod
# def robot_fences_053():
#     return f"""
#     053.robot_fences
#     6
#     0a 3e 0i 0i 2i 0j
#     0b 0e 0h 5i 0j 0j
#     0b 0e 5h 0i 0j 0k
#     0b 0f 0g 6g 0k 1k
#     0b 0g 0g 0g 1l 0m
#     3b 0c 0d 0d 0m 0m
#     """

# @staticmethod
# def robot_fences_054():
#     return f"""
#     054.robot_fences
#     6
#     0a 0a 0h 1j 0j 0k
#     0a 0a 0i 0m 0m 3o
#     0b 4c 0i 0l 3m 0o
#     3c 2c 0l 0l 0n 0o
#     2d 0d 0d 0g 0g 0o
#     1e 0f 0f 0f 0f 0o
#     """

# @staticmethod
# def robot_fences_055():
#     return f"""
#     055.robot_fences
#     6
#     0a 0i 0j 0j 0k 0o
#     0a 0i 0l 0l 0l 0o
#     4a 1i 0i 6m 0n 0o
#     0b 0g 0g 0h 0n 0o
#     0c 0f 0f 5f 0f 0o
#     2c 0c 1d 0e 5e 6e
#     """

# @staticmethod
# def robot_fences_056():
#     return f"""
#     056.robot_fences
#     6
#     1a 0b 0e 0m 0m 5q
#     0c 0c 3e 0k 0m 0p
#     0c 0d 0k 0k 2m 0p
#     0f 0g 0k 0l 0n 0p
#     0g 0g 0j 2l 5o 0o
#     0h 0h 0h 6h 0h 1i
#     """

# @staticmethod
# def robot_fences_057():
#     return f"""
#     057.robot_fences
#     6
#     0a 0a 0m 2n 0n 4n
#     0b 0b 0m 0m 0m 0n
#     0c 0d 0d 0d 3d 0l
#     0e 5e 6h 0i 0i 2l
#     0e 0e 0h 3i 0i 0k
#     2e 0f 1g 0j 0j 0j
#     """

# @staticmethod
# def robot_fences_058():
#     return f"""
#     058.robot_fences
#     6
#     0a 0a 6b 2i 0k 5l
#     0c 0f 0i 0i 0k 0l
#     0c 0g 4h 0i 0k 0m
#     0c 0h 0h 0i 0j 0m
#     2d 0h 1h 0j 0j 0m
#     0d 0e 0e 3e 6e 4e
#     """

# @staticmethod
# def robot_fences_059():
#     return f"""
#     059.robot_fences
#     6
#     0a 0f 0f 0f 1i 0j
#     0a 0d 0e 0f 0i 5j
#     0b 0d 1d 0h 6j 0j
#     0b 0d 0g 0h 0k 0k
#     0b 0d 0g 0g 0k 1k
#     0b 1c 0c 0c 5k 6l
#     """

# @staticmethod
# def robot_fences_060():
#     return f"""
#     060.robot_fences
#     6
#     4A 0C 5F 1G 0G 0G
#     0A 0C 0F 0H 0H 0M
#     0A 0C 0E 4H 0J 0J
#     3A 0C 0D 0H 0I 0J
#     0B 2C 0D 0D 3K 0K
#     0B 0D 3D 2K 0K 0L
#     """

# @staticmethod
# def robot_fences_061():
#     return f"""
#     061.robot_fences
#     7
#     2a 3a 0d 0d 0d 0e 4l
#     0b 0a 0f 0g 3h 0i 0l
#     5b 7c 0f 4f 0h 0h 0l
#     4b 0c 0j 0j 0j 0k 5l
#     0m 0p 6p 0q 5q 0q 0r
#     3n 0p 4q 0q 0s 6s 0t
#     0n 2n 0o 6o 4t 0t 0t
#     """

# @staticmethod
# def robot_fences_062():
#     return f"""
#     062.robot_fences
#     7
#     0a 0b 4o 0o 1q 6t 0t
#     0b 0b 0o 2o 0p 0t 0t
#     3b 0c 0d 5o 0p 0r 0t
#     0e 0f 0f 7p 0p 1s 0s
#     0f 6f 0i 0j 2j 0m 3s
#     2f 0h 5h 6k 0k 4m 0n
#     5g 0h 0h 0h 3l 0m 0m
#     """

# @staticmethod
# def robot_fences_063():
#     return f"""
#     063.robot_fences
#     7
#     5a 0a 4k 1n 0o 3r 2r
#     0a 5k 0k 0k 0o 0p 0r
#     0a 0b 0g 0k 0l 0s 4s
#     3b 0b 0g 5g 0l 7m 0t
#     2b 0e 0f 0g 5m 0m 0t
#     0c 0d 5h 2i 0i 1j 0t
#     0d 0d 6h 0h 0i 0t 5t
#     """

# @staticmethod
# def robot_fences_064():
#     return f"""
#     064.robot_fences
#     7
#     3a 4b 0b 5b 0c 0c 0d
#     5e 0e 1s 0q 6q 0r 0t
#     0e 0i 0p 1p 0q 5q 4t
#     7f 0i 4i 0p 0t 0t 0t
#     0g 0i 0n 0n 1n 0o 6o
#     0h 0i 0j 0k 0o 0o 0o
#     0h 0j 5j 0k 4l 3l 1m
#     """

# @staticmethod
# def robot_fences_065():
#     return f"""
#     065.robot_fences
#     7
#     0a 0a 7k 5l 6l 0l 1m
#     0a 0a 0k 0l 0l 1p 0p
#     6a 0b 0n 0n 7o 0p 4p
#     0c 0c 0q 0s 5s 0s 7s
#     0d 0d 0q 4q 0q 5r 0s
#     4e 0f 5g 0i 1i 0r 6r
#     1f 0f 0g 0h 0i 6j 0j
#     """

# @staticmethod
# def robot_fences_066():
#     return f"""
#     066.robot_fences
#     7
#     5a 0a 4c 0c 3c 6d 0h
#     0a 0b 0c 0e 4g 0g 0h
#     0f 0f 5f 0f 0g 0g 1h
#     0i 4k 0l 2l 0m 3r 0r
#     0j 0k 0l 0m 0m 0q 4r
#     0j 0k 7n 0n 0o 0q 0r
#     1j 0k 0n 5n 0o 0p 7r
#     """

# @staticmethod
# def robot_fences_067():
#     return f"""
#     067.robot_fences
#     7
#     7a 0b 0b 0r 0r 0r 0r
#     1c 0h 0h 6h 0l 0l 7r
#     0d 0h 0i 0j 0k 0l 0s
#     0d 0g 0g 0j 4m 0q 2s
#     0d 4f 0f 5m 0m 0q 0s
#     0e 0e 0f 0m 2o 0q 4s
#     6e 0f 0f 7n 0o 4p 3s
#     """

# @staticmethod
# def robot_fences_068():
#     return f"""
#     068.robot_fences
#     7
#     5a 4a 0b 0c 0c 0g 0h
#     0a 0a 0a 0c 5c 0g 0h
#     4d 1e 0f 0f 0f 0g 3h
#     1i 0k 4k 0m 0m 7n 0n
#     0i 6j 0k 1l 0m 0t 0t
#     7o 0p 5q 0s 0s 0t 0u
#     0o 2p 0p 0r 0s 0s 5u
#     """

# @staticmethod
# def robot_fences_069():
#     return f"""
#     069.robot_fences
#     7
#     4a 0a 7f 0g 1g 5h 6i
#     0b 1a 0a 0c 0d 0h 0i
#     0b 2b 4c 0c 6e 0e 0i
#     6j 0l 0m 0n 0n 0n 0o
#     0k 0l 6r 0r 0r 0s 0t
#     0l 6l 0q 0q 0q 0q 2t
#     5p 0p 0p 0p 0p 0q 1t
#     """

# @staticmethod
# def robot_fences_070():
#     return f"""
#     070.robot_fences
#     7
#     2a 0a 0h 7h 4k 0k 1l
#     0a 0b 0g 0i 0j 6k 0s
#     1c 0f 0g 2g 0p 0r 0s
#     0c 0f 4f 0m 7p 0q 5s
#     0c 0c 7f 0m 0q 3q 0t
#     6d 0c 0m 0m 0o 0o 0t
#     0d 0e 0m 6n 0o 0o 2o
#     """

# @staticmethod
# def robot_fences_071():
#     return f"""
#     071.robot_fences
#     7
#     6a 0a 3k 0l 0l 0q 0t
#     0b 0a 0k 0l 0m 6q 0s
#     5b 0j 2k 0n 6p 0q 3r
#     0b 0n 0n 0n 0p 0r 0r
#     0b 0f 4f 0g 0h 0i 5i
#     0b 0f 0g 0g 0h 0h 6i
#     0c 0d 0d 0d 5d 0d 0e
#     """

# @staticmethod
# def robot_fences_072():
#     return f"""
#     072.robot_fences
#     7
#     0a 0b 0b 0b 0b 2n 0o
#     0a 0b 0h 0i 0m 0n 0n
#     4a 0a 7h 0i 0l 0p 0s
#     0c 0c 0g 7j 0l 0q 5s
#     3c 0f 1g 0j 0l 0q 0s
#     0c 0e 0g 0k 0k 0q 2r
#     0d 6d 0g 4k 0k 3r 0r
#     """

# @staticmethod
# def robot_fences_073():
#     return f"""
#     073.robot_fences
#     7
#     6a 1j 2k 0l 0l 0l 0m
#     0b 0j 0k 1k 0l 0l 0t
#     0b 6b 0p 0p 0p 0p 0t
#     0c 0n 0p 0q 0r 0s 5t
#     2c 0o 7r 0r 0r 0s 0t
#     0c 0c 0g 3h 0h 7i 0t
#     0d 0e 0e 0f 0h 0i 6i
#     """

# @staticmethod
# def robot_fences_074():
#     return f"""
#     074.robot_fences
#     7
#     4a 0y 1l 0l 0l 5m 0m
#     0a 1i 0i 0k 0l 0m 0n
#     0a 0i 0j 0k 0k 0o 0o
#     0a 4c 0c 0k 0k 0p 1p
#     1b 0c 0d 0d 0e 0p 0p
#     0b 0c 0d 6d 0e 3e 7z
#     0b 0c 0f 0g 5h 0h 0h
#     """

# @staticmethod
# def robot_fences_075():
#     return f"""
#     075.robot_fences
#     7
#     0a 0a 0n 0n 0n 0p 0q
#     0a 0b 6b 7o 0p 5p 0t
#     0b 0b 3b 0r 0s 0s 0t
#     0c 0j 0k 0k 0k 3k 5k
#     0c 7g 0g 0i 2l 0l 0m
#     7d 6g 0h 0i 0i 2m 0m
#     0e 0e 0e 2e 0f 0f 0f
#     """

# @staticmethod
# def robot_fences_076():
#     return f"""
#     076.robot_fences
#     7
#     0a 0a 0a 0b 0c 5c 0c
#     0d 0e 0i 0i 3q 0r 0s
#     0f 0f 6i 0q 2q 0r 0s
#     0f 0f 0i 0i 0k 1p 4s
#     0f 0j 0j 0k 6k 0n 7o
#     0g 0h 0h 0h 0h 2n 0n
#     6g 7h 0l 0m 1m 0n 5n
#     """

# @staticmethod
# def robot_fences_077():
#     return f"""
#     077.robot_fences
#     7
#     2a 0h 0h 6h 0i 0z 3l
#     1a 0g 0g 0k 2k 6l 0l
#     0a 0g 3g 0k 0j 0l 0l
#     0a 0f 0g 0m 4o 0p 0r
#     0a 0f 0n 0n 0o 0p 0r
#     0b 2f 0e 0e 0o 0p 0p
#     6c 0c 2d 0e 0o 0p 0q
#     """

# @staticmethod
# def robot_fences_078():
#     return f"""
#     078.robot_fences
#     7
#     0a 0b 3b 2b 0c 0c 7c
#     0d 6e 0e 1f 0p 0q 5r
#     0d 0d 0d 0d 0p 7r 0r
#     0g 3g 0g 0o 5p 0s 2s
#     0h 0i 0g 0g 0n 0s 0t
#     0i 5i 0l 0m 0n 0n 0n
#     0j 0j 0k 0k 0k 0k 0k
#     """

# @staticmethod
# def robot_fences_079():
#     return f"""
#     079.robot_fences
#     7
#     0a 0a 0b 2d 0e 0e 0e
#     0c 1c 0d 3d 0f 0g 0s
#     2c 0c 0d 0d 0g 0g 1s
#     5h 0h 0l 0l 0n 0p 4s
#     0h 0i 5l 0m 0n 0q 0s
#     0j 0k 7l 0l 0o 2q 0r
#     0k 0k 0o 0o 0o 0q 5q
#     """

# @staticmethod
# def robot_fences_080():
#     return f"""
#     080.robot_fences
#     7
#     0a 0a 0a 0a 0d 1e 7f
#     1a 0b 0c 0c 3c 0u 6u
#     7g 0g 0q 0r 0r 5u 4t
#     0h 0h 0q 0q 0s 0s 0t
#     0i 5i 0i 0n 0s 0s 3t
#     0j 0k 0m 0n 0o 0o 0p
#     0k 3k 4l 0l 0o 0o 0p
#     """

# @staticmethod
# def robot_fences_081():
#     return f"""
#     081.robot_fences
#     7
#     0a 0a 0h 0h 0h 0t 0u
#     0b 0a 0g 1g 0h 0r 0s
#     0b 0a 0g 0i 1p 0r 2s
#     1c 0a 5j 0k 0p 2p 0q
#     2d 0d 4j 0k 0n 0o 0o
#     0e 0f 0k 2k 0l 0l 0l
#     7e 0e 0e 0e 0l 0l 0m
#     """

# @staticmethod
# def robot_fences_082():
#     return f"""
#     082.robot_fences
#     7
#     0a 0b 0a 0c 0c 0d 0d
#     0a 0a 0a 0f 0g 3n 0o
#     6e 0f 0f 0f 0n 0n 0p
#     0h 5l 0m 0n 4n 0p 0p
#     0h 0h 0h 0q 0q 5t 0t
#     0i 0i 0h 0q 0r 0s 0t
#     0j 1k 0k 0s 3s 0s 6t
#     """

# @staticmethod
# def robot_fences_083():
#     return f"""
#     083.robot_fences
#     7
#     0a: 0b 2b 0b 6c 0c 0c
#     0d 0i 0i 0j 0k 0k 0k
#     0d 0h 0h 0l 5n 0n 0o
#     2d 0h 0l 0l 0m 4n 0o
#     0d 0g 0l 0p 3p 0q 0q
#     6e 0f 0f 5f 0p 2r 0r
#     0e 4e 3e 0f 0s 0s 0t
#     """

# @staticmethod
# def robot_fences_084():
#     return f"""
#     084.robot_fences
#     7
#     7a 0a 0b 0b 0b 0b 0c
#     0a 1d 0j 0k 0l 4l 0o
#     0e 0i 0j 0k 3l 0o 4o
#     0e 0e 0j 0j 7l 0o 0p
#     0f 0e 0g 0h 0l 3o 0p
#     0f 0e 0g 0h 0m 0n 6p
#     0f 0f 0g 0g 0m 0n 3q
#     """

# @staticmethod
# def robot_fences_085():
#     return f"""
#     085.robot_fences
#     7
#     0a 1a 4b 0f 0f 0h 0h
#     0c 0d 0e 0e 0f 7g 0h
#     4i 0i 0i 0n 0o 0p 0p
#     0i 3i 0n 0n 1o 0p 0p
#     0j 0j 6j 0j 0q 0r 0r
#     0j 0k 0m 0m 4s 0s 0t
#     0l 0m 2m 0m 0s 0s 7t
#     """

# @staticmethod
# def robot_fences_086():
#     return f"""
#     086.robot_fences
#     7
#     0a 0a 0k 0m 0m 6n 1o
#     0b 0a 3a 0l 0m 0n 0n
#     0b 0b 0p 0s 0s 3s 0t
#     0c 4c 0p 0r 0s 0s 0u
#     0c 0d 6q 0u 0u 0u 0u
#     0c 6d 0e 0f 0f 0i 7j
#     0c 0e 0e 0g 1f 0h 0j
#     """

# @staticmethod
# def robot_fences_087():
#     return f"""
#     087.robot_fences
#     7
#     0a 4a 0k 1l 0l 0o 0p
#     0b 0a 0a 0m 3n 0p 0p
#     5b 0d 0d 0n 0n 7s 0t
#     0c 0c 0d 0n 0q 0t 0t
#     0e 2e 0e 0q 0q 4t 0t
#     0f 0f 0g 0j 0j 0j 4j
#     3f 6g 0g 0g 0h 0i 2i
#     """

# @staticmethod
# def robot_fences_088():
#     return f"""
#     088.robot_fences
#     7
#     0a 0g 1h 5q 0q 4q 0s
#     0a 0g 0i 0q 0r 0s 0s
#     0a 0g 0i 0r 0r 5t 7t
#     0a 0g 0j 0j 4k 0l 6t
#     0b 0f 0j 0j 0k 0k 0p
#     0b 1d 0d 0e 0m 0m 0p
#     0b 0c 0c 7c 0n 1o 0p
#     """

# @staticmethod
# def robot_fences_089():
#     return f"""
#     089.robot_fences
#     7
#     2a 0j 0k 0m 0m 0m 0r
#     0a 0k 0k 0l 0l 0m 0r
#     0a 0i 0i 6i 0n 3q 0r
#     6b 0g 0g 5i 0n 0q 0r
#     0b 0f 0g 0h 0o 4q 0r
#     0c 0f 6f 0f 0o 0q 0s
#     5c 0d 0e 4f 0o 0p 2s
#     """

# @staticmethod
# def robot_fences_090():
#     return f"""
#     090.robot_fences
#     7
#     0A 0B 0C 0C 0C 0D 7D
#     0E 6E 0F 0F 0F 0F 0F
#     0E 0G 0H 0H 0I 0J 5K
#     0E 4G 7R 2S 0T 3J 0L
#     0Q 0P 0R 0R 0T 0J 0L
#     0Q 0Q 0N 0T 0T 0U 0M
#     0O 0N 0N 0M 0M 7M 4M
#     """

# @staticmethod
# def robot_fences_091():
#     return f"""
#     091.robot_fences
#     8
#     0a 7a 0a 8a 0b 2p 4p 1p
#     7c 0j 2j 0n 0o 0p 0x 4x
#     8c 0j 0m 0n 0n 0q 2w 0x
#     0d 4j 3n 0n 0n 0q 0w 7x
#     0d 0k 0k 0l 0l 0l 0w 0x
#     0f 0l 4l 0l 5r 0r 7u 0v
#     0f 0g 0h 0i 0r 0r 0u 0v
#     0f 0g 0g 2i 0s 0t 8u 0u
#     """

# @staticmethod
# def robot_fences_092():
#     return f"""
#     092.robot_fences
#     8
#     0a: 0b 7p 0p 0p 2q 0r 6r
#     0b 3b 0n 2o 0p 0p 0r 0s
#     0b 0e 0e 0o 0r 0r 0r 0y
#     8c 0e 0f 0t 0w 0w 5y 0y
#     0c 4d 0g 0t 0w 0x 0y 0y
#     3g 0g 0g 0t 0t 0u 1v 0v
#     0h 5l 0l 0l 1l 4m 0m 8m
#     0i 0i 0j 7k 0l 3m 0m 0m
#     """

# @staticmethod
# def robot_fences_093():
#     return f"""
#     093.robot_fences
#     8
#     7a 0q 0r 0q 4s 0s 0s 0u
#     0a 0q 0q 0q 0s 0t 0s 6z
#     0b 0o 0o 5o 3p 0v 2w 0z
#     0b 0m 0m 0m 0p 0w 0w 0z
#     2b 1l 0m 0m 0n 0w 0x 5y
#     0c 0c 2g 0g 0g 0h 0x 0x
#     0c 2d 8f 0f 7i 0k 0k 0k
#     4c 8c 0e 0f 0i 5i 1j 0k
#     """

# @staticmethod
# def robot_fences_094():
#     return f"""
#     094.robot_fences
#     8
#     0a 0a 0a 0b 0b 0b 3b 5b
#     0c 0i 0j 1j 0j 0r 0r 0u
#     5c 0k 0l 0l 3l 0r 0s 0u
#     0c 0l 0l 0n 0o 0r 0t 0u
#     6c 0l 7m 0n 0o 0q 0q 0q
#     0c 0c 0m 0n 0o 4o 0o 0p
#     0d 6d 0d 0e 1f 0f 8g 0h
#     1d 0d 2d 8e 0g 6g 0g 3h
#     """

# @staticmethod
# def robot_fences_095():
#     return f"""
#     095.robot_fences
#     8
#     4a 0o 1p 3r 0r 0r 6r 0u
#     0a 3n 0q 0r 4r 0t 0t 8u
#     0a 0n 0q 5s 0s 0t 0v 0w
#     8a 0n 2n 0s 0s 3t 0w 0w
#     0a 0a 0b 0i 3i 0j 0w 0x
#     2c 0d 0f 0h 0i 0j 0w 0w
#     0c 0f 4f 0g 0g 0j 0m 3m
#     0e 0f 0f 6g 0g 1k 0l 0m
#     """

# @staticmethod
# def robot_fences_096():
#     return f"""
#     096.robot_fences
#     8
#     0a 0i 0n 0o 0p 0x 0y 0y
#     0a 0j 6n 0p 1p 0r 0y 8y
#     0a 0j 0n 0q 0r 6r 0w 0w
#     0a 2k 0l 0m 0s 0t 0t 4w
#     0b 0l 0l 0m 0m 8t 4u 0u
#     7b 0b 0m 0m 0m 0t 0u 0v
#     0c 0e 1e 0e 0g 0g 0h 0h
#     8d 0e 0e 0f 6f 0g 0g 0g
#     """

# @staticmethod
# def robot_fences_097():
#     return f"""
#     097.robot_fences
#     8
#     0a 0a 1p 2p 0q 0v 0v 0w
#     0a 0a 0a 4r 0r 7v 0v 0w
#     1b 0b 0a 0r 7s 0t 0t 0w
#     0b 3b 0n 0o 0t 0t 0t 0u
#     0c 0g 0g 0g 0j 5j 0k 4m
#     0d 0f 0j 3j 0j 0j 0k 0l
#     0d 0e 0h 0h 0i 0i 0k 0l
#     7d 0e 0h 0h 0i 1i 0k 0k
#     """

# @staticmethod
# def robot_fences_098():
#     return f"""
#     098.robot_fences
#     8
#     0a 0a 0c 0c 0d 0e 0f 0f
#     0a 0b 7c 0c 0f 0f 0f 1f
#     5a 0a 0p 7p 3p 0p 8q 0r
#     0g 3n 0n 8o 0p 5p 0q 7q
#     0h 0k 0k 0k 0v 0v 0w 0y
#     0i 0i 0k 0l 0s 0v 0w 0y
#     0i 0i 0l 0l 0t 3t 0w 8y
#     0j 0l 0l 0m 0t 0u 7y 0y
#     """

# @staticmethod
# def robot_fences_099():
#     return f"""
#     099.robot_fences
#     8
#     4a 0a 0b 0b 8e 0f 3u 0v
#     0a 0b 0b 0b 0d 0d 0u 7v
#     0a 0c 0d 1d 0d 6d 0u 0v
#     6g 0g 7o 0o 0q 0q 0u 0w
#     0g 0g 1n 0p 0p 0q 0u 0w
#     0h 6i 0n 0p 0p 0r 0t 0w
#     0j 0j 0l 5m 0p 0s 0t 0w
#     0k 0j 0m 0m 0p 0s 0t 2w
#     """

# @staticmethod
# def robot_fences_100():
#     return f"""
#     100.robot_fences
#     8
#     0a 0e 7k 0k 0s 2t 0t 0t
#     0a 7e 0k 0k 0r 0r 0t 1u
#     0b 0d 1j 8k 0o 0r 0r 0u
#     0b 0d 0i 0i 0o 0p 0q 3u
#     7b 0d 0i 0i 4o 0v 0v 0v
#     4c 0d 0i 1l 0n 0n 0v 0v
#     0d 0d 0l 0l 7m 0n 4v 0z
#     0f 0g 3h 0h 0h 0h 0z 7z
#     """

# @staticmethod
# def robot_fences_101():
#     return f"""
#     101.robot_fences
#     8
#     0a 0g 0h 0i 0j 0k 0l 2l
#     0b 0g 0h 0h 0j 0l 0l 0x
#     2b 0g 3g 0h 6j 0j 0w 0x
#     0b 0m 0n 2u 0u 0v 0x 0x
#     0c 8o 5o 0o 1u 0u 0y 0y
#     0c 0c 0p 0o 0s 0s 0y 0y
#     0d 0e 0f 0q 0q 0s 0t 0y
#     4d 0d 0f 0f 0f 0r 0t 0t
#     """

# @staticmethod
# def robot_fences_102():
#     return f"""
#     102.robot_fences
#     8
#     0a 0b 0r 0s 0u 0u 0z 0z
#     0b 0b 0r 0r 0t 0u 0v 0z
#     2b 0q 6q 0q 3t 0t 0z 0z
#     1b 0c 0d 0d 6h 0o 0p 0p
#     0d 0d 0d 8d 0h 0n 0n 0n
#     0e 0e 1h 0h 0h 2l 0l 0m
#     0f 0g 0h 0f 0i 0l 7m 0m
#     3f 1f 0f 0f 0j 0k 0k 0k
#     """

# @staticmethod
# def robot_fences_103():
#     return f"""
#     103.robot_fences
#     8
#     8a 0a 0m 0m 2u 0v 0w 0w
#     1b 3k 0m 0m 0u 0u 0w 0w
#     0b 0j 0l 0l 0n 0u 0u 0w
#     0b 0i 0i 8i 0n 0t 0u 0w
#     4b 0g 0h 0n 0n 0o 0p 0p
#     0c 0g 0g 1g 0o 0o 0p 0r
#     0c 0f 4g 0g 0o 0q 0r 0r
#     0c 0d 0d 0d 0e 0r 0r 0s
#     """

# @staticmethod
# def robot_fences_104():
#     return f"""
#     104.robot_fences
#     8
#     0a 1a 0c 0c 0g 0g 0g 8g
#     0a 0b 0c 0d 0e 0f 6f 0f
#     0h 0v 0v 0v 0v 0v 0w 0x
#     0i 0s 7t 0t 0t 0w 0w 0y
#     0i 0r 0t 0t 1u 8y 0z 0y
#     8i 0r 0r 5r 0r 0y 0y 0y
#     0j 0l 0m 0m 0o 0o 0p 0q
#     0j 0j 0j 7m 0n 0o 0p 6p
#     """

# @staticmethod
# def robot_fences_105():
#     return f"""
#     105.robot_fences
#     8
#     7a 5a 0o 0o 1o 0r 0r 4y
#     0b 0a 0p 0q 0p 0r 0s 0y
#     0b 0a 4p 0p 0p 0t 0t 0y
#     0b 2c 0d 0d 0u 0u 0y 0y
#     0e 0f 0e 0e 0u 0v 0y 0z
#     0e 0e 0e 0k 0l 0v 0v 0w
#     0g 0g 0k 0k 0m 1m 0w 0w
#     0h 0i 0j 6j 0m 0n 0w 0x
#     """

# @staticmethod
# def robot_fences_106():
#     return f"""
#     106.robot_fences
#     8
#     0a 0r 0r 0r 0u 2u 0v 5z
#     0b 0r 0s 8r 0t 0u 0v 0z
#     0c 0d 7s 0s 0s 0s 5s 0z
#     0c 6f 0w 0w 0y 5y 0y 0z
#     0e 0f 0f 0w 0x 3x 0y 1z
#     0g 0g 0h 0i 0p 0p 0p 0q
#     0i 0i 0i 0i 0m 0n 0n 7q
#     0j 0k 0k 0k 0l 0n 0o 0q
#     """

# @staticmethod
# def robot_fences_107():
#     return f"""
#     107.robot_fences
#     8
#     5a 0b 0c 0c 2c 0d 0d 0e
#     6a 0a 0c 0c 0c 0d 0d 0e
#     0a 0a 0m 0n 5n 0n 0q 0q
#     0f 1l 0l 0n 0n 0o 0p 6p
#     0f 0f 0l 0r 0s 0s 0t 0u
#     0g 0f 0l 0r 0r 0s 0w 0w
#     0h 0i 0i 0j 0i 5s 0w 0y
#     2h 0h 0i 0i 0i 0k 0w 1x
#     """

# @staticmethod
# def robot_fences_108():
#     return f"""
#     108.robot_fences
#     8
#     0a 0a 0a 0k 0l 0l 0n 0n
#     0a 0b 7c 0l 0l 0l 0m 0n
#     0c 0c 0c 7l 0o 0p 0q 0q
#     0d 0d 0c 0o 1o 0q 0q 0r
#     5d 0j 0j 0s 0t 0t 0v 0w
#     0e 0e 0j 0s 0t 0s 0u 4w
#     0f 0f 0g 0s 0s 3s 6u 0w
#     0h 0h 0h 2h 0h 0i 7u 1w
#     """

# @staticmethod
# def robot_fences_109():
#     return f"""
#     109.robot_fences
#     8
#     0a 7b 0c 0d 0f 4f 0g 0g
#     0a 0b 6b 0e 0f 0f 0g 0h
#     0a 0a 0a 0e 0e 0e 0e 0e
#     0i 0i 0m 0m 0n 0n 0o 0z
#     8i 0j 5l 0t 0u 0v 0v 3z
#     0i 4i 2l 0s 0u 0w 0x 0z
#     0k 0l 0l 0q 0u 0w 0x 0z
#     0k 0k 0q 0q 0r 5w 0x 0y
#     """

# @staticmethod
# def robot_fences_110():
#     return f"""
#     110.robot_fences
#     8
#     0a 0a 0a 0m 2m 0o 0o 0o
#     0b 0b 0k 0l 0n 2o 0p 0q
#     0b 8b 0l 0l 0p 0p 0p 0r
#     0c 0c 0s 0t 0w 0w 0w 0w
#     0c 0f 0f 0t 0u 0v 0v 0w
#     0c 0f 0g 0g 8g 0i 0v 0w
#     0c 6e 0g 0e 0g 3i 0i 0j
#     2e 0e 1e 0e 0h 8h 0h 0h
#     """

# @staticmethod
# def robot_fences_111():
#     return f"""
#     111.robot_fences
#     8
#     0a 0h 6h 0h 0i 0q 0t 3t
#     0b 0h 0h 4h 0q 0q 0t 0t
#     3b 1j 0m 0o 0o 0r 0v 0u
#     0b 0k 2m 0o 0p 0r 0v 0v
#     0b 0k 0m 0n 0p 0r 0z 7v
#     0b 0k 0l 0l 0p 0s 0z 0z
#     0b 0d 0d 0d 6g 0g 0g 1z
#     0c 0d 0d 0e 0f 5g 0z 0z
#     """

# @staticmethod
# def robot_fences_112():
#     return f"""
#     112.robot_fences
#     8
#     0a 0d 2e 0h 0h 0o 0p 8p
#     0a 0d 0e 0h 0h 0o 0o 0q
#     7a 0d 0g 0h 0o 0o 0o 3q
#     0a 0f 0g 0l 0l 0n 0n 0q
#     0b 0f 0f 0l 0m 0n 0z 5q
#     0c 0i 0i 8i 0i 0z 0z 6t
#     0c 0i 5k 0k 2r 0r 0t 0t
#     0c 0j 0k 0k 0s 0t 4t 0u
#     """

# @staticmethod
# def robot_fences_113():
#     return f"""
#     113.robot_fences
#     8
#     0a 0b 0b 0c 0c 0c 0v 0v
#     0b 7b 0c 5c 0d 0c 0v 0v
#     0e 0f 0f 0g 0g 0g 0v 0v
#     0e 0h 0h 0q 0r 0r 0s 0t
#     0e 0h 0o 0o 0p 0r 0u 0u
#     0e 0j 0j 0k 0k 0l 0m 0u
#     0i 4j 0j 0k 0k 0l 0n 0u
#     0i 0j 0j 4k 0k 2l 0l 1l
#     """

# @staticmethod
# def robot_fences_114():
#     return f"""
#     114.robot_fences
#     8
#     0a 0a 0z 0A 0A 0A 0B 4K
#     0b 0a 0D 0D 0F 0G 0G 0K
#     0q 0q 0q 8H 0H 0J 0K 0K
#     0c 8d 0q 0s 0v 0v 0w 0x
#     0e 0e 0r 0s 0t 0v 0v 7x
#     0e 3e 0e 0s 0t 0t 0u 0x
#     0f 0f 0f 0p 0p 0p 0p 0p
#     0g 0g 0g 0h 0i 0i 5i 0o
#     """

# @staticmethod
# def robot_fences_115():
#     return f"""
#     115.robot_fences
#     8
#     0a 3m 0m 0m 0u 0v 0v 0z
#     0b 1m 6m 0m 4w 0w 0x 0z
#     2c 0n 0n 0r 0r 0w 0y 0z
#     0c 6n 0n 0q 0r 0y 0y 0z
#     0d 0n 0n 0p 0r 0r 0t 0z
#     0d 0d 0o 0p 0p 0r 4s 0s
#     0e 0f 0g 0g 0i 0j 0s 0s
#     0e 0e 0g 7h 0i 0i 1k 0l
#     """

# @staticmethod
# def robot_fences_116():
#     return f"""
#     116.robot_fences
#     8
#     4a 0a 3t 0u 2w 0w 0w 0A
#     0a 0a 0j 0j 0v 6w 0w 0A
#     0a 0b 0j 0k 7q 0w 0B 2F
#     0c 0h 0j 0k 0q 0q 0C 0F
#     0d 0h 0j 0l 0p 0p 0C 0E
#     0e 0g 0i 0i 0o 0p 0C 0D
#     0e 0f 0i 0i 0m 0m 0D 0D
#     0f 0f 0i 0i 0m 0n 1D 3D
#     """

# @staticmethod
# def robot_fences_117():
#     return f"""
#     117.robot_fences
#     8
#     1a 0b 0c 0f 0f 0h 0h 0h
#     0a 7d 0d 0f 0f 0g 0h 0h
#     0a 0d 6d 0e 0f 0f 0h 0i
#     7j 0n 0o 0o 0r 0w 6w 0w
#     0j 0m 0o 0q 0r 0v 0v 0w
#     0k 0l 0o 0p 0s 0v 0v 0w
#     0k 0l 0p 0p 0s 0u 0v 0v
#     0k 6l 0l 5l 0s 0t 0t 0t
#     """

# @staticmethod
# def robot_fences_118():
#     return f"""
#     118.robot_fences
#     8
#     0a 0f 5g 0g 0g 0g 0v 0w
#     7a 0e 0i 0i 2i 0p 0u 0w
#     0a 0e 0i 0i 0n 0p 0t 0t
#     2b 0e 0h 0i 0o 0p 0s 0t
#     0b 0d 0h 0p 0p 6p 0r 8t
#     0b 0c 0h 0l 0m 0q 0r 0r
#     0b 0c 0j 0l 0m 0m 0m 0r
#     0b 0c 0k 0k 0k 0m 0m 0r
#     """

# @staticmethod
# def robot_fences_119():
#     return f"""
#     119.robot_fences
#     8
#     0a 0a 0a 0a 0a 0a 0b 0b
#     0c 0l 0l 0n 7q 0w 5x 0x
#     0d 0l 0l 4o 0q 0q 0x 0x
#     0d 0e 0m 0o 0s 0s 0x 0y
#     0d 0e 0g 2o 0r 0s 0v 0z
#     0f 0g 0g 0p 0r 0t 0v 0v
#     3f 0g 0h 0h 4r 0t 0u 0v
#     0f 0g 6g 0h 0i 0j 0k 0k
#     """

# @staticmethod
# def robot_fences_120():
#     return f"""
#     120.robot_fences
#     8
#     0A 0B 0D 0E 0E 4E 0F 0G
#     0C 0C 0D 2E 1E 0E 0G 0G
#     8C 0C 2I 0J 0K 0K 0G 0G
#     0C 0H 0I 0L 0L 0K 0U 0T
#     0P 3P 0I 0L 0M 0S 0U 0U
#     0P 2P 0Q 0M 0M 0S 5U 0U
#     0Q 0Q 0Q 0O 0N 0S 0V 0W
#     0Q 0R 0R 0R 0R 0R 0W 0W
#     """

# @staticmethod
# def robot_fences_121():
#     return f"""
#     121.robot_fences
#     9
#     0a 0a 2a 4a 0b 6b 0c 0d 0d
#     0e 0e 0f 0f 3H 0F 0F 0I 0I
#     0e 8D 0D 0E 0H 0J 0K 0K 0M
#     0g 0D 6J 0J 5J 0J 0K 0L 4M
#     7h 0h 1A 0B 0B 3B 0B 8C 0C
#     0i 0i 0i 0i 0s 0t 0u 0v 7v
#     8j 0Z 0p 0p 0s 0w 0w 0x 0z
#     0j 0o 0p 0q 0r 2r 0w 0y 5z
#     1k 0l 0l 0l 0l 0m 0m 0n 0n
#     """

# @staticmethod
# def robot_fences_122():
#     return f"""
#     122.robot_fences
#     9
#     0a 5a 0p 7q 0q 8q 0G 0H 0H
#     5b 0a 0o 0o 0r 0s 0G 0I 0J
#     0c 0m 0m 0n 0r 1s 0F 0K 0L
#     0c 0m 0t 0u 3v 0E 7F 0K 4L
#     0c 0j 0t 1t 0v 7D 0F 0K 0L
#     0d 7j 0l 0t 1v 0y 0y 0K 0L
#     2e 0i 0l 0t 0v 0x 0z 0K 7L
#     3e 0i 0k 0t 0w 0x 0A 0B 0L
#     0e 0f 0f 0g 0h 6h 0A 0B 0C
#     """

# @staticmethod
# def robot_fences_123():
#     return f"""
#     123.robot_fences
#     9
#     0a 0a 9b 0c 0u 7v 3w 0x 4x
#     0a 0c 0c 0c 0v 0v 0w 0x 0x
#     0a 2d 0d 0F 6G 0H 9J 0K 0K
#     0d 0d 0y 0F 0G 0I 0J 0K 0M
#     0d 0f 0z 0z 2A 0B 5E 0L 0M
#     0e 0f 0m 0n 0o 0B 0E 6M 0M
#     2g 0k 7l 0l 0o 3C 0D 0M 9M
#     0g 0i 0i 0j 0p 0r 6r 0s 0t
#     0h 0j 0j 5j 3p 9q 0r 0s 0t
#     """

# @staticmethod
# def robot_fences_124():
#     return f"""
#     124.robot_fences
#     9
#     8a 0a 0a 0b 0b 0b 0b 0b 0c
#     3d 0Z 0W 0E 0F 0G 6G 0J 0K
#     0d 0e 0W 0G 0G 7G 0H 6J 0K
#     0e 0e 0A 0B 0B 0C 0H 0I 0K
#     0e 2k 0k 0l 0m 0m 0w 0w 5w
#     0e 0k 0k 0k 0m 0o 0w 0x 6w
#     6e 0i 0i 0j 0n 9o 0v 0v 0w
#     0f 0h 3i 0j 0p 0p 0r 0t 0u
#     2f 0g 0g 3g 0p 1q 0r 0s 0s
#     """

# @staticmethod
# def robot_fences_125():
#     return f"""
#     125.robot_fences
#     9
#     0a 0a 0b 0s 0s 0t 0t 0E 1E
#     9c 0c 1d 0s 0s 0t 0t 0F 0F
#     0e 3e 0p 0p 0q 0t 0D 0F 0G
#     0f 0f 4f 0o 0q 0r 0D 0H 0J
#     0g 0g 0n 0n 0n 0n 0C 0I 0J
#     0h 0m 5m 0m 9y 0z 0C 0K 0L
#     7i 0m 0m 0x 0x 0z 0B 0K 0L
#     0i 0k 8l 0v 0w 7z 0B 3L 0L
#     0j 0j 0l 0u 5u 0u 7A 0L 8M
#     """

# @staticmethod
# def robot_fences_126():
#     return f"""
#     126.robot_fences
#     9
#     0a 0p 3q 0q 0z 0z 0G 0H 0J
#     6a 3p 0q 0x 0y 8z 0G 4I 0J
#     0a 2p 0r 0x 1y 0A 0B 0I 5I
#     0a 0p 0r 0s 0s 0w 0B 0B 0C
#     0a 7o 0s 0s 0w 0w 5B 0D 4F
#     0a 0o 0s 0s 0u 0v 0B 0D 0E
#     0b 0m 0n 0n 0u 0v 0v 0v 0E
#     0b 0h 0i 0i 4j 0k 0k 0l 0l
#     0b 0c 0c 0d 0d 0e 0e 0f 0g
#     """

# @staticmethod
# def robot_fences_127():
#     return f"""
#     127.robot_fences
#     9
#     0a 0j 0m 7n 0q 1r 3s 0t 0t
#     9b 0j 2o 0o 0q 0u 0E 0F 0G
#     0b 3j 0o 0p 0p 0u 0E 0G 0G
#     0c 0i 6o 0o 9v 0v 0E 0H 0H
#     0d 7i 0k 0l 0v 0v 0C 0C 0C
#     0e 0e 0k 0l 0l 0v 0C 0D 0D
#     0e 0h 0k 0l 0w 0w 0A 0A 0D
#     0f 0g 0g 2g 0w 0w 0y 0z 0D
#     0f 0f 0g 0g 1x 0x 0y 0z 0B
#     """

# @staticmethod
# def robot_fences_128():
#     return f"""
#     128.robot_fences
#     9
#     0a 0b 0b 0c 0c 0i 0j 3j 7k
#     0a 0e 8g 0g 0h 2i 0j 0l 0o
#     7a 0e 1f 0g 0h 0m 6m 0n 3o
#     0d 5e 0C 0D 0E 0G 0G 0G 9G
#     0p 0p 0C 0D 0E 0F 0F 0M 0N
#     0q 0s 0t 0H 1I 0J 0K 0L 0N
#     4r 0s 0t 0w 0w 0J 0J 0L 0O
#     0r 0v 0v 0w 0w 0y 0y 0z 0B
#     0r 0u 0v 0v 5w 0x 0y 0A 0B
#     """

# @staticmethod
# def robot_fences_129():
#     return f"""
#     129.robot_fences
#     9
#     0a 0b 0b 6c 0c 0d 0j 0j 0j
#     0e 0g 0g 0h 0i 0i 5j 0j 0k
#     0e 0l 0m 0m 3n 0n 0o 1p 0p
#     0f 0q 0r 0r 0B 0I 3J 0I 0L
#     0f 0t 0t 2t 0B 5I 0I 0I 0L
#     0s 0t 0u 0s 0A 0D 0D 0E 0L
#     0s 5s 0s 0s 0A 6C 0D 0D 0L
#     5v 0w 0w 0y 0y 0z 0F 0F 0L
#     0x 0y 0y 0y 0y 0z 0G 0G 4H
#     """

# @staticmethod
# def robot_fences_130():
#     return f"""
#     130.robot_fences
#     9
#     0a 5b 0b 9i 0j 0k 8k 0n 0o
#     4a 0c 0d 0i 0j 0l 0m 0n 0n
#     0a 0c 0c 0g 0h 0l 6n 0n 0n
#     0a 0e 0e 0e 0e 0f 0H 0H 0H
#     0p 0q 0B 0B 0C 0D 4D 0H 0H
#     0p 0q 0A 0E 0F 0F 0F 0G 0G
#     0r 0r 9A 0I 0I 0J 0K 0K 0L
#     2r 0t 0z 0I 0I 0J 0J 0M 0M
#     0s 6t 0u 0u 0v 8w 0w 0x 2y
#     """

# @staticmethod
# def robot_fences_131():
#     return f"""
#     131.robot_fences
#     9
#     0a 0g 8h 0h 0t 0t 0I 0J 7J
#     0b 0g 0i 0l 0t 0E 0H 0K 0K
#     9b 0j 0l 0l 0t 0E 0G 0L 0M
#     0c 0j 0m 0t 0t 0F 0G 7M 8M
#     0c 0j 0m 0m 0v 0w 0w 0x 0D
#     0c 0k 0m 0s 0u 0z 0z 0C 0D
#     0d 0d 0m 0s 0u 3y 0z 0C 1C
#     0d 0e 0m 0r 0u 0y 0z 0A 0B
#     0f 0f 0n 0o 0o 0p 7p 0q 0q
#     """

# @staticmethod
# def robot_fences_132():
#     return f"""
#     132.robot_fences
#     9
#     9a 0a 0b 0c 0c 4c 0c 0c 3c
#     0d 0d 0e 0f 0f 0f 8I 0J 7J
#     0g 0h 0h 0C 0D 0D 0I 3K 0L
#     0h 0h 5x 0x 0E 0F 0F 0K 0L
#     0h 0h 0w 0x 0G 2G 0H 0K 0M
#     0i 0j 0v 0x 0y 0z 0A 0A 0A
#     0k 0k 0v 0x 0y 0z 0z 0B 0B
#     0k 0m 0n 0n 0p 0q 0r 0s 1u
#     0l 0m 6n 0o 0o 0q 0r 8s 5t
#     """

# @staticmethod
# def robot_fences_133():
#     return f"""
#     133.robot_fences
#     9
#     0a 0c 8c 0c 0d 0d 0e 0F 0F
#     0a 0a 0a 0b 0w 0A 0B 9C 0F
#     5o 0o 0o 0o 0w 8A 0B 0D 0F
#     0e 0e 0n 0o 0x 0A 0E 0G 8H
#     0f 0n 0n 0o 0y 0z 0G 0G 0H
#     0f 0m 0p 0p 0y 0z 0I 0I 0L
#     0g 0m 0q 0r 0r 0s 3s 0t 0v
#     7h 0i 0h 0k 0k 0l 0s 0u 0v
#     0h 5h 0h 9j 0k 0k 0k 0u 0u
#     """

# @staticmethod
# def robot_fences_134():
#     return f"""
#     134.robot_fences
#     9
#     0a 0n 0n 0n 0n 0o 0o 0K 0K
#     0a 0p 0s 0s 0D 0E 0E 0J 0K
#     6a 0q 0q 0s 0C 0F 0F 0H 1I
#     0a 0r 0s 0s 0C 0G 0G 0H 0H
#     0a 0t 0v 0w 0w 1y 0y 0y 0H
#     0a 0t 5v 0w 0x 0y 2z 0z 0A
#     0b 0t 0u 0u 0y 6y 0z 0B 0B
#     0b 0d 1e 0f 0f 0i 4i 0j 0k
#     0c 0d 0e 0g 0h 0i 0l 4m 0m
#     """

# @staticmethod
# def robot_fences_135():
#     return f"""
#     135.robot_fences
#     9
#     0a 0a 8m 0n 2n 0o 0s 0v 0w
#     0a 0k 0k 0k 0l 0l 0s 3v 0w
#     0a 0a 0p 0q 0q 0r 6s 0s 0w
#     0b 0b 0j 0j 0j 0t 0u 0u 0w
#     6c 0c 0c 0j 0j 0t 0u 0w 0w
#     0c 3c 0c 0i 0t 0t 0x 0x 0y
#     0d 0g 0g 0i 8i 0i 0z 0z 0D
#     9e 0g 0g 5h 0h 0A 0B 0B 0C
#     0f 0f 0h 0h 0h 0A 5B 0B 0C
#     """

# @staticmethod
# def robot_fences_136():
#     return f"""
#     136.robot_fences
#     9
#     0a 9a 0x 0y 0y 0C 4C 0F 0G
#     0a 0p 0p 0A 0A 0B 0B 0F 0F
#     0b 4q 0q 0z 0A 0A 0D 0E 0F
#     0b 0r 0s 0s 0s 0s 0D 0F 2F
#     0c 0c 0s 0t 0u 9u 0D 0H 0H
#     0d 0d 0s 2t 3v 0w 0I 0J 8J
#     0d 1l 0l 0m 0v 0w 0K 0K 0K
#     0e 0f 0k 0m 0n 0o 0K 0L 0L
#     0f 0f 0g 5h 0h 0i 0i 0j 0j
#     """

# @staticmethod
# def robot_fences_137():
#     return f"""
#     137.robot_fences
#     9
#     0a 0y 0C 0D 0F 0F 0I 0J 2K
#     0a 8y 0B 0D 0E 2F 0F 0H 0K
#     0b 0z 0A 0A 0E 0G 7H 0H 0L
#     0b 0o 0o 0p 0r 0s 0H 0M 0N
#     0c 0n 0p 0p 0r 5t 0x 0x 0N
#     0c 0p 0p 1q 0q 0t 4u 0u 7w
#     0d 0f 0f 0f 0g 9j 0u 0u 8w
#     0d 0f 0h 0i 0i 0j 0k 2u 0v
#     0e 0f 0f 0i 0i 0l 0m 0m 0v
#     """

# @staticmethod
# def robot_fences_138():
#     return f"""
#     138.robot_fences
#     9
#     0a 0a 0b 0c 0c 0d 0e 0e 0v
#     0f 0g 0h 0h 0i 0i 0u 0u 0v
#     0f 0h 0h 0h 0j 1k 0r 9u 0v
#     0l 0l 0m 0p 0p 0p 0r 0t 0t
#     2n 0n 0o 0p 0p 8p 0q 0s 0s
#     0w 0y 7A 0F 0F 0G 0H 0H 0N
#     9w 0y 0A 0E 0F 0I 5I 0J 0N
#     0x 0y 0B 0C 0D 0K 0L 0L 3M
#     0x 0z 0z 0C 0C 0O 0O 0O 2O
#     """

# @staticmethod
# def robot_fences_139():
#     return f"""
#     139.robot_fences
#     9
#     2a 0a 0d 0d 0d 0e 0e 4j 0j
#     9b 0d 0d 0f 8f 0g 0j 0j 0j
#     0c 0c 0d 7f 0h 0h 0h 0i 0i
#     0j 0j 0q 0r 0r 0s 0t 0t 0u
#     0m 0m 8m 0m 0p 0s 0s 0s 0v
#     0k 0m 0o 0o 0p 0p 0p 0s 1v
#     0k 0l 0w 0w 0x 0y 0E 7G 0G
#     0k 0k 0z 0z 0A 0A 0E 0F 0G
#     3k 0k 0B 1C 0C 0D 0G 0G 4G
#     """

# @staticmethod
# def robot_fences_140():
#     return f"""
#     140.robot_fences
#     9
#     0a 0b 0b 0d 0d 0e 0f 0f 0g
#     0a 0a 2c 0h 0h 0y 8z 0A 0K
#     0a 0a 0c 0i 0t 0y 0z 0J 0K
#     0j 0q 0q 0s 0t 0y 0I 0J 0K
#     0k 0r 0r 0t 0t 6x 2H 0H 0K
#     0k 0r 0r 0u 2u 0x 0E 0H 0J
#     2l 0l 0m 5p 0w 8w 0E 0F 0J
#     0n 9p 0p 0p 0v 0F 0F 0F 0G
#     0n 0o 0p 0p 0v 0B 0C 0D 0D
#     """

# @staticmethod
# def robot_fences_141():
#     return f"""
#     141.robot_fences
#     9
#     0a 0b 0c 0d 0d 5f 0g 0g 0F
#     7b 0b 0d 0d 9e 0f 0h 4E 0F
#     8j 0j 0j 5n 0n 0o 0p 0E 0F
#     0j 0j 0m 0m 0m 0o 0p 0D 0F
#     0i 0j 0k 0l 0m 0A 0A 0D 0F
#     0q 0r 0r 0u 0v 0v 0A 0B 0F
#     0s 0s 0t 0u 0v 0v 0B 9B 0C
#     0t 0u 0t 0v 0v 0w 0B 0B 1C
#     0t 0t 0t 0x 0y 0z 0z 0B 0C
#     """

# @staticmethod
# def robot_fences_142():
#     return f"""
#     142.robot_fences
#     9
#     6a 0d 0d 0f 0f 0h 0i 0i 0i
#     2b 0d 0f 0f 0g 0E 0E 0K 0K
#     0b 0d 0f 0t 0t 0D 0E 7K 0K
#     0c 0d 0d 0e 0t 0C 0E 0I 0J
#     0j 0q 0r 0t 0t 2B 0F 0F 0J
#     0j 0q 0s 0u 0u 0B 0G 0H 0H
#     0k 3p 0p 2v 0w 0x 7x 0x 0A
#     0k 0m 0p 0v 0w 0w 0x 0x 9z
#     0l 7m 0n 0n 0o 5o 0x 2y 0y
#     """

# @staticmethod
# def robot_fences_143():
#     return f"""
#     143.robot_fences
#     9
#     0a 0a 0B 0B 0B 0B 9E 0F 0G
#     0b 0c 0c 0z 0B 0C 0C 0D 3G
#     0d 0q 0q 8z 0z 0C 0C 0D 0G
#     0d 0p 0p 0u 0z 0z 0A 0D 0G
#     0d 0o 0p 0u 0u 0v 0w 0w 4G
#     0e 0o 1p 4s 0s 0t 0t 0x 0G
#     0e 0g 0g 0r 0s 0s 0t 0x 0y
#     0f 0g 0g 1i 0j 0k 0l 0x 0x
#     0f 0g 0h 0i 6j 0k 0m 0x 0x
#     """

# @staticmethod
# def robot_fences_144():
#     return f"""
#     144.robot_fences
#     9
#     1a 0o 0p 0q 0q 0s 0t 0u 7v
#     0b 9o 0p 0r 0s 0s 0t 0u 0F
#     0b 0w 1B 0B 8C 0C 0D 0E 0F
#     0c 4w 0A 0G 0G 0M 0M 0M 0O
#     0c 0x 0x 0y 4G 0N 0N 0O 0O
#     0d 0d 0e 0y 0G 0H 0I 0J 0K
#     0e 0e 0e 0z 0H 0H 0I 0I 0K
#     9f 0g 0h 0i 0i 0j 0k 0I 0L
#     0f 0g 0h 0l 0l 2m 0m 0n 0L
#     """

# @staticmethod
# def robot_fences_145():
#     return f"""
#     145.robot_fences
#     9
#     0a 0a 0b 0b 0b 0c 0c 0c 0d
#     0e 0f 0f 0f 0f 0f 0f 0k 0l
#     0g 0g 5g 0h 0i 0i 0j 0k 0J
#     6g 0g 0g 5C 0D 0E 0F 0I 0J
#     0m 0n 0z 0C 0D 0E 0F 0H 0K
#     0o 0y 0z 0A 0D 0E 0G 0H 0L
#     8o 0y 0A 0A 0B 0L 0L 0L 0L
#     0o 1q 0q 0r 0s 4t 0u 0v 0w
#     1p 0p 0r 0r 0s 8s 0u 0v 0x
#     """

# @staticmethod
# def robot_fences_146():
#     return f"""
#     146.robot_fences
#     9
#     6a 0a 0i 0j 0j 0j 0j 0k 0k
#     0b 0a 0a 0a 0a 0I 0J 0L 0L
#     1b 0l 0o 0o 0H 0I 0K 0M 6M
#     0b 0l 0o 0E 0E 0F 0F 0G 0G
#     0b 0m 0p 0s 0s 0u 0u 2y 0y
#     0c 0n 0p 0r 0s 0u 0u 0x 0y
#     0d 0n 0q 4r 0t 0v 8w 0x 0y
#     0d 0g 4h 0h 0t 0A 0B 0B 7C
#     0e 0f 0f 0h 1z 0A 0B 0B 0D
#     """

# @staticmethod
# def robot_fences_147():
#     return f"""
#     147.robot_fences
#     9
#     4a 0a 0a 0m 0m 0B 0E 0F 0F
#     0a 0b 0n 0n 0n 0B 0D 0G 0G
#     0e 0e 0n 3x 0x 0B 6B 0C 1C
#     0c 9d 0n 0o 0x 0M 0N 1P 0P
#     0c 0d 0f 4v 0x 0x 0N 0P 0Q
#     0g 0g 0r 0v 0w 0x 0N 0O 0Q
#     0h 0p 0r 0t 0u 0z 0A 0A 0Q
#     0h 0q 0q 0s 0u 0y 0y 0y 0Q
#     0i 0i 0j 0j 1k 0l 0l 0Q 0Q
#     """

# @staticmethod
# def robot_fences_148():
#     return f"""
#     148.robot_fences
#     9
#     0a 0b 0c 0c 0c 0i 0i 0m 0m
#     0a 0a 0f 0g 0h 0i 0i 0l 0l
#     0d 0e 0f 6g 0h 0i 0i 0j 0k
#     0n 3n 0D 0E 8I 0I 0J 0L 9L
#     0o 2q 0D 0E 0H 0J 3J 0L 0L
#     6p 0q 0F 0G 0G 0J 0K 0L 0L
#     0r 0t 0t 0v 0B 0B 0B 0C 0C
#     0r 0s 0u 0u 0x 0y 0y 5z 0z
#     0s 0s 0s 0s 0s 0w 0w 0z 0A
#     """

# @staticmethod
# def robot_fences_149():
#     return f"""
#     149.robot_fences
#     9
#     4a 0a 0b 0b 0B 0C 0C 0G 0G
#     0c 0w 0w 0x 0B 0D 0D 0G 0G
#     0d 6w 0w 0y 0A 0D 0H 0H 0J
#     0e 0e 0u 0y 0z 0E 0I 0I 3J
#     0e 8t 0u 0v 0z 0F 0J 0J 0J
#     0f 0f 0f 0q 0r 0r 0t 0s 0s
#     0f 1f 0h 4i 0i 0o 0p 0p 0p
#     0g 0g 0g 0i 0j 0l 3l 7m 0m
#     0g 0g 5g 0j 0j 0k 0l 0m 0n
#     """

# @staticmethod
# def robot_fences_150():
#     return f"""
#     150.robot_fences
#     9
#     0A 2K 0L 0M 0P 0P 0P 0P 0Q
#     0B 0K 0K 0N 0N 0O 6P 0P 7U
#     0B 0I 0J 0R 0S 0T 0T 0T 0U
#     0C 1H 0H 0R 8R 0T 0V 0e 0e
#     7D 0G 0R 0R 0R 0T 0T 0e 0e
#     0D 0G 0X 0Y 0Z 0d 0d 0d 0e
#     0E 0E 0X 0a 0a 0i 0i 0i 0i
#     0E 0F 0W 0b 1b 0c 0f 9g 0i
#     0F 0F 9V 0V 0c 0c 0f 0h 0h
#     """

