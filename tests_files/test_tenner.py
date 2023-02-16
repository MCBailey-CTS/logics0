# from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
# from techniques.LockedCandidatesPointing import LockedCandidatesPointing
from colorama import Fore, Style

from Loc import Loc
from Puzzle import Puzzle

EXPLICITLY = "EXPLICITLY"



class Tenner(Puzzle):

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)
        self.grid = []
        array = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            array.append(temp)
        array.pop(0)
        array.pop(0)
        for row in range(len(self) + 1):
            temp = []
            split = array[row].replace("-1", "0123456789", -1) \
                .replace("\r", " ", -1) \
                .replace("\t", " ", -1)\
                .replace("  ", " ", -1)\
                .strip().split(' ')

            for t in split:
                if len(t) == 0:
                    continue
                if row != len(self) and t == "00":
                    temp.append("0_________")
                elif row != len(self) and t == "01":
                    temp.append("_1________")
                elif row != len(self) and t == "02":
                    temp.append("__2_______")
                elif row != len(self) and t == "03":
                    temp.append("___3______")
                elif row != len(self) and t == "04":
                    temp.append("____4_____")
                elif row != len(self) and t == "05":
                    temp.append("_____5____")
                elif row != len(self) and t == "06":
                    temp.append("______6___")
                elif row != len(self) and t == "07":
                    temp.append("_______7__")
                elif row != len(self) and t == "08":
                    temp.append("________8_")
                elif row != len(self) and t == "09":
                    temp.append("_________9")
                else:
                    temp.append(t)
            self.grid.append(temp)

    def int_to_cell_string(self, candidate: int) -> str:
        string = ""
        for i in self.expected_candidates():
            if i == candidate:
                string += f'{candidate}'
            else:
                string += '_'
        return string

    @property
    def col_length(self) -> int:
        return 10

    def is_row_house_solved(self, row: int) -> bool:
        solved_candidates = set(
            [self.cell_candidates(loc)[0] for loc in self.house_row_cell_locs(row) if self.is_cell_solved(loc)])
        return solved_candidates.issuperset(self.expected_candidates()) and solved_candidates.issubset(
            self.expected_candidates())

    def is_col_house_solved(self, col: int) -> bool:
        solved_candidates = [
            self.cell_candidates(loc)[0]
            for loc in self.house_col_cell_locs(col)
            if self.is_cell_solved(loc)
        ]
        if len(solved_candidates) != len(self):
            return False
        total = self.total(col)
        if total is None:
            return True
        return sum(solved_candidates) == total

    def is_solved(self) -> bool:
        for row in range(len(self)):
            if not self.is_row_house_solved(row):
                print(f'print bad row: {row}')

                return False

        for col in range(self.col_length):
            if not self.is_col_house_solved(col):
                print(f'print bad col: {col}')
                return False

        for r in range(len(self)):
            for c in range(self.col_length):
                cell = Loc(r, c)
                if not self.is_cell_solved(cell):
                    # print(f'{self.__grid[r][c]}///////////////////////////')
                    return False
                solved_candidate = self.cell_candidates(cell)[0]
                directions = [
                    cell.north(),
                    cell.east(),
                    cell.south(),
                    cell.west(),
                    cell.north().east(),
                    cell.north().west(),
                    cell.south().east(),
                    cell.south().west()
                ]
                for direction in directions:
                    if direction.row < 0 or direction.col < 0:
                        continue
                    if direction.row >= len(self) or direction.col >= 10:
                        continue

                    if not self.is_cell_solved(direction):
                        return False

                    other = self.cell_candidates(direction)[0]

                    if other == solved_candidate:
                        print(f'{cell} {direction}')
                        return False

        return True

    def expected_candidates(self) -> list:
        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __str__(self):
        string = f'{Fore.RED}{self.id()}{Style.RESET_ALL}\n'
        string += f'{len(self)}\n'
        for r in range(len(self) + 1):
            for c in range(self.col_length):

                cell_candidates = self.cell_candidates(Loc(r, c))

                if len(cell_candidates) == 0:
                    string += f'{Fore.GREEN}{self.grid[r][c].ljust(self.col_length)}{Style.RESET_ALL} '
                else:
                    string += f'{self.grid[r][c].ljust(self.col_length)} '
            string += '\n'
        return string

    def house_row_cell_locs(self, loc_row: int|Loc) -> list[Loc]:
        if isinstance(loc_row, Loc):
            return self.house_row_cell_locs(loc_row.row)
        return [Loc(loc_row, col) for col in range(self.col_length)]

    def house_col_cell_locs(self, loc_col: int|Loc) -> list[Loc]:
        if isinstance(loc_col, Loc):
            return self.house_col_cell_locs(loc_col.col)
        return [Loc(row, loc_col) for row in range(len(self))]

    def total(self, col: int) -> int|None:
        string = self.grid[len(self)][col]
        if string.isnumeric():
            return int(string)
        return None

# @pytest.mark.parametrize("puzzle_string, constructor, techniques", [
#
#
#     ('tenner_easier_002', Tenner, Solving.tenner_techniques()),
#     ('tenner_easier_003', Tenner, Solving.tenner_techniques()),
#     ('tenner_easier_004', Tenner, Solving.tenner_techniques()),
#     ('tenner_001', Tenner, Solving.tenner_techniques()),
#     ('tenner_002', Tenner, Solving.tenner_techniques()),
#     ('tenner_003', Tenner, Solving.tenner_techniques()),
#     ('tenner_004', Tenner, Solving.tenner_techniques()),
#     ('tenner_005', Tenner, Solving.tenner_techniques()),
#     ('tenner_006', Tenner, Solving.tenner_techniques()),
#     ('tenner_008', Tenner, Solving.tenner_techniques()),
#     ('tenner_009', Tenner, Solving.tenner_techniques()),
#     ('tenner_019', Tenner, Solving.tenner_techniques()),
#     ('tenner_easier_001', Tenner, Solving.tenner_techniques()),
#
#
# ])
# def test_default_puzzle(puzzle_string, constructor, techniques):
#     # if "\n" in puzzle_string:
#     #     pytest.skip(puzzle_string)
#     result = getattr(Constants, puzzle_string)
#     # puzzle = Tenner(puzzle_string)
#     if default_test_puzzle(result(), constructor, techniques):
#         return
#     assert False

#
# def test_tenner_004():
#     if default_test_puzzle(
#             f"""
#             0_________ 0123456789 _____5____ 0123456789 0123456789 0123456789 _1________ 0123456789 _________9 __2_______
#             ________8_ _1________ 0_________ 0123456789 _______7__ _________9 _____5____ 0123456789 0123456789 ______6___
#             _________9 0123456789 ________8_ _1________ 0123456789 0123456789 0123456789 0123456789 _____5____ 0123456789
#             17         08        13          07         16         23         06         13         17         15
#             """,
#             Tenner,
#             Solving.tenner_techniques()):
#         return
#     assert False






# @staticmethod
# def tenner_001():
#     return f"""
#     001.tenner
#     3
#     0123456789 0123456789 0123456789 ___3______ _______7__ 0_________ ____4_____ _____5____ _1________ __2_______
#     ___3______ _1________ 0123456789 __2_______ 0123456789 ________8_ _________9 _______7__ ____4_____ _____5____
#     ______6___ _______7__ 0123456789 0123456789 _________9 __2_______ _1________ ___3______ 0123456789 0123456789
#     17         17         10         10         22         10         14         15         13         07
#     """

# @staticmethod
# def tenner_002():
#     return f"""
#     002.tenner
#     3
#     _____5____ 0123456789 _______7__ _1________ __2_______ 0123456789 0123456789 ___3______ ______6___ 0123456789
#     _1________ 0123456789 ____4_____ 0123456789 ________8_ _____5____ _________9 _______7__ 0123456789 ___3______
#     ________8_ ___3______ _1________ _________9 0123456789 __2_______ 0123456789 _____5____ ____4_____ 0_________
#     14         18         12         10         17         07         19         15         12         11
#     """

# @staticmethod
# def tenner_003():
#     return f"""
#     003.tenner
#     3
#     0123456789 _______7__ _1________ ________8_ 0123456789 0123456789 ______6___ 0123456789 _____5____ ____4_____
#     0_________ 0123456789 ______6___ _____5____ _1________ 0123456789 _______7__ ___3______ ________8_ 0123456789
#     0123456789 _________9 0123456789 _______7__ ___3______ 0123456789 __2_______ _____5____ 0123456789 0_________
#     09         20         15         20         04         15         15         17         14         06
#     """

# @staticmethod
# def tenner_004():
#     return f"""
#     004.tenner
#     3
#     0_________ 0123456789 _____5____ 0123456789 0123456789 0123456789 _1________ 0123456789 _________9 __2_______
#     ________8_ _1________ 0_________ 0123456789 _______7__ _________9 _____5____ 0123456789 0123456789 ______6___
#     _________9 0123456789 ________8_ _1________ 0123456789 0123456789 0123456789 0123456789 _____5____ 0123456789
#     17         08        13          07         16         23         06         13         17         15
#     """

# @staticmethod
# def tenner_005():
#     return f"""
#     005.tenner
#     3
#     05 -1 -1 08 02 03 -1 -1 -1 -1
#     -1 -1 -1 -1 07 -1 08 05 -1 02
#     -1 00 05 08 04 06 -1 -1 -1 03
#     15 05 14 17 13 09 22 16 19 05
#     """

# @staticmethod
# def tenner_006():
#     return f"""
#     006.tenner
#     3
#     -1 09 07 -1 02 -1 -1 04 -1 06
#     05 06 -1 -1 -1 04 -1 -1 07 00
#     -1 -1 -1 -1 -1 -1 09 -1 03 -1
#     15 22 09 09 19 06 20 09 15 11
#     """

# @staticmethod
# def tenner_007():
#     return f"""
#     007.tenner
#     3
#     -1 03 00 09 -1 07 02 -1 -1 -1
#     02 -1 -1 -1 -1 -1 -1 05 -1 09
#     -1 -1 -1 -1 -1 -1 06 -1 -1 -1
#     16 15 11 19 05 12 09 20 14 14
#     """

# @staticmethod
# def tenner_008():
#     return f"""
#     008.tenner
#     4
#     03 01 -1 07 06 02 -1 05 09 -1
#     06 09 -1 -1 05 -1 -1 -1 -1 03
#     -1 08 -1 -1 02 07 -1 04 -1 06
#     -1 06 -1 -1 01 05 -1 09 02 07
#     16 24 10 28 14 22 05 25 12 24
#     """

# @staticmethod
# def tenner_009():
#     return f"""
#     009.tenner
#     4
#     -1 00 01 07 -1 -1 -1 -1 -1 04
#     -1 -1 02 03 00 07 01 -1 -1 -1
#     03 -1 01 -1 08 06 -1 -1 00 07
#     07 -1 -1 -1 02 -1 -1 01 -1 -1
#     24 21 08 21 16 15 19 16 21 19
#     """

# @staticmethod
# def tenner_010():
#     return f"""
#     010.tenner
#     4
#     -1 04 00 -1 08 06 -1 -1 -1 -1
#     -1 06 -1 -1 03 -1 -1 -1 -1 07
#     -1 07 03 -1 -1 05 -1 -1 -1 -1
#     09 -1 00 -1 03 01 -1 08 -1 -1
#     25 19 08 29 16 12 23 11 23 14
#     """

# @staticmethod
# def tenner_011():
#     return f"""
#     011.tenner
#     4
#     -1 -1 -1 02 -1 -1 -1 05 -1 -1
#     -1 01 06 -1 09 -1 -1 -1 03 -1
#     -1 -1 02 -1 -1 -1 00 -1 08 -1
#     -1 08 01 -1 02 -1 -1 -1 -1 00
#     24 15 18 12 16 26 11 19 26 13
#     """

# @staticmethod
# def tenner_012():
#     return f"""
#     012.tenner
#     4
#     05 06 02 -1 -1 -1 -1 09 -1 -1
#     09 -1 -1 -1 02 -1 04 -1 -1 -1
#     -1 00 -1 -1 -1 -1 -1 -1 -1 -1
#     07 -1 -1 08 06 -1 -1 -1 -1 09
#     24 14 14 25 09 14 16 19 24 21
#     """

# @staticmethod
# def tenner_013():
#     return f"""
#     013.tenner
#     4
#     09 -1 -1 03 -1 -1 02 -1 -1 -1
#     07 -1 -1 06 -1 -1 -1 03 -1 -1
#     -1 -1 -1 -1 07 -1 -1 -1 -1 -1
#     -1 04 06 -1 -1 -1 03 -1 08 -1
#     21 09 17 14 31 11 17 23 15 22
#     """

# @staticmethod
# def tenner_014():
#     return f"""
#     014.tenner
#     5
#     -1 06 00 04 -1 -1 -1 -1 -1 -1
#     -1 01 -1 -1 -1 -1 05 -1 -1 -1
#     -1 -1 -1 -1 03 00 07 08 01 05
#     01 -1 07 09 08 -1 06 03 00 -1
#     09 -1 -1 -1 -1 07 -1 01 -1 -1
#     24 25 15 30 25 19 22 21 21 23
#     """

# @staticmethod
# def tenner_015():
#     return f"""
#     015.tenner
#     5
#     -1 02 -1 -1 -1 -1 -1 -1 04 07
#     -1 -1 01 00 -1 08 07 -1 06 -1
#     -1 -1 02 -1 -1 -1 -1 -1 -1 01
#     -1 -1 08 -1 05 07 06 -1 -1 03
#     -1 -1 -1 04 06 -1 -1 -1 05 -1
#     31 15 18 24 24 26 18 28 17 24
#     """

# @staticmethod
# def tenner_016():
#     return f"""
#     016.tenner
#     5
#     06 -1 03 04 08 -1 -1 01 -1 05
#     -1 -1 -1 -1 -1 -1 -1 -1 -1 06
#     -1 -1 00 -1 05 08 07 -1 -1 -1
#     06 02 -1 08 -1 -1 -1 -1 -1 -1
#     03 -1 -1 09 -1 -1 -1 00 01 -1
#     25 15 11 33 22 30 23 20 21 25
#     """

# @staticmethod
# def tenner_017():
#     return f"""
#     017.tenner
#     5
#     00 07 -1 -1 -1 01 -1 -1 -1 06
#     -1 -1 -1 07 -1 02 -1 -1 -1 -1
#     -1 -1 -1 08 -1 -1 05 09 06 -1
#     -1 -1 -1 -1 -1 -1 -1 -1 00 -1
#     01 02 -1 -1 -1 -1 -1 07 05 08
#     25 16 31 19 30 12 20 26 21 25
#     """

# @staticmethod
# def tenner_018():
#     return f"""
#     018.tenner
#     5
#     -1 04 -1 -1 -1 09 06 -1 -1 -1
#     06 -1 00 07 -1 -1 -1 -1 -1 -1
#     -1 -1 -1 -1 02 -1 09 -1 -1 03
#     05 -1 02 -1 00 06 -1 -1 -1 -1
#     09 -1 -1 06 -1 -1 01 -1 08 00
#     24 20 16 28 13 30 24 27 27 16
#     """

# @staticmethod
# def tenner_019():
#     return f"""
#     019.tenner
#     6
#     05 -1 -1 -1 -1 00 -1 -1 04 -1
#     -1 -1 01 -1 09 -1 04 -1 -1 -1
#     -1 06 -1 05 02 -1 03 08 09 04
#     -1 04 09 -1 00 -1 -1 -1 01 -1
#     02 06 -1 -1 09 05 -1 07 -1 -1
#     09 08 -1 03 00 07 -1 -1 02 -1
#     28 41 16 22 21 28 30 31 26 27
#     """

# @staticmethod
# def tenner_020():
#     return f"""
#     020.tenner
#     6
#     -1 -1 -1 08 02 00 07 -1 -1 06
#     -1 -1 -1 -1 -1 -1 08 02 01 00
#     -1 -1 01 -1 -1 -1 -1 -1 -1 -1
#     -1 08 06 00 -1 04 -1 02 01 -1
#     06 -1 07 -1 03 02 05 -1 -1 00
#     -1 01 00 -1 09 08 -1 -1 05 -1
#     18 26 23 30 33 22 39 25 31 23
#     """

# @staticmethod
# def tenner_021():
#     return f"""
#     021.tenner
#     6
#     -1 00 07 02 -1 09 -1 -1 01 03
#     -1 04 -1 09 01 -1 07 -1 -1 08
#     01 -1 -1 -1 -1 02 -1 -1 07 04
#     02 05 -1 -1 -1 07 00 -1 01 -1
#     -1 -1 -1 -1 -1 -1 04 -1 -1 -1
#     -1 -1 -1 00 03 -1 -1 -1 08 05
#     26 18 25 24 27 30 31 37 19 33
#     """

# @staticmethod
# def tenner_022():
#     return f"""
#     022.tenner
#     6
#     -1 08 -1 -1 -1 09 03 05 06 -1
#     06 -1 -1 05 -1 07 -1 -1 01 -1
#     05 -1 02 -1 04 01 -1 00 -1 -1
#     -1 -1 -1 -1 02 -1 -1 -1 -1 01
#     -1 -1 -1 01 -1 -1 00 -1 -1 -1
#     01 05 -1 04 02 06 08 -1 -1 -1
#     14 41 15 29 26 33 32 27 32 21
#     """

# @staticmethod
# def tenner_023():
#     return f"""
#     023.tenner
#     6
#     -1 00 04 03 -1 -1 05 -1 -1 -1
#     -1 -1 -1 -1 01 00 08 -1 -1 -1
#     04 -1 -1 -1 07 -1 -1 02 -1 03
#     07 -1 -1 -1 -1 -1 00 -1 -1 -1
#     -1 01 04 -1 -1 07 -1 -1 -1 09
#     03 -1 05 01 -1 06 -1 -1 -1 07
#     35 26 25 30 23 25 26 14 29 37
#     """

# @staticmethod
# def tenner_024():
#     return f"""
#     024.tenner
#     6
#     -1 -1 -1 -1 -1 -1 00 09 01 05
#     -1 08 -1 -1 -1 05 -1 -1 07 -1
#     -1 05 -1 02 -1 -1 -1 01 -1 -1
#     -1 -1 -1 -1 -1 06 -1 09 05 07
#     08 -1 00 -1 09 -1 05 -1 -1 -1
#     07 03 -1 -1 -1 -1 -1 -1 -1 01
#     33 22 13 34 26 41 22 29 32 18
#     """

# @staticmethod
# def tenner_challenging_001():
#     return f"""
#     challenging_001.tenner
#     4
#     __ __ 03 __ 05 __ __ __ 06 __
#     06 __ 05 09 03 08 __ __ __ __
#     __ 00 __ __ __ __ 06 __ 08 05
#     02 05 __ 09 __ __ __ __ 03 __
#     18 12 19 27 18 19 15 17 19 16
#     """

# @staticmethod
# def tenner_challenging_002():
#     return f"""
#     challenging_002.tenner
#     3
#     __ __ __ __ __ __ __ __ __ __
#     __ 04 __ __ __ 09 __ __ 02 __
#     __ 01 09 05 08 04 __ 07 06 03
#     13 14 20 13 13 18 10 14 12 08
#     """

# @staticmethod
# def tenner_challenging_003():
#     return f"""
#     challenging_003.tenner
#     5
#     __ 07 __ __ 04 02 08 __ __ __
#     09 __ __ 07 __ 00 __ 06 08 __
#     __ __ __ 08 03 04 __ __ 07 09
#     __ 01 03 __ __ __ __ __ 06 __
#     05 __ 02 __ 04 00 __ __ __ __
#     19 24 17 30 14 11 28 27 28 27
#     """

# @staticmethod
# def tenner_challenging_004():
#     return f"""
#     challenging_004.tenner
#     6
#     __ 09 05 __ __ __ __ 02 08 04
#     05 __ __ __ 09 __ 04 06 __ __
#     07 __ 04 __ 05 __ __ __ __ 08
#     __ __ __ __ 07 __ 01 08 05 04
#     __ __ __ 06 __ __ 03 04 07 __
#     __ 06 __ __ 09 __ 05 __ __ 02
#     35 26 26 26 35 16 22 29 29 26
#     """

# @staticmethod
# def tenner_easier_001():
#     return f"""
#     easier_001.tenner
#     3
#     0123456789 _________9 ____4_____ 0123456789 0123456789 _______7__ 0123456789 ___3______ 0123456789 0123456789
#     ____4_____ ________8_ 0123456789 __2_______ 0123456789 _1________ 0123456789 _______7__ 0_________ ___3______
#     0123456789 _________9 ____4_____ 0123456789 0123456789 0123456789 ___3______ __2_______ _1________ 0123456789
#     13 26 14 02 20 14 16 12 06 12
#     """

# @staticmethod
# def tenner_easier_002():
#     return f"""
#     easier_002.tenner
#     6
#     01 05 04 07 -1 -1 -1 -1 02 -1
#     -1 -1 -1 05 08 01 02 07 04 -1
#     -1 -1 04 07 02 09 -1 -1 -1 01
#     03 -1 01 08 -1 -1 02 06 -1 04
#     00 09 06 02 01 03 04 05 -1 07
#     05 -1 01 -1 -1 06 08 07 03 09
#     18 28 22 33 20 27 19 41 26 36
#     """

# @staticmethod
# def tenner_easier_003():
#     return f"""
#     easier_003.tenner
#     4
#     -1 04 -1 00 -1 09 -1 08 -1 05
#     -1 07 -1 01 06 -1 -1 03 -1 08
#     02 05 -1 07 -1 01 06 09 00 04
#     -1 -1 02 -1 09 -1 03 -1 -1 06
#     05 23 25 09 25 23 15 24 08 23
#     """

# @staticmethod
# def tenner_easier_004():
#     return f"""
#     easier_004.tenner
#     5
#     04 -1 -1 00 08 06 -1 -1 07 -1
#     -1 01 06 09 03 -1 07 -1 02 08
#     -1 04 -1 01 -1 -1 -1 -1 09 -1
#     01 06 -1 08 -1 09 07 02 -1 04
#     07 04 -1 02 01 06 05 09 08 03
#     20 18 13 20 19 27 25 32 31 20
#     """

# @staticmethod
# def tenner_harder_001():
#     return f"""
#     harder_001.tenner
#     3
#     -1 06 02 -1 -1 -1 04 -1 -1 -1
#     -1 -1 08 -1 -1 -1 -1 -1 -1 -1
#     -1 07 -1 -1 -1 -1 -1 01 04 00
#     11 14 13 20 13 06 16 15 11 16
#     """

# @staticmethod
# def tenner_harder_002():
#     return f"""
#     harder_002.tenner
#     4
#     -1 -1 -1 -1 -1 -1 -1 07 -1 -1
#     03 01 -1 -1 -1 -1 -1 -1 00 06
#     -1 -1 -1 06 -1 01 02 -1 -1 -1
#     -1 04 03 -1 -1 00 -1 -1 09 08
#     16 18 16 16 22 15 13 24 14 26
#     """

# @staticmethod
# def tenner_harder_003():
#     return f"""
#     harder_003.tenner
#     5
#     08 -1 -1 01 05 -1 03 -1 09 -1
#     04 01 -1 -1 -1 -1 -1 -1 -1 -1
#     -1 -1 -1 07 00 -1 04 -1 -1 03
#     -1 -1 09 -1 03 08 -1 -1 07 -1
#     -1 -1 -1 08 -1 07 -1 -1 -1 00
#     16 17 27 25 18 26 25 22 30 19
#     """

# @staticmethod
# def tenner_harder_004():
#     return f"""
#     harder_004.tenner
#     6
#     01 -1 -1 00 -1 -1 05 07 -1 -1
#     02 -1 -1 -1 03 08 -1 -1 -1 -1
#     01 -1 -1 -1 07 -1 -1 03 -1 02
#     -1 -1 -1 -1 03 04 -1 09 01 -1
#     -1 09 -1 -1 -1 -1 05 -1 -1 02
#     00 -1 02 04 -1 01 07 -1 06 -1
#     19 30 26 19 31 30 34 28 28 25
#     """
