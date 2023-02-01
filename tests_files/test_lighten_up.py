# from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# from techniques.LockedCandidatesPointing import LockedCandidatesPointing

EXPLICITLY = "EXPLICITLY"

# @pytest.mark.parametrize("puzzle_string, constructor, techniques", [
#
#
#     ('lightenup_001', LightenUp, Solving.lightenup_techniques()),
#     ('lightenup_002', LightenUp, Solving.lightenup_techniques()),
#     ('lightenup_003', LightenUp, Solving.lightenup_techniques()),
#     ('lightenup_004', LightenUp, Solving.lightenup_techniques()),
#     ('lightenup_005', LightenUp, Solving.lightenup_techniques()),
#
#
# ])
# def test_default_puzzle(puzzle_string, constructor, techniques):
#     if "\n" in puzzle_string:
#         pytest.skip(puzzle_string)
#     result = getattr(Constants, puzzle_string)
#     assert default_test_puzzle(result(), constructor, techniques)




# @staticmethod
# def lightenup_001():
#     return f"""
#     001.lightenup
#     5
#     +- +- ?? +- ??
#     +- +- +- 04 +-
#     +- +- 04 +- +-
#     +- +- +- +- +-
#     +- 00 +- +- +-
#     """

# @staticmethod
# def lightenup_002():
#     return f"""
#     002.lightenup
#     5
#     +- +- ?? +- +-
#     +- +- +- +- +-
#     +- 03 +- +- +-
#     +- +- ?? +- 03
#     +- +- +- ?? +-
#     """

# @staticmethod
# def lightenup_003():
#     return f"""
#     003.lightenup
#     5
#     +- +- +- +- +-
#     +- +- +- 02 +-
#     +- 02 +- +- +-
#     +- +- 04 +- ??
#     +- +- +- ?? +-
#     """

# @staticmethod
# def lightenup_004():
#     return f"""
#     004.lightenup
#     5
#     +- +- +- +- +-
#     +- 01 +- +- +-
#     +- 03 +- +- 01
#     03 +- 02 +- +-
#     +- +- +- +- +-
#     """

# @staticmethod
# def lightenup_005():
#     return f"""
#     005.lightenup
#     5
#     +- +- +- +- 02
#     +- +- +- +- +-
#     ?? +- +- +- +-
#     +- +- 03 +- ??
#     +- +- +- ?? +-
#     """

# @staticmethod
# def lightenup_006():
#     return f"""
#     006.lightenup
#     5
#     +- +- +- +- ??
#     +- 01 +- +- ??
#     +- +- +- +- +-
#     +- +- +- 03 +-
#     +- +- +- +- 01
#     """

# @staticmethod
# def lightenup_007():
#     return f"""
#     007.lightenup
#     5
#     +- +- 00 +- +-
#     +- +- +- +- +-
#     ?? +- +- +- 01
#     +- +- +- +- +-
#     +- 00 00 +- +-
#     """

# @staticmethod
# def lightenup_009():
#     return f"""
#     009.lightenup
#     5
#     +- +- ?? +- +-
#     +- 02 +- +- +-
#     +- +- +- +- 02
#     +- +- +- +- +-
#     +- ?? +- 02 +-
#     """

# @staticmethod
# def lightenup_010():
#     return f"""
#     010.lightenup
#     5
#     +- +- +- +- +-
#     +- +- +- +- +-
#     00 00 +- +- 01
#     +- +- +- +- +-
#     +- 01 +- 01 +-
#     """

# @staticmethod
# def lightenup_011():
#     return f"""
#     011.lightenup
#     5
#     +- 01 +- +- +-
#     +- +- +- +- +-
#     +- +- +- 00 +-
#     01 +- +- +- +-
#     +- +- ?? 01 +-
#     """

# @staticmethod
# def lightenup_012():
#     return f"""
#     012.lightenup
#     5
#     +- +- +- 01 +-
#     +- 02 +- ?? +-
#     +- +- +- 00 +-
#     +- +- +- +- 01
#     +- +- +- +- +-
#     """

# @staticmethod
# def lightenup_013():
#     return f"""
#     013.lightenup
#     5
#     +- +- ?? +- ??
#     +- +- 02 +- +-
#     01 +- +- +- +-
#     +- +- +- +- +-
#     +- +- +- 02 +-
#     """

# @staticmethod
# def lightenup_014():
#     return f"""
#     014.lightenup
#     5
#     +- +- +- 00 00
#     +- +- +- 01 +-
#     +- +- +- +- +-
#     +- +- +- 01 +-
#     00 +- +- +- +-
#     """

# @staticmethod
# def lightenup_015():
#     return f"""
#     015.lightenup
#     5
#     +- +- +- +- +-
#     +- 01 +- +- 00
#     +- +- +- +- +-
#     +- +- 02 +- 02
#     +- +- ?? +- +-
#     """

# @staticmethod
# def lightenup_016():
#     return f"""
#     016.lightenup
#     6
#     00 +- 00 +- +- 01
#     +- +- +- +- +- +-
#     01 +- +- +- 00 +-
#     +- +- 03 +- +- +-
#     +- 01 +- +- +- +-
#     +- +- +- +- +- +-
#     """

# @staticmethod
# def lightenup_017():
#     return f"""
#     017.lightenup
#     6
#     +- +- +- +- +- 02
#     +- +- +- +- +- +-
#     +- +- +- +- +- 02
#     02 +- +- ?? +- +-
#     +- +- +- 01 +- ??
#     +- 01 +- +- +- +-
#     """

# @staticmethod
# def lightenup_018():
#     return f"""
#     018.lightenup
#     6
#     +- +- 00 +- +- +-
#     01 +- +- +- 03 +-
#     +- 00 01 +- +- +-
#     +- +- +- +- +- +-
#     +- +- +- +- +- ??
#     +- 00 +- +- +- +-
#     """

# @staticmethod
# def lightenup_019():
#     return f"""
#     019.lightenup
#     6
#     +- 02 +- +- 02 +-
#     +- +- +- +- +- +-
#     +- +- +- 01 +- +-
#     +- +- 01 +- +- +-
#     +- +- 00 02 +- +-
#     +- +- +- +- +- 00
#     """

# @staticmethod
# def lightenup_020():
#     return f"""
#     020.lightenup
#     6
#     +- ?? +- +- 02 +-
#     +- ?? +- 01 +- +-
#     +- +- +- +- +- +-
#     +- +- 04 +- +- +-
#     +- +- +- +- +- 00
#     +- 01 +- +- +- +-
#     """

# @staticmethod
# def lightenup_021():
#     return f"""
#     021.lightenup
#     6
#     01 +- +- +- +- +-
#     +- +- 00 +- 03 +-
#     +- ?? +- +- +- +-
#     +- +- +- +- +- ??
#     +- +- +- +- +- +-
#     +- +- +- 01 +- 01
#     """

# @staticmethod
# def lightenup_022():
#     return f"""
#     022.lightenup
#     6
#     +- 02 +- +- +- ??
#     +- 00 +- +- +- +-
#     +- +- +- +- 01 +-
#     +- +- +- +- +- +-
#     +- +- +- 01 02 +-
#     +- +- +- +- +- 01
#     """

# @staticmethod
# def lightenup_023():
#     return f"""
#     023.lightenup
#     6
#     01 +- +- +- +- +-
#     01 +- +- 00 +- +-
#     +- +- +- +- +- +-
#     +- +- +- +- +- +-
#     00 +- +- +- 02 +-
#     00 +- +- 01 +- +-
#     """

# @staticmethod
# def lightenup_024():
#     return f"""
#     024.lightenup
#     7
#     ?? +- ?? +- +- +- +-
#     +- +- +- +- +- 01 +-
#     +- +- 02 +- +- +- ??
#     +- +- +- +- +- +- ??
#     +- 02 +- 00 ?? +- ??
#     +- +- +- +- 02 +- +-
#     +- 00 +- +- +- +- +-
#     """

# @staticmethod
# def lightenup_025():
#     return f"""
#     025.lightenup
#     7
#     ?? +- +- +- +- +- +-
#     +- 01 02 +- 02 +- +-
#     +- +- +- 04 +- ?? ??
#     01 ?? +- +- +- +- +-
#     +- +- +- +- +- +- 01
#     01 +- +- +- +- +- +-
#     +- +- ?? +- +- +- +-
#     """

# @staticmethod
# def lightenup_026():
#     return f"""
#     026.lightenup
#     7
#     +- 01 +- +- +- +- +-
#     +- +- +- 02 +- +- +-
#     +- +- +- +- 02 +- 01
#     +- +- ?? ?? +- +- +-
#     00 ?? +- 02 +- +- 01
#     +- +- +- +- +- +- +-
#     01 +- +- +- +- 01 +-
#     """

# @staticmethod
# def lightenup_027():
#     return f"""
#     027.lightenup
#     7
#     +- +- +- ?? +- +- +-
#     00 +- 02 +- +- +- +-
#     +- +- +- +- ?? 00 +-
#     ?? +- +- +- +- +- +-
#     ?? +- 01 +- +- +- +-
#     02 +- +- +- +- ?? ??
#     +- +- +- 01 +- +- +-
#     """

# @staticmethod
# def lightenup_028():
#     return f"""
#     028.lightenup
#     7
#     ?? +- +- 01 +- +- ??
#     +- +- +- +- +- ?? +-
#     +- +- +- +- +- +- 03
#     +- +- +- +- ?? +- +-
#     03 +- +- +- +- +- +-
#     +- +- +- +- +- +- ??
#     +- +- +- 02 +- +- +-
#     """

# @staticmethod
# def lightenup_029():
#     return f"""
#     029.lightenup
#     7
#     +- +- +- +- 00 +- 01
#     +- +- +- +- 00 +- +-
#     01 +- +- +- 01 +- +-
#     +- +- +- ?? +- +- +-
#     01 +- +- +- ?? +- +-
#     01 +- 02 +- 02 +- +-
#     +- +- +- +- +- +- ??
#     """

# @staticmethod
# def lightenup_030():
#     return f"""
#     030.lightenup
#     7
#     +- ?? +- +- +- +- 01
#     +- +- 01 +- +- +- ??
#     +- +- +- +- +- +- +-
#     +- 00 00 00 01 +- +-
#     +- +- +- +- +- +- +-
#     +- +- ?? +- +- +- +-
#     +- ?? +- +- 01 +- 01
#     """

# @staticmethod
# def lightenup_031():
#     return f"""
#     031.lightenup
#     7
#     00 +- +- ?? +- 01 +-
#     +- +- +- +- +- +- +-
#     +- 02 +- +- 02 +- +-
#     ?? +- 02 +- +- +- +-
#     +- +- +- +- +- +- ??
#     +- +- +- 01 +- +- 01
#     +- 00 01 +- +- +- +-
#     """

# @staticmethod
# def lightenup_032():
#     return f"""
#     032.lightenup
#     7
#     +- +- +- +- +- +- 01
#     ?? +- +- +- ?? 02 +-
#     +- +- +- 00 +- +- +-
#     +- +- 00 ?? +- +- +-
#     +- 02 +- +- +- 01 +-
#     +- +- +- +- +- +- +-
#     ?? ?? +- 02 +- +- +-
#     """

# @staticmethod
# def lightenup_033():
#     return f"""
#     033.lightenup
#     7
#     ?? 00 +- +- +- 00 +-
#     +- +- +- +- +- +- +-
#     +- +- 00 00 +- +- +-
#     +- +- +- +- +- 01 00
#     +- +- +- +- +- +- +-
#     +- 01 +- 01 +- +- 01
#     00 ?? +- +- +- +- +-
#     """

# @staticmethod
# def lightenup_034():
#     return f"""
#     034.lightenup
#     8
#     +- 02 +- +- ?? +- +- +-
#     +- +- +- +- 01 +- +- +-
#     +- 03 +- +- +- +- +- +-
#     +- +- +- 01 +- +- +- +-
#     +- +- 01 +- +- +- +- 02
#     01 +- +- ?? +- +- 03 +-
#     +- +- 01 00 +- +- +- +-
#     +- +- +- +- +- +- 01 ??
#     """

# @staticmethod
# def lightenup_035():
#     return f"""
#     035.lightenup
#     8
#     +- +- +- +- 00 +- 00 +-
#     +- 01 +- 00 +- +- +- +-
#     +- +- +- +- +- +- +- ??
#     +- +- +- 00 +- 02 +- +-
#     +- +- +- +- +- +- +- +-
#     +- +- 00 +- 01 00 00 +-
#     +- 00 +- +- ?? +- +- +-
#     +- +- +- +- +- 01 +- +-
#     """

# @staticmethod
# def lightenup_070():
#     return f"""
#     070.lightenup
#     10
#     ?? ?? 01 +- +- +- +- +- +- +-
#     +- +- +- +- +- +- +- +- +- +-
#     +- +- 01 +- 00 +- +- +- +- 02
#     +- ?? +- +- +- +- +- +- +- +-
#     01 ?? +- +- 01 +- +- 00 +- +-
#     +- +- +- +- ?? ?? +- +- ?? +-
#     +- 03 +- +- ?? +- +- 02 +- ??
#     +- ?? 01 +- +- +- +- +- +- +-
#     +- +- +- +- +- ?? +- +- 01 +-
#     +- +- +- +- 01 +- +- +- +- +-
#     """

# @staticmethod
# def lightenup_078():
#     return f"""
#     078.lightenup
#     11
#     +- 02 ?? +- +- +- 01 +- +- +- ??
#     +- +- +- +- +- ?? +- +- ?? +- +-
#     +- +- +- +- +- +- 03 +- +- 00 +-
#     +- ?? ?? ?? +- +- +- +- +- +- +-
#     +- +- +- 03 +- ?? +- 00 +- +- 01
#     +- +- +- +- +- 00 +- ?? +- +- +-
#     +- +- +- +- +- +- +- +- +- +- +-
#     ?? +- +- +- +- +- +- +- 00 +- +-
#     02 +- +- +- +- +- 01 +- +- +- +-
#     +- +- ?? 01 +- +- +- 02 +- 04 +-
#     +- +- +- +- +- +- ?? ?? +- +- +-
#     """

# @staticmethod
# def lightenup_080():
#     return f"""
#     080.lightenup
#     11
#     ?? +- 02 +- +- 01 +- +- 00 +- +-
#     +- +- +- +- +- +- 01 +- +- +- +-
#     +- 00 +- +- +- +- +- 02 +- ?? +-
#     +- 01 +- 01 ?? 01 +- +- +- +- 01
#     ?? +- +- +- +- +- +- +- +- 01 +-
#     +- +- +- +- +- +- +- +- ?? +- +-
#     +- +- 01 +- +- 02 +- 01 +- +- +-
#     +- 01 +- +- +- +- +- +- +- +- 01
#     00 +- +- +- +- 02 +- +- +- +- +-
#     +- +- 01 +- +- +- +- +- +- +- +-
#     +- +- +- ?? ?? +- +- +- +- +- 01
#     """

# @staticmethod
# def lightenup_081():
#     return f"""
#     081.lightenup
#     11
#     ?? +- +- +- +- +- +- +- ?? +- +-
#     +- +- +- ?? +- +- ?? +- +- +- 01
#     02 +- +- 02 +- 02 +- 03 +- +- ??
#     +- +- +- +- ?? ?? +- +- +- +- +-
#     ?? +- +- +- +- +- +- +- +- 01 +-
#     ?? +- 00 +- +- +- ?? +- +- +- +-
#     +- +- +- +- +- +- +- +- 01 ?? +-
#     +- +- +- 03 +- +- +- +- +- ?? +-
#     +- ?? +- +- +- +- +- +- 02 +- +-
#     01 +- +- +- +- 02 +- +- +- +- +-
#     +- +- +- 01 +- +- +- +- ?? +- +-
#     """