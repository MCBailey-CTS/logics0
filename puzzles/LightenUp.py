from typing import Optional

from Loc import Loc
from puzzles import Puzzle


class LightenUp(Puzzle):
    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)

    def is_solved(self) -> bool:
        for r in range(len(self)):
            for c in range(len(self)):
                loc = Loc(r, c)
                if self.grid[r][c] == '??':
                    continue

                if self.grid[r][c] == '_-':
                    extending = self.extending_cell_locs(loc)
                    if all('_-' == self.grid[loc0.row][loc0.col] for loc0 in extending):
                        return False

                number = self.light_number(loc)

                if number is None:
                    continue

                surrounding = [loc0 for loc0 in self.surrounding_light(loc) if self.grid[loc0.row][loc0.col] == '+_']

                if len(surrounding) != number:
                    return False

        return True


    def is_candidate_cell(self, loc: Loc) -> bool:
        string = self.grid[loc.row][loc.col]
        return '+' in string or '-' in string or '_' in string

    def is_light_block(self, loc: Loc) -> bool:
        return self.grid[loc.row][loc.col].isnumeric()

    def light_number(self, loc: Loc) -> Optional[int]:
        if not self.is_light_block(loc):
            return None
        return int(self.grid[loc.row][loc.col])

    def cell_candidates(self, loc: Loc) -> Optional[list[str]]:
        if not self.is_candidate_cell(loc):
            return None
        string = self.grid[loc.row][loc.col]
        temp = set()
        if '+' in string:
            temp.add('+')
        if '-' in string:
            temp.add('-')
        return list(temp)

    def surrounding_light(self, loc: Loc) -> list[Loc]:
        valid = []
        directions = [
            loc.north(),
            loc.east(),
            loc.south(),
            loc.west(),
        ]

        for temp in directions:
            if temp.is_valid_parks(self.grid):
                valid.append(temp)

        return valid

    def extending_cell_locs(self, loc: Loc) -> list[Loc]:
        locs_to_remove = []

        next_loc = loc.west()
        while next_loc.col >= 0 and self.is_candidate_cell(next_loc):
            locs_to_remove.append(next_loc)
            next_loc = next_loc.west()

        next_loc = loc.east()
        while next_loc.col < len(self) and self.is_candidate_cell(next_loc):
            locs_to_remove.append(next_loc)
            next_loc = next_loc.east()

        next_loc = loc.north()
        while next_loc.row >= 0 and self.is_candidate_cell(next_loc):
            locs_to_remove.append(next_loc)
            next_loc = next_loc.north()

        next_loc = loc.south()
        while next_loc.row < len(self) and self.is_candidate_cell(next_loc):
            locs_to_remove.append(next_loc)
            next_loc = next_loc.south()
        return locs_to_remove

    def __str__(self):
        string = f'{self.id()}\n'
        string += f'{len(self)}\n'
        for r in range(len(self)):
            for c in range(len(self)):
                if self.grid[r][c] == '+_':
                    string += f'++ '
                    # string += f'{Back.LIGHTYELLOW_EX}{self.grid[r][c].ljust(2)}{Style.RESET_ALL} '
                    continue
                if self.grid[r][c] == '_-':
                    string += f'.. '
                    continue

                string += f'{self.grid[r][c].ljust(2)} '
            # string += f'{Back.LIGHTYELLOW_EX}{self.grid[r][c].ljust(2)}{Style.RESET_ALL} '
            #
            string += '\n'
        return string
