from Loc import Loc
from puzzles import Puzzle


class RobotCrosswords(Puzzle):
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
            split = line.split(' ')
            other = []

            for item in split:
                if item == '.' or item == '_':
                    other.append('123456789')
                elif item == 'x':
                    other.append('xxxxxxxxx')
                elif item.isalnum():
                    number = int(item)
                    temp = ''
                    for num in range(1, 10):
                        if number == num:
                            temp += f'{num}'
                        else:
                            temp += '_'
                    other.append(temp)
            # print(split)
            # self.grid.append(line.split(" "))
            self.grid.append(other)

    def __str__(self) -> str:
        string = f'///////////////////////////////////\n'
        string += f'{self.id()}\n'
        string += f'{self.__length}\n'
        for r in range(self.__length):
            for c in range(self.__length):
                string += f'{self.grid[r][c]} '
            string += '\n'
        string += f'///////////////////////////////////'
        return string

    def is_solved(self) -> bool:
        for house in self.houses():
            solved_candidates = [self.cell_candidates(loc)[0] for loc in house if len(self.cell_candidates(loc)) == 1]
            if len(solved_candidates) != len(house):
                return False
            if not RobotCrosswords.is_solved_candidate_house(solved_candidates):
                return False

        return True

    @staticmethod
    def is_solved_candidate_house(candidates: list[int]) -> bool:
        __sorted = sorted(candidates)
        return all(__sorted[i] + 1 == __sorted[i + 1] for i in range(len(candidates) - 1))

    def houses(self) -> list[list[Loc]]:
        houses = []
        for i in range(len(self)):
            for house in [self.house_row(i), self.house_col(i)]:
                actual_cells = set(
                    [loc for index, loc in enumerate(house) if 'x' not in self.grid[loc.row][loc.col]])
                house_chunks = []
                while len(actual_cells) > 0:
                    current = actual_cells.pop()
                    current_set = {current}
                    for other in list(actual_cells):
                        if any(other.is_next_to(loc) for loc in current_set):
                            actual_cells.remove(other)
                            current_set.add(other)
                    house_chunks.append(current_set)
                for house0 in house_chunks:
                    houses.append(list(house0))
        return houses

#
# def solve0(self, puzzle: RobotCrosswords) -> int:
#       edits = 0
#       for i in range(len(puzzle)):
#
#           for house in [puzzle.house_row(i), puzzle.house_col(i)]:
#               actual_cells = set(
#                   [loc for index, loc in enumerate(house) if 'x' not in puzzle.grid[loc.row][loc.col]])
#               house_chunks = []
#               while len(actual_cells) > 0:
#                   current = actual_cells.pop()
#                   current_set = {current}
#
#                   for other in list(actual_cells):
#                       if any(other.is_next_to(loc) for loc in current_set):
#                           actual_cells.remove(other)
#                           current_set.add(other)
#
#                   house_chunks.append(current_set)
#               for house0 in house_chunks:
#                   edits += self.solve1(puzzle, list(house0))
#
#       return edits
