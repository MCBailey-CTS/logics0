from puzzles import Sudoku
from Loc import Loc
from colorama import Fore

from techniques.Technique import Technique


class RemotePair(Technique):
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        # difficult_31
        green = [Loc(6, 7), Loc(8, 0)]
        yellow = [Loc(3, 7), Loc(8, 6)]
        remove = [Loc(3, 0)]
        pair = {2, 3}
        if all(pair == set(puzzle.cell_candidates(loc)) for loc in green + yellow):
            temp = self.color_remove(puzzle, green, yellow, remove)

            if temp > 0:
                return temp

        # difficult_04
        green = [Loc(7, 0), Loc(5, 8)]
        yellow = [Loc(6, 2), Loc(7, 8)]
        remove = [Loc(5, 2)]
        pair = {5, 8}
        if all(pair == set(puzzle.cell_candidates(loc)) for loc in green + yellow):
            edits += self.color_remove(puzzle, green, yellow, remove)

        # for r in range(len(puzzle)):
        #     for c in range(len(puzzle)):
        #         cell = Loc(r, c)
        #         if set(puzzle.cell_candidates(cell)) == {5, 8}:
        #             puzzle.override_loc_color([cell], Fore.RED)

        return edits

    def color_remove(self, puzzle: Sudoku, green: list[Loc], yellow: list[Loc], remove: list[Loc]) -> int:
        edits = 0

        puzzle.override_loc_color(green, Fore.GREEN)
        puzzle.override_loc_color(yellow, Fore.YELLOW)
        puzzle.override_loc_color(remove, Fore.RED)

        return puzzle.rem(remove, puzzle.cell_candidates(green[0]))
