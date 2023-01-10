
class Futoshiki:
    def __init__(self, puzzle: str) -> None:
        array = []
        for line in puzzle.split("\n"):
            temp = line.strip()
            if len(temp) == 0:
                continue
            # print(temp)

            array.append(temp)
        self.Constantsid = array[0]
        self.Constantslength = int(array[1])
        array.pop(0)
        array.pop(0)
        self.Constantsgrid = []
        for r in range(self.Constantslength * 2 - 1):
            line = array[0].strip().replace("  ", " ", -1).split(" ")
            print(line)
            self.Constantsgrid.append(line)
            array.pop(0)

        # print("/////")
        # print(array)

    def id(self) -> str:
        return self.Constantsid

    @property
    def length(self):
        return self.Constantslength

    def cell_string(self, loc: Loc) -> str:
        return self.Constantsgrid[loc.row][loc.col]

    def cell_candidates(self, loc: Loc) -> list[int]:
        return [int(s) for s in self.Constantsgrid[loc.row][loc.col] if s.isnumeric()]

    def rem(self, locs: list[Loc], candidates: list) -> int:
        edits = 0

        for loc in locs:
            for candidate in candidates:
                cell_candidates = self.cell_candidates(loc)
                if candidate not in cell_candidates:
                    continue
                self.Constantsgrid[loc.row][loc.col] = self.Constantsgrid[loc.row][loc.col].replace(candidate, "_")
                edits += 1

        return edits

    def __str__(self):
        string = f'{self.Constantsid}\n'
        string += f'{self.Constantslength}\n'

        for r in range(self.Constantslength * 2 - 1):
            for c in range(self.Constantslength * 2 - 1):
                string += f'{self.Constantsgrid[r][c]} '
            string += '\n'
        return string

