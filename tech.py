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

                expected_candidates = tech. HiddenSingleRobotFences.get_required_candidates(puzzle, fence_house)

                candidates_to_remove = list(set(puzzle.expected_candidates()).difference(expected_candidates))
                # print(candidates_to_remove)

                candidates_to_remove = list(set(puzzle.expected_candidates()).difference(range(temp_min, temp_max + 1)))
                # print(candidates_to_remove)

                for loc in fence_house:
                    edits += puzzle.rem(loc, candidates_to_remove)

            return edits




