from Loc import Loc
from _puzzles import RobotCrosswords


class RobotCrosswordsHouses:
    def solve0(self, puzzle: RobotCrosswords) -> int:
        edits = 0

        houses = []

        for row in range(puzzle.length):
            house = []
            for col in range(puzzle.length):
                house.append(Loc(row, col))
            houses.append(house)

        for col in range(puzzle.length):
            house = []
            for row in range(puzzle.length):
                house.append(Loc(row, col))
            houses.append(house)

        for house in houses:

            # temp_house = list(house)
            #
            #
            #
            #
            #
            #
            # continue

            string = ""

            all_crosswords = []

            in_crossword = False

            crossword = []

            for index in range(len(house)):
                if 'x' in puzzle.grid[house[index].row][house[index].col]:
                    if in_crossword:
                        all_crosswords.append(list(crossword))
                        crossword = []
                        in_crossword = False
                        # continue
                elif in_crossword:
                    crossword.append(house[index])
                else:
                    crossword.append(house[index])
                    in_crossword = True
            # for cross in

            print(all_crosswords)

            # loc = house[index]

            #     string += f'{puzzle.grid[loc.row][loc.col]} '
            #
            # string = string.replace('xx', 'x', -1).replace('xx', 'x', -1).replace('xx', 'x', -1).replace('xx', 'x', -1).replace('xx', 'x', -1).strip()
            # .split(" ")

            # string = string.strip()

            # print(string)

        return edits
