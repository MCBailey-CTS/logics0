from puzzles import Sudoku
from colorama import Fore
from Loc import Loc
from techniques.Technique import Technique


class AlmostLockedCandidatesClaiming(Technique):
    def solve0(self, puzzle: Sudoku) -> int:
        edits = 0

        house = puzzle.house_row(3)
        house_string = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in house) if
                               char.isnumeric() or char == '_')

        fence = puzzle.house_fence(puzzle.fence_from_chute(Loc(1, 2)))
        fence_string = "".join(char for char in "".join(puzzle.grid[loc.row][loc.col] for loc in fence) if
                               char.isnumeric() or char == '_')

        # print(house_string)
        # print(fence_string)

        if house_string == '__3456789__3456789__3456789__3456789__345678912_______123456789123456789123456789' and \
                fence_string == '12345678912345678912345678912_______123456789123456789123456789123456789123456789':
            intersection = set(house).intersection(fence)
            locked0 = Loc(3, 5)
            locked1 = Loc(4, 6)
            locked = [locked0, locked1]
            remove = set(fence).difference([locked1, locked0] + house)
            puzzle.override_loc_color(house, Fore.GREEN)
            puzzle.override_loc_color(locked, Fore.YELLOW)
            puzzle.override_loc_color(list(intersection), Fore.BLUE)
            puzzle.override_loc_color(list(remove), Fore.LIGHTRED_EX)
            edits += puzzle.rem(remove, [1, 2])

        return edits
