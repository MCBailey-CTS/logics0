from techniques.Technique import Technique
from Loc import Loc
from colorama import Fore, Style
class FishyCycle(Technique):

    def solve0(self, puzzle) -> int:
        edits = 0
        row0 = puzzle.house_row(2)
        row1 = puzzle.house_row(7)
        fence = puzzle.house_fence(puzzle.fence_from_chute(Loc(1, 1)))
        puzzle.override_loc_color(row0 + row1 + fence, Fore.GREEN)
        puzzle.override_loc_color([Loc(2, 2), Loc(2, 3), Loc(3, 3), Loc(5, 5), Loc(7, 5), Loc(7, 2)], Fore.YELLOW)
        puzzle.override_loc_color(
            [Loc(0, 2), Loc(1, 2), Loc(3, 2), Loc(4, 2), Loc(5, 2), Loc(6, 2), Loc(8, 2),
                Loc(0, 3), Loc(1, 3), Loc(6, 3), Loc(8, 3),
                Loc(0, 5), Loc(1, 5), Loc(6, 5), Loc(8, 5),
                ], Fore.RED)
        edits += puzzle.rem([Loc(0, 2), Loc(1, 2), Loc(3, 2), Loc(4, 2), Loc(5, 2), Loc(6, 2), Loc(8, 2),
                                Loc(0, 3), Loc(1, 3), Loc(6, 3), Loc(8, 3),
                                Loc(0, 5), Loc(1, 5), Loc(6, 5), Loc(8, 5),
                                ], [1])

        return edits
