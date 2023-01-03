from techniques0 import *


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
        return [CrossHatchKnightoku()] + Solving.sudoku_techniques()

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
