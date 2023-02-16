# # from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# # from techniques.LockedCandidatesPointing import LockedCandidatesPointing
# from Loc import Loc
# from tests_files.test_lighten_up import LightenUp
#
# EXPLICITLY = "EXPLICITLY"
#
#
from Loc import Loc
from tests_files.test_lighten_up import LightenUp


class Lighthouses(LightenUp):
    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)

    def is_solved(self) -> bool:

        for r in range(len(self)):
            for c in range(len(self)):
                loc = Loc(r, c)
                if self.grid[r][c] == '+-':
                    return False

                if self.grid[r][c] == '+_' or self.is_light_block(loc):
                    for surrounding in self.surrounding(loc):
                        if self.grid[surrounding.row][surrounding.col] == '+_':
                            return False

                number = self.light_number(loc)

                if number is None:
                    continue

                # if loc != Loc(1, 0):
                #     continue

                solved_light = []
                solved_empty = []
                unsolved = []

                print(self.extending_cell_locs(loc))
                for loc0 in self.extending_cell_locs(loc):
                    if self.grid[loc0.row][loc0.col] == '+-':
                        unsolved.append(loc0)
                    if self.grid[loc0.row][loc0.col] == '+_':
                        solved_light.append(loc0)
                    if self.grid[loc0.row][loc0.col] == '_-':
                        solved_empty.append(loc0)

                if number != len(solved_light):
                    print("bade number of lights")
                    print(f'{number} {len(solved_light)}')
                    return False

        return True

    def extending_cell_locs(self, loc: Loc) -> list[Loc]:
        locs_to_remove = []

        rows = self.house_row(loc.row)
        cols = self.house_col(loc.col)
        locs = set(rows + cols)
        locs.remove(loc)
        return [loc0 for loc0 in locs if self.is_candidate_cell(loc0)]
#
# # @pytest.mark.parametrize("puzzle_string, constructor, techniques", [
# #
# #
# #
# #     ('lighthouses_001', Lighthouses, Solving.lighthouses_techniques()),
# #     ('lighthouses_002', Lighthouses, Solving.lighthouses_techniques()),
# #
# #
# # ])
# # def test_default_puzzle(puzzle_string, constructor, techniques):
# #     if "\n" in puzzle_string:
# #         pytest.skip(puzzle_string)
# #     result = getattr(Constants, puzzle_string)
# #     assert default_test_puzzle(result(), constructor, techniques)
#
#
# # @staticmethod
# # def lighthouses_001():
# #     return f"""
# #     001.lighthouses
# #     5
# #     +- +- +- +- +-
# #     03 +- +- +- +-
# #     +- +- +- +- +-
# #     +- +- 02 +- +-
# #     +- +- +- +- 01
# #     """
#
# # @staticmethod
# # def lighthouses_002():
# #     return f"""
# #     002.lighthouses
# #     5
# #     02 +- +- +- +-
# #     +- +- +- +- +-
# #     +- +- 00 +- 01
# #     +- +- +- +- +-
# #     +- +- 00 +- 01
# #     """
#
# # @staticmethod
# # def lighthouses_003():
# #     return f"""
# #     003.lighthouses
# #     5
# #     +- +- +- +- 02
# #     +- +- +- +- +-
# #     +- +- 00 +- +-
# #     +- +- +- +- +-
# #     02 +- 01 +- +-
# #     """
#
# # @staticmethod
# # def lighthouses_004():
# #     return f"""
# #     004.lighthouses
# #     5
# #     +- +- 01 +- +-
# #     02 +- +- +- +-
# #     +- +- 01 +- +-
# #     +- +- +- +- +-
# #     +- +- +- +- 03
# #     """
#
# # @staticmethod
# # def lighthouses_005():
# #     return f"""
# #     005.lighthouses
# #     6
# #     +- +- +- +- +- +-
# #     01 +- +- +- +- 01
# #     +- +- +- +- +- +-
# #     02 +- +- +- 01 +-
# #     +- +- +- +- +- +-
# #     +- +- 04 +- +- +-
# #     """
#
# # @staticmethod
# # def lighthouses_006():
# #     return f"""
# #     006.lighthouses
# #     6
# #     +- +- +- +- +- 02
# #     +- +- +- +- +- +-
# #     00 +- +- +- +- +-
# #     +- +- 01 +- +- +-
# #     +- +- +- +- +- +-
# #     +- +- +- 02 +- 01
# #     """
#
#
# # @staticmethod
# # def lighthouses_007():
# #     return f"""
# #     007.lighthouses
# #     6
# #     02 +- +- +- +- +-
# #     +- +- +- +- +- +-
# #     +- +- 01 +- +- +-
# #     00 +- +- +- +- +-
# #     +- +- +- +- +- +-
# #     01 +- +- +- +- 03
# #     """
#
#
# # @staticmethod
# # def lighthouses_008():
# #     return f"""
# #     008.lighthouses
# #     6
# #     01 +- +- +- +- 01
# #     +- +- +- +- +- +-
# #     +- +- +- +- +- 00
# #     +- +- +- 03 +- +-
# #     +- +- +- +- +- +-
# #     +- +- +- +- +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_009():
# #     return f"""
# #     009.lighthouses
# #     7
# #     02 +- 01 +- +- +- +-
# #     +- +- +- +- +- +- +-
# #     02 +- 01 +- +- +- +-
# #     +- +- +- +- +- +- +-
# #     +- +- 02 +- +- +- +-
# #     +- +- +- +- +- +- +-
# #     +- +- 02 +- 05 +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_010():
# #     return f"""
# #     010.lighthouses
# #     7
# #     +- 01 +- 00 +- 02 +-
# #     +- +- +- +- +- +- +-
# #     +- +- 03 +- +- +- +-
# #     +- +- +- +- +- +- +-
# #     02 +- +- +- +- +- +-
# #     +- +- +- +- +- +- +-
# #     +- +- +- 01 +- +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_011():
# #     return f"""
# #     011.lighthouses
# #     7
# #     +- +- +- +- 01 +- +-
# #     +- +- +- +- +- +- +-
# #     +- +- 00 +- +- 01 +-
# #     +- +- +- +- +- +- +-
# #     +- +- 03 +- +- +- +-
# #     +- +- +- +- +- +- +-
# #     03 +- 01 +- +- +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_012():
# #     return f"""
# #     012.lighthouses
# #     7
# #     01 +- +- +- +- +- 03
# #     +- +- +- +- +- +- +-
# #     +- 01 +- +- +- +- 02
# #     +- +- +- +- +- +- +-
# #     +- +- 01 +- +- +- +-
# #     +- +- +- +- +- +- +-
# #     +- +- +- +- 04 +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_013():
# #     return f"""
# #     013.lighthouses
# #     8
# #     +- +- +- +- +- +- +- 00
# #     +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- 01
# #     00 +- 03 +- +- +- +- +-
# #     +- +- +- +- +- +- +- +-
# #     03 +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +-
# #     +- +- +- +- 03 +- +- 01
# #     """
#
#
# # @staticmethod
# # def lighthouses_014():
# #     return f"""
# #     014.lighthouses
# #     8
# #     +- +- +- 01 +- 01 +- +-
# #     +- +- +- +- +- +- +- +-
# #     +- +- 04 +- +- +- +- +-
# #     02 +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- 03
# #     +- +- +- +- +- 00 +- +-
# #     +- +- +- +- +- +- +- 02
# #     +- +- +- +- 03 +- +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_015():
# #     return f"""
# #     015.lighthouses
# #     8
# #     +- +- +- +- +- +- +- +-
# #     +- 04 +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +-
# #     +- +- +- 00 +- 00 +- +-
# #     +- +- +- +- +- +- +- 03
# #     +- +- +- 01 +- +- +- +-
# #     +- +- +- +- +- 01 +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_016():
# #     return f"""
# #     016.lighthouses
# #     8
# #     +- +- +- 02 +- 02 +- +-
# #     +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- 01 +-
# #     03 +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- 02
# #     +- +- +- +- +- 02 +- +-
# #     +- +- +- +- +- +- +- 01
# #     +- 02 +- +- +- +- +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_017():
# #     return f"""
# #     017.lighthouses
# #     8
# #     +- +- +- 01 +- +- +- +-
# #     +- +- +- +- +- +- +- +-
# #     04 +- +- +- +- +- +- 02
# #     +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- 04 +- +-
# #     +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- 03 +- +-
# #     +- +- +- +- +- +- +- 00
# #     """
#
# # @staticmethod
# # def lighthouses_018():
# #     return f"""
# #     018.lighthouses
# #     8
# #     +- +- +- +- +- +- +- 01
# #     +- +- +- +- +- 01 +- +-
# #     00 +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +-
# #     03+ - +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +-
# #     +- 01 +- 02 +- 01 +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_019():
# #     return f"""
# #     019.lighthouses
# #     9
# #     +- +- +- +- +- +- +- 02 +-
# #     +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +-
# #     +- 04 +- +- +- +- +- +- 01
# #     +- +- +- +- +- +- +- +- +-
# #     +- +- +- 01 +- +- +- +- +-
# #     +- +- +- +- +- +- 03 +- 01
# #     +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- 01 +- +- +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_020():
# #     return f"""
# #     020.lighthouses
# #     9
# #     +- 03 +- +- +- +- +- +- 04
# #     +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- 04
# #     +- +- +- 02 +- +- +- +- +-
# #     01 +- +- +- +- +- +- +- +-
# #     +- +- 01 +- 01 +- +- +- +-
# #     +- +- +- +- +- +- +- +- +-
# #     +- 01 +- +- +- +- +- +- +-
# #     +- +- +- +- +- 01 +- +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_021():
# #     return f"""
# #     021.lighthouses
# #     9
# #     03 +- +- +- +- +- +- +- 02
# #     +- +- +- +- +- +- 01 +- +-
# #     +- +- +- +- +- +- +- +- 02
# #     +- +- 02 +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- 01
# #     +- +- +- +- +- +- +- +- +-
# #     +- +- +- 03 +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +-
# #     +- 02 +- 01 +- +- +- +- 01
# #     """
#
#
# # @staticmethod
# # def lighthouses_022():
# #     return f"""
# #     022.lighthouses
# #     9
# #     02 +- +- +- 01 +- +- +- +-
# #     +- +- 03 +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +-
# #     02 +- +- +- +- +- +- 01 +-
# #     +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- 02
# #     +- +- 04 +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- 00 +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_023():
# #     return f"""
# #     023.lighthouses
# #     9
# #     +- +- +- +- +- +- +- +- +-
# #     +- +- 03 +- 04 +- +- +- +-
# #     +- +- +- +- +- +- +- +- +-
# #     +- +- 01 +- +- +- +- +- +-
# #     +- +- +- +- 03+ - +- +- +-
# #     +- +- +- +- +- +- +- +- +-
# #     04 +- +- +- +- +- +- +- 03
# #     +- +- +- +- +- +- +- +- +-
# #     +- 1+- +- +- +- +- 03 +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_024():
# #     return f"""
# #     024.lighthouses
# #     9
# #     02 +- +- +- +- +- +- +- 03
# #     +- +- +- +- +- +- 03 +- +-
# #     +- +- +- +- 04 +- +- +- +-
# #     +- +- +- +- +- +- +- +- +-
# #     01 +- +- +- +- +- +- +- +-
# #     +- +- 03 +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +-
# #     +- +- +- 02 +- 02 +- +- +-
# #     +- +- +- +- +- +- +- +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_025():
# #     return f"""
# #     025.lighthouses
# #     9
# #     02 +- +- +- +- 01 +- +- +-
# #     +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- 02 +-
# #     +- +- +- +- +- 01 +- +- +-
# #     +- +- +- +- +- +- +- +- 02
# #     +- +- +- +- +- +- 01 +- +-
# #     +- +- 01 +- 00 +- +- +- +-
# #     +- +- +- +- +- +- +- +- +-
# #     +- 01 +- 01 +- +- +- +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_026():
# #     return f"""
# #     026.lighthouses
# #     10
# #     +- +- +- +- +- +- +- +- +- 01
# #     +- +- +- +- +- +- 01 +- +- +-
# #     02 +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- 02 +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- 01
# #     +- +- +- 03 +- +- +- 03 +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     01 +- 02 +- 03 +- +- 02 +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_027():
# #     return f"""
# #     027.lighthouses
# #     10
# #     +- +- +- +- +- +- +- 02 +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- 03 +- +- +- +- +- 01 +- 00
# #     +- +- +- +- +- 02 +- +- +- +-
# #     +- +- +- +- +- +- +- +- 02 +-
# #     +- +- +- 02 +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- 02 +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- 00 +- +- +-
# #     """
#
# # @staticmethod
# # def lighthouses_028():
# #     return f"""
# #     028.lighthouses
# #     10
# #     +- +- +- +- 01 +- +- +- +- +-
# #     01 +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- 02 +- +- +- 01
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- 04 +- +- 02 +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- 01 +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- 02
# #     00 +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- 03 +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_029():
# #     return f"""
# #     029.lighthouses
# #     10
# #     03 +- +- +- +- +- +- +- 05 +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- 01 +- +- +- +- +-
# #     02 +- 01 +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- 01
# #     02 +- +- +- +- 04 +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- 03 +- +- +- +- +- +-
# #     """
#
# # @staticmethod
# # def lighthouses_030():
# #     return f"""
# #     030.lighthouses
# #     10
# #     +- +- 06 +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     02 +- +- +- +- +- +- +- 02 +-
# #     +- +- +- 01 +- +- +- +- +- +-
# #     +- +- +- +- +- 06 +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- 02 +- +- +- +- +- 03 +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- 02 +- +- +- +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_031():
# #     return f"""
# #     031.lighthouses
# #     10
# #     +- +- +- +- +- +- +- +- +- 03
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- 02 +- +- +- +-
# #     +- +- +- 04 +- +- +- 00 +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- 04 +- +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- 03 +- 03 +- +-
# #     +- +- +- +- +- +- +- +- +- +-
# #     01 +- +- +- +- +- +- +- +- +-
# #     """
#
#
# # @staticmethod
# # def lighthouses_032():
# #     return f"""
# #     032.lighthouses
# #     11
# #     +- +- 01 +- 02 +- +- +- 01 +- +-
# #     04 +- +- +- +- +- +- +- +- +- +-
# #     +- +- 02 +- +- +- +- +- +- +- +-
# #     02 +- +- +- +- +- +- +- +- +- +-
# #     +- +- 02 +- 03 +- 02 +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- 02 +- +- +- +- 03
# #     +- +- +- +- +- +- +- +- +- +- +-
# #     +- +- 02 +- +- +- +- +- +- +- +-
# #     02 +- +- +- +- +- +- +- +- +- +-
# #     +- +- 03 +- +- +- +- 04 +- +- +-
# #     """
#
# # @staticmethod
# # def lighthouses_033():
# #     return f"""
# #     033.lighthouses
# #     11
# #     +- +- +- +- +- +- +- +- +- +- 00
# #     +- +- +- +- +- +- +- 02 +- +- +-
# #     01 +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +- 03
# #     +- +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- 01 +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- +- 03
# #     +- +- +- +- +- +- +- +- +- +- +-
# #     +- +- +- +- +- +- +- +- +- 03 +-
# #     +- +- 02 +- 03 +- +- +- +- +- +-
# #     """
