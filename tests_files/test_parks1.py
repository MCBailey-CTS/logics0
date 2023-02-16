import pytest
from colorama import Fore, Style

from Loc import Loc
from Puzzle import Puzzle
from _defaults import default_test_puzzle
from tech import tech
from techniques.Parks1Shapes import Parks1Shapes
from techniques.Parks1XWing import Parks1XWing

EXPLICITLY = "EXPLICITLY"


class Parks1(Puzzle):
    def expected_candidates(self) -> list:
        return [0, 1]

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)
        self.grid = []
        self.__color_fence_dict = {
            'a': Fore.RED,
            'b': Fore.CYAN,
            'c': Fore.GREEN,
            'd': Fore.LIGHTBLUE_EX,
            'e': Fore.LIGHTMAGENTA_EX,
            'f': Fore.LIGHTGREEN_EX,
            'g': Fore.LIGHTWHITE_EX,
            'h': Fore.LIGHTYELLOW_EX,
            'i': Fore.LIGHTRED_EX,
            'j': Fore.YELLOW,
            'k': Fore.RED
        }
        array = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            array.append(temp)
        array.pop(0)
        array.pop(0)
        for line in array:
            self.grid.append(line.split(" "))

    def is_solved(self) -> bool:
        houses = []
        for house in self.houses_rows():
            houses.append(house)
        for house in self.houses_cols():
            houses.append(house)
        fence_dict = {}
        # for house in puzzle.
        for r in range(len(self)):
            for c in range(len(self)):
                loc = Loc(r, c)
                fence = self.cell_fence(loc)
                if fence not in fence_dict:
                    fence_dict[fence] = []
                fence_dict[fence].append(loc)

        for fence in fence_dict.keys():
            fence_locs = fence_dict[fence]
            houses.append(fence_locs)
        for house in houses:
            solved_empty = [loc for loc in house if
                            len(self.cell_candidates(loc)) == 1 and self.cell_candidates(loc)[0] == 0]
            solved_tree = [loc for loc in house if
                           len(self.cell_candidates(loc)) == 1 and self.cell_candidates(loc)[0] == 1]
            unsolved = list(set(house).difference(solved_tree + solved_empty))
            if len(solved_tree) == 1:
                continue
            if len(unsolved) != 0:
                return False

        for r in range(len(self)):
            for c in range(len(self)):
                loc = Loc(r, c)
                candidates0 = self.cell_candidates(loc)
                if len(candidates0) != 1 or candidates0[0] != 1:
                    continue
                directions = [
                    loc.north().west(),
                    loc.north().east(),
                    loc.south().west(),
                    loc.south().east(),
                ]

                for direction in directions:
                    if not direction.is_valid_parks(self.grid):
                        continue
                    candidates1 = self.cell_candidates(direction)
                    if len(candidates1) != 1:
                        return False
                    if candidates1[0] == 1 and candidates0[0] == 1:
                        return False

        return True

    def color_fence(self, loc: Loc) -> str:

        return self.__color_fence_dict[self.cell_fence(loc)]

    def __str__(self) -> str:
        string = f'{Fore.LIGHTCYAN_EX}########################\n'
        string += f'{self.id()}\n'
        string += f'{len(self)}\n'
        for r in range(len(self)):
            for c in range(len(self)):
                loc = Loc(r, c)
                grid_string = self.grid[r][c]
                candidates = "".join([char for char in grid_string if not char.isalpha()])
                # fence = [char for char in grid_string if char.isalpha()][0]
                # string += f'{self.color_fence(loc)}{candidates}{fence}{Style.RESET_ALL} '
                # fence = [char for char in grid_string if char.isalpha()][0]
                string += f'{self.color_fence(loc)}{candidates}{self.cell_fence(loc)}{Style.RESET_ALL} '
            string += '\n'
        string += f'{Fore.CYAN}########################\n{Style.RESET_ALL}'
        return string


def parks1_techniques() -> list:
    return [
        tech.Parks1CrossHatch(),
        tech.Parks1HiddenSingle(),
        tech.Parks1CrossHatchTouching(),
        tech.Parks1LockedCandidatesPointing(),
        tech.Parks1LockedCandidatesClaiming(),
        tech.Parks1Bent3(),
        tech.Parks1Shape_00_01(),
        Parks1Shapes(),
        tech.Parks1DominateFence(),
        Parks1XWing()
    ]


# @staticmethod
# def parks1_explicit_cross_hatch_actual():
#     return f"""
#     parks1_explicit_cross_hatch_actual.parks1
#     5
#     10a 10a 10c 10d 10e
#     10a 10a 10c 10c 10e
#     10b 1_a 10c 10e 10e
#     10b 10b 10b 10e 10e
#     10b 10b 10b 10b 10b
#     """

# @staticmethod
# def parks1_explicit_cross_hatch_expected():
#     return f"""
#     parks1_explicit_cross_hatch_expected.parks1
#     5
#     _0a _0a 10c 10d 10e
#     _0a _0a _0c 10c 10e
#     _0b 1_a _0c _0e _0e
#     _0b _0b _0b 10e 10e
#     10b _0b 10b 10b 10b
#     """

# @staticmethod
# def parks1_explicit_hidden_single_actual():
#     return f"""
#     parks1_explicit_hidden_single_actual.parks1
#     5
#     _0a _0a _0c _0d 10e
#     _0a 10a 10c _0c 10e
#     10b _0a 10c _0e 10e
#     10b 10b 10b 10e 10e
#     10b 10b 10b _0b 10b
#     """

# @staticmethod
# def parks1_explicit_hidden_single_expected():
#     return f"""
#     parks1_explicit_hidden_single_expected.parks1
#     5
#     _0a _0a _0c _0d 1_e
#     _0a 1_a 10c _0c 10e
#     10b _0a 10c _0e 10e
#     10b 10b 10b 1_e 10e
#     10b 10b 10b _0b 10b
#     """


# @pytest.mark.parametrize("puzzle_string, constructor, techniques", [


#     ('parks1_001', Parks1, parks1_techniques()),
#     ('parks1_002', Parks1, parks1_techniques()),
#     ('parks1_003', Parks1, parks1_techniques()),
#     ('parks1_006', Parks1, parks1_techniques()),
#     ('parks1_007', Parks1, parks1_techniques()),
#     ('parks1_008', Parks1, parks1_techniques()),
#     ('parks1_beach_001', Parks1, parks1_techniques()),
#     ('parks1_beach_002', Parks1, parks1_techniques()),
#     ('parks1_beach_003', Parks1, parks1_techniques()),
#     ('parks1_beach_004', Parks1, parks1_techniques()),
#     ('parks1_maui_001', Parks1, parks1_techniques()),
#     ('parks1_spring_001', Parks1, parks1_techniques()),
#     ('parks1_spring_002', Parks1, parks1_techniques()),
#     ('parks1_spring_003', Parks1, parks1_techniques()),
#     ('parks1_spring_004', Parks1, parks1_techniques()),
#     ('parks1_spring_005', Parks1, parks1_techniques()),
#     ('parks1_spring_006', Parks1, parks1_techniques()),
#     ('parks1_spring_007', Parks1, parks1_techniques()),
#     ('parks1_spring_008', Parks1, parks1_techniques()),
#
#
#     ("parks1_011", Parks1, parks1_techniques()),
#     ("parks1_012", Parks1, parks1_techniques()),
#     ("parks1_013", Parks1, parks1_techniques()),
#     ("parks1_014", Parks1, parks1_techniques()),
#     ("parks1_spring_009", Parks1, parks1_techniques()),
#     ("parks1_spring_010", Parks1, parks1_techniques()),
#     ("parks1_spring_011", Parks1, parks1_techniques()),
#     ("parks1_spring_012", Parks1, parks1_techniques()),
#     ("parks1_spring_013", Parks1, parks1_techniques()),
#     ("parks1_spring_014", Parks1, parks1_techniques()),
#     ("parks1_spring_015", Parks1, parks1_techniques()),
#     ("parks1_spring_017", Parks1, parks1_techniques()),
#     ("parks1_spring_018", Parks1, parks1_techniques()),
#     ("parks1_spring_019", Parks1, parks1_techniques()),
#     ("parks1_spring_020", Parks1, parks1_techniques()),
#     ("parks1_spring_021", Parks1, parks1_techniques()),
#     ("parks1_spring_022", Parks1, parks1_techniques()),
#     ("parks1_spring_023", Parks1, parks1_techniques()),
#     ("parks1_spring_024", Parks1, parks1_techniques()),
#     ("parks1_spring_025", Parks1, parks1_techniques()),
#     ("parks1_spring_026", Parks1, parks1_techniques()),
#     ('parks1_005', Parks1, parks1_techniques()),
#     ("parks1_spring_028", Parks1, parks1_techniques()),
#     ("parks1_spring_029", Parks1, parks1_techniques()),
#     ("parks1_spring_030", Parks1, parks1_techniques()),
#     ("parks1_spring_031", Parks1, parks1_techniques()),
#     ("parks1_spring_032", Parks1, parks1_techniques()),
#     ("parks1_spring_033", Parks1, parks1_techniques()),
#     ("parks1_spring_034", Parks1, parks1_techniques()),
#     ("parks1_spring_039", Parks1, parks1_techniques()),
#     ("parks1_spring_045", Parks1, parks1_techniques()),
#     ("parks1_spring_047", Parks1, parks1_techniques()),
#     ("parks1_spring_062", Parks1, parks1_techniques()),
#     ("parks1_winter_049", Parks1, parks1_techniques()),
#
#
# ])
# def test_default_puzzle(puzzle_string, constructor, techniques):
#     if "\n" in puzzle_string:
#         pytest.skip(puzzle_string)
#     result = getattr(Constants, puzzle_string)
#     assert default_test_puzzle(result(), constructor, techniques)


# def test_robot_fences_020():
#     puzzle_string = f"""
#
#     """assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())
#     
#     assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_001():
    puzzle_string = f"""
    001.parks1
    5
    10a 10a 10b 10e 10d
    10a 10a 10b 10b 10d
    10c 10a 10b 10d 10d
    10c 10c 10c 10d 10d
    10c 10c 10c 10c 10c
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_002():
    puzzle_string = f"""
    002.parks1
    5
    10a 10a 10a 10a 10a
    10b 10a 10a 10a 10e
    10a 10a 10a 10d 10e
    10a 10c 10d 10d 10e
    10a 10c 10d 10d 10d
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_003():
    puzzle_string = f"""
    003.parks1
    5
    10a 10a 10d 10d 10d
    10a 10a 10d 10d 10d
    10b 10d 10d 10d 10d
    10b 10c 10c 10e 10e
    10b 10b 10e 10e 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_004():
    puzzle_string = f"""
    004.parks1
    5
    10a 10a 10e 10e 10e
    10a 10a 10b 10e 10e
    10b 10b 10b 10d 10e
    10b 10c 10c 10d 10e
    10b 10c 10d 10d 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_005():
    puzzle_string = f"""
    005.parks1
    5
    10a 10a 10a 10b 10b
    10a 10b 10b 10b 10e
    10a 10c 10c 10e 10e
    10c 10c 10e 10e 10d
    10c 10d 10d 10d 10d
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_006():
    puzzle_string = f"""
    006.parks1
    5
    10a 10a 10a 10d 10d
    10a 10b 10d 10d 10d
    10b 10b 10d 10d 10d
    10c 10c 10d 10e 10e
    10c 10e 10e 10e 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_007():
    puzzle_string = f"""
    007.parks1
    6
    10a 10a 10f 10f 10f 10f
    10a 10a 10f 10f 10f 10f
    10a 10a 10d 10d 10f 10f
    10a 10d 10d 10d 10e 10f
    10b 10d 10d 10d 10e 10f
    10b 10b 10b 10c 10c 10c
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_008():
    puzzle_string = f"""
    008.parks1
    6
    10a 10a 10b 10d 10d 10d
    10a 10a 10d 10d 10d 10d
    10a 10a 10c 10c 10d 10f
    10a 10f 10f 10f 10f 10f
    10a 10f 10f 10f 10e 10f
    10f 10f 10f 10f 10f 10f
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_009():
    puzzle_string = f"""
    009.parks1
    6
    10a 10b 10b 10b 10f 10f
    10a 10b 10b 10b 10f 10f
    10a 10a 10a 10f 10f 10f
    10a 10c 10d 10f 10f 10f
    10c 10c 10d 10f 10f 10e
    10c 10c 10f 10f 10e 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_010():
    puzzle_string = f"""
    010.parks1
    6
    10a 10a 10c 10c 10c 10c
    10a 10c 10c 10f 10d 10c
    10a 10c 10c 10f 10d 10d
    10b 10b 10f 10f 10e 10d
    10b 10f 10f 10e 10e 10d
    10b 10b 10b 10e 10e 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_011():
    puzzle_string = f"""
    011.parks1
    6
    10c 10c 10c 10e 10e 10e
    10c 10c 10c 10e 10e 10e
    10c 10d 10d 10f 10e 10e
    10f 10f 10f 10f 10f 10f
    10f 10f 10a 10a 10f 10f
    10a 10a 10a 10b 10b 10f
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_012():
    puzzle_string = f"""
    012.parks1
    6
    10a 10a 10a 10a 10e 10e
    10a 10a 10b 10e 10e 10e
    10a 10a 10f 10f 10f 10e
    10a 10f 10f 10c 10c 10d
    10f 10f 10f 10f 10c 10c
    10f 10f 10f 10c 10c 10c
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_013():
    puzzle_string = f"""
    013.parks1
    6
    10b 10c 10c 10c 10d 10a
    10b 10c 10a 10c 10d 10a
    10b 10a 10a 10a 10a 10a
    10a 10a 10a 10a 10a 10a
    10e 10f 10f 10a 10f 10f
    10e 10e 10f 10f 10f 10f
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_014():
    puzzle_string = f"""
    014.parks1
    7
    10g 10g 10g 10g 10b 10b 10b
    10g 10g 10e 10g 10c 10c 10b
    10g 10f 10e 10d 10d 10c 10b
    10g 10f 10e 10e 10d 10c 10c
    10g 10f 10f 10e 10d 10a 10a
    10g 10g 10a 10a 10a 10a 10a
    10a 10a 10a 10a 10a 10a 10a
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_beach_001():
    puzzle_string = f"""
    beach_001.parks1
    5
    10a 10a 10a 10a 10a
    10b 10a 10a 10a 10a
    10b 10c 10d 10e 10e
    10c 10c 10c 10e 10e
    10c 10c 10c 10e 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_beach_002():
    puzzle_string = f"""
    beach_002.parks1
    5
    10a 10a 10a 10c 10c
    10a 10a 10c 10d 10c
    10b 10a 10c 10c 10c
    10b 10b 10c 10e 10e
    10b 10b 10b 10b 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_beach_003():
    puzzle_string = f"""
    beach_003.parks1
    5
    10a 10d 10d 10d 10e
    10a 10d 10d 10d 10e
    10a 10a 10d 10d 10e
    10a 10a 10c 10c 10e
    10b 10c 10c 10c 10c
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_beach_004():
    puzzle_string = f"""
    beach_004.parks1
    5
    10a 10a 10a 10a 10a
    10a 10a 10a 10e 10e
    10a 10c 10c 10c 10e
    10b 10c 10c 10d 10c
    10b 10b 10c 10c 10c
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_maui_001():
    puzzle_string = f"""
    maui_001.parks1
    12
    10a 10a 10a 10a 10a 10a 10a 10i 10i 10i 10i 10i
    10a 10a 10a 10a 10a 10a 10a 10a 10a 10i 10i 10i
    10a 10b 10b 10d 10d 10a 10a 10a 10a 10i 10i 10l
    10c 10e 10e 10d 10d 10h 10a 10h 10i 10i 10i 10l
    10c 10d 10e 10d 10d 10h 10h 10h 10h 10i 10i 10l
    10c 10d 10d 10d 10d 10h 10h 10h 10h 10i 10i 10l
    10f 10f 10f 10f 10h 10h 10h 10h 10k 10k 10k 10l
    10f 10f 10f 10f 10g 10g 10h 10h 10k 10k 10k 10k
    10f 10f 10f 10f 10g 10g 10j 10j 10k 10k 10k 10k
    10f 10f 10f 10f 10j 10j 10j 10j 10k 10k 10k 10k
    10f 10f 10f 10j 10j 10j 10j 10j 10k 10k 10k 10k
    10f 10f 10f 10j 10j 10j 10k 10k 10k 10k 10k 10k
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_001():
    puzzle_string = f"""
    spring_001.parks1
    5
    10a 10e 10e 10e 10e
    10a 10a 10e 10e 10e
    10a 10b 10c 10e 10e
    10a 10c 10c 10c 10d
    10c 10c 10c 10d 10d
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_002():
    puzzle_string = f"""
    spring_002.parks1
    5
    10a 10a 10a 10a 10a
    10b 10a 10a 10a 10a
    10b 10b 10a 10d 10d
    10b 10c 10c 10d 10e
    10b 10b 10c 10c 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_003():
    puzzle_string = f"""
    spring_003.parks1
    5
    10a 10a 10b 10d 10d
    10a 10b 10b 10c 10c
    10b 10b 10b 10c 10c
    10b 10b 10b 10c 10e
    10b 10c 10c 10c 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_004():
    puzzle_string = f"""
    spring_004.parks1
    5
    10a 10a 10a 10d 10d
    10a 10a 10a 10d 10d
    10a 10a 10a 10d 10e
    10b 10b 10b 10d 10e
    10b 10b 10c 10c 10c
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_005():
    puzzle_string = f"""
    spring_005.parks1
    5
    10a 10a 10d 10d 10e
    10a 10a 10a 10e 10e
    10a 10a 10a 10e 10e
    10a 10b 10e 10e 10e
    10b 10b 10c 10c 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_006():
    puzzle_string = f"""
    spring_006.parks1
    5
    10a 10a 10a 10a 10a
    10b 10a 10a 10a 10e
    10b 10c 10a 10a 10a
    10b 10c 10c 10d 10a
    10c 10c 10c 10d 10a
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_007():
    puzzle_string = f"""
    spring_007.parks1
    5
    10a 10a 10a 10d 10d
    10a 10a 10c 10d 10d
    10a 10a 10c 10d 10d
    10a 10a 10c 10d 10e
    10b 10b 10b 10b 10b
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_008():
    puzzle_string = f"""
    spring_008.parks1
    5
    10a 10a 10b 10b 10b
    10a 10a 10b 10b 10b
    10b 10b 10b 10d 10e
    10b 10c 10e 10e 10e
    10c 10c 10e 10e 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_009():
    puzzle_string = f"""
    spring_009.parks1
    5
    10a 10c 10c 10c 10c
    10a 10c 10c 10c 10c
    10a 10c 10d 10d 10d
    10a 10a 10d 10e 10e
    10b 10b 10b 10b 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_010():
    puzzle_string = f"""
    spring_010.parks1
    5
    10a 10a 10d 10d 10d
    10b 10c 10d 10d 10d
    10b 10c 10c 10d 10e
    10b 10c 10e 10e 10e
    10b 10e 10e 10e 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_011():
    puzzle_string = f"""
    spring_011.parks1
    5
    10a 10e 10e 10e 10e
    10a 10e 10e 10e 10e
    10a 10b 10b 10d 10e
    10b 10b 10c 10d 10d
    10b 10b 10c 10d 10d
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_012():
    puzzle_string = f"""
    spring_012.parks1
    5
    10a 10a 10c 10c 10c
    10a 10b 10c 10d 10e
    10a 10b 10c 10d 10e
    10a 10d 10d 10d 10e
    10d 10d 10d 10d 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_013():
    puzzle_string = f"""
    spring_013.parks1
    5
    10a 10a 10d 10d 10e
    10a 10a 10b 10d 10e
    10b 10b 10b 10d 10d
    10b 10b 10b 10b 10b
    10c 10c 10c 10c 10b
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_014():
    puzzle_string = f"""
    spring_014.parks1
    5
    10a 10c 10c 10c 10c
    10a 10c 10c 10c 10c
    10b 10b 10c 10d 10e
    10b 10b 10d 10d 10e
    10b 10b 10b 10b 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_015():
    puzzle_string = f"""
    spring_015.parks1
    5
    10a 10a 10d 10e 10e
    10a 10a 10d 10e 10e
    10a 10a 10b 10c 10c
    10b 10b 10b 10c 10c
    10b 10c 10c 10c 10c
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_spring_016():
    puzzle_string = f"""
    spring_016.parks1
    5
    10a 10a 10a 10b 10b
    10a 10a 10a 10b 10b
    10c 10d 10d 10d 10c
    10c 10c 10c 10c 10c
    10e 10c 10c 10c 10c
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_017():
    puzzle_string = f"""
    spring_017.parks1
    5
    10a 10d 10d 10d 10d
    10a 10d 10d 10d 10e
    10a 10a 10b 10e 10e
    10b 10b 10b 10e 10e
    10c 10c 10c 10e 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_018():
    puzzle_string = f"""
    spring_018.parks1
    5
    10a 10d 10d 10d 10e
    10a 10c 10c 10e 10e
    10a 10a 10c 10c 10e
    10b 10a 10b 10e 10e
    10b 10b 10b 10b 10b
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_019():
    puzzle_string = f"""
    spring_019.parks1
    5
    10a 10a 10a 10a 10c
    10a 10a 10c 10c 10c
    10a 10a 10c 10e 10e
    10b 10c 10c 10d 10e
    10b 10b 10d 10d 10d
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_020():
    puzzle_string = f"""
    spring_020.parks1
    5
    10a 10a 10a 10e 10e
    10a 10a 10e 10e 10e
    10a 10a 10e 10d 10e
    10b 10b 10c 10d 10d
    10b 10b 10c 10d 10d
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_021():
    puzzle_string = f"""
    spring_021.parks1
    5
    10a 10a 10a 10d 10e
    10a 10b 10a 10d 10e
    10a 10b 10a 10d 10e
    10b 10b 10c 10e 10e
    10b 10c 10c 10c 10c
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_022():
    puzzle_string = f"""
    spring_022.parks1
    5
    10b 10d 10d 10e 10e
    10b 10b 10d 10e 10e
    10a 10b 10c 10c 10e
    10a 10b 10c 10c 10c
    10a 10a 10a 10a 10c
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_023():
    puzzle_string = f"""
    spring_023.parks1
    5
    10a 10d 10d 10d 10d
    10a 10d 10d 10d 10d
    10a 10a 10c 10e 10e
    10b 10c 10c 10e 10e
    10b 10b 10c 10e 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_024():
    puzzle_string = f"""
    spring_024.parks1
    5
    10a 10a 10a 10e 10e
    10a 10a 10a 10e 10e
    10a 10a 10a 10d 10e
    10b 10c 10c 10d 10e
    10b 10b 10c 10d 10d
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_025():
    puzzle_string = f"""
    spring_025.parks1
    5
    10c 10c 10e 10e 10e
    10b 10c 10c 10c 10e
    10b 10b 10d 10d 10e
    10a 10b 10b 10d 10d
    10a 10a 10a 10a 10d
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_026():
    puzzle_string = f"""
    spring_026.parks1
    5
    10a 10a 10a 10a 10e
    10a 10b 10b 10e 10e
    10a 10b 10b 10d 10d
    10b 10b 10b 10c 10d
    10b 10c 10c 10c 10c
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_spring_027():
    puzzle_string = f"""
    spring_027.parks1
    5
    10a 10a 10a 10d 10d
    10b 10b 10a 10d 10d
    10c 10b 10c 10d 10e
    10c 10b 10c 10d 10e
    10c 10c 10c 10e 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_028():
    puzzle_string = f"""
    spring_028.parks1
    5
    10a 10a 10b 10b 10d
    10a 10b 10b 10d 10d
    10a 10b 10e 10e 10e
    10c 10b 10b 10c 10e
    10c 10c 10c 10c 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_029():
    puzzle_string = f"""
    spring_029.parks1
    5
    10a 10a 10a 10a 10d
    10a 10c 10c 10d 10d
    10a 10c 10d 10d 10e
    10b 10c 10c 10d 10e
    10b 10b 10b 10e 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_030():
    puzzle_string = f"""
    spring_030.parks1
    6
    10a 10a 10a 10a 10f 10f
    10a 10a 10a 10d 10f 10f
    10a 10a 10a 10e 10e 10f
    10a 10a 10a 10e 10e 10e
    10b 10e 10e 10e 10e 10e
    10c 10c 10c 10c 10c 10c
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_031():
    puzzle_string = f"""
    spring_031.parks1
    6
    10a 10a 10a 10e 10e 10e
    10a 10a 10a 10e 10f 10e
    10b 10b 10b 10d 10f 10f
    10c 10b 10c 10d 10d 10d
    10c 10c 10c 10c 10c 10d
    10c 10c 10c 10c 10c 10d
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_032():
    puzzle_string = f"""
    spring_032.parks1
    6
    10a 10a 10a 10a 10e 10e
    10b 10b 10b 10a 10a 10e
    10b 10b 10c 10c 10e 10e
    10b 10b 10c 10c 10e 10f
    10c 10c 10c 10d 10d 10f
    10c 10d 10d 10d 10f 10f
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_033():
    puzzle_string = f"""
    spring_033.parks1
    6
    10a 10a 10a 10e 10e 10e
    10a 10b 10a 10a 10e 10e
    10a 10b 10a 10e 10e 10f
    10b 10b 10c 10c 10e 10f
    10b 10c 10c 10d 10d 10f
    10b 10d 10d 10d 10f 10f
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_034():
    puzzle_string = f"""
    spring_034.parks1
    5
    10c 10c 10e 10e 10e
    10b 10c 10c 10c 10e
    10b 10b 10d 10d 10e
    10a 10b 10b 10d 10d
    10a 10a 10a 10a 10d
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_039():
    puzzle_string = f"""
    spring_039.parks1
    7
    10a 10b 10b 10e 10e 10e 10e
    10a 10b 10c 10e 10e 10e 10e
    10c 10c 10c 10e 10e 10e 10f
    10c 10c 10c 10d 10g 10g 10f
    10c 10d 10c 10d 10d 10g 10f
    10d 10d 10d 10d 10d 10d 10f
    10d 10d 10d 10d 10f 10f 10f
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_045():
    puzzle_string = f"""
    spring_045.parks1
    7
    10a 10a 10a 10a 10a 10f 10f
    10a 10f 10f 10f 10f 10f 10g
    10a 10a 10e 10e 10e 10f 10g
    10a 10a 10e 10d 10e 10g 10g
    10c 10c 10c 10d 10d 10g 10g
    10b 10b 10c 10c 10c 10g 10g
    10b 10b 10g 10g 10g 10g 10g
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_spring_046():
    puzzle_string = f"""
    spring_046.parks1
    7
    10a 10d 10d 10d 10d 10d 10d
    10a 10a 10a 10d 10e 10e 10d
    10b 10b 10d 10d 10e 10d 10d
    10b 10d 10d 10f 10f 10d 10d
    10d 10c 10d 10d 10g 10g 10d
    10d 10c 10c 10d 10g 10g 10d
    10d 10d 10d 10d 10d 10g 10g
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_047():
    puzzle_string = f"""
    spring_047.parks1
    7
    10a 10a 10a 10a 10a 10f 10f
    10a 10f 10f 10f 10f 10f 10g
    10a 10a 10e 10e 10e 10f 10g
    10a 10a 10e 10d 10e 10g 10g
    10c 10c 10c 10d 10d 10g 10g
    10b 10b 10c 10c 10c 10g 10g
    10b 10b 10g 10g 10g 10g 10g
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_spring_051():
    puzzle_string = f"""
    spring_051.parks1
    8
    10a 10a 10a 10b 10b 10b 10e 10e
    10a 10b 10a 10b 10b 10b 10e 10e
    10b 10b 10b 10b 10b 10e 10e 10h
    10b 10b 10b 10b 10b 10b 10h 10h
    10c 10c 10c 10b 10b 10f 10h 10h
    10c 10c 10c 10b 10f 10f 10g 10g
    10d 10c 10c 10d 10d 10f 10f 10g
    10d 10d 10d 10d 10f 10f 10f 10f
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_spring_062():
    puzzle_string = f"""
    spring_062.parks1
    8
    10a 10a 10c 10c 10h 10h 10h 10h
    10a 10a 10a 10a 10h 10h 10h 10h
    10a 10a 10b 10a 10h 10h 10h 10h
    10d 10d 10e 10e 10e 10h 10h 10h
    10d 10d 10e 10g 10g 10g 10h 10h
    10d 10d 10e 10f 10f 10g 10f 10f
    10d 10d 10d 10f 10f 10f 10f 10f
    10d 10d 10d 10d 10f 10f 10f 10f
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_winter_037():
    puzzle_string = f"""
    winter_037.parks1
    7
    10a 10b 10c 10c 10c 10d 10d
    10a 10b 10a 10a 10c 10d 10d
    10a 10a 10a 10a 10a 10d 10g
    10a 10e 10e 10e 10g 10d 10g
    10e 10e 10g 10g 10g 10g 10g
    10e 10e 10g 10e 10f 10f 10g
    10e 10e 10e 10e 10e 10f 10g
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_winter_038():
    puzzle_string = f"""
    winter_038.parks1
    7
    10a 10a 10a 10a 10a 10a 10e
    10a 10b 10b 10d 10d 10e 10e
    10b 10b 10b 10f 10d 10f 10f
    10b 10b 10b 10f 10d 10f 10g
    10c 10c 10b 10f 10f 10f 10g
    10c 10b 10b 10b 10b 10g 10g
    10c 10b 10b 10b 10b 10b 10g
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_winter_039():
    puzzle_string = f"""
    winter_039.parks1
    7
    10a 10e 10e 10e 10f 10g 10g
    10a 10a 10e 10e 10f 10g 10g
    10a 10a 10c 10e 10f 10f 10g
    10a 10a 10c 10c 10c 10d 10d
    10a 10b 10c 10c 10c 10c 10c
    10b 10b 10c 10c 10c 10c 10c
    10b 10b 10c 10c 10c 10c 10c
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_winter_040():
    puzzle_string = f"""
    winter_040.parks1
    7
    10a 10a 10b 10b 10b 10b 10b
    10a 10a 10a 10a 10a 10b 10a
    10a 10a 10d 10d 10a 10a 10a
    10a 10d 10d 10e 10g 10g 10a
    10a 10a 10d 10e 10g 10g 10g
    10c 10c 10e 10e 10f 10f 10g
    10c 10c 10f 10f 10f 10g 10g
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_winter_041():
    puzzle_string = f"""
    winter_041.parks1
    7
    10g 10g 10g 10d 10a 10a 10a
    10g 10c 10c 10d 10d 10d 10a
    10b 10b 10c 10e 10d 10d 10a
    10b 10b 10e 10e 10a 10a 10a
    10a 10b 10a 10e 10a 10a 10h
    10a 10a 10a 10a 10a 10h 10h
    10a 10h 10h 10h 10h 10h 10h
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_winter_042():
    puzzle_string = f"""
    winter_042.parks1
    7
    10a 10d 10d 10d 10e 10e 10e
    10a 10a 10d 10d 10d 10d 10e
    10a 10a 10d 10d 10d 10d 10f
    10a 10c 10c 10c 10d 10d 10f
    10a 10c 10c 10c 10f 10f 10f
    10b 10c 10c 10c 10f 10f 10f
    10b 10b 10b 10c 10f 10g 10g
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_winter_044():
    puzzle_string = f"""
    winter_044.parks1
    7
    10a 10a 10c 10c 10e 10e 10e
    10a 10c 10c 10c 10d 10e 10e
    10a 10c 10c 10c 10d 10d 10d
    10c 10c 10c 10c 10c 10g 10g
    10b 10c 10c 10c 10c 10c 10g
    10b 10c 10b 10c 10c 10g 10g
    10b 10b 10b 10h 10h 10h 10h
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_winter_045():
    puzzle_string = f"""
    winter_045.parks1
    7
    10a 10a 10a 10e 10e 10f 10f
    10a 10e 10e 10e 10f 10f 10f
    10a 10b 10b 10c 10f 10g 10g
    10b 10b 10b 10c 10f 10g 10g
    10c 10c 10c 10c 10f 10g 10g
    10c 10d 10d 10d 10d 10d 10g
    10c 10d 10d 10d 10d 10d 10g
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_winter_046():
    puzzle_string = f"""
    winter_046.parks1
    8
    10a 10a 10a 10a 10g 10g 10g 10g
    10b 10a 10a 10a 10g 10g 10g 10h
    10b 10c 10c 10a 10g 10g 10g 10h
    10c 10c 10c 10f 10f 10f 10f 10h
    10c 10c 10d 10d 10f 10f 10f 10h
    10e 10e 10e 10e 10f 10f 10f 10h
    10e 10e 10e 10e 10f 10f 10f 10h
    10e 10e 10e 10e 10e 10e 10f 10h
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_winter_047():
    puzzle_string = f"""
    winter_047.parks1
    8
    10a 10a 10a 10a 10e 10e 10h 10h
    10b 10a 10a 10e 10e 10e 10g 10h
    10b 10a 10e 10e 10e 10e 10g 10g
    10b 10a 10e 10e 10e 10g 10g 10g
    10a 10a 10e 10e 10e 10f 10f 10f
    10a 10a 10e 10e 10e 10f 10f 10f
    10c 10c 10c 10e 10e 10f 10f 10f
    10d 10d 10d 10d 10f 10f 10f 10f
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_winter_048():
    puzzle_string = f"""
    winter_048.parks1
    8
    10a 10a 10a 10a 10a 10a 10c 10c
    10a 10d 10b 10b 10a 10a 10a 10c
    10a 10d 10d 10b 10a 10a 10a 10h
    10d 10d 10e 10g 10g 10g 10g 10h
    10d 10d 10e 10f 10f 10f 10g 10h
    10e 10d 10e 10f 10f 10f 10f 10f
    10e 10e 10e 10f 10f 10f 10f 10f
    10e 10e 10f 10f 10f 10f 10f 10f
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


# @pytest.mark.skip("skipped")
def test_parks1_winter_049():
    puzzle_string = f"""
    winter_049.parks1
    8
    10a 10d 10d 10e 10e 10f 10h 10h
    10a 10d 10d 10d 10f 10f 10h 10h
    10a 10a 10d 10f 10f 10f 10h 10h
    10a 10a 10f 10f 10f 10g 10h 10h
    10a 10a 10a 10a 10f 10g 10g 10g
    10a 10b 10c 10g 10g 10g 10g 10g
    10a 10c 10c 10g 10g 10g 10g 10g
    10c 10c 10c 10c 10g 10g 10g 10g
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_winter_050():
    puzzle_string = f"""
    winter_050.parks1
    8
    10a 10a 10d 10d 10h 10h 10h 10h
    10a 10b 10d 10d 10h 10h 10h 10h
    10a 10b 10d 10d 10h 10h 10h 10h
    10a 10b 10d 10d 10h 10h 10g 10h
    10b 10b 10b 10d 10d 10d 10g 10g
    10c 10c 10c 10f 10f 10f 10f 10g
    10c 10c 10c 10f 10f 10f 10f 10g
    10e 10e 10e 10e 10f 10f 10g 10g
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())


@pytest.mark.skip("skipped")
def test_parks1_winter_051():
    puzzle_string = f"""
    winter_051.parks1
    8
    10a 10a 10a 10b 10b 10b 10g 10g
    10a 10b 10a 10b 10b 10b 10g 10g
    10b 10b 10b 10b 10b 10g 10g 10h
    10b 10b 10b 10b 10b 10b 10h 10h
    10c 10c 10c 10b 10b 10e 10h 10h
    10c 10c 10c 10b 10e 10e 10f 10f
    10d 10c 10c 10d 10d 10e 10e 10f
    10d 10d 10d 10d 10e 10e 10e 10e
    """
    assert default_test_puzzle(puzzle_string, Parks1, parks1_techniques())
