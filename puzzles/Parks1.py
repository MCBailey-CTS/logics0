from puzzles import Puzzle
from Loc import Loc
from colorama import Fore, Style


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
            'h':Fore.LIGHTYELLOW_EX,
            'i':Fore.LIGHTRED_EX,
            'j':Fore.YELLOW,
            'k':Fore.RED
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
        for r in range(self.length):
            for c in range(self.length):
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

        for r in range(self.length):
            for c in range(self.length):
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
        string += f'{self.length}\n'
        for r in range(self.length):
            for c in range(self.length):
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