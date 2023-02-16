from tech import tech
from techniques.AbstractPaintingTech import AbstractPaintingTech
from techniques.Bug import Bug
from techniques.CrossHatch import CrossHatch
from techniques.CrossHatchSumscrapers import CrossHatchSumscrapers
from techniques.HiddenSingle import HiddenSingle
from techniques.HiddenSingleSumscrapers import HiddenSingleSumscrapers
from techniques.LockedCandidatesClaiming import LockedCandidatesClaiming
from techniques.LockedCandidatesPointing import LockedCandidatesPointing
from techniques.NakedPair import NakedPair
from techniques.RobotCrosswordsTech import RobotCrosswordsTech, RobotCrosswordsPowerSet
from techniques.TennerHiddenSingle import TennerHiddenSingle
from techniques.UniqueRectangleType1 import UniqueRectangleType1
from techniques.UniqueRectangleType2 import UniqueRectangleType2
from techniques.UniqueRectangleType4 import UniqueRectangleType4


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
            # FinnedXWing(),
            Bug(),
            tech.HiddenPair(),
            # tech.NakedTriple(),
            # tech.XWing(),
            # XyWing(),
            # SwordFish(),
            # JellyFish(),
        ]

    @staticmethod
    def kropki_techniques() -> list:
        return [
            tech.KropkiBlack(),
            tech.KropkiWhite(),
            tech.KropkiEmpty(),
            CrossHatch(),
            tech.KropkiBb(),
            tech.KropkiBw(),
            NakedPair(),
            tech.KropkiDominatingEmpty(),
            tech.KropkiDiamond()
        ]

    # @staticmethod
    # def robot_fences_techniques() -> list:
    #     return [CrossHatchRobotFences(), HiddenSingleRobotFences()]


    @staticmethod
    def parks2_techniques() -> list:
        return []

    @staticmethod
    def tenner_techniques() -> list:
        return [tech.TennerCrossHatch(),
                tech.TennerNakedPair(),
                tech.TennerHiddenPair(),
                TennerHiddenSingle(),
                tech.TennerTotalHiddenSingle(),
                tech.TennerPowerSetTotals(),
                tech.TennerNakedPairColumn()]

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
        return [
            CrossHatch(),
            tech.MathraxMathAddition(),
            tech.MathraxMathSubtraction(),
            tech.MathraxMathMultiplication(),
            tech.MathraxMathDivision(),
            tech.MathraxMath04XWing(),
            tech.MathraxMath01MinusXWing(),
            tech.MathraxMath02MinusXWing(),
            tech.MathraxOdd(),
            tech.MathraxEven(),
            NakedPair(),
            tech.NakedTriple(),
            tech.MathraxMath04MinusXWing(),
            # tech.XWing(),
            tech.HiddenPair()
        ]

    @staticmethod
    def sumscrapers_techniques() -> list:
        return [tech.SumscrapersTech(), CrossHatchSumscrapers(), HiddenSingleSumscrapers(),
                tech.SumscrapersSecondInLine(), tech.SumscrapersLastIsMax(), tech.SumscrapersNextToScraper()]

    @staticmethod
    def skyscrapers_techniques() -> list:
        return [
            CrossHatchSumscrapers(), HiddenSingleSumscrapers(), tech.SkyscrapersN(), tech.Skyscrapers1(),
            tech.SkyscrapersRange()
        ]

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
        return [RobotCrosswordsTech(), RobotCrosswordsPowerSet()]



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
    def lightenup_techniques() -> list:
        return [tech.LightenUpTech()]

    @staticmethod
    def lighthouses_techniques() -> list:
        return [tech.LighthousesTech()]
