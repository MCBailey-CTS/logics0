from techniques0 import HiddenSingle
from techniques0.Technique import Technique
from puzzles import *
from Loc import Loc
from typing import Optional, Union
from colorama import Fore, Back, Style


class tech:
    class LighthousesTech(Technique):
        def solve0(self, puzzle: Lighthouses) -> int:
            edits = 0

            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)

                    number = puzzle.light_number(loc)

                    if puzzle.grid[r][c] == '+_':
                        edits += puzzle.rem(puzzle.surrounding(loc), ['+'])

                    if number is not None:
                        edits += puzzle.rem(puzzle.surrounding(loc), ['+'])
                        row_locs = puzzle.house_row(r)
                        col_locs = puzzle.house_col(c)
                        extending = [loc0 for loc0 in set(row_locs + col_locs) if
                                     puzzle.is_candidate_cell(loc0) and loc0 != loc]
                        if number == 0:
                            edits += puzzle.rem(extending, ['+'])

                        solved_light = []
                        solved_empty = []
                        unsolved = []

                        for loc0 in extending:
                            if puzzle.grid[loc0.row][loc0.col] == '+-':
                                unsolved.append(loc0)
                            if puzzle.grid[loc0.row][loc0.col] == '+_':
                                solved_light.append(loc0)
                            if puzzle.grid[loc0.row][loc0.col] == '_-':
                                solved_empty.append(loc0)

                        if len(unsolved) == 1 and len(solved_light) == 1 and number == 2:
                            edits += puzzle.rem(unsolved, ['-'])

                        # if len(unsolved) == 2 and number == 2 and len(solved_light) == 0:
                        #     edits += puzzle.rem(unsolved, ['-'])
                        #
                        if number == 1 and len(unsolved) == 1:
                            edits += puzzle.rem(unsolved, ['-'])

                        if len(solved_light) == 1 and len(unsolved) == 2 and number == 3:
                            edits += puzzle.rem(unsolved, ['-'])

                        if len(solved_light) == 0 and len(unsolved) == 3 and number == 2:
                            for un in unsolved:
                                temp_set = set(unsolved)

                                temp_set.remove(un)

                                other0, other1 = temp_set

                                if un.is_next_to(other0) and not un.is_next_to(other1):
                                    edits += puzzle.rem([other1], ['-'])

                                    if un.col == other0.col:
                                        surrounding0 = puzzle.surrounding(un)
                                        surrounding1 = puzzle.surrounding(other0)

                                        intersection = set(surrounding0).intersection(surrounding1)

                                        locs_to_rem = [loc1 for loc1 in intersection if
                                                       loc1.row == un.row or loc1.row == other0.row]
                                        edits += puzzle.rem(locs_to_rem, ['+'])

            return edits

    class Skyscrapers1:
        def solve0(self, puzzle: Skyscrapers) -> int:
            edits = 0

            for index in range(len(puzzle)):
                north = puzzle.north_scraper(index)
                south = puzzle.south_scraper(index)
                east = puzzle.east_scraper(index)
                west = puzzle.west_scraper(index)

                if north == 1:
                    edits += puzzle.rem([Loc(0, index)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

                if south == 1:
                    edits += puzzle.rem([Loc(len(puzzle) - 1, index)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

                if west == 1:
                    edits += puzzle.rem([Loc(index, 0)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

                if east == 1:
                    edits += puzzle.rem([Loc(index, len(puzzle) - 1)], set(puzzle.expected_candidates()).difference(
                        [max(puzzle.expected_candidates())]))

            return edits

    class SkyscrapersRange:
        def solve0(self, puzzle: Skyscrapers) -> int:
            edits = 0
            tuples: list[tuple[Optional[int], list[Loc]]] = []

            for index in range(len(puzzle)):
                house = puzzle.house_row(index)
                tuples.append((puzzle.west_scraper(index), house))
                house = list(house)
                house.reverse()
                tuples.append((puzzle.east_scraper(index), house))
                house = puzzle.house_col(index)
                tuples.append((puzzle.north_scraper(index), house))
                house = list(house)
                house.reverse()
                tuples.append((puzzle.south_scraper(index), house))

            for tuple0 in tuples:
                scraper, house = tuple0
                if scraper is None:
                    continue

                string = "".join([puzzle.grid[loc.row][loc.col] for loc in house])

                if string == "1____23__23____4" and scraper == 4:
                    edits += puzzle.rem([house[1]], [3])

                if string == "1____23__23____4" and scraper == 3:
                    edits += puzzle.rem([house[1]], [2])

                if string == "123_1_3_12_____4" and scraper == 2:
                    edits += puzzle.rem([house[0]], [1, 2, 4])

                if string == "123_123_123____4" and scraper == 2:
                    edits += puzzle.rem([house[0]], [1, 2, 4])

                if string == "12__12_____4__3_" and scraper == 3:
                    edits += puzzle.rem([house[0]], [1])

                if string == "_23__23____41___" and scraper == 3:
                    edits += puzzle.rem([house[0]], [3])

                if string == "_23__23____41___" and scraper == 2:
                    edits += puzzle.rem([house[0]], [2])

                if string == "123_123_123____4" and scraper == 3:
                    edits += puzzle.rem([house[0]], [3])

                if string == "123_123_12341234" and scraper == 3:
                    edits += puzzle.rem([house[0]], [3])

                if string == "12__12____3____4" and scraper == 3:
                    edits += puzzle.rem([house[0]], [1])

                if string == "_2_4_2_41_____3_" and scraper == 2:
                    edits += puzzle.rem([house[0]], [4])

                if string == "1_3__2_____41_3_" and scraper == 2:
                    edits += puzzle.rem([house[0]], [1])

                if string == "1234123412341234" and scraper == 3:
                    edits += puzzle.rem([house[0]], [4])

                if string == "1234123412341234" and scraper == 2:
                    edits += puzzle.rem([house[0]], [4])

            # 1___ ___4 _23_ _23_

            # print(string)

            # house_candidates = [puzzle.cell_candidates(loc) for loc in house]
            # for index in range(puzzle.length):
            #     candidates = house_candidates[index]
            #     if len(candidates) != 1:
            #         continue
            #     solved_candidate = candidates[0]
            #     if solved_candidate != puzzle.length:
            #         continue
            #     if index == 0 or index == puzzle.length - 1:
            #         continue
            #
            #
            #     print("her111r")

            # candidates1 = puzzle.cell_candidates(house[1])
            #
            # if len(candidates1) != 1:
            #     continue
            # if candidates1[0] != puzzle.length:
            #     continue
            # difference = scraper - puzzle.length
            #
            # edits += puzzle.rem([house[0]], set(puzzle.expected_candidates()).difference([difference]))

            return edits

    class SkyscrapersN:
        def solve0(self, puzzle: Skyscrapers) -> int:
            edits = 0

            for index in range(len(puzzle)):
                north = puzzle.north_scraper(index)
                south = puzzle.south_scraper(index)
                east = puzzle.east_scraper(index)
                west = puzzle.west_scraper(index)

                if north == len(puzzle):
                    edits += puzzle.rem([Loc(0, index)], set(puzzle.expected_candidates()).difference(
                        [min(puzzle.expected_candidates())]))

                if south == len(puzzle):
                    edits += puzzle.rem([Loc(len(puzzle) - 1, index)], set(puzzle.expected_candidates()).difference(
                        [min(puzzle.expected_candidates())]))

                if west == len(puzzle):
                    edits += puzzle.rem([Loc(index, 0)], set(puzzle.expected_candidates()).difference(
                        [min(puzzle.expected_candidates())]))

                if east == len(puzzle):
                    edits += puzzle.rem([Loc(index, len(puzzle) - 1)], set(puzzle.expected_candidates()).difference(
                        [min(puzzle.expected_candidates())]))

            return edits

    class MinesweeperSolver:

        @staticmethod
        def surrounding(puzzle, loc: Loc) -> list[Loc]:
            valid = []
            directions = [
                loc.north(),
                loc.east(),
                loc.south(),
                loc.west(),
                loc.north().east(),
                loc.north().west(),
                loc.south().east(),
                loc.south().west(),
            ]

            for temp in directions:
                if temp.is_valid_parks(puzzle.grid):
                    valid.append(temp)

            return valid

        def solve0(self, puzzle: Minesweeper) -> int:
            edits = 0
            for r in range(len(puzzle)):
                for c in range(len(puzzle)):
                    loc = Loc(r, c)
                    if puzzle.is_number_cell(loc):
                        number = int(puzzle.grid[loc.row][loc.col])

                        if number == 0:
                            edits += puzzle.rem()

            return edits

    class CrossHatchRobotFences:
        @staticmethod
        def solve0(puzzle: Sudoku) -> int:
            edits = 0
            for cell in list(puzzle.unsolved_cells()):
                neighbors = set(puzzle.house_row(cell.row) + puzzle.house_col(cell.col))
                neighbors.remove(cell)
                for neighbor in neighbors:
                    if neighbor not in puzzle.unsolved_cells():
                        _candidates = puzzle.cell_candidates(neighbor)
                        if len(_candidates) == 1:
                            edits += puzzle.rem(cell, [list(_candidates)[0]])
            return edits

    class HiddenSingleRobotFences:

        @staticmethod
        def get_required_candidates(puzzle: RobotFences, house: list[Loc]) -> list[int]:
            length = len(puzzle)
            solved_candidates = [puzzle.cell_candidates(loc)[0] for loc in house if
                                 len(puzzle.cell_candidates(loc)) == 1]

            minimum = min(solved_candidates)
            maximum = max(solved_candidates)

            temp_min = max([1, maximum - length + 1])
            temp_max = max([length, minimum + length - 1])

            return list(range(temp_min, temp_max + 1))

        @staticmethod
        def solve0(puzzle: RobotFences) -> int:
            edits = 0
            # return edits
            for cell in list(puzzle.unsolved_cells()):
                neighbors = set(puzzle.house_row(cell.row) + puzzle.house_col(cell.col))
                neighbors.remove(cell)
                for neighbor in neighbors:
                    if neighbor not in puzzle.unsolved_cells():
                        _candidates = puzzle.cell_candidates(neighbor)
                        if len(_candidates) == 1:
                            edits += puzzle.rem(cell, [list(_candidates)[0]])

            for fence_house in puzzle.houses_fences():

                if len(fence_house) == len(puzzle):
                    edits += HiddenSingle.solve1(puzzle, fence_house)
                    continue

                #  get the solved candidates in the fence_house
                solved_candidates = [puzzle.cell_candidates(loc)[0] for loc in fence_house if
                                     len(puzzle.cell_candidates(loc)) == 1]

                if len(solved_candidates) == 0:
                    continue

                length = len(fence_house)

                minimum = min(solved_candidates)
                maximum = max(solved_candidates)

                temp_min = max([1, maximum - length + 1])
                temp_max = max([length, minimum + length - 1])

                expected_candidates = tech.HiddenSingleRobotFences.get_required_candidates(puzzle, fence_house)

                candidates_to_remove = list(set(puzzle.expected_candidates()).difference(expected_candidates))
                # print(candidates_to_remove)

                candidates_to_remove = list(set(puzzle.expected_candidates()).difference(range(temp_min, temp_max + 1)))
                # print(candidates_to_remove)

                for loc in fence_house:
                    edits += puzzle.rem(loc, candidates_to_remove)

            return edits

    class FutoshikiGreaterThanLessThan:  # (BaseFutoshikiTechnique):
        def solve0(self, puzzle: Futoshiki) -> int:
            edits = 0

            for r in range(puzzle.length * 2 - 1):
                for c in range(puzzle.length * 2 - 1):

                    even_row = r % 2 == 0
                    even_col = c % 2 == 0

                    if even_row and even_col:
                        continue

                    if not even_row and not even_col:
                        continue

                    if even_row:
                        loc = Loc(r, c)
                        string = puzzle.cell_string(loc)

                        if string == '>':
                            edits += self.solve_greater_than(puzzle, loc.east(), loc.west())

                        # print(puzzle.cell_string(loc))
            # for row_house in puzzle.house_row_cells()

            return edits

        def solve_greater_than(self, puzzle: Futoshiki, lesser: Loc, greater: Loc):
            edits = 0
            lesser_candidates = puzzle.cell_candidates(lesser)
            greater_candidates = puzzle.cell_candidates(greater)

            min_greater = min(greater_candidates)
            max_lesser = max(lesser_candidates)

            print(min_greater)
            print(max_lesser)

            for candidate in lesser_candidates:
                if candidate >= min_greater:
                    print(f'removing {candidate} from {lesser}')
                    edits += puzzle.rem([lesser], [str(candidate)])

            # print(lesser_candidates)
            # print(greater_candidates)

            return edits

    class FutoshikiCrossHatch:
        def solve0(self, puzzle: Futoshiki) -> int:
            edits = 0
            return edits

    class RobotCrosswordsHouses:
        def solve0(self, puzzle: RobotCrosswords) -> int:
            edits = 0

            houses = []

            for row in range(len(puzzle)):
                house = []
                for col in range(len(puzzle)):
                    house.append(Loc(row, col))
                houses.append(house)

            for col in range(len(puzzle)):
                house = []
                for row in range(len(puzzle)):
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

    class MagnetsFullHouse:
        def __int__(self):
            self.EMPTY = 0

        def solve0(self, puzzle: Magnets) -> int:
            edits = 0

            for i in range(puzzle.length):
                plus_row_value = puzzle.plus_row_value(i)
                minus_row_value = puzzle.minus_row_value(i)
                row_house = puzzle.house_row(i)

                if plus_row_value + minus_row_value == puzzle.length:
                    edits += puzzle.rem(row_house, [self.EMPTY])

                plus_col_value = puzzle.plus_col_value(i)
                minus_col_value = puzzle.minus_col_value(i)
                col_house = puzzle.house_col(i)

                if plus_col_value + minus_col_value == puzzle.length:
                    edits += puzzle.rem(col_house, [self.EMPTY])

            return edits

    class MagnetsPair:
        def __int__(self):
            self.PLUS = 1
            self.MINUS = 0
            self.EMPTY = self.MINUS

        def solve1(self, puzzle: Magnets, loc0: Loc, loc1: Loc) -> int:
            edits = 0
            candidates0 = puzzle.cell_candidates(loc0)
            candidates1 = puzzle.cell_candidates(loc1)

            if self.EMPTY not in candidates0:
                edits += puzzle.rem([loc1], [self.EMPTY])

            if self.EMPTY not in candidates1:
                edits += puzzle.rem([loc0], [self.EMPTY])

            if self.PLUS not in candidates0:
                edits += puzzle.rem([loc1], [self.MINUS])

            if self.PLUS not in candidates1:
                edits += puzzle.rem([loc0], [self.MINUS])

            if self.MINUS not in candidates0:
                edits += puzzle.rem([loc1], [self.PLUS])

            if self.MINUS not in candidates1:
                edits += puzzle.rem([loc0], [self.PLUS])

            return edits

        def solve0(self, puzzle: Magnets) -> int:
            edits = 0

            # loc0 = Loc(1, 1)
            # loc1 = Loc(1, 2)

            for magnets_fence_pair in puzzle.house_fences():
                loc0, loc1 = magnets_fence_pair
                #
                #     if puzzle.house_fence(loc0) != 'a':
                #         continue
                #
                edits += self.solve1(puzzle, loc0, loc1)

            return edits

        class MagnetsZero:
            def __int__(self):
                self.PLUS = 1
                self.MINUS = 0
                self.EMPTY = self.MINUS

            def solve0(self, puzzle: Magnets) -> int:
                edits = 0
                for i in range(puzzle.length):
                    plus_row_value = puzzle.plus_row_value(i)
                    row_house = puzzle.house_row(i)
                    if plus_row_value == 0:
                        for loc in row_house:
                            edits += puzzle.rem([loc], [self.PLUS])
                    plus_col_value = puzzle.plus_col_value(i)
                    col_house = puzzle.house_col(i)
                    if plus_col_value == 0:
                        for loc in col_house:
                            edits += puzzle.rem([loc], [self.PLUS])
                    minus_row_value = puzzle.minus_row_value(i)
                    row_house = puzzle.house_row(i)
                    if minus_row_value == 0:
                        for loc in row_house:
                            edits += puzzle.rem([loc], [self.MINUS])
                    minus_col_value = puzzle.minus_col_value(i)
                    col_house = puzzle.house_col(i)
                    print(minus_col_value)
                    if minus_col_value == 0:
                        for loc in col_house:
                            edits += puzzle.rem([loc], [self.MINUS])
                return edits

    class MathraxHiddenSingle:

        def solve0(self, puzzle: Mathrax) -> int:
            edits = 0
            return edits

        class MathraxMath:

            def solve0(self, puzzle: Mathrax) -> int:
                edits = 0
                for r in range(1, len(puzzle) * 2 - 1, 2):
                    for c in range(1, len(puzzle) * 2 - 1, 2):
                        loc = Loc(r, c)
                        string = puzzle.grid[r][c]
                        if '+' in string:
                            number = int(string.replace('+', ''))
                            edits += self.solve_addition(puzzle, number, loc.top_left(), loc.bottom_right())
                            edits += self.solve_addition(puzzle, number, loc.top_right(), loc.bottom_left())
                return edits

            @staticmethod
            def __solve_addition(puzzle: Mathrax, number: int, cell0: Loc, cell1: Loc) -> int:
                edits = 0
                candidates1 = set(puzzle.cell_candidates(cell1))
                for candidate0 in puzzle.cell_candidates(cell0):
                    if any(candidate0 + candidate1 == number for candidate1 in candidates1):
                        continue
                    edits += puzzle.rem([cell0], [candidate0])
                return edits

            def solve_addition(self, puzzle: Mathrax, number: int, cell0: Loc, cell1: Loc) -> int:
                edits = self.__solve_addition(puzzle, number, cell0, cell1)
                edits = self.__solve_addition(puzzle, number, cell1, cell0)
                return edits
