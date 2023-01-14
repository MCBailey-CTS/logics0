from Loc import Loc
from puzzles import Puzzle


class Minesweeper(Puzzle):
    def is_solved(self) -> bool:
        return False

    def __init__(self, puzzle: str) -> None:
        super().__init__(puzzle)
        array = []
        self.grid = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            array.append(temp)
        array.pop(0)
        array.pop(0)
        for line in array:
            self.grid.append(line.split(' '))

    def is_number_cell(self, loc: Loc) -> bool:
        return self.grid[loc.row][loc.col].isalnum()

    def is_mine_cell(self, loc: Loc) -> bool:
        return not self.is_number_cell(loc)

    def __str__(self):
        string = f'{self.id()}\n'
        string += f'{len(self)}\n'
        for r in range(len(self)):
            for c in range(len(self)):
                string += f'{self.grid[r][c]} '
            string += '\n'
        return string

    def rem(self, locs: list[Loc], candidates: list[str]) -> int:
        edits = 0

        for loc in locs:
            for candidate in candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                self.grid[loc.row][loc.col] = self.grid[loc.row][loc.col].replace(str(candidate), "_")
                edits += 1

        return edits
