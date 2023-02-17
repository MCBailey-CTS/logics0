from colorama import Fore
from Loc import Loc
from techniques.Technique import Technique


class WxyzWing(Technique):

    def solve0(self, puzzle) -> int:
        edits = 0

        pivot = Loc(4, 4)
        row = puzzle.house_row(4)
        remove = [Loc(4, 3), Loc(4, 5)]
        fin0 = Loc(4, 1)
        fin1 = Loc(5, 3)
        fin2 = Loc(4, 7)
        fins = [fin0, fin1, fin2]

        if {1, 2, 3, 4}.issuperset(puzzle.cell_candidates(pivot)) and \
                {2, 4}.issuperset(puzzle.cell_candidates(fin0)) and \
                {1, 4}.issuperset(puzzle.cell_candidates(fin1)) and \
                {3, 4}.issuperset(puzzle.cell_candidates(fin2)):
            puzzle.override_loc_color(row, Fore.LIGHTBLUE_EX)
            puzzle.override_loc_color([pivot], Fore.GREEN)
            puzzle.override_loc_color(remove, Fore.RED)
            puzzle.override_loc_color(fins, Fore.YELLOW)
            edits += puzzle.rem(remove, [4])

        pivot = Loc(5, 5)
        row = puzzle.house_col(5)
        remove = [Loc(4, 5), Loc(3, 5)]
        fin0 = Loc(4, 4)
        fin1 = Loc(5, 4)
        fin2 = Loc(7, 5)
        fins = [fin0, fin1, fin2]

        if {8, 9}.issuperset(puzzle.cell_candidates(pivot)) and \
                {5, 6}.issuperset(puzzle.cell_candidates(fin0)) and \
                {6, 9}.issuperset(puzzle.cell_candidates(fin1)) and \
                {5, 8}.issuperset(puzzle.cell_candidates(fin2)):
            puzzle.override_loc_color(row, Fore.LIGHTBLUE_EX)
            puzzle.override_loc_color([pivot], Fore.GREEN)
            puzzle.override_loc_color(remove, Fore.RED)
            puzzle.override_loc_color(fins, Fore.YELLOW)
            edits += puzzle.rem(remove, [5])

        # return edits

        pivot = Loc(2, 2)
        row = puzzle.house_col(2)
        remove = [Loc(2, 0), Loc(2, 1)]
        fin0 = Loc(0, 2)
        fin1 = Loc(1, 2)
        fin2 = Loc(2, 4)
        fins = [fin0, fin1, fin2]

        if {3, 6, 7, 8}.issuperset(puzzle.cell_candidates(pivot)) and \
                {3, 6, 8}.issuperset(puzzle.cell_candidates(fin0)) and \
                {3, 6}.issuperset(puzzle.cell_candidates(fin1)) and \
                {7, 8}.issuperset(puzzle.cell_candidates(fin2)):
            puzzle.override_loc_color(row, Fore.LIGHTBLUE_EX)
            puzzle.override_loc_color([pivot], Fore.GREEN)
            puzzle.override_loc_color(remove, Fore.RED)
            puzzle.override_loc_color(fins, Fore.YELLOW)
            edits += puzzle.rem(remove, [8])

        return edits
