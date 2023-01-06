from techniques0 import CrossHatch, HiddenSingle, NakedPair, LockedCandidatesPointing, LockedCandidatesClaiming, \
    KropkiBlack, KropkiWhite, KropkiEmpty, CrossHatchRobotFences, HiddenSingleRobotFences, Parks1CrossHatch, \
    Parks1HiddenSingle, Parks1CrossHatchTouching, Parks1LockedCandidatesPointing, Parks1Bent3, Parks1Shape_00_01, \
    Parks1Shapes, Parks1DominateFence, TennerCrossHatch, TennerNakedPair, TennerHiddenPair, TennerHiddenSingle, \
    TennerTotalHiddenSingle, TennerPowerSetTotals, TennerNakedPairColumn, SumscrapersTech, SumscrapersSecondInLine, \
    CrossHatchSumscrapers, HiddenSingleSumscrapers, SumscrapersNextToScraper, SumscrapersLastIsMax, SkyscrapersN, \
    Skyscrapers1, SkyscrapersRange, MinesweeperSolver, RobotCrosswordsHouses, PowerGridTech, PowerGridCrossHatch, \
    PowerGridHiddenPower, AbstractPaintingTech
from techniques0.sudoku.UniqueRectangleType2 import UniqueRectangleType2
from techniques0.sudoku.Bug import Bug
from techniques0.sudoku.HiddenPair import HiddenPair
from techniques0.sudoku.NakedTriple import NakedTriple
from techniques0.sudoku.UniqueRectangleType1 import UniqueRectangleType1
from techniques0.sudoku.UniqueRectangleType4 import UniqueRectangleType4
from techniques0.sudoku.XWing import XWing
from techniques0.sudoku.XyWing import XyWing
from techniques0.sudoku.SwordFish import SwordFish
from techniques0.sudoku.JellyFish import JellyFish

PLUS = "+"
MINUS = "-"
EMPTY = "."


class Solving:
    @staticmethod
    def sudoku_techniques() -> list:
        return [
            CrossHatch(),
            HiddenSingle(),
            NakedPair(),
            LockedCandidatesPointing(),
            LockedCandidatesClaiming(),
            UniqueRectangleType1(),
            UniqueRectangleType2(),
            UniqueRectangleType4(),
            Bug(),
            HiddenPair(),
            NakedTriple(),
            XWing(),
            XyWing(),
            # SwordFish(),
            # JellyFish(),
        ]

    @staticmethod
    def kropki_techniques() -> list:
        return [
            KropkiBlack(),
            KropkiWhite(),
            KropkiEmpty(),
            # KropkiNakedPair(),
        ]

    @staticmethod
    def robot_fences_techniques() -> list:
        return [CrossHatchRobotFences(), HiddenSingleRobotFences()]

    @staticmethod
    def parks1_techniques() -> list:
        return [
            Parks1CrossHatch(),
            Parks1HiddenSingle(),
            Parks1CrossHatchTouching(),
            Parks1LockedCandidatesPointing(),
            Parks1Bent3(),
            Parks1Shape_00_01(),
            Parks1Shapes(),
            Parks1DominateFence(),
        ]

    @staticmethod
    def parks2_techniques() -> list:
        return []

    @staticmethod
    def tenner_techniques() -> list:
        return [TennerCrossHatch(),
                TennerNakedPair(),
                TennerHiddenPair(),
                TennerHiddenSingle(),
                TennerTotalHiddenSingle(),
                TennerPowerSetTotals(),
                TennerNakedPairColumn()]

    @staticmethod
    def futoshiki_techniques() -> list:
        return []

    @staticmethod
    def clouds_techniques() -> list:
        return []

    @staticmethod
    def knightoku_techniques() -> list:
        # return [CrossHatchKnightoku()] + Solving.sudoku_techniques()
        return Solving.sudoku_techniques()
    @staticmethod
    def kakuro_techniques() -> list:
        return []

    @staticmethod
    def lighthouses_techniques() -> list:
        return []

    @staticmethod
    def walls_techniques() -> list:
        return []

    @staticmethod
    def tents_techniques() -> list:
        return []

    @staticmethod
    def mathrax_techniques() -> list:
        return []

    @staticmethod
    def sumscrapers_techniques() -> list:
        return [SumscrapersTech(), CrossHatchSumscrapers(), HiddenSingleSumscrapers(),
                SumscrapersSecondInLine(), SumscrapersLastIsMax(), SumscrapersNextToScraper()]

    @staticmethod
    def skyscrapers_techniques() -> list:
        return [
            CrossHatchSumscrapers(), HiddenSingleSumscrapers(), SkyscrapersN(), Skyscrapers1(),
            SkyscrapersRange()
        ]

    @staticmethod
    def minesweeper_techniques():
        return [MinesweeperSolver()]

    @staticmethod
    def snail3_techniques() -> list:
        return []

    @staticmethod
    def mine_ships_techniques() -> list:
        return []

    @staticmethod
    def sentinels_techniques() -> list:
        return []

    @staticmethod
    def nurikabe_techniques() -> list:
        return []

    @staticmethod
    def robot_crosswords_techniques() -> list:
        return [RobotCrosswordsHouses()]

    @staticmethod
    def power_grid_techniques() -> list:
        return [
            PowerGridTech(),
            PowerGridCrossHatch(),
            PowerGridHiddenPower()
        ]

    @staticmethod
    def abstractpainting_techniques() -> list:
        return [
            AbstractPaintingTech()
        ]

    @staticmethod
    def battle_ships_techniques() -> list:
        return []

    @staticmethod
    def hidden_stars_techniques() -> list:
        return []

    @staticmethod
    def magnets_techniques() -> list:
        return []

    @staticmethod
    def lightenup_techniques() -> list:
        return [
            # Techs.LightenUpTech()
        ]

# 2865
