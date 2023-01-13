from puzzles import LightenUp
from Loc import Loc


class Lighthouses(LightenUp):
    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)

    def is_solved(self) -> bool:

        for r in range(self.length):
            for c in range(self.length):
                loc = Loc(r, c)
                if self.grid[r][c] == '+-':
                    return False

                if self.grid[r][c] == '+_' or self.is_light_block(loc):
                    for surrounding in self.surrounding(loc):
                        if self.grid[surrounding.row][surrounding.col] == '+_':
                            return False

                number = self.light_number(loc)

                if number is None:
                    continue

                # if loc != Loc(1, 0):
                #     continue

                solved_light = []
                solved_empty = []
                unsolved = []

                print(self.extending_cell_locs(loc))
                for loc0 in self.extending_cell_locs(loc):
                    if self.grid[loc0.row][loc0.col] == '+-':
                        unsolved.append(loc0)
                    if self.grid[loc0.row][loc0.col] == '+_':
                        solved_light.append(loc0)
                    if self.grid[loc0.row][loc0.col] == '_-':
                        solved_empty.append(loc0)

                if number != len(solved_light):
                    print("bade number of lights")
                    print(f'{number} {len(solved_light)}')
                    return False


        return True

    def extending_cell_locs(self, loc: Loc) -> list[Loc]:
        locs_to_remove = []

        rows = self.house_row(loc.row)
        cols = self.house_col(loc.col)
        locs = set(rows + cols)
        locs.remove(loc)
        return [loc0 for loc0 in locs if self.is_candidate_cell(loc0)]



