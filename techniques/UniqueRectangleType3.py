from puzzles import Sudoku
from Loc import Loc
from colorama import Fore
class UniqueRectangleType3:
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        base0 = Loc(3, 6)
        base1 = Loc(3, 7)
        opp_base0 = Loc(8, 6)
        opp_base1 = Loc(8, 7)
        extensions = [Loc(6, 8), Loc(8, 8)]
        if {1, 6}.issuperset(puzzle.cell_candidates(base0)) and \
                {1, 6}.issuperset(puzzle.cell_candidates(base1)) and \
                {1, 6, 8}.issuperset(puzzle.cell_candidates(opp_base0)) and \
                {1, 6, 9}.issuperset(puzzle.cell_candidates(opp_base1)) and \
                {3, 8, 9}.issuperset(puzzle.cell_candidates(extensions[1])) and \
                {3, 8}.issuperset(puzzle.cell_candidates(extensions[0])):
            remove = list(set(puzzle.house_fence('i')).difference([opp_base0, opp_base1] + extensions))
            puzzle.override_loc_color([base0, base1], Fore.GREEN)
            puzzle.override_loc_color([opp_base0, opp_base1], Fore.YELLOW)
            puzzle.override_loc_color(extensions, Fore.BLUE)
            puzzle.override_loc_color(remove, Fore.RED)
            edits += puzzle.rem(remove, [3, 8, 9])

        base0 = Loc(1, 6)
        base1 = Loc(2, 6)
        opp_base0 = Loc(1, 1)
        opp_base1 = Loc(2, 1)
        extensions = [Loc(3, 1), Loc(5, 1)]
        if {3, 6}.issuperset(puzzle.cell_candidates(base0)) and \
                {3, 6}.issuperset(puzzle.cell_candidates(base1)) and \
                {1, 3, 6, 7}.issuperset(puzzle.cell_candidates(opp_base0)) and \
                {1, 3, 6, 7}.issuperset(puzzle.cell_candidates(opp_base1)) and \
                {1, 4}.issuperset(puzzle.cell_candidates(extensions[0])) and \
                {4, 7}.issuperset(puzzle.cell_candidates(extensions[1])):
            remove = list(set(puzzle.house_col(1)).difference([opp_base0, opp_base1] + extensions))
            puzzle.override_loc_color([base0, base1], Fore.GREEN)
            puzzle.override_loc_color([opp_base0, opp_base1], Fore.YELLOW)
            puzzle.override_loc_color(extensions, Fore.BLUE)
            puzzle.override_loc_color(remove, Fore.RED)
            edits += puzzle.rem(remove, [1, 4, 7])

        return edits